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
const LIVE = A.CHAPTERS.filter(c => c.live).length;
ok(A.QUESTIONS.length === A.UNITS.reduce((n, u) => n + u.qs.length, 0), `QUESTIONS loaded & fully unit-referenced (${A.QUESTIONS.length})`);
ok(LIVE >= 28 && A.CHAPTERS.filter(c => c.live).every((c, i) => c.n === i + 1), `${LIVE} live chapters, contiguous from 1`);
ok($('heroSub').textContent.includes(LIVE + ' of 54'), `home hero shows "${LIVE} of 54"`);

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

/* ---------------- 6. full CH26 playthrough (Airway Malformations & Foreign Bodies) ---------------- */
console.log('— full CH26 playthrough (121 Q / 9 units)');
const ch26u = A.unitsOf(26);
ok(ch26u.length === 9, `CH26 has 9 units (${ch26u.length})`);
ok(ch26u.reduce((n, u) => n + u.qs.length, 0) === 121, 'CH26 has 121 questions');
const seen26 = new Set();
let n26 = 0, multiCorrect = 0;
for (const u of ch26u) {
  A.openGuide(u);
  ok($('gTitle').textContent === u.title && $('gCount').textContent.startsWith(u.qs.length + ' questions'), `guide renders for ${u.id}`);
  A.beginUnit();
  ok(A.order.length === u.qs.length, `${u.id}: ${A.order.length} questions in book order`);
  while (A.order[A.idx]) {
    const cur = A.order[A.idx];
    seen26.add(cur.q.type || 'mcq');
    const btns = $('opts').children;
    const correctIdx = btns.map((b, i) => (cur.opts[i] && cur.opts[i].ok) ? i : -1).filter(i => i >= 0);
    if (correctIdx.length !== 1) multiCorrect++;
    btns[correctIdx[0]].click();
    ok(A.locked, `${cur.q.id} answered`);
    A.nextQ(); n26++;
  }
  ok(A.S.done.includes(u.id), `${u.id} marked done`);
}
ok(n26 === 121, `all 121 CH26 questions answered (${n26})`);
ok(multiCorrect === 0, 'every CH26 question has exactly one correct option');
ok(['mcq', 'fill', 'tf', 'match', 'case', 'odd'].every(t => seen26.has(t)), `CH26 covers all 6 formats: ${[...seen26].sort().join(', ')}`);
console.log('— after CH26'); ok(A.CHAPTERS.filter(c => c.live).length === LIVE, 'live chapter count unchanged after playthrough');

/* ---------------- 7. full CH27 playthrough (Asthma) ---------------- */
console.log('— full CH27 playthrough (141 Q / 10 units)');
const ch27u = A.unitsOf(27);
ok(ch27u.length === 10, `CH27 has 10 units (${ch27u.length})`);
ok(ch27u.reduce((n, u) => n + u.qs.length, 0) === 141, 'CH27 has 141 questions');
const seen27 = new Set();
let n27 = 0, multi27 = 0;
for (const u of ch27u) {
  A.openGuide(u);
  ok($('gTitle').textContent === u.title && $('gCount').textContent.startsWith(u.qs.length + ' questions'), `guide renders for ${u.id}`);
  A.beginUnit();
  ok(A.order.length === u.qs.length, `${u.id}: ${A.order.length} questions in book order`);
  while (A.order[A.idx]) {
    const cur = A.order[A.idx];
    seen27.add(cur.q.type || 'mcq');
    const btns = $('opts').children;
    const ci = btns.map((b, i) => (cur.opts[i] && cur.opts[i].ok) ? i : -1).filter(i => i >= 0);
    if (ci.length !== 1) multi27++;
    btns[ci[0]].click();
    A.nextQ(); n27++;
  }
}
ok(n27 === 141, `all 141 CH27 questions answered (${n27})`);
ok(multi27 === 0, 'every CH27 question has exactly one correct option');
ok(['mcq', 'fill', 'tf', 'match', 'case', 'odd'].every(t => seen27.has(t)), `CH27 covers all 6 formats: ${[...seen27].sort().join(', ')}`);

