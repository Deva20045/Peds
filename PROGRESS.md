# PROGRESS — PULSE · Paediatrics (Marrow Edition 8 Companion)

Single source of truth for the PULSE Paediatrics app. Update this file on every chapter.

## Goal
Rebuild **Marrow Paediatrics 8th Edition** as a single-HTML study app with
**line-by-line questions in strict book order** (every line of the book → a question,
first line → last line) so the user can master the subject without re-reading the PDF.
Same architecture as the live ORTHO app:
`https://deva20045.github.io/ORTHO/pulse-ortho-complete.html`

- One HTML file, no dependencies, works offline in the browser
- Schema: `QUESTIONS {id, sec, page, q, opts[4], ans, exp}` · `UNITS {id, ch, n, title, sec, qs[], guide}` · `CHAPTERS {n, t, p, live}`
- Questions run in **fixed book order** (only the 4 options shuffle per run — anti-bias)
- Unit = small book sub-section; each unit opens with a **guide** (2–4 line summary of that section)
- XP / day-streak / unit-locking / review-wrong-answers — identical behaviour to ORTHO app
- Storage keys namespaced `pulse_peds_*` (independent progress from the ORTHO app on the same device)

## Source PDF
- File: `Pediatric_Marrow_E8.pdf` (173 MB, PDF v1.3, **259 pages**, A4)
- Title metadata: "pediatrics @marrow ed.pdf" · iOS Quartz export (app screenshots, scanned/hand-annotated)
- **Scanned images — no text layer.** Content extracted by 300 dpi render + visual reading + Tesseract 5.5 OCR cross-check.
- Watermark hash in content: `648c85cfee3b03a74e182fab`

## PDF → book page map (offset formula)
```
book page = PDF page      (offset = 0)
```
- PDF p1 = cover (unnumbered). Content starts at PDF p2 = book page 2.
- Every page footer: `Paediatrics • v1.0 • Marrow 8.0 • 2024 ... Page X/N`
  → `X/N` = chapter-relative page (N = chapter length). **Footer "Page 1/N" marks a chapter start.**
- Each chapter has a big title on its first page. Smaller underlined titles with a
  `00:MM:SS` timestamp are **sub-sections** inside a chapter (→ become UNITS, not chapters).
- Bottom-right watermark = `ChapterName [box] bookPage` (extra verification signal).
- Question `page` field = book page (== PDF page). Unit `sec` = "Section title · p#".

## Chapter list — ALL 54 (verified: bottom-footer "Page 1/N" + 200 dpi footer-crop OCR, 54/54 match)
Book sections (from footers): Neonatology (1–7) · Growth & Development (8–13) · Nutrition (14–17) ·
Genetics & Infections (18–21) · Gastrointestinal System (22–25) · Respiratory System (26–29) ·
Cardiovascular System (30–33) · Genitourinary System (34–38) · Nervous System (39–42) ·
Endocrine System (43–46) · Childhood Malignancies (47–48) · Paediatric Rheumatology (49) ·
Haematology (50–52) · Miscellaneous (53–54).

