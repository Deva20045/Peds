#!/usr/bin/env python3
"""Repair MATCH questions bank-wide.

audit.py's build_match() computed the displayed-column-B order and the
'correct' option using inverse permutations of each other, so for ~2/3 of
auto-built match questions the marked-correct option is NOT the true mapping.

Ground truth lives in every match exp:  "Correct pairs: A→v1; B→v2; C→v3; D→v4. (Book p#)"
where v_i are the TRUE values (not the displayed column-B order).

This script re-derives the true mapping from exp, guarantees an option string
equal to that mapping exists (replacing the bogus answer option if needed),
points ans at it, and rewrites the chN_data.py files.
"""
import glob, importlib.util, re, sys

PAT = re.compile(r"^A-(\d), B-(\d), C-(\d), D-(\d)$")


def true_mapping_from_exp(exp, pairs):
    """Return [pA,pB,pC,pD] where p_i = 1-based displayed position of A_i's true value."""
    m = re.search(r"Correct pairs:\s*(.*?)\.\s*\(Book", exp)
    if not m:
        return None
    # split on ';' but a fragment without '→' belongs to the previous value
    vals = []
    for part in m.group(1).split(";"):
        part = part.strip()
        if "→" in part:
            vals.append(part.split("→", 1)[1].strip())
        elif vals:
            vals[-1] += "; " + part
    if len(vals) != 4:
        return None
    colB = [p[1].strip().casefold() for p in pairs]
    perm = []
    for v in vals:
        vf = v.casefold()
        if vf not in colB:
            return None
        perm.append(colB.index(vf) + 1)
    if sorted(perm) != [1, 2, 3, 4]:
        return None
    return perm


def opt_str(perm):
    return ", ".join(f"{chr(65+i)}-{perm[i]}" for i in range(4))


def fix_questions(questions, label):
    fixed = 0
    for q in questions:
        if q.get("type") != "match":
            continue
        exp, pairs, opts = q["exp"], q["pairs"], q["opts"]
        perm = true_mapping_from_exp(exp, pairs)
        if perm is None:
            print(f"  !! {q.get('id')}: cannot derive mapping — skipped")
            continue
        truth = opt_str(perm)
        cur = opts[q["ans"]]
        if cur == truth:
            continue
        if truth in opts:
            q["ans"] = opts.index(truth)
        else:
            # replace the bogus answer option with the true mapping
            opts[q["ans"]] = truth
        fixed += 1
        print(f"  fixed {q.get('id')}: {cur!r} -> {truth!r}")
    return fixed


def load(fp):
    spec = importlib.util.spec_from_file_location("m_" + re.sub(r"\W", "_", fp), fp)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def write_module(fp, mod):
    header = getattr(mod, "__doc__", "") or ""
    lines = []
    lines.append('"""' + header.strip() + '"""' if header.strip() else "")
    src = open(fp, encoding="utf-8").read()
    # Replace UNITS/QUESTIONS literals by re-dumping them with pprint (stable, valid python)
    import pprint
    new_src = re.sub(r"^CH\s*=.*$", f"CH = {mod.CH}", src, flags=re.M)
    new_src = re.sub(r"^UNITS\s*=.*?(?=^QUESTIONS\s*=)", "UNITS = " + pprint.pformat(mod.UNITS, width=100000, sort_dicts=False) + "\n\n", new_src, flags=re.M | re.S)
    new_src = re.sub(r"^QUESTIONS\s*=.*$", "QUESTIONS = " + pprint.pformat(mod.QUESTIONS, width=100000, sort_dicts=False) + "\n", new_src, flags=re.M | re.S)
    open(fp, "w", encoding="utf-8").write(new_src)


def main():
    files = sorted(glob.glob("ch*_data.py"), key=lambda f: int(re.search(r"ch(\d+)_", f).group(1)))
    total = 0
    for fp in files:
        mod = load(fp)
        n = fix_questions(mod.QUESTIONS, fp)
        if n:
            write_module(fp, mod)
        total += n
    # verify
    bad = 0
    for fp in files:
        mod = load(fp)
        for q in mod.QUESTIONS:
            if q.get("type") != "match":
                continue
            perm = true_mapping_from_exp(q["exp"], q["pairs"])
            if perm is None or q["opts"][q["ans"]] != opt_str(perm):
                bad += 1
                print(f"STILL WRONG: {fp} {q['id']}")
    print(f"\nfixed {total} match questions; remaining wrong: {bad}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
