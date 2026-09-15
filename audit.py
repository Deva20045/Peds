#!/usr/bin/env python3
"""
PULSE Paediatrics — question bank re-audit pipeline (format mix + distractor quality).

What it does, per chapter (ch*_data.py):
  A. TRIM giveaway correct-answers (parentheticals, trailing clauses) — detail moves to `exp`.
  B. REPLACE weak distractors (Surgery / Observation only / Only-X / Normal-X / very short
     filler vs long correct) with REAL same-topic sibling answers mined from the same
     unit/chapter (substring-safe, length-matched, deduped).
  C. FORMAT CONVERSION:
       - stems ending with "—" become FILL-UP questions ("___" blank)
       - a spread of those become TRUE/FALSE statements instead (verb-safelist grammar
         check; FALSE variants swap in a plausible distractor; T/F alternated ~50/50)
       - one MATCH-THE-FOLLOWING per eligible unit, auto-built from 4 consecutive
         short-answer facts (column B shown deranged; options = mapping combinations)
  D. INSERT hand-crafted CLINICAL CASES (bank_cases.py) and ODD-ONE-OUT (bank_odd.py)
     at the end of their target units.
  E. Normalize `sec` to the unit's short section title, rotate the answer index,
     renumber ids per chapter, rebuild unit->question refs, keep strict book order.

Usage:  python3 audit.py           # apply + write files
        python3 audit.py --report  # dry-run, print quality report only
"""
import glob, importlib.util, random, re, sys, copy, collections

DRY = "--report" in sys.argv
rng = random.Random(20260915)

# ----------------------------------------------------------------------------- helpers
GENERIC_DISTRACTOR = re.compile(
    r"^(surgery|observation only|does not exist|none of these|all of the above|"
    r"no treatment|not applicable|no change|no effect)$", re.I)
SOFT_GENERIC = re.compile(
    r"^(none|no|yes|normal|never|both|"
    r"only [a-z .\-/]{1,24}|normal [a-z .\-/]{1,24}|no [a-z .\-/]{1,24})$", re.I)
BINARY_WORDS = {"yes", "no", "present", "absent", "normal", "both", "never", "true",
                "false", "positive", "negative"}
ADJ_BLACKLIST = {"abundant", "scanty", "absent", "present", "increased", "decreased",
                 "reduced", "normal", "abnormal", "common", "rare", "generalized",
                 "localised", "localized", "diffuse"}

EPONYMS = {
    "down", "turner", "klinefelter", "noonan", "digeorge", "williams", "prader", "angelman",
    "crouzon", "apert", "carpenter", "seckel", "rett", "epstein", "bohn", "ballard", "apgar",
    "silverman", "anderson", "downe", "bell", "kramer", "pedersen", "hutchinson", "clutton",
    "nagayama", "koplik", "pastia", "forchheimer", "fanconi", "potter", "barrett",
    "hirschsprung", "meckel", "wilms", "beckwith", "wiedemann", "russell", "silver",
    "kallmann", "soto", "marfan", "morquio", "hunter", "hurler", "sanfilippo", "beckwith-wiedemann",
    "de", "laurence", "moon", "bardet", "biedl", "ehlers", "danlos", "maroteaux", "lamy",
    "lecere", "lepre", "mrsopa", "dequervain", "hashimoto", "graves", "addison", "cushing",
    "nelson", "perthes", "legg", "calve", "osgood", "schlatter", "kohler", "seaver", "freiberg",
}

VERB_SAFE = [
    "is", "are", "was", "were", "has", "have", "comprises", "consists of", "extends up to",
    "extends upto", "begins", "appears", "recovers", "presents with", "is caused by", "is due to",
    "is seen in", "is found in", "is located", "is treated with", "is scored", "is defined as",
    "is called", "is classified as", "is obtained", "is checked", "is measured", "occurs",
    "is given", "is associated with", "is suggestive of", "indicates", "should be", "can be",
    "is present", "is absent", "is seen", "is divided into", "spans", "corresponds to",
    "is based on", "is derived", "starts", "ends", "is less than", "is more than", "is used",
    "is done", "is preferred", "is best", "lies", "is maintained", "is kept", "is placed",
    "is inserted", "is given as", "is administered", "develops", "results", "presents",
    "resolves", "is known as", "shows", "reveals", "demonstrates", "causes", "results in",
    "leads to", "is positive", "is negative", "crosses", "remains", "is formed", "is secreted",
    "is excreted", "is metabolized", "is conjugated", "occurs in", "occurs at", "is born",
    "is achieved", "is attained", "is reached", "is produced", "is released", "is absorbed",
    "is lost", "is gained", "is added", "is avoided", "is suspected", "is diagnosed",
    "is inherited", "is transmitted", "is affected", "is involved", "is preserved",
    "is delayed", "is advanced", "is reduced", "is increased", "is decreased",
    "stands for", "is managed with", "are seen in", "is calculated as", "occurs due to",
    "are associated with", "is used in", "is indicated in", "is contraindicated in",
    "is used for", "is also called", "m/c seen in", "gets", "means",
    "cause", "causes", "results from", "is obtained from", "is derived from",
]

