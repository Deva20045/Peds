#!/usr/bin/env python3
"""Data-integrity validation for the re-audited PULSE Paediatrics bank."""
import glob, importlib.util, re, sys, collections

TYPES = {"mcq", "fill", "tf", "match", "case", "odd"}
errors, warns = [], []

all_ids = set()
per_type = collections.Counter()
files = sorted(glob.glob("ch*_data.py"), key=lambda f: int(re.search(r"ch(\d+)_", f).group(1)))
for fp in files:
    ch = int(re.search(r"ch(\d+)_", fp).group(1))
    spec = importlib.util.spec_from_file_location(fp[:-3], fp)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    units, questions = mod.UNITS, mod.QUESTIONS
    qmap = {q["id"]: q for q in questions}

    # ids unique bank-wide, sequential per chapter
    for n, q in enumerate(questions, 1):
        if q["id"] in all_ids: errors.append(f"{fp}: duplicate id {q['id']}")
        all_ids.add(q["id"])
        if q["id"] != f"PEDS-C{ch}-{n:03d}":
            errors.append(f"{fp}: id {q['id']} not sequential (expected PEDS-C{ch}-{n:03d})")
        t = q.get("type")
        if t not in TYPES: errors.append(f"{q['id']}: bad type {t!r}")
        per_type[t] += 1
        # per-type rules
        if t == "tf":
            if q["opts"] != ["True", "False"]: errors.append(f"{q['id']}: tf opts must be True/False")
            if q["ans"] not in (0, 1): errors.append(f"{q['id']}: tf ans must be 0/1")
            if "True —" not in q["exp"] and "False —" not in q["exp"]:
                warns.append(f"{q['id']}: tf exp lacks True/False prefix")
        elif t == "fill":
            if "___" not in q["q"]: errors.append(f"{q['id']}: fill missing ___ blank")
        elif t == "match":
            if len(q.get("pairs", [])) != 4: errors.append(f"{q['id']}: match needs 4 pairs")
            maps = [o for o in q["opts"]]
            pat = re.compile(r"^A-\d, B-\d, C-\d, D-\d$")
            if not all(pat.match(o) for o in maps): errors.append(f"{q['id']}: match opts not mapping strings")
            if len(set(maps)) != 4: errors.append(f"{q['id']}: match options not distinct")
            # correct option must be a true permutation and differ from others
            nums = [int(x) for x in re.findall(r"\d", maps[q["ans"]])]
            if sorted(nums) != [1, 2, 3, 4]: errors.append(f"{q['id']}: match answer not a permutation")
        elif t == "case":
            if not q.get("stem"): errors.append(f"{q['id']}: case missing stem")
        # generic option rules
        if t != "tf":
            if len(q["opts"]) != 4: errors.append(f"{q['id']}: {len(q['opts'])} opts (need 4)")
            if len({o.strip().casefold() for o in q["opts"]}) != 4:
                errors.append(f"{q['id']}: duplicate options {q['opts']}")
            if not (0 <= q["ans"] < len(q["opts"])): errors.append(f"{q['id']}: ans out of range")
            if not q.get("exp"): errors.append(f"{q['id']}: missing exp")
            if "Book p" not in q["exp"]: warns.append(f"{q['id']}: exp lacks Book page ref")
        if not isinstance(q.get("page"), int): errors.append(f"{q['id']}: page not int")

    # unit refs complete + ordered + pages non-decreasing (strict book order)
    seen = []
    for u in units:
        for qid in u["qs"]:
            if qid not in qmap: errors.append(f"{fp}: unit {u['id']} refs missing {qid}")
            else: seen.append(qid)
    if seen != [q["id"] for q in questions]:
        errors.append(f"{fp}: unit order != question order (strict book order broken)")
    pages = [qmap[qid]["page"] for qid in seen if qid in qmap]
    if pages != sorted(pages):
        bad = [(i, pages[i-1], pages[i]) for i in range(1, len(pages)) if pages[i] < pages[i-1]]
        errors.append(f"{fp}: pages not non-decreasing at {bad[:3]}")

print(f"files: {len(files)} | questions: {len(all_ids)} | types: {dict(per_type)}")
print(f"errors: {len(errors)} | warnings: {len(warns)}")
for e in errors[:25]: print("  ERR:", e)
for w in warns[:10]: print("  warn:", w)
sys.exit(1 if errors else 0)
