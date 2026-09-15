#!/usr/bin/env node
/* PULSE Paediatrics — full-flow DOM-simulation validation (no deps).
   Stubs the DOM, runs the app <script>, and plays through:
   home → chapters → path → guide → full unit quiz (every question type,
   right + wrong answers, keyboard T/F) → unit-done → review → localStorage. */
const fs = require('fs');
const vm = require('vm');

const html = fs.readFileSync('pulse-peds-complete.html', 'utf8');
const m = html.match(/<script>([\s\S]*)<\/script>/);
if (!m) { console.error('no script found'); process.exit(1); }
const script = m[1];

/* ---------------- DOM stub ---------------- */
class El {
  constructor(tag) { this.tag = tag || 'div'; this._children = []; this._q = {};
    this._text = ''; this._html = ''; this.className = ''; this.disabled = false;
    this.onclick = null; this.style = {}; this._cls = new Set(); }
  set innerHTML(v) { this._html = v; this._children = []; }   // '' clears children, like real DOM
  get innerHTML() { return this._html; }
  set textContent(v) { this._text = v; this._html = v; this._children = []; }
  get textContent() { return this._text; }
  get children() { return this._children; }
  appendChild(c) { this._children.push(c); return c; }
  remove() {}
  click() { if (this.onclick) this.onclick(); }
  get classList() { const self = this; return {
    add(...a) { a.forEach(x => self._cls.add(x)); self.className = [...self._cls].join(' '); },
    remove(...a) { a.forEach(x => self._cls.delete(x)); self.className = [...self._cls].join(' '); },
    toggle(x, force) { const on = force === undefined ? !self._cls.has(x) : force;
      on ? self._cls.add(x) : self._cls.delete(x); self.className = [...self._cls].join(' '); return on; },
    contains(x) { return self._cls.has(x); } }; }
  querySelector(sel) { if (!this._q[sel]) this._q[sel] = new El('span'); return this._q[sel]; }
  getBoundingClientRect() { return { left: 0, top: 0, width: 10, height: 10 }; }
}
const els = {};
const $get = id => { if (!els[id]) els[id] = new El('div'); return els[id]; };
const listeners = {};
const sandbox = {
  console,
  document: {
    getElementById: $get,
    createElement: t => new El(t),
    body: new El('body'),
    addEventListener: (ev, fn) => { (listeners[ev] = listeners[ev] || []).push(fn); },
  },
  window: { scrollY: 0 },
  localStorage: { _m: {}, getItem(k) { return k in this._m ? this._m[k] : null; },
                  setItem(k, v) { this._m[k] = String(v); }, removeItem(k) { delete this._m[k]; } },
  setTimeout: (fn) => fn && fn(),
  Date, Math, JSON, Object, Array, String, Number, RegExp, parseInt, parseFloat,
};
vm.createContext(sandbox);
const expose = `
;globalThis.__APP = {
  QUESTIONS, UNITS, CHAPTERS, S, QBYID,
  show, goBack, unitsOf, openGuide, beginUnit, nextQ, renderQ,
  get order(){return order;}, get idx(){return idx;}, get locked(){return locked;},
};`;
vm.runInContext(script + expose, sandbox, { filename: 'app.js' });
const A = sandbox.__APP;

const $ = id => sandbox.document.getElementById(id);
let fails = 0;
const ok = (cond, msg) => { console.log((cond ? '  ✓ ' : '  ✗ FAIL ') + msg); if (!cond) fails++; };

/* ---------------- 1. boot / home ---------------- */
console.log('— boot & home');
ok(A.QUESTIONS.length === 2541, `QUESTIONS loaded (${A.QUESTIONS.length})`);
ok(A.CHAPTERS.filter(c => c.live).length === 25, '25 live chapters');
ok($('heroSub').textContent.includes('25 of 54'), 'home hero shows "25 of 54"');

/* ---------------- 2. chapters list ---------------- */
console.log('— chapters');
A.show('chapters');
ok($('chList').children.length === 54, '54 chapter rows rendered');
const firstLive = $('chList').children.find(c => c.onclick);
firstLive.onclick();
ok($('pathTitle').textContent === 'Normal Newborn', 'chapter 1 path opens');
ok($('nodes').children.filter(c => c.className === 'node').length === 14, '14 units in CH1 path');

/* ---------------- 3. guide → quiz ---------------- */
console.log('— guide & unit quiz');
const unit = A.unitsOf(1)[0];
A.openGuide(unit);
ok($('gTitle').textContent === unit.title, 'guide title renders');
ok($('gCount').textContent.includes('questions'), 'guide count renders');
A.beginUnit();