def sec_short(sec):
    return sec.split(" · p")[0].strip()

def is_num(s):
    return bool(re.search(r"\d", s))

def looks_proper(word):
    w = word.strip()
    if not w: return False
    if w[0] in "<>(≥≤±0123456789": return True
    if len(w) >= 2 and w[0].isupper() and w[1].isupper(): return True      # acronym (VDRL, ENBS)
    if w.lower() in EPONYMS: return True
    if len(w) >= 2 and re.fullmatch(r"[IVX]+", w): return True             # roman numerals (IV, III)
    return False

def lower_first(s):
    w = s.split()[0] if s.split() else ""
    if looks_proper(w): return s
    return s[0].lower() + s[1:] if s else s

def strip_blank(stem):
    """'X is —' -> 'X is'   (also handles '-', ':', trailing spaces)"""
    s = stem.rstrip()
    while s and s[-1] in "—-:. ":
        s = s[:-1].rstrip()
    return s

def ends_with_verb(stem):
    s = strip_blank(stem).lower()
    for v in VERB_SAFE:
        if s.endswith(" " + v): return True
    return False

def trim_correct(ans, exp):
    """Shorten giveaway correct answers; detail is preserved in exp."""
    orig = ans
    # 1. leading parenthetical-free split: "Blood (fluctuant swelling)" -> "Blood"
    m = re.match(r"^(.{4,}?)\s*\(([^()]*)\)\s*$", ans)
    if m and len(m.group(1)) >= 3 and not m.group(1).rstrip().endswith(("d/t", ">", "<", "/", "eg", "Eg")):
        head, paren = m.group(1).strip(), m.group(2).strip()
        if paren and paren.lower() not in exp.lower():
            exp = exp.rstrip()[:-1] + f"; ({paren})." if exp.rstrip().endswith(".") else exp + f" ({paren})"
        ans = head
    # 2. cut trailing clause after ";"
    if len(ans) > 34 and ";" in ans:
        head = ans.split(";")[0].strip()
        if len(head) >= 10:
            ans = head
    # 3. cut at "→"/"->" keeping first segment
    if len(ans) > 40 and ("→" in ans or "->" in ans):
        head = re.split(r"→|->", ans)[0].strip().rstrip(",;")
        if len(head) >= 10:
            ans = head
    # 4. cut at " Eg"/" eg"/"e.g."
    m = re.search(r"\s(e\.g\.|eg:|Eg:|Eg)\s", ans)
    if m and len(ans[:m.start()]) >= 8:
        ans = ans[:m.start()].strip()
    return ans, exp, ans != orig

def flag_distractor(d, correct):
    c, dl = correct.strip(), d.strip()
    if not dl: return True
    if dl.casefold() == c.casefold(): return True
    if GENERIC_DISTRACTOR.match(dl): return True
    # binary-flavoured questions legitimately use Yes/No/Present/Absent/Normal distractors
    cb, db = c.lower() in BINARY_WORDS, dl.lower() in BINARY_WORDS
    if cb and db: return False
    if SOFT_GENERIC.match(dl):
        # soft filler is only a problem when the correct answer is long/compound
        if "+" in c or " and " in c.lower(): return True
        if len(c) >= 25 and len(dl) < 0.45 * len(c): return True
        return False
    return False

