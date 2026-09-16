#!/usr/bin/env python3
"""Quality checks for new chapter data: match semantics, length-giveaway, answer-key distribution."""
import importlib.util, re, sys, json, pathlib
from collections import Counter

def load(fp):
    spec = importlib.util.spec_from_file_location(pathlib.Path(fp).stem, fp)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

def check(fp):
    m = load(fp)
    ch = m.CH
    problems = []
    for q in m.QUESTIONS:
        t = q.get("type")
        if t == "match":
            bcol = [p[1] for p in q["pairs"]]
            correct = q["opts"][q["ans"]]
            nums = [int(x) for x in re.findall(r"\d", correct)]
            if sorted(nums) != [1, 2, 3, 4]:
                problems.append(f"{q['id']}: correct opt not a permutation: {correct}")
            if correct == "A-1, B-2, C-3, D-4":
                problems.append(f"{q['id']}: correct combination is identity (B column not deranged)")
            if len(set(q["opts"])) != 4:
                problems.append(f"{q['id']}: duplicate mapping options")
        if t != "tf":
            lens = [len(o) for o in q["opts"]]
            c = lens[q["ans"]]
            longest_d = max(l for i, l in enumerate(lens) if i != q["ans"])
            if c > 1.6 * longest_d:
                problems.append(f"{q['id']}: length giveaway ({c} vs {longest_d})")
    # answer key distribution (non-TF)
    dist = Counter(q["ans"] for q in m.QUESTIONS if q.get("type") != "tf")
    tf_dist = Counter(q["ans"] for q in m.QUESTIONS if q.get("type") == "tf")
    types = Counter(q.get("type") for q in m.QUESTIONS)
    print(f"CH{ch}: {len(m.QUESTIONS)} Q | types {dict(types)} | non-TF ans dist {dict(sorted(dist.items()))} | TF dist {dict(sorted(tf_dist.items()))}")
    for p in problems:
        print("  !!", p)
    return len(problems)

if __name__ == "__main__":
    total = sum(check(fp) for fp in sys.argv[1:])
    sys.exit(1 if total else 0)