/* ---------------- 8. full CH28 playthrough (Respiratory Infections) ---------------- */
console.log('— full CH28 playthrough (Respiratory Infections)');
const ch28u = A.unitsOf(28);
ok(ch28u.length === 13, `CH28 has 13 units (${ch28u.length})`);
const q28 = ch28u.reduce((n, u) => n + u.qs.length, 0);
ok(q28 === 140, `CH28 has 140 questions (${q28})`);
const seen28 = new Set();
let n28 = 0, multi28 = 0;
for (const u of ch28u) {
  A.openGuide(u);
  ok($('gTitle').textContent === u.title && $('gCount').textContent.startsWith(u.qs.length + ' questions'), `guide renders for ${u.id}`);
  A.beginUnit();
  ok(A.order.length === u.qs.length, `${u.id}: ${A.order.length} questions in book order`);
  while (A.order[A.idx]) {
    const cur = A.order[A.idx];
    seen28.add(cur.q.type || 'mcq');
    const btns = $('opts').children;
    const ci = btns.map((b, i) => (cur.opts[i] && cur.opts[i].ok) ? i : -1).filter(i => i >= 0);
    if (ci.length !== 1) multi28++;
    btns[ci[0]].click();
    A.nextQ(); n28++;
  }
}
ok(n28 === q28, `all ${q28} CH28 questions answered (${n28})`);
ok(multi28 === 0, 'every CH28 question has exactly one correct option');
ok(['mcq', 'fill', 'tf', 'match', 'case', 'odd'].every(t => seen28.has(t)), `CH28 covers all 6 formats: ${[...seen28].sort().join(', ')}`);

/* ---------------- 9. full CH29–CH42 playthroughs (Cardio, Renal, Neurology) ---------------- */
const NEW_CH = { 29: [6, 88], 30: [6, 71], 31: [10, 149], 32: [11, 143], 33: [9, 110], 34: [8, 93], 35: [9, 114], 36: [5, 67], 37: [6, 114], 38: [4, 74], 39: [5, 123], 40: [6, 135], 41: [7, 169], 42: [6, 139] };
for (const ch of Object.keys(NEW_CH)) {
  const [uN, qN] = NEW_CH[ch];
  const cu = A.unitsOf(+ch);
  ok(cu.length === uN, `CH${ch} has ${uN} units (${cu.length})`);
  const qTotal = cu.reduce((n, u) => n + u.qs.length, 0);
  ok(qTotal === qN, `CH${ch} has ${qN} questions (${qTotal})`);
  const seen = new Set();
  let played = 0, multi = 0;
  for (const u of cu) {
    A.openGuide(u);
    ok($('gTitle').textContent === u.title && $('gCount').textContent.startsWith(u.qs.length + ' questions'), `guide renders for ${u.id}`);
    A.beginUnit();
    ok(A.order.length === u.qs.length, `${u.id}: ${A.order.length} questions in book order`);
    while (A.order[A.idx]) {
      const cur = A.order[A.idx];
      seen.add(cur.q.type || 'mcq');
      const btns = $('opts').children;
      const ci = btns.map((b, i) => (cur.opts[i] && cur.opts[i].ok) ? i : -1).filter(i => i >= 0);
      if (ci.length !== 1) multi++;
      btns[ci[0]].click();
      A.nextQ(); played++;
    }
    ok(A.S.done.includes(u.id), `${u.id} marked done`);
  }
  ok(played === qN, `all ${qN} CH${ch} questions answered (${played})`);
  ok(multi === 0, `every CH${ch} question has exactly one correct option`);
  ok(['mcq', 'fill', 'tf', 'match', 'case', 'odd'].every(t => seen.has(t)), `CH${ch} covers all 6 formats: ${[...seen].sort().join(', ')}`);
}
console.log('— after CH29–CH42'); ok(A.CHAPTERS.filter(c => c.live).length === LIVE, 'live chapter count unchanged after batch playthroughs');

console.log(fails ? `\n${fails} FAILURES` : '\nALL CHECKS PASSED ✓');
process.exit(fails ? 1 : 0);
