# PULSE · Paediatrics — Marrow Edition 8 Companion

Live app: **https://deva20045.github.io/Peds/**

- Single-HTML, offline, no dependencies
- **3711 questions · 303 units · 35 chapters live (CH1–CH35)**
- Build: `python3 build_app.py` → `pulse-peds-complete.html` + `index.html`
- Storage keys `pulse_peds_*` (independent from ORTHO)

## Question formats (re-audit, Sep 2026)
Every unit now mixes **six formats** — no more single-format drilling:

| Format | Badge | Count | What it is |
|---|---|---|---|
| MCQ | MCQ | 1832 | Single-best-answer with same-category, length-balanced options |
| Fill-up | FILL UP | 1158 | Blank (___) completion — definitions, milestones, table rows |
| True / False | TRUE / FALSE | 318 | Statement judged true or subtly false (~50/50, keyboard T/F) |
| Match the following | MATCH | 147 | Column A ↔ deranged Column B; pick the correct combination |
| Clinical case | CLINICAL | 158 | Hand-written patient vignette → diagnosis / next step |
| Odd one out | ODD ONE OUT | 98 | Three share a property, one doesn't (exp names the property) |

Options shuffle every run; the correct answer's position is also randomised in the data.

## Anti-predictability rules (applied to all 35 chapters)
- **Length-giveaway eliminated**: 46.9% → 10.3% of questions had a correct option >1.6× longer than every distractor (now trimmed, detail moved to the explanation, or distractors enriched with real same-section values)
- **546 junk distractors removed** ("Surgery", "Observation only", "Only heart", "Normal X-ray"…) — replaced with real confusable values mined from the same book section
- **Same-section distractor pool only** — replacements keep the option category (drugs vs drugs, ages vs ages)
- Duplicated-option source bugs fixed (8 questions), 4 junk questions dropped (video-timestamp metadata, Yes/No table artifacts)
- Every explanation still cites the book page; strict book order preserved (validated)

## Re-audit pipeline
- `audit.py` — the re-audit: loads git-original `ch*_data.py`, fixes distractors, converts formats, inserts the hand-written banks, renumbers, rewrites the files
- `bank_cases.py` — 80 hand-crafted clinical vignettes (4 per chapter)
- `bank_odd.py` — 40 hand-crafted odd-one-outs (2 per chapter)
- `validate.py` — data-integrity validator (ids, unit refs, strict book order, per-type rules)
- `validate.js` — Node DOM-simulation of the full app flow, all 6 types (118 checks)
- `python3 build_app.py` — rebuilds the single-HTML app

## Current chapters
| # | Chapter | Q | Units | Format mix (M·F·TF·MT·CS·OO) |
|---|---------|---|-------|------------------------------|
| 1 | Normal Newborn (p2–6) | 152 | 14 | 10·113·20·3·4·2 |
| 2 | Neonatal Resuscitation (p7–10) | 110 | 9 | 1·85·15·3·4·2 |
| 3 | NEC & Neonatal Sepsis (p11–15) | 107 | 8 | 3·81·14·3·4·2 |
| 4 | Respiratory Distress in Newborn (p16–20) | 110 | 9 | 1·84·16·3·4·2 |
| 5 | Neonatal Jaundice (p21–24) | 109 | 8 | 14·76·12·1·4·2 |
| 6 | Neonatal Hypothermia & Hypoglycemia (p25–29) | 114 | 8 | 12·81·12·3·4·2 |
| 7 | Neonatal Reflexes, HIE & Seizures (p30–34) | 149 | 9 | 105·23·7·8·4·2 |
| 8 | Normal Growth (p35–40) | 146 | 10 | 90·36·7·7·4·2 |
| 9 | Abnormalities of Head Size and Shape (p41–44) | 94 | 9 | 62·19·6·1·4·2 |
| 10 | Abnormalities of Stature (p45–47) | 82 | 9 | 44·26·5·1·4·2 |
| 11 | Normal Development (p48–51) | 91 | 8 | 51·28·1·5·4·2 |
| 12 | Disorders of Development (p52–53) | 41 | 5 | 21·13·0·1·4·2 |
| 13 | Behavioural Disorders (p54–57) | 89 | 8 | 48·25·5·5·4·2 |
| 14 | Breastfeeding (p58–61) | 69 | 8 | 39·22·1·1·4·2 |
| 15 | Malnutrition (p62–65) | 82 | 8 | 45·26·1·4·4·2 |
| 16 | Obesity (p66–68) | 85 | 7 | 58·12·7·2·4·2 |
| 17 | Rickets and Scurvy (p69–73) | 94 | 7 | 57·21·10·0·4·2 |
| 18 | Genetic Disorders (p74–79) | 112 | 8 | 69·23·10·4·4·2 |
| 19 | Childhood Infections (p80–85) | 119 | 8 | 67·29·12·5·4·2 |
| 20 | TORCH Infections (p86–91) | 94 | 8 | 55·19·9·5·4·2 |
| 21 | COVID-19 in Children (p92–94) | 82 | 8 | 43·19·9·5·4·2 |
| 22 | Disorders of Oesophagus in Children (p95–98) | 82 | 8 | 41·24·9·2·4·2 |
| 23 | Diarrheal Disorders in Children (p99–103) | 104 | 9 | 56·29·8·5·4·2 |
| 24 | Disorders of Liver in Children (p104–110) | 129 | 10 | 82·29·7·5·4·2 |
| 25 | Surgical GI Disorders in Children (p111–115) | 95 | 9 | 54·25·7·3·4·2 |
| 26 | Airway Malformations & Foreign Bodies (p116–119) | 121 | 9 | 65·30·9·7·4·6 |
| 27 | Asthma (p120–123) | 141 | 10 | 69·35·17·7·6·7 |
| 28 | Respiratory Infections (p124–128) | 140 | 13 | 49·42·21·8·10·10 |
| 29 | Cystic Fibrosis (p130–132) | 88 | 6 | 60·10·6·5·5·2 |
| 30 | Fetal Circulation & Intro to CHD (p133–135) | 71 | 6 | 48·10·4·4·4·1 |
| 31 | Acyanotic Congenital Heart Defects (p136–141) | 149 | 10 | 89·25·15·7·8·5 |
| 32 | Cyanotic Congenital Heart Defects (p142–148) | 143 | 11 | 106·11·9·6·5·6 |
| 33 | Acute Rheumatic Fever (p149–152) | 110 | 9 | 74·12·11·5·5·3 |
| 34 | Congenital Anomalies of Kidney & Urinary Tract (p153–156) | 93 | 8 | 63·9·6·6·6·3 |
| 35 | Nephrotic and Nephritic Syndrome (p157–161) | 114 | 9 | 81·6·10·7·5·5 |

Next: CH36 Inherited Tubular Disorders (p162–165)