| # | Chapter | Book p | Pages | Status |
|---|---------|:------:|:-----:|--------|
| 1 | Normal Newborn | 2 | 5 | ✅ DONE — 143 Q, 14 units |
| 2 | Neonatal Resuscitation | 7 | 4 | ✅ DONE — 101 Q, 9 units |
| 3 | Necrotizing Enterocolitis and Neonatal Sepsis | 11 | 5 | ✅ DONE — 98 Q, 8 units |
| 4 | Respiratory Distress in Newborn | 16 | 5 | ✅ DONE — 101 Q, 9 units |
| 5 | Neonatal Jaundice | 21 | 4 | ✅ DONE — 102 Q, 8 units |
| 6 | Neonatal Hypothermia and Neonatal Hypoglycemia | 25 | 5 | ✅ DONE — 105 Q, 8 units |
| 7 | Neonatal Reflexes, HIE and Neonatal Seizures | 30 | 5 | ✅ DONE — 135 Q, 9 units |
| 8 | Normal Growth | 35 | 6 | ✅ DONE — 135 Q, 10 units |
| 9 | Abnormalities of Head Size and Shape | 41 | 4 | ✅ DONE — 88 Q, 9 units |
| 10 | Abnormalities of Stature | 45 | 3 | ✅ DONE — 75 Q, 9 units |
| 11 | Normal Development | 48 | 4 | ✅ DONE — 80 Q, 8 units |
| 12 | Disorders of Development | 52 | 2 | ✅ DONE — 34 Q, 5 units |
| 13 | Behavioural Disorders in Children | 54 | 4 | ✅ DONE — 79 Q, 8 units |
| 14 | Breastfeeding | 58 | 4 | ✅ DONE — 62 Q, 8 units |
| 15 | Malnutrition | 62 | 4 | ✅ DONE — 72 Q, 8 units |
| 16 | Obesity | 66 | 3 | ✅ DONE — 77 Q, 7 units |
| 17 | Rickets and Scurvy | 69 | 5 | ✅ DONE — 88 Q, 7 units |
| 18 | Genetic Disorders | 74 | 6 | ✅ DONE — 102 Q, 8 units |
| 19 | Childhood Infections | 80 | 6 | ✅ DONE — 108 Q, 8 units |
| 20 | TORCH Infections | 86 | 6 | ✅ DONE — 83 Q, 8 units |
| 21 | COVID-19 in Children | 92 | 3 | ✅ DONE — 82 Q, 8 units |
| 22 | Disorders of Oesophagus in Children | 95 | 4 | ✅ DONE — 82 Q, 8 units |
| 23 | Diarrheal Disorders in Children | 99 | 5 | ✅ DONE — 104 Q, 9 units |
| 24 | Disorders of Liver in Children | 104 | 7 | ✅ DONE — 129 Q, 10 units |
| 25 | Surgical GI Disorders in Children | 111 | 5 | ✅ DONE — 95 Q, 9 units |
| 26 | Airway Malformations and Foreign Bodies | 116 | 4 | ✅ DONE — 121 Q, 9 units |
| 27 | Asthma | 120 | 4 | ✅ DONE — 141 Q, 10 units |
| 28 | Respiratory Infections | 124 | 6 | ⏳ |
| 29 | Cystic Fibrosis | 130 | 3 | ⏳ |
| 30 | Fetal Circulation and Introduction to Congenital Heart Diseases | 133 | 3 | ⏳ |
| 31 | Acyanotic Congenital Heart Defects | 136 | 6 | ⏳ |
| 32 | Cyanotic Congenital Heart Defects | 142 | 7 | ⏳ |
| 33 | Acute Rheumatic Fever | 149 | 4 | ⏳ |
| 34 | Congenital Anomalies of Kidney and Urinary Tract | 153 | 4 | ⏳ |
| 35 | Nephrotic and Nephritic Syndrome | 157 | 5 | ⏳ |
| 36 | Inherited Tubular Disorders | 162 | 4 | ⏳ |
| 37 | Acute Kidney Injury and Chronic Kidney Disease | 166 | 5 | ⏳ |
| 38 | UR and UTI Management Guidelines | 171 | 4 | ⏳ |
| 39 | Congenital Anomalies and Hydrocephalus | 175 | 6 | ⏳ |
| 40 | Seizure Disorders | 181 | 6 | ⏳ |
| 41 | Cerebral Palsy and CNS Infections | 187 | 7 | ⏳ |
| 42 | Neuromuscular Disorders | 194 | 5 | ⏳ |
| 43 | Growth Hormone Deficiency and Hypothyroidism | 199 | 5 | ⏳ |
| 44 | Adrenal Disorders in Children | 204 | 5 | ⏳ |
| 45 | Pubertal Disorders | 209 | 4 | ⏳ |
| 46 | Diabetic Ketoacidosis | 213 | 2 | ⏳ |
| 47 | Haematological Malignancies | 215 | 8 | ⏳ |
| 48 | Solid Tumours in Children | 223 | 4 | ⏳ |
| 49 | Rheumatic Disorders of Childhood | 227 | 8 | ⏳ |
| 50 | Approach to Anaemia in Children and Nutritional Anaemia | 235 | 6 | ⏳ |
| 51 | Congenital Haemolytic Anaemia | 241 | 7 | ⏳ |
| 52 | Bleeding Disorders | 248 | 5 | ⏳ |
| 53 | Paediatric Resuscitation | 253 | 3 | ⏳ |
| 54 | Shock | 256 | 4 | ⏳ |

