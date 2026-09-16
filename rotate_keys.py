#!/usr/bin/env python3
"""Rotate answer positions for non-TF questions so the key is uniform.
target index = (1-based position within chapter) % 4. Rewrites files canonically."""
import importlib.util, json, sys, pathlib

def load(fp):
    spec = importlib.util.spec_from_file_location(pathlib.Path(fp).stem, fp)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

def dump(fp, m):
    src = pathlib.Path(fp).read_text(encoding="utf-8")
    # keep original docstring (first line up to closing """)
    if src.startswith('"""'):
        end = src.find('"""', 3)
        doc = src[: end + 3]
    else:
        doc = f'"""CH{m.CH} data. Line-by-line bank in strict book order."""'
    lines = [doc, f"CH = {m.CH}", "", "UNITS = ["]
    for u in m.UNITS:
        lines.append(" " + json.dumps(u, ensure_ascii=False) + ",")
    lines.append("]")
    lines.append("")
    lines.append("QUESTIONS = [")
    for q in m.QUESTIONS:
        lines.append(" " + json.dumps(q, ensure_ascii=False) + ",")
    lines.append("]")
    lines.append("")
    pathlib.Path(fp).write_text("\n".join(lines), encoding="utf-8")

def rotate(fp):
    m = load(fp)
    for i, q in enumerate(m.QUESTIONS, 1):
        if q.get("type") == "tf":
            continue
        target = i % 4
        cur = q["ans"]
        if target == cur:
            continue
        opts = q["opts"]
        rot = (target - cur) % 4
        q["opts"] = opts[-rot:] + opts[:-rot] if rot else opts
        q["ans"] = target
    dump(fp, m)
    from collections import Counter
    dist = Counter(q["ans"] for q in m.QUESTIONS if q.get("type") != "tf")
    print(f"CH{m.CH} rotated: non-TF ans dist {dict(sorted(dist.items()))}")

if __name__ == "__main__":
    for fp in sys.argv[1:]:
        rotate(fp)