def sibling_pool(chapter_qs, unit_qs, correct, compound_only=False):
    """Real answer values from the SAME SECTION ONLY (tight topic match)."""
    c_low = correct.strip().lower()
    is_bin = c_low in BINARY_WORDS
    def ok(cand):
        cl, c = cand.strip().lower(), correct.strip().lower()
        if cl == c: return False
        if cl in c or c in cl: return False               # substring -> possibly also true
        if GENERIC_DISTRACTOR.match(cand.strip()): return False
        if SOFT_GENERIC.match(cand.strip()) and not is_bin: return False
        if compound_only and not re.search(r"[,+/;]", cand): return False
        if len(cand) < 2: return False
        words = cand.split()
        if len(words) == 1 and words[0].lower() in ADJ_BLACKLIST and not is_bin: return False
        return True
    pool = []
    for q in unit_qs:
        if q.get("type") not in (None, "mcq", "fill"): continue   # never mine tf/match/case/odd options
        cand = q["opts"][q["ans"]].strip()
        if ok(cand) and cand not in pool: pool.append(cand)
    return pool

def replace_distractors(q, unit_qs, chapter_qs, stats):
    a = q["ans"]; correct = q["opts"][a]
    counts = collections.Counter(o.strip().casefold() for o in q["opts"])
    flagged = [i for i, o in enumerate(q["opts"])
               if i != a and (flag_distractor(o, correct) or counts[o.strip().casefold()] > 1)]
    if not flagged: return
    pool = sibling_pool(chapter_qs, unit_qs, correct)
    # keep numeric-ness consistent when possible
    if is_num(correct):
        pool.sort(key=lambda c: (not is_num(c), abs(len(c) - len(correct))))
    else:
        pool.sort(key=lambda c: (is_num(c) and is_num(correct) is False, abs(len(c) - len(correct))))
    used = {o.strip().casefold() for o in q["opts"]}
    for i in flagged:
        cand = next((c for c in pool if c.strip().casefold() not in used), None)
        if cand:
            q["opts"][i] = cand
            used.add(cand.strip().casefold())
            stats["distractor_replaced"] += 1
        else:
            stats["distractor_left"] += 1

# ------------------------------------------------------------------ match building
def clean_a_item(stem):
    s = stem.rstrip()
    if s.endswith("___"): s = s[:-3].rstrip()
    if s.endswith("—"): s = s[:-1].rstrip()
    for v in (" is due to", " are due to", " is caused by", " are caused by", " is seen in",
              " is found in", " is located", " presents with", " extends up to", " is managed with",
              " is treated with", " is used in", " is used for", " is indicated in", " stands for",
              " is also called", " is calculated as", " is associated with", " is suggestive of",
              " appears", " recovers", " begins", " comprises", " spans", " occurs", " develops",
              " presents", " starts", " ends", " shows", " reveals", " gets", " means", " are", " is"):
        if s.endswith(v): s = s[: -len(v)].rstrip()
    s = re.sub(r"^(The |A |An )", "", s)
    s = s.rstrip(" ?.:")
    if s and s[0].islower(): s = s[0].upper() + s[1:]
    return s

BAD_ITEM_TAIL = ("by", "from", "as", "aka", "in", "on", "with", "due", "to", "for",
                 "seen", "known", "called", "m/c", "of", "also", "and", "or")

def item_word_overlap(item, vals):
    """True if the A-item leaks a B-value word (>=6 chars) — reverse-question garbage guard."""
    iw = {w.strip(".,;:()/'’").lower() for w in item.split()}
    iw = {w for w in iw if len(w) >= 6}
    for v in vals:
        vw = {w.strip(".,;:()/'’").lower() for w in v.split()}
        if iw & vw: return True
    return False

