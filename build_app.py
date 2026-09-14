#!/usr/bin/env python3
"""
PULSE Paediatrics builder - reconstructs pulse-peds-complete.html from ortho_template.html
+ peds/ch*_data.py (UNITS + QUESTIONS).
"""
import pathlib, json, re, glob, importlib.util, sys

HERE = pathlib.Path(__file__).parent
TEMPLATE = HERE / "ortho_template.html"
OUT = HERE / "pulse-peds-complete.html"
INDEX = HERE / "index.html"

# Hardcoded 54-chapter master list (from pulse-peds-complete.html, verified)
CHAPTERS_MASTER = [
    (1, "Normal Newborn", 2),
    (2, "Neonatal Resuscitation", 7),
    (3, "Necrotizing Enterocolitis and Neonatal Sepsis", 11),
    (4, "Respiratory Distress in Newborn", 16),
    (5, "Neonatal Jaundice", 21),
    (6, "Neonatal Hypothermia and Neonatal Hypoglycemia", 25),
    (7, "Neonatal Reflexes, HIE and Neonatal Seizures", 30),
    (8, "Normal Growth", 35),
    (9, "Abnormalities of Head Size and Shape", 41),
    (10, "Abnormalities of Stature", 45),
    (11, "Normal Development", 48),
    (12, "Disorders of Development", 52),
    (13, "Behavioural Disorders in Children", 54),
    (14, "Breastfeeding", 58),
    (15, "Malnutrition", 62),
    (16, "Obesity", 66),
    (17, "Rickets and Scurvy", 69),
    (18, "Genetic Disorders", 74),
    (19, "Childhood Infections", 80),
    (20, "TORCH Infections", 86),
    (21, "COVID-19 in Children", 92),
    (22, "Disorders of Oesophagus in Children", 95),
    (23, "Diarrheal Disorders in Children", 99),
    (24, "Disorders of Liver in Children", 104),
    (25, "Surgical GI Disorders in Children", 111),
    (26, "Airway Malformations and Foreign Bodies", 116),
    (27, "Asthma", 120),
    (28, "Respiratory Infections", 124),
    (29, "Cystic Fibrosis", 130),
    (30, "Fetal Circulation and Introduction to Congenital Heart Diseases", 133),
    (31, "Acyanotic Congenital Heart Defects", 136),
    (32, "Cyanotic Congenital Heart Defects", 142),
    (33, "Acute Rheumatic Fever", 149),
    (34, "Congenital Anomalies of Kidney and Urinary Tract", 153),
    (35, "Nephrotic and Nephritic Syndrome", 157),
    (36, "Inherited Tubular Disorders", 162),
    (37, "Acute Kidney Injury and Chronic Kidney Disease", 166),
    (38, "UR and UTI Management Guidelines", 171),
    (39, "Congenital Anomalies and Hydrocephalus", 175),
    (40, "Seizure Disorders", 181),
    (41, "Cerebral Palsy and CNS Infections", 187),
    (42, "Neuromuscular Disorders", 194),
    (43, "Growth Hormone Deficiency and Hypothyroidism", 199),
    (44, "Adrenal Disorders in Children", 204),
    (45, "Pubertal Disorders", 209),
    (46, "Diabetic Ketoacidosis", 213),
    (47, "Haematological Malignancies", 215),
    (48, "Solid Tumours in Children", 223),
    (49, "Rheumatic Disorders of Childhood", 227),
    (50, "Approach to Anaemia in Children and Nutritional Anaemia", 235),
    (51, "Congenital Haemolytic Anaemia", 241),
    (52, "Bleeding Disorders", 248),
    (53, "Paediatric Resuscitation", 253),
    (54, "Shock", 256),
]