const TYPE_LABEL = { mcq: 'MCQ', fill: 'Fill up', tf: 'True / False', match: 'Match the following', odd: 'Odd one out', case: 'Clinical case' };
const seenTypes = new Set();
let answeredWrong = 0, n = 0;
while (true) {
  const cur = A.order[A.idx];
  if (!cur) break;
  const q = cur.q; n++;
  seenTypes.add(q.type || 'mcq');
  ok($('qcount').textContent === `QUESTION ${n} OF ${A.order.length}`, `qcount #${n}`);
  ok($('qtype').textContent === TYPE_LABEL[q.type || 'mcq'], `type badge = ${TYPE_LABEL[q.type || 'mcq']}`);
  ok($('qtag').textContent.includes(`Book p${q.page}`), `qtag page p${q.page}`);
  // vignette
  if (q.type === 'case') {
    ok(!$('vign').classList.contains('hidden') && $('vign').textContent.length > 20, 'case vignette visible');
  } else {
    ok($('vign').classList.contains('hidden'), 'vignette hidden for non-case');
  }
  // fill blank
  if (q.type === 'fill') {
    ok($('qtext').innerHTML.includes('class="blank"'), 'fill blank rendered');
  }
  // match table
  if (q.type === 'match') {
    ok(!$('matchbox').classList.contains('hidden'), 'matchbox visible');
    ok(($('matchbox').innerHTML.match(/class="mi"/g) || []).length === 8, 'matchbox has 8 cells (A-D + 1-4)');
  } else {
    ok($('matchbox').classList.contains('hidden'), 'matchbox hidden for non-match');
  }
  // tf buttons
  const btns = $('opts').children;
  if (q.type === 'tf') {
    ok(btns.length === 2 && $('opts').className.includes('tfrow'), 'tf renders 2 True/False buttons');
  } else {
    ok(btns.length === 4, `4 options rendered (${q.type})`);
  }
  // answer: wrong on question 2 and 4, right otherwise; keyboard for one tf
  const right = btns.findIndex(b => cur.opts[btns.indexOf(b)] && cur.opts[btns.indexOf(b)].ok);
  let clicked = null;
  if (q.type === 'tf' && n === 1) {
    const key = q.ans === 0 ? 't' : 'f';
    listeners.keydown[0]({ key });
    clicked = 'kbd';
    ok(!A.locked, `tf keyboard '${key}' answered`);
  } else if (n === 2 || n === 4) {
    const wrongIdx = btns.findIndex(b => { const i = btns.indexOf(b); return !cur.opts[i].ok; });
    btns[wrongIdx].click(); clicked = 'wrong'; answeredWrong++;
  } else {
    btns[right].click(); clicked = 'right';
  }
  ok(A.locked, `question ${n} answered (${clicked})`);
  ok($('nextBtn').classList.contains('hidden') === false, 'next button shown after answer');
  ok($('fb').className.includes('show'), 'feedback shown');
  A.nextQ();
}

/* ---------------- 4. unit done + review + persistence ---------------- */
console.log('— unit done');
ok($('dScore').textContent === `${n - answeredWrong}/${n}`, `score ${$('dScore').textContent}`);
ok($('dRev').children.length === answeredWrong + (answeredWrong ? 1 : 0), 'review lists wrong answers');
const revHTML = $('dRev').children.map(c => c.innerHTML).join('');
ok(!revHTML.includes('undefined'), 'review has no undefined');
ok(A.S.done.includes(unit.id), 'unit marked done (localStorage)');
ok(sandbox.localStorage._m['pulse_peds_xp'], 'XP persisted under pulse_peds_xp key');

/* ---------------- 5. play a unit containing every type ---------------- */
console.log('— type coverage scan across bank');
const typeUnits = {};
for (const u of A.UNITS) {
  for (const qid of u.qs) {
    const q = A.QBYID[qid];
    if (q && (q.type === 'match' || q.type === 'case' || q.type === 'odd') && !typeUnits[q.type]) typeUnits[q.type] = u;
  }
}
for (const t of ['match', 'case', 'odd']) {
  ok(typeUnits[t], `found a unit with a ${t} question (${typeUnits[t] ? typeUnits[t].id : 'none'})`);
  if (typeUnits[t]) {
    A.openGuide(typeUnits[t]); A.beginUnit();
    // jump straight to the target-type question
    while (A.order[A.idx] && A.order[A.idx].q.type !== t) {
      const cur = A.order[A.idx];
      $('opts').children.forEach(b => { const i = $('opts').children.indexOf(b); if (cur.opts[i] && cur.opts[i].ok) b.click(); });
      A.nextQ();
    }
    const cur = A.order[A.idx];
    ok(cur && cur.q.type === t, `${t} question reached & rendered`);
    const btns = $('opts').children;
    btns.forEach(b => { const i = btns.indexOf(b); if (cur.opts[i] && cur.opts[i].ok) b.click(); });
    ok($('fb').innerHTML.length > 10, `${t} answered, feedback shown`);
    A.show('home');
  }
}

console.log(fails ? `\n${fails} FAILURES` : '\nALL CHECKS PASSED ✓');
process.exit(fails ? 1 : 0);