Page math: 258 content pages (2–259) + 1 cover = 259 PDF pages ✓

## Per-chapter pipeline
1. **Render** chapter pages @300 dpi grayscale (`pdftoppm -r 300 -gray`).
2. **Read visually** (every line, table, figure caption) + **OCR cross-check**
   (`tesseract --psm 6`); zoom-crop any ambiguous number/word.
   (100 dpi full-page OCR already exists for every page in `ocr/low/pg-NNN.txt` as a map/summary.)
3. **Write questions** in strict book order → `peds/chN_data.py` (UNITS + QUESTIONS, same fields as ch1).
   - One fact/line per question; 4 options; `ans` index; `exp` = one-line rationale ending `(Book p#)`.
   - Units follow the book's own sub-sections; unit `guide` = 2–4 line summary of the section.
4. **Register** the chapter: set `live:true` in `build_app.py` CHAPTERS (data file auto-discovered via `ch*_data.py`).
5. **Rebuild** `pulse-peds-complete.html` (`python3 peds/build_app.py`), validate
   (node DOM-simulation of the full quiz flow), update this file, deploy to
   `deva20045.github.io/PEDIATRICS/`.

## App build
- Generator: `peds/build_app.py` (reads ORTHO template `peds/ortho_template.html` → swaps data/branding/storage keys)
- Output: `peds/pulse-peds-complete.html` + `peds/index.html` (meta-refresh redirect, same pattern as ORTHO)
- Deploy: upload both files to GitHub repo folder `PEDIATRICS/` (same as `ORTHO/`) → live at
  **https://deva20045.github.io/PEDIATRICS/** (index auto-redirects to the app)

## Validation (per build)
- `node --check` on the extracted `<script>`
- Node DOM-simulation: home → chapters (54 rows, locks) → path → guide → full unit quiz →
  unit-done (score/XP/accuracy/review) → localStorage `pulse_peds_*` persistence.