def load_data():
    all_units = []
    all_questions = []
    ch_files = sorted(glob.glob(str(HERE / "ch*_data.py")))
    live_chs = set()
    for fp in ch_files:
        # Use importlib to load module
        spec = importlib.util.spec_from_file_location(pathlib.Path(fp).stem, fp)
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
        except Exception as e:
            print(f"Failed to load {fp}: {e}")
            sys.exit(1)
        # Expect UNITS and QUESTIONS attributes
        if not hasattr(mod, "UNITS") or not hasattr(mod, "QUESTIONS"):
            print(f"WARNING: {fp} missing UNITS/QUESTIONS")
            continue
        units = getattr(mod, "UNITS")
        questions = getattr(mod, "QUESTIONS")
        # live chapter is CH attribute or infer from units
        ch_num = getattr(mod, "CH", None)
        if ch_num is None:
            # infer from first unit or first question
            if units:
                ch_num = units[0].get("ch")
            elif questions:
                # parse id PEDS-C{N}
                try:
                    ch_num = int(questions[0]["id"].split("-")[1][1:])
                except:
                    ch_num = None
        if ch_num is not None:
            live_chs.add(ch_num)
        all_units.extend(units)
        all_questions.extend(questions)
        print(f"Loaded {fp}: {len(questions)} Q, {len(units)} U (CH{ch_num})")
    # Sort
    # Units by (ch, n)
    all_units.sort(key=lambda u: (u["ch"], u["n"]))
    # Questions by chapter then numeric id order (which respects book page order if author done correctly)
    # We will sort by (ch, page, numeric id) to ensure strict book order? But numeric id already reflects author order.
    # However to be safe, we should not resort questions arbitrarily; instead, we group by chapter and sort by numeric id.
    # Global QUESTIONS order must be chapter 1 questions in order, then chapter 2, etc, each unit in order.
    # Our all_questions currently in file glob order which is ch1..chN; but within chapter, they are in file order already (which is book order).
    # To ensure overall order is ch-sorted, we will sort by (ch, question_number)
    def q_sort_key(q):
        try:
            ch = int(q["id"].split("-")[1][1:])
            num = int(q["id"].split("-")[2])
            # use ch and num for ordering; page also considered but not needed
            return (ch, num)
        except:
            return (999, 999)
    all_questions.sort(key=q_sort_key)
    # Re-sort units by ch and n (already)
    return all_units, all_questions, live_chs