def build_match(unit_qs, stats):
    """One match question from a run of up-to-4 short-answer facts (1 gap tolerated).
    Returns (match_q, insert_after_id) so it lands right after its source facts."""
    best = None
    run, gap = [], 0
    for q in unit_qs:
        if q.get("type") in ("tf", "match", "case", "odd"):
            run, gap = [], 0; continue
        stem = q["q"].rstrip()
        a = q["opts"][q["ans"]].strip()
        item = clean_a_item(stem)
        ok = (not stem.lower().startswith(("which", "in the book", "all these", "a baby", "a child",
                                           "consider", "match"))
              and "—" not in item and not item.endswith(BAD_ITEM_TAIL)
              and len(item) >= 6 and len(item) <= 62 and len(a) <= 32 and len(a) >= 2
              and re.search(r"[A-Za-z]", item) and re.search(r"[A-Za-z0-9]", a))
        ok = (ok and not item_word_overlap(item, [x[2] for x in run] + [a]))
        if ok:
            run.append((q, item, a)); gap = 0
            if len(run) >= 4:
                best = list(run[-4:]); break
        elif run and gap == 0:
            gap = 1                                    # tolerate one skipped question
        else:
            run, gap = [], 0
    if not best: return None
    items = [b[1] for b in best]; vals = [b[2] for b in best]
    if len({v.casefold() for v in vals}) < 4 or len({i.casefold() for i in items}) < 4: return None
    if any(item_word_overlap(i, vals) for i in items): return None
    # deranged display order for column B (never identity)
    order = list(range(4))
    while True:
        rng.shuffle(order)
        if all(order[i] != i for i in range(4)): break
    disp = [vals[order.index(i)] for i in range(4)]              # disp[j] = value shown at position j+1
    def mp(perm):  # perm[i] = displayed position (0-based) for A_i
        return ", ".join(f"{chr(65+i)}-{perm[i]+1}" for i in range(4))
    true_perm = [order.index(i) for i in range(4)]               # A_i true value at displayed index
    correct_opt = mp(true_perm)
    others = []
    tries = 0
    while len(others) < 3 and tries < 200:
        tries += 1
        perm = list(range(4)); rng.shuffle(perm)
        s = mp(perm)
        if s != correct_opt and s not in others and perm != true_perm:
            others.append(s)
    if len(others) < 3: return None
    opts = [correct_opt] + others
    page = best[-1][0]["page"]
    exp = "Correct pairs: " + "; ".join(f"{chr(65+i)}→{vals[i]}" for i in range(4)) + f". (Book p{page})"
    mq = {
        "type": "match",
        "sec": best[0][0]["sec"],
        "page": page,
        "q": "Match Column A with Column B — select the correctly matched combination:",
        "pairs": [[items[i], disp[i]] for i in range(4)],
        "opts": opts,
        "ans": 0,
        "exp": exp,
    }
    stats["match_built"] += 1
    return mq, best[-1][0]["id"]

# ------------------------------------------------------------------ main pipeline
def load_chapters():
    out = []
    for fp in sorted(glob.glob("ch*_data.py"), key=lambda f: int(re.search(r"ch(\d+)_", f).group(1))):
        spec = importlib.util.spec_from_file_location(fp[:-3], fp)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        out.append((int(re.search(r"ch(\d+)_", fp).group(1)), mod.UNITS, mod.QUESTIONS))
    return out