## Status
- [x] Template fetched & schema reverse-engineered (ORThO: 3061 Q / 425 units / 24 ch)
- [x] PDF downloaded (Google Drive confirm-token workaround) & page-map formula established
- [x] 259-page OCR pass complete (`ocr/low/`) + footer/watermark pass (`ocr/wm/`)
- [x] All 54 chapters identified & page-ranged (54/54 double-verified)
- [x] **CH1 Normal Newborn (p2–6): DONE** — 143 questions, 14 units, line-by-line, strict book order
- [x] App built: 54 chapters listed, CH1 live, full-flow simulation passing
- [x] **CH2 Neonatal Resuscitation (p7–10): DONE** — 101 questions, 9 units (Priority → Algorithm → 4 pre-birth Qs → Initial steps → HR assessment → BMV & O2 targets → MRSOPA → ETT → Compression & adrenaline)
- [x] App rebuilt: 244 questions live (2 chapters), strict book order verified, full CH2 playthrough passing
- [x] **CH3 NEC & Neonatal Sepsis (p11–15): DONE** — 98 questions, 8 units (NEC etiology, Bell's staging, NEC management, sepsis spectrum, etiology/features, investigations, treatment, sepsis algorithm)
- [x] **CH4 Respiratory Distress in Newborn (p16–20): DONE** — 101 questions, 9 units (clinical features, Silverman-Anderson, Downe's score, causes, TTNB, RDS, RDS management/surfactant, MAS, CDH)
- [x] App rebuilt: **443 questions live (4 chapters, 40 units)**, strict book order verified across all 4, full CH3+CH4 playthrough passing
- [x] CH11–15 handoff bundle prepared: `PULSE_PEDS_handoff_ch11-15.zip` (300 dpi page images for book p48–65, OCR cross-check text, full build pipeline + validator, HANDOFF.md) — new-chat route failed, building here instead
- [x] **CH5 Neonatal Jaundice (p21–24): DONE** — 102 questions, 8 units (intro/metabolism, assessment Kramer+TcB, types table, causes, breastfeeding/breastmilk jaundice, normogram+phototherapy, DVET, management protocol)
- [x] App rebuilt: **545 questions live (5 chapters, 48 units)**, strict book order verified across all 5, full playthrough passing (102/102 CH5)
- [x] **Definitive handoff bundle prepared: `PULSE_PEDS_CONTINUE.zip`** — covers CH6–15 (book p25–65, 41 pages @300dpi as JPEGs) + full pipeline + `CONTINUE.md` (any new chat: user says "continue" → agent builds NEXT chapter per PROGRESS.md). Supersedes the earlier ch11-15 zip.
- [x] **CH6 Neonatal Hypothermia and Neonatal Hypoglycemia (p25–29): DONE** — 105 questions, 8 units (temperature regulation / brown fat / modes of heat loss, hypothermia classification, stable KMC prevention, unstable NICU radiant warmer & incubator, hypoglycemia definition & screening <45/<2.5kg/<35wks/IDM+SGA+LGA+sepsis/asphyxia, manifestations & management jitteriness→seizure/GIR 6→12, resistant hypoglycemia >12/>7d + GSD nesidioblastosis glucagon/diazoxide/octreotide, IDM Pedersen LGA/ASH/RDS/lazy colon/polycythemia + overt 1st-trimester VSD/NTD/caudal regression)
- [x] App rebuilt: **650 questions live (6 chapters, 56 units)**, strict book order verified across all 6, full CH6 playthrough passing (105/105)
- [x] **CH7 Neonatal Reflexes, HIE and Neonatal Seizures (p30–34): DONE** — 135 questions, 9 units (neonatal reflexes table, moro abnormalities, postnatal SPL, birth asphyxia definitions, Sarnat staging, complications/PVL, therapeutic hypothermia 33.5-34.5°C, seizures types/etiology, management phenobarbitone→phenytoin/levetiracetam→midazolam + pyridoxine GABA trial)
- [x] **CH8 Normal Growth (p35–40): DONE** — 135 questions, 10 units (phases of growth, pubertal sequences, Tanner SMR F/M, laws of growth, weight, length/height & arm span, HC/CC, MAC/Skin fold, WHO/IAP charts & interpretation)
- [x] App rebuilt: **920 questions live (8 chapters, 75 units)**, strict book order verified across all 8, full CH7+CH8 playthrough passing (135/135 each)
- [x] **CH9 Abnormalities of Head Size and Shape (p41–44): DONE** — 88 questions, 9 units (microcephaly primary/secondary/PKU, teratogens FAS/hydantoin, Rett/Seckel, macrocephaly, megalencephaly lysosomal/genetic, craniosynostosis sutures/rule/types, Crouzon/Apert/Carpenter)
- [x] App rebuilt: **1008 questions live (9 chapters, 84 units)**, strict book order verified across all 9, full CH9 playthrough passing (88/88)
- [x] **CH10 Abnormalities of Stature (p45–47): DONE** — 75 Q, 9 units (short/tall stature, US:LS, MPH, bone age, algorithm)
- [x] **CH11 Normal Development (p48–51): DONE** — 80 Q, 8 units (gross/fine motor, tower/drawing, language/social, vision/hearing, assessment)
- [x] **CH12 Disorders of Development (p52–53): DONE** — 34 Q, 5 units (DQ, red flags, screening/definitive tests, causes, dissociation/deviance/regression)
- [x] **CH13 Behavioural Disorders (p54–57): DONE** — 79 Q, 8 units (breath-holding, bruxism, pica, thumb sucking, tantrums, tics/Tourette, enuresis)
- [x] **CH14 Breastfeeding (p58–61): DONE** — 62 Q, 8 units (latching, preterm feeding, properties HMO, composition, foremilk/hindmilk, deficiencies, contraindications, storage)
- [x] **CH15 Malnutrition (p62–65): DONE** — 72 Q, 8 units (wasting/stunting, marasmus vs kwashiorkor, SAM home/hospital, Phase I stabilization)
- [x] App rebuilt: **1410 questions live (15 chapters, 130 units)**, strict book order verified across all 15, full CH11-15 playthroughs passing
- [x] **CH1–6 data files restored** (ch1_data.py…ch6_data.py) — extracted from the committed 15-chapter build `pulse-peds-complete.html` (143+101+98+101+102+105 = 650 Q, refs + book order verified); they were missing from the workspace, which made the last rebuild drop them
- [x] **CH16 Obesity (p66–68): DONE** — 77 Q, 7 units (definitions/BMI/skinfold/waist, etiology exogenous vs pathological, monogenic MC4R/leptin + endocrine, hypothalamic VMN/ROHHAD, syndromic PWS/BWS/LM-BB + drugs, complications, management lifestyle/orlistat/liraglutide/LAGB) — visually re-verified line-by-line against 300dpi renders
- [x] **CH17 Rickets and Scurvy (p69–73): DONE** — 88 Q, 7 units (etiology, pathophysiology, head/chest/limb deformity, investigations + Vit D table + X-ray signs, treatment 2000/3000 IU + monitoring, refractory rickets incl. PHEX/phosphatonin + VDDR I/II + approach algorithm, scurvy) — visually re-verified line-by-line
- [x] **CH18 Genetic Disorders (p74–79): DONE** — 102 Q, 8 units (aneuploidies, Down incl. pathogenesis 95/4/1 + features + associations + recurrence table, Edwards, Patau, Turner karyotype + features, Noonan table, Klinefelter, DiGeorge CATCH-22 + Williams, imprinting Prader-Willi, Angelman, Fragile X TRD) — visually re-verified line-by-line
- [x] **CH19 Childhood Infections (p80–85): DONE** — 108 Q, 8 units (classification 1st–6th disease, measles + Koplik + SSPE + Vitamin A dosing, scarlet fever + Pastia's, rubella + Forchheimer, erythema infectiosum 3 stages + aplastic crisis, roseola + Nagayama, HFMD + onychomadesis, varicella + acyclovir + Oka vaccine + VZIG) — visually re-verified line-by-line
- [x] **CH20 TORCH Infections (p86–91): DONE** — 83 Q, 8 units (TORCH general aspects, CRS triad + salt-and-pepper + blueberry muffin + PRP, CMV most common + periventricular calcification + ganciclovir, toxo triad + pyrimethamine-sulfadiazine-folinic + spiramycin, congenital/perinatal varicella, early/late syphilis + VDRL + penicillin G, Zika, parvovirus B19 hydrops) — visually re-verified line-by-line
- [x] App rebuilt: **1868 questions live (20 chapters, 168 units)** — full data-integrity validation (unique ids, unit refs complete+ordered, strict book order all 20) + jsdom DOM simulation of the complete flow (home → 54 rows w/ locks → path → guide → full CH20 playthrough → unitdone score/XP/accuracy/review → localStorage persistence → next-unit unlock → CH1 playthrough) ALL PASSING
- [x] **RE-AUDIT (format mix + anti-predictability) of all 20 chapters — DONE** — user feedback: options too easily predictable, single-format monotony. Fixes:
  - **6 question types in the engine + UI**: MCQ · Fill-up (___ blank) · True/False (keyboard T/F) · Match-the-following (2-column table + combination options) · Clinical case (vignette block) · Odd-one-out — each with a coloured type badge; review screen tags the type and shows the vignette
  - **Distractor quality pass**: correct-answer length-giveaway 46.9% → 10.3% (416 answers trimmed, detail moved to exp); 546 junk distractors ("Surgery", "Observation only", "Only X", "Normal X"…) replaced with real same-section sibling values (substring-safe, category-preserving); 8 duplicate-option source bugs fixed; 4 junk questions dropped (video-timestamp rows, Yes/No table artifacts)
  - **Format conversions**: 609 "—"-blank stems → fill-ups; +194 topic-header/fragment stems → fill-ups; 170 → True/False statements (verb-safelist grammar, ~50/50 T/F, false ones swap in a plausible distractor); 65 match questions auto-built from 4 consecutive same-section facts (column B deranged, options = mapping permutations)
  - **Hand-crafted banks**: `bank_cases.py` (80 clinical vignettes, 4/chapter, options same-category & similar length) + `bank_odd.py` (40 odd-one-outs, 2/chapter, exp names the shared property)
  - **Bank: 2049 Q** = 852 MCQ · 842 fill · 170 TF · 65 match · 80 case · 40 odd; ans-index distribution balanced; strict book order + unit refs + unique ids all validated (`validate.py`, 0 errors) and full DOM flow re-simulated (`validate.js`, 118 checks pass)
  - Pipeline: restore git originals → `python3 audit.py` → `python3 validate.py` → `python3 build_app.py` → `node validate.js`
- [x] **GI/COVID batch CH21–CH25 (p92–115): DONE** — 492 questions, 45 units (U169–U212):
  - **CH21 COVID-19 in Children (p92–94)** — 82 Q, 8 units U169–U176 (virus/variants & transmission, clinical spectrum mild–severe + MIS-C, danger signs & tachypnea 60/50/40/30 + SpO2 90–93/<90, diagnosis RT-PCR/CT, mild & moderate management + O2 94–96%, severe/critical + dexa 0.15–6 mg/kg + remdesivir, PIMS-TS/IVIG 2 g/kg + MP 2 mg/kg/d, prevention & vaccines, COVID case). Defect fixed: dexa dose zoom-verified 0.15–6 mg/kg (was 0.15–0.6).
  - **CH22 Disorders of Oesophagus (p95–98)** — 82 Q, 8 units U177–U184 (dysphagia causes, EA/TEF types & C-penta + coiled NG, EA management & complications, GERD physiology & red flags, GERD management + Nissen, achalasia + manometry, caustic/corrosive ingestion & Zargar, FB ingestion batteries/magnets + esophageal FB case). C22-046 redesigned semantically (Sandifer→BIND pairs).
  - **CH23 Diarrheal Disorders (p99–103)** — 104 Q, 9 units U185–U193 (classification acute/persistent/chronic, ORS 245 mosm composition, Plan A/B/C, ORS-modify & contraindications, AD management zinc 14 d + Vit A + ondansetron 0.15, persistent diarrhea 5 rules, celiac criteria/anti-tTG/serology-first, osmotic vs secretory, celiac-biopsy clinical case). Celiac biopsy IOC case appended as C23-104.
  - **CH24 Disorders of Liver (p104–110)** — 129 Q, 10 units U194–U203 (bilirubin metabolism, hyperbilirubinemias table + CN I/II cases, cholestasis conj ≥1/≥20% + approach, EHBA vs neonatal hepatitis + Kasai <60 d + HIDA + transplant, metabolic Wilson ATP7B/Cp/biopsy Cu>250 + DPA/knock-knees, autoimmune/PSC/UDCA, portal HTN & BCS, hepatic failure/encephalopathy + PELD, Wilson disease 20 Q U202, GSD table 20 Q U203 + cases CN-I & IHPS). C24-127 page→110 (validated).
  - **CH25 Surgical GI Disorders (p111–115)** — 95 Q, 9 units U204–U212 (IHPS statue/clue + USG ≥4/≥16 + ½NS+K+5%D → Ramstedt + case, duodenal atresia 30% Down + double bubble + windsock + d-d-dostomy, atresia types/joint protocol/complications, intussusception triad + doughnut/claw + aerostat + 10–20% recurrence + case, malrotation/Ladd, Hirschsprung meconium>48h + RB + absent RAIR + AChE + pull-through, anorectal malformations, mesenteric cyst/omphalocele/gastroschisis, misc).
  - Quality passes: answer-key rotation (uniform ans distribution), match normalize + arrow-aware verify (85/85 correct), length-giveaway trim 67→18 flagged (worst chapter 8.2%), 100 clinical cases (4/chapter incl. CH21–25 inline), CH24 4th case (CN type I) inserted → 2541 Q.
  - Build: `validate.py` 2541 Q / 0 errors / 1 pre-existing warn (C5-038); `node --check` OK; `validate.js` ALL CHECKS PASSED (2541/25 live/"25 of 54" expectations updated). `build_app.py` reads only `ch*_data.py` — inline cases/odds merge-safe.
- [x] **RESPIRATORY BATCH #1 — CH26 Airway Malformations and Foreign Bodies (p116–119): DONE** — 121 Q, 9 units (U213–U221), visually re-verified line-by-line against the 200 dpi renders (+ 350–400 dpi zooms on: onset "within 2 weeks/2 weeks after birth", resolution "6–12 months of age" (low-res read "4–5" corrected after zoom), table (positional variation / cry / stridor), "only 10–20% radiopaque", "5 back blows + 5 chest compressions"):
  - **U213 Laryngomalacia — pathology & structures affected** (m/c congenital laryngeal malformation; malacia = softness/floppiness/laxity; supraglottic structures — epiglottis, arytenoids, aryepiglottic folds; 3 distinct "which of these is affected" items + match)
  - **U214 Clinical manifestations (stridor)** (stridor = upper airway obstruction sign; floppy structures fall over the glottic opening; onset soon after birth/within 2 weeks; intermittent on crying/agitation/after feeding; postural variation supine +, prone −) + laryngomalacia case
  - **U215 Laryngomalacia vs congenital subglottic stenosis** (table: positional variation + / −, cry muffled / normal, stridor inspiratory / biphasic) + subglottic-stenosis case
  - **U216 Diagnosis & management** (laryngoscopy; omega Ω-shaped epiglottis; reassurance; resolves by 6–12 months) + management case
  - **U217 Congenital lobar emphysema** (cartilaginous bronchial dysplasia → abnormal compliance → collapse on expiration = ball valve effect → air trapping → hyperinflation; LUL > RML; compression atelectasis → impaired oxygenation → respiratory distress; mediastinal shift to unaffected side; X-ray first-line, CT chest IOC; lobectomy) + odd-one-out
  - **U218 CPAM** (hamartomatous/dysplastic tissue → multiple cysts; m/c cystic lung disease of newborn; non-functional cysts → no gaseous exchange → distress; ↑ infection → recurrent pneumonia; X-ray → CT IOC; ↑ risk of sarcoma/carcinoma → resection within 1 year) + case
  - **U219 Pulmonary sequestration** (segregation of non-functioning lung, no bronchial communication; systemic supply from lower thoracic/abdominal aorta → ↑ recurrent infections; lower lobes; intrapulmonary = common pleura / extrapulmonary = separate pleura; X-ray → CT IOC; surgical resection) + odd-one-out
  - **U220 Foreign bodies — intro & presentation** (paediatric emergency, < 3 years, lower > upper airway → m/c bronchus R>L; nuts/coins/small rounded plastic toys; immediate = choking, small child acute recurrent cough, older child choking sign = clutching of neck + gag response; caregiver h/o choking)
  - **U221 Foreign bodies — delayed presentation, consequences, investigation & management** (retained FB → recurrent unexplained wheeze mimicking bronchodilator-unresponsive asthma; suppurative — same-site recurrent pneumonia → bronchiectasis, lung abscess; complete obstruction → collapse/atelectasis, partial → ball valve → hyperinflation; X-ray unreliable, only 10–20% radiopaque; act on suspicion triad; bronchus → rigid bronchoscope; > 1 year Heimlich (epigastric thrust backwards & upwards), < 1 year 5 back blows + 5 chest compressions) + FB case
  - Format mix 65 MCQ · 30 fill · 9 T/F (5 T / 4 F) · 7 match · 6 odd · 4 clinical cases; answer-key rotation → uniform index distribution (28/28/28/28 non-TF); length-giveaway check clean; 4 authoring defects caught & fixed during review (2 option/answer-index mismatches, 2 odd-one-out keys, 1 duplicate IOC pair) + 6 fill-blank markers normalised to `___`
  - Build: `validate.py` **2662 Q / 221 U / 26 chapters / 0 errors** (1 pre-existing warn C5-038); `node --check` on the extracted script OK; `validate.js` extended with a **full CH26 playthrough (all 121 Q across 9 units)** → ALL CHECKS PASSED
- [x] App rebuilt: **2662 questions live (26 chapters, 221 units)** — home hero shows "26 of 54"
- [x] **RESPIRATORY BATCH #2 — CH27 Asthma (p120–123): DONE** — 141 Q, 10 units (U222–U231), line-by-line against the 200 dpi renders + 350–400 dpi zooms (table values, ICS dose bands, review-after-2-months flow, exacerbation table, device age cut-offs):
  - **U222 Characteristics & phenotypes** (bronchoconstriction d/t airway hyper-responsiveness + chronic airway inflammation, reversible obstruction, variable intensity & frequency, management by subjective symptoms; allergic/atopic m/c in children with good response vs non-allergic m/c in adults difficult to treat; exercise-induced) + odd-one-out
  - **U223 Phases** (early: allergen→IgE→IgE-bound mast cell, degranulation within 10 min, histamine most important + prostaglandins/leukotrienes C,D,E/bradykinin → bronchoconstriction, mucosal edema, ↑ secretions → β2-agonist; late: 3–4 h onset, peak 10–12 h, eosinophil/basophil/lymphocyte recruitment, repeated exposure → chronic inflammation, steroids inhibit) + 2 T/F + match + odd-one-out
  - **U224 Clinical features** (recurrent wheeze/cough/chest tightness; ↑ late night/early mornings; varying intensity & frequency) + T/F
  - **U225 Lung function** (FEV1 ↓ with FEV1/FVC < 0.8; bronchodilator FEV1 ↑ > 12%; exercise FEV1 ↓ > 15%; diurnal AM–PM FEV1/PEF ↑ > 20%) + match + case + odd-one-out
  - **U226 Management & steps** (GINA; exacerbating factors + pharmacotherapy; > 12 yr as adults; 6–11 yr stepwise; reliever SABA SOS; Steps I–V table with SABA/ICS/LABA escalation and biological agents last resort) + match + step-IV case + T/F
  - **U227 Drugs** (SABA, LABA formoterol synergistic + steroid-sparing; budesonide ICS low 200–400 / medium 400–800 / high > 800 mcg; omalizumab anti-IgE, mepolizumab anti-IL5, dupilumab anti-IL4 receptor, anti-TSLP thymic stromal lymphopoietin) + match + odd-one-out
  - **U228 Preschool < 5 yr** (may resolve > 5 yr; episodic vs multitrigger wheeze — cold, exertion, food; ↑ probability: > 10 d after URI AND > 3 episodes; daily low-dose ICS + SABA, review 2 months → improvement = stop, no improvement = 6–11 yr protocol) + case + odd-one-out
  - **U229 Exacerbation classification** (sensorium normal/anxious/agitated; retractions absent/moderate/severe; SpO2 > 95 / 90–95 / < 90%; PEFR > 80 / 60–80 / < 60%) + match + severe-exacerbation case
  - **U230 Exacerbation management** (mild — MDI salbutamol 4–10 puffs q20min; moderate — salbutamol + ipratropium (centrally acting anticholinergic) + O2 to keep SpO2 > 95% + oral prednisolone; severe — nebulised salbutamol + ipratropium + oral prednisolone or iv hydrocortisone + inj magnesium sulphate) + match + severe case + 2 T/F + odd-one-out
  - **U231 Devices** (by age: ≥ 12 yr MDI; 4–12 yr MDI + spacer; < 4 yr MDI + spacer + face mask; spacer suspends drug → inhaled over few breaths; rotahaler not commonly used — mouth piece, insertion hole, rota chamber/rotacap powdered on twisting) + match + device case + odd-one-out
  - Format mix 69 MCQ · 35 fill · 17 T/F (9 T / 8 F) · 7 match · 7 odd · 6 clinical cases; answer-key rotation → 31/31/31/31 non-TF index distribution; 5 fill stems normalised to `___`
  - Build: `validate.py` **2803 Q / 231 U / 27 chapters / 0 errors** (1 pre-existing warn C5-038); `node --check` OK; `validate.js` extended with a **full CH27 playthrough (all 141 Q across 10 units)** → ALL CHECKS PASSED
- [x] App rebuilt: **2803 questions live (27 chapters, 231 units)** — home hero shows "27 of 54"
- [ ] **NEXT: CH28 Respiratory Infections (p124–129)**
- [ ] Pending in this book: CH28–CH54 (source PDFs already present in `source/chapters/`)
