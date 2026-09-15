#!/usr/bin/env python3
"""Insert extra hand-written cases into CH21/CH23, then renumber ids sequentially
and rebuild UNITS qs arrays (per-chapter unit counts), rewriting the files."""
import importlib.util, re, pprint

NEW = {
    21: {"after": "PEDS-C21-051", "counts": [8, 10, 14, 8, 12, 10, 6, 14], "q":
         {'type': 'case', 'sec': 'Treatment', 'page': 93,
          'stem': 'A 2-year-old has COVID-19 with SpO2 91% in room air, respiratory rate 42/min; she is irritable but arousable with no danger signs.',
          'q': 'The site of care and key therapy are —',
          'opts': ['Ward of a COVID-19 hospital / DCHC with O2 (target SpO2 94–96%)', 'Home isolation with paracetamol only', 'ICU with invasive ventilation', 'No treatment needed'],
          'ans': 0,
          'exp': 'SpO2 90–93% without danger signs = moderate disease → ward of COVID-19 hospital/DCHC; O2 target 94–96%, fluid & electrolyte balance, steroids in progressive disease. (Book p92–93)'}},
    23: {"after": "PEDS-C23-103", "counts": [7, 8, 14, 12, 9, 13, 10, 14, 17], "q":
         {'type': 'case', 'sec': 'Diagnosis', 'page': 103,
          'stem': 'A 20-month-old has chronic diarrhea with failure to thrive and a dimorphic anemia not responding to 3 months of oral iron. Anti-tTG antibody is positive.',
          'q': 'The confirmatory investigation of choice (in India) is —',
          'opts': ['Small intestinal (duodenal) biopsy', 'Repeat anti-tTG titre after 6 months', 'Hb electrophoresis', 'Stool fat estimation'],
          'ans': 0,
          'exp': 'Iron-refractory dimorphic anemia + chronic diarrhea + anti-tTG +ve → celiac disease; duodenal biopsy (villous atrophy, ↑ crypt length, ↑ IEL > 30/100 enterocytes) is the IOC in India. (Book p103)'}},
}

def load(fp):
    spec = importlib.util.spec_from_file_location("rn_" + re.sub(r"\W", "_", fp), fp)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

for ch, spec in NEW.items():
    fp = f"ch{ch}_data.py"
    mod = load(fp)
    qs = mod.QUESTIONS
    idx = next(i for i, q in enumerate(qs) if q["id"] == spec["after"]) + 1
    qs.insert(idx, dict(spec["q"]))
    # renumber
    for i, q in enumerate(qs, 1):
        q["id"] = f"PEDS-C{ch}-{i:03d}"
    # rebuild units
    counts = spec["counts"]
    assert sum(counts) == len(qs), (ch, sum(counts), len(qs))
    pos = 0
    for u, c in zip(mod.UNITS, counts):
        u["qs"] = [q["id"] for q in qs[pos:pos + c]]
        pos += c
    assert pos == len(qs)
    # rewrite file
    header = (mod.__doc__ or "").strip()
    out = [f'"""{header}"""', f"CH = {ch}", "", "UNITS = " + pprint.pformat(mod.UNITS, width=100000, sort_dicts=False), "", "QUESTIONS = " + pprint.pformat(qs, width=100000, sort_dicts=False), ""]
    open(fp, "w", encoding="utf-8").write("\n".join(out))
    print(f"ch{ch}: now {len(qs)} questions, {len(mod.UNITS)} units")
print("done")