def build():
    all_units, all_questions, live_chs = load_data()
    # Build CHAPTERS json
    chapters = []
    for n, t, p in CHAPTERS_MASTER:
        chapters.append({"n": n, "t": t, "p": p, "live": (n in live_chs)})
    # Load template
    if TEMPLATE.exists():
        tmpl = TEMPLATE.read_text(encoding="utf-8")
    else:
        # fallback to current out file
        tmpl = OUT.read_text(encoding="utf-8")
    # Replace title
    tmpl = tmpl.replace(
        "<title>PULSE · Orthopaedics — Marrow Edition 8 Companion</title>",
        "<title>PULSE · Paediatrics — Marrow Edition 8 Companion</title>"
    )
    # Replace branding possibly elsewhere? Ensure footer title also?
    # Replace storage keys: pulse_* -> pulse_peds_*
    # Be careful not to double-replace if already done
    if "pulse_peds_xp" not in tmpl:
        tmpl = tmpl.replace("'pulse_xp'", "'pulse_peds_xp'")
        tmpl = tmpl.replace("'pulse_done'", "'pulse_peds_done'")
        tmpl = tmpl.replace("'pulse_unlock'", "'pulse_peds_unlock'")
        tmpl = tmpl.replace("'pulse_streak'", "'pulse_peds_streak'")
        # also double quotes variant
        tmpl = tmpl.replace('"pulse_xp"', '"pulse_peds_xp"')
        tmpl = tmpl.replace('"pulse_done"', '"pulse_peds_done"')
        tmpl = tmpl.replace('"pulse_unlock"', '"pulse_peds_unlock"')
        tmpl = tmpl.replace('"pulse_streak"', '"pulse_peds_streak"')
        # In JS, localStorage keys are strings; also replace without quotes? The template uses store('pulse_xp')
        tmpl = tmpl.replace("pulse_done", "pulse_peds_done")
        tmpl = tmpl.replace("pulse_xp", "pulse_peds_xp")
        tmpl = tmpl.replace("pulse_unlock", "pulse_peds_unlock")
        tmpl = tmpl.replace("pulse_streak", "pulse_peds_streak")
        # Undo double prefix if any (pulse_peds_peds)
        tmpl = tmpl.replace("pulse_peds_peds_", "pulse_peds_")

    # Helper to replace JS arrays with balancing logic
    def replace_js_array(text, var, new_json):
        # Find "const VAR = [" and replace balanced array
        pat = f"const {var} = "
        idx = text.find(pat)
        if idx == -1:
            raise Exception(f"const {var} not found")
        start = idx + len(pat)
        while start < len(text) and text[start] in " \n\r\t":
            start += 1
        if text[start] != "[":
            raise Exception(f"Expected [ for {var} at {start}")
        # Find matching ]
        depth = 0
        in_str = False
        escape = False
        end = -1
        for i in range(start, len(text)):
            c = text[i]
            if in_str:
                if escape:
                    escape = False
                elif c == "\\":
                    escape = True
                elif c == '"':
                    in_str = False
                continue
            else:
                if c == '"':
                    in_str = True
                elif c == '[':
                    depth += 1
                elif c == ']':
                    depth -= 1
                    if depth == 0:
                        end = i + 1
                        break
        if end == -1:
            raise Exception(f"Unterminated array for {var}")
        # Include semicolon if present
        # Find semicolon after array
        semi = end
        while semi < len(text) and text[semi] in " \n\r\t":
            semi += 1
        if semi < len(text) and text[semi] == ";":
            end = semi + 1
        new_text = text[:idx] + f"const {var} = {new_json};" + text[end:]
        return new_text

    import json as jsjson
    # Ensure JSON dumps with proper escaping
    questions_json = jsjson.dumps(all_questions, ensure_ascii=False, separators=(",", ":"))
    units_json = jsjson.dumps(all_units, ensure_ascii=False, separators=(",", ":"))
    chapters_json = jsjson.dumps(chapters, ensure_ascii=False, separators=(",", ":"))

    tmpl = replace_js_array(tmpl, "QUESTIONS", questions_json)
    tmpl = replace_js_array(tmpl, "UNITS", units_json)
    tmpl = replace_js_array(tmpl, "CHAPTERS", chapters_json)

    # Also ensure the footer text mentions Paediatrics
    tmpl = tmpl.replace("PULSE · Orthopaedics · question order follows the book", "PULSE · Paediatrics · question order follows the book")
    # Fix main hero heading (screenshot showed Orthopaedics) and any other hardcoded orthopaedics strings
    tmpl = tmpl.replace("<h1>Orthopaedics</h1>", "<h1>Paediatrics</h1>")
    # Generic safety: any remaining Orthopaedics in static HTML (not in QUESTIONS/UNITS which are already peds)
    tmpl = tmpl.replace("Orthopaedics", "Paediatrics")

    OUT.write_text(tmpl, encoding="utf-8")
    print(f"Built {OUT} with {len(all_questions)} Q, {len(all_units)} U, {len([c for c in chapters if c['live']])} live chapters")

    # Also ensure index.html exists (simple redirect)
    if not INDEX.exists():
        INDEX.write_text("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PULSE · Paediatrics — Marrow Edition 8 Companion</title>
<meta http-equiv="refresh" content="0; url=pulse-peds-complete.html">
<style>
  body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;
       background:#120d1a;color:#f4eefb;font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}
  a{color:#e0607e;font-weight:800;font-size:20px;text-decoration:none;padding:14px 22px;
    border:1px solid #3a2d52;border-radius:12px;background:#221a30;display:inline-block;margin-top:10px}
  p{color:#a89bbd}
  div{text-align:center}
</style>
</head>
<body>
<div>
  <p>Opening your quiz…</p>
  <a href="pulse-peds-complete.html">▶ Open PULSE Peds Quiz</a>
</div>
<script>location.replace("pulse-peds-complete.html");</script>
</body>
</html>""", encoding="utf-8")

if __name__ == "__main__":
    build()