def main():
    stats = collections.Counter()
    chapters = load_chapters()
    result = {}

    for ch, units, questions in chapters:
        qmap = {q["id"]: q for q in questions}
        unit_qs = [[qmap[qid] for qid in u["qs"]] for u in units]

        # ---- A0: drop source junk (video-timestamp metadata, Yes/No table artifacts)
        for uq in unit_qs:
            junk = [q for q in uq if "timestamp" in q["q"].lower()
                    or (q["opts"][q["ans"]].strip().lower() in ("yes", "no")
                        and sum(1 for i, o in enumerate(q["opts"])
                                if i != q["ans"] and o.strip().lower() in ("yes", "no", "only pharm")) >= 2)]
            for q in junk:
                uq.remove(q)
                stats["junk_dropped"] += 1

        # ---- A+B: trim correct answers, fix distractors (two passes so pools include trims)
        for _ in range(2):
            for uq in unit_qs:
                for q in uq:
                    newa, newexp, changed = trim_correct(q["opts"][q["ans"]], q["exp"])
                    if changed:
                        q["opts"][q["ans"]] = newa; q["exp"] = newexp; stats["trimmed"] += 1
                    replace_distractors(q, uq, questions, stats)

        # ---- C0: auto match per unit (built first, inserted right after its 4 source facts)
        unit_matches = []
        for u, uq in zip(units, unit_qs):
            built = build_match(uq, stats)
            if built:
                mq, after_id = built
                mq["sec"] = sec_short(u["sec"])
                unit_matches.append((uq, mq, after_id))

        # ---- C: format conversion (TF avoids questions already used as match sources)
        match_src_ids = {aid for _, _, aid in unit_matches}
        tf_true_next = rng.random() < 0.5

        def make_tf(q, base, mode):
            """Convert q to a True/False statement in place. Returns True on success."""
            nonlocal tf_true_next
            correct = q["opts"][q["ans"]].strip()
            if correct.endswith(("+", "/", ">", "→", "-", ",", "and", "or", "with", "d/t")):
                return False
            if correct.split()[0].lower() in ("assess", "check", "look", "do", "give", "start",
                                              "consider", "monitor", "lookfor", "rule"):
                return False
            if mode == "copula":
                w = base.split()[-1].lower()
                unit_words = {"months", "weeks", "days", "years", "hours", "minutes", "cm", "kg",
                              "sd", "ml", "mg", "dl", "wks", "hr"}
                plural = (re.search(r"[a-z]s$", w) and w not in unit_words
                          and not re.search(r"(ss|sis|us)$", w))
                cop = "are" if plural else "is"
                base = f"{base} {cop}"
            ds = [o.strip() for j, o in enumerate(q["opts"]) if j != q["ans"]]
            ds = [d for d in ds if not d.endswith(("+", "/", ">", "→", "-", ",", "and", "or", "with", "d/t"))]
            ds.sort(key=lambda d: (is_num(d) != is_num(correct), abs(len(d) - len(correct))))
            if tf_true_next or not ds:
                stmt = f"{base} {lower_first(correct)}."
                q.update(type="tf", q=stmt, opts=["True", "False"], ans=0, exp="True — " + q["exp"])
            else:
                stmt = f"{base} {lower_first(ds[0])}."
                q.update(type="tf", q=stmt, opts=["True", "False"], ans=1,
                         exp=f"False — correct: {correct}. {q['exp']}")
            tf_true_next = not tf_true_next
            return True

        for uq in unit_qs:
            # TF candidates: (index, join_mode) — 'direct' = stem ends with a verb,
            # 'copula' = short topic-header noun phrase joined with is/are
            cands = []
            for i, q in enumerate(uq):
                if q.get("type") not in (None, "mcq") or q["id"] in match_src_ids: continue
                stem = q["q"].rstrip()
                a = q["opts"][q["ans"]].strip()
                if len(a) > 60 or len(stem) > 92: continue
                if a.endswith(("+", "/", ">", "→", "-", ",", "and", "or", "with", "d/t")): continue
                low = stem.lower()
                if stem.endswith("—") and ends_with_verb(stem):
                    cands.append((i, "direct")); continue
                if stem.endswith(("?", ".", ":", "—", "→", ">", "/", "+")) or low.startswith(
                        ("which", "all", "a baby", "a child", "in the book", "consider", "match",
                         "after ", "before ", "when ", "if ", "during ", "without ")):
                    continue
                if " how " in f" {low} " or "image" in low:
                    continue
                last = low.split()[-1] if low.split() else ""
                if last in ("includes", "comprises", "means", "shows", "reveals", "presents",
                            "starts", "ends", "occurs", "causes", "cause", "gives", "gets", "acts",
                            "leads", "disappears", "persists", "resolves", "recurs", "progresses",
                            "develops", "appears", "begins", "improves", "worsens", "increases",
                            "decreases"):
                    continue
                if ends_with_verb(stem):
                    cands.append((i, "direct"))
                elif (len(stem) <= 52 and re.search(r"[A-Za-z]$", stem)
                      and not low.endswith(("and", "or", "of", "the", "in", "to", "for", "with",
                                            "due", "by", "from", "as", "at", "on", "upon", "into"))):
                    topical = (" of " in low or low.startswith((
                        "etiology", "treatment", "investigation", "complication", "cause", "diagnosis",
                        "prognosis", "prevention", "onset", "incubation", "management", "drug", "dose",
                        "vaccine", "agent", "vector", "period", "age group", "clinical features",
                        "risk factor", "contraindication", "features", "manifestation", "signs",
                        "symptoms", "site", "source", "route", "stage")))
                    if topical:
                        cands.append((i, "copula"))
            n_tf = 2 if len(cands) >= 6 else (1 if cands else 0)
            tf_pos = {}
            if n_tf >= 1: tf_pos[cands[len(cands) // 3][0]] = cands[len(cands) // 3][1]
            if n_tf >= 2: tf_pos[cands[(2 * len(cands)) // 3][0]] = cands[(2 * len(cands)) // 3][1]
            # leftovers (topic-header stems) can become FILL-UPS: "Etiology of X is ___"
            fill_pos = {}
            n_fill_conv = min(6, max(0, 3 - len([i for i in tf_pos if uq[i]["q"].rstrip().endswith("—")])))
            for i, mode in cands:
                if i in tf_pos or n_fill_conv <= 0: continue
                if rng.random() < 0.4:
                    fill_pos[i] = mode; n_fill_conv -= 1
            # short table-row fragments ("Head control", "Peaks by", "6 months") → "Head control: ___"
            frag_pos = set()
            for i, q in enumerate(uq):
                if i in tf_pos or i in fill_pos or q["id"] in match_src_ids: continue
                if q.get("type") not in (None, "mcq"): continue
                stem = q["q"].rstrip()
                low = stem.lower()
                if (len(stem) <= 26 and not stem.endswith(("?", ".", ":", "—"))
                        and not low.startswith(("which", "how", "all", "in the book"))
                        and not stem.isdigit() and re.search(r"[A-Za-z]", stem)
                        and rng.random() < 0.45 and len(frag_pos) < 5):
                    frag_pos.add(i)
            for i, q in enumerate(uq):
                stem = q["q"].rstrip()
                if not stem.endswith("—"):
                    if i in tf_pos:
                        if make_tf(q, strip_blank(stem), tf_pos[i]):
                            stats["tf"] += 1
                        else:
                            q["type"] = "mcq"
                    elif i in fill_pos:
                        q["type"] = "fill"
                        q["q"] = f"{stem} ___" if fill_pos[i] == "direct" else f"{stem} is ___"
                        stats["fill_topic"] += 1
                    elif i in frag_pos:
                        q["type"] = "fill"
                        q["q"] = f"{stem} ___" if stem.lower().endswith(("by", "till", "=", "in", "at")) else f"{stem}: ___"
                        stats["fill_frag"] += 1
                    else:
                        q["type"] = "mcq"
                    continue
                if i in tf_pos:
                    if make_tf(q, strip_blank(stem), "direct"):
                        stats["tf"] += 1
                    else:
                        q["type"] = "fill"
                        q["q"] = re.sub(r"\s*—\s*$", " ___", stem)
                else:
                    q["type"] = "fill"
                    q["q"] = re.sub(r"\s*—\s*$", " ___", stem)
            for q in uq:
                if q.get("type") in (None, "mcq"): q["type"] = "mcq"

        # ---- C2: insert the pre-built match questions after their source facts
        for uq, mq, after_id in unit_matches:
            pos = next((i for i, q in enumerate(uq) if q["id"] == after_id), len(uq) - 1)
            uq.insert(pos + 1, mq)

        # ---- D: hand-crafted banks (page = the unit's last page → book order preserved)
        try:
            from bank_cases import CASES
        except ImportError:
            CASES = []
        try:
            from bank_odd import ODD
        except ImportError:
            ODD = []
        def unit_last_page(u, uq):
            return max([q["page"] for q in uq], default=u["sec"].split("p")[-1].split("·")[-1].strip() or 1)
        for entry in CASES:
            if entry["ch"] != ch: continue
            u = next((x for x in units if x["id"] == entry.get("unit") or
                      entry.get("unit_title", "").lower() in x["title"].lower()), None)
            if u is None:
                print(f"  !! CASE unit not found ch{ch}: {entry.get('unit') or entry.get('unit_title')}")
                stats["case_missed"] += 1; continue
            ui = units.index(u)
            cq = {"type": "case", "sec": sec_short(u["sec"]), "page": unit_last_page(u, unit_qs[ui]),
                  "stem": entry["stem"], "q": entry["q"], "opts": entry["opts"],
                  "ans": entry["ans"], "exp": entry["exp"]}
            unit_qs[ui].append(cq); stats["case"] += 1
        for entry in ODD:
            if entry["ch"] != ch: continue
            ut = (entry.get("unit_title") or "").lower()
            u = next((x for x in units if x["id"] == entry.get("unit") or
                      (ut and ut in x["title"].lower())), None)
            if u is None:
                print(f"  !! ODD unit not found ch{ch}: {entry.get('unit') or entry.get('unit_title')}")
                stats["odd_missed"] += 1; continue
            ui = units.index(u)
            oq = {"type": "odd", "sec": sec_short(u["sec"]), "page": unit_last_page(u, unit_qs[ui]),
                  "q": entry["q"], "opts": entry["opts"], "ans": entry["ans"], "exp": entry["exp"]}
            unit_qs[ui].append(oq); stats["odd"] += 1

        # ---- D2: final enrichment — remaining length-giveaways get compound sibling distractors
        for uq in unit_qs:
            for q in uq:
                if q["type"] not in ("mcq", "fill"): continue
                a = q["ans"]; c = q["opts"][a]
                ds = [(i, o) for i, o in enumerate(q["opts"]) if i != a]
                if len(c) < 25 or not all(len(c) > 1.6 * len(o) for _, o in ds): continue
                pool = sibling_pool(questions, uq, c, compound_only=True)
                pool = [p for p in pool if len(p) > 0.45 * len(c)]
                pool.sort(key=lambda p: abs(len(p) - len(c)))
                used = {o.strip().casefold() for o in q["opts"]}
                for i, o in ds:
                    if len(c) <= 1.6 * len(q["opts"][i]): continue
                    cand = next((p for p in pool if p.strip().casefold() not in used), None)
                    if cand:
                        q["opts"][i] = cand; used.add(cand.strip().casefold())
                        stats["compound_enriched"] += 1

        # ---- E: normalize sec, rotate ans, renumber, rebuild
        final = []
        for u, uq in zip(units, unit_qs):
            for q in uq:
                q["sec"] = sec_short(u["sec"])
                final.append(q)
        for q in final:
            if q["type"] in ("mcq", "fill", "odd", "match") and len(q["opts"]) == 4:
                pos = rng.randrange(4)
                if pos != q["ans"]:
                    opts = q["opts"][:]
                    opts[pos], opts[q["ans"]] = opts[q["ans"]], opts[pos]
                    q["opts"] = opts; q["ans"] = pos
        for n, q in enumerate(final, 1):
            q["id"] = f"PEDS-C{ch}-{n:03d}"
        for u, uq in zip(units, unit_qs):
            u["qs"] = [q["id"] for q in uq]
        result[ch] = (units, final)

    # ---------------------------------------------------------------- report
    print("== stats ==", dict(stats))
    allq = [q for _, (_, qs) in result.items() for q in qs]
    print("total:", len(allq))
    print("types:", dict(collections.Counter(q["type"] for q in allq)))
    giveaway = sum(1 for q in allq if len(q["opts"]) == 4 and
                   all(len(q["opts"][q["ans"]]) > 1.6 * len(o) for i, o in enumerate(q["opts"]) if i != q["ans"]))
    print(f"length-giveaway: {giveaway} ({100*giveaway/len(allq):.1f}%)  [was 875 / 46.9%]")
    gen = sum(1 for q in allq for i, o in enumerate(q["opts"]) if i != q["ans"] and GENERIC_DISTRACTOR.match(o.strip())
              and not (q["opts"][q["ans"]].strip().lower() in BINARY_WORDS))
    print(f"generic distractors left: {gen}  [was ~546]")
    ansdist = collections.Counter(q["ans"] for q in allq)
    print("ans index dist:", dict(sorted(ansdist.items())))

    if DRY:
        # print a sample of rewritten questions for eyeballing
        sample = [q for q in allq if q["type"] == "tf"][:6] + \
                 [q for q in allq if q["type"] == "match"][:4] + \
                 [q for q in allq if q["type"] == "fill"][:6]
        for q in sample:
            print("----", q["id"], q["type"])
            print("   Q:", q["q"][:160])
            print("   opts:", q["opts"], "| ans:", q["ans"])
        return

    # ---------------------------------------------------------------- write files
    for ch, (units, final) in sorted(result.items()):
        with open(f"ch{ch}_data.py", "w", encoding="utf-8") as f:
            f.write(f'"""CH{ch} — re-audited: format mix (mcq/fill/tf/match/case/odd) + tuned distractors.\n'
                    f'Auto-generated by audit.py — hand-tuned content lives in bank_cases.py / bank_odd.py."""\n')
            f.write(f"CH = {ch}\nUNITS = ")
            f.write(repr(units))
            f.write("\nQUESTIONS = ")
            f.write(repr(final))
            f.write("\n")
        print(f"wrote ch{ch}_data.py ({len(final)} Q, {len(units)} U)")

if __name__ == "__main__":
    main()
