CH = 12
UNITS = [
    {"id": "PEDS-U102", "ch": 12, "n": 1, "title": "Assessment — DQ and Global Delay", "sec": "Assessment of development · p51", "qs": [], "guide": "DQ = DA/CA x100 Developmental delay DQ <70 Global delay ≥2 domains → significant neurological Eg cerebral palsy. Preterm corrected age = postnatal - preterm correction (40w - actual gestation) calculated upto 2y."},
    {"id": "PEDS-U103", "ch": 12, "n": 2, "title": "Red Flag Signs", "sec": "Red Flag Signs · p51", "qs": [], "guide": "Upper limits: visual fixation/following 2m, head control 5m, vocalization 6m, sitting without support 10m, standing with support 12m, standing/walking without support + single words 18m."},
    {"id": "PEDS-U104", "ch": 12, "n": 3, "title": "Tests for Developmental Assessment", "sec": "Tests · p51", "qs": [], "guide": "Screening Good Doctor Treats Patients: Goodenough-Harris Draw a man, Denver II, Trivandrum, Phatak Baroda. Definitive: Bayley II (infant/toddler), Stanford Binet, Weschler, Vineland adaptive II."},
    {"id": "PEDS-U105", "ch": 12, "n": 4, "title": "Causes of Developmental Delay", "sec": "Causes · p52", "qs": [], "guide": "Congenital: chromosomal Down, genetic Fragile X/Rett, congenital hypothyroidism, brain anomalies, TORCH. Acquired: severe head trauma, meningitis, perinatal asphyxia."},
    {"id": "PEDS-U106", "ch": 12, "n": 5, "title": "Variants — Dissociation, Deviance, Regression", "sec": "Variants · p52", "qs": [], "guide": "Dissociation variation between ≥2 domains Eg isolated language delay hearing deficit. Deviance milestones out of sequence Eg early rolling head later due ↑ extensor tone cerebral palsy. Regression loss of previously acquired milestones graph peaks then falls Eg Rett, SSPE, Leukodystrophy."},
]

def q(num, sec, page, qtext, opts, ans, exp):
    assert len(opts)==4 and 0 <= ans <4
    return {"id": f"PEDS-C12-{num:03d}", "sec": sec, "page": page, "q": qtext, "opts": opts, "ans": ans, "exp": exp}

QUESTIONS = [
    q(1,"PEDS-U102",51,"Developmental quotient formula",["DA/CA x100","CA/DA x100","DA+CA","DA-CA"],0,"Developmental quotient = Developmental age (DA)/Chronological age (CA) x100 (Book p51 00:00:11)"),
    q(2,"PEDS-U102",51,"Developmental delay",["DQ <70","DQ >100","DQ <100","DQ <50"],0,"Developmental delay : DQ <70 (Book p51)"),
    q(3,"PEDS-U102",51,"Global developmental delay",["Delay in ≥2 domains → Significant neurological disorder (Eg cerebral palsy)","≥1 domain","Only language","Only motor"],0,"Global developmental delay : Delay in ≥2 domains → Significant neurological disorder (Eg : Cerebral palsy) (Book p51)"),
    q(4,"PEDS-U102",51,"Corrected age formula",["Postnatal age - Preterm correction","Postnatal + correction","CA - DA","DA - CA"],0,"Corrected age = Postnatal age - Preterm correction (Book p51)"),
    q(5,"PEDS-U102",51,"Preterm correction calculated upto",["2 years","1 year","3 years","5 years"],0,"Preterm correction (Calculated upto 2 years) =40 weeks - Actual weeks of gestation (Book p51)"),
    q(6,"PEDS-U102",51,"Preterm correction =",["40 weeks - Actual weeks of gestation","Actual -40","Postnatal -40","40+Actual"],0,"=40 weeks - Actual weeks of gestation of preterm baby (Book p51)"),
    q(7,"PEDS-U103",51,"Red Flag visual fixation or following upper limit",["2 months","5 months","6 months","10 months"],0,"Visual fixation or following 2 months (Book p51)"),
    q(8,"PEDS-U103",51,"Head control",["5 months","2 months","6 months","10 months"],0,"Head control 5 months (Book p51)"),
    q(9,"PEDS-U103",51,"Vocalization",["6 months","2 months","5 months","10 months"],0,"Vocalization 6 months (Book p51)"),
    q(10,"PEDS-U103",51,"Sitting without support",["10 months","12 months","6 months","18 months"],0,"Sitting without support 10 months (Book p51)"),
    q(11,"PEDS-U103",51,"Standing with support",["12 months","10 months","18 months","5 months"],0,"Standing with support 12 months (Book p51)"),
    q(12,"PEDS-U103",51,"Standing/walking without support + Single words",["18 months","12 months","10 months","5 months"],0,"Standing/walking without support + Single words 18 months (Book p51)"),
    q(13,"PEDS-U103",51,"Red Flag definition",["When a milestone takes longer than the upper limit to develop","Always delayed","Normal","Early"],0,"When a milestones takes longer than the upper limit to develop (Book p51)"),
    q(14,"PEDS-U104",51,"Screening tests mnemonic",["Good Doctor Treats Patients","PLABB","LOX-STD","SIPS"],0,"Screening tests (mnemonic - Good Doctor Treats Patients) (Book p51)"),
    q(15,"PEDS-U104",51,"1 Goodenough-Harris",["Draw a man test","Denver II","Trivandrum","Baroda"],0,"1. Goodenough-Harris ‘Draw a man’ test (Book p51)"),
    q(16,"PEDS-U104",51,"2 Denver",["Denver II","Goodenough","Trivandrum","Baroda"],0,"2. Denver II (Book p51)"),
    q(17,"PEDS-U104",51,"3 Trivandrum",["Trivandrum development screening test","Denver","Goodenough","Baroda"],0,"3. Trivandrum development screening test (Book p51)"),
    q(18,"PEDS-U104",51,"4 Phatak's",["Baroda screening test","Denver","Goodenough","Trivandrum"],0,"4. Phatak's Baroda screening test (Book p51)"),
    q(19,"PEDS-U104",51,"Definitive tests: Bayley II",["Infant and toddler development","Intelligence scale","Adaptive","Draw a man"],0,"1. Bayley II scale (Infant and toddler development) (Book p51)"),
    q(20,"PEDS-U104",51,"Stanford Binet",["Intelligence scale","Infant toddler","Adaptive","Screening"],0,"2. Stanford Binet Intelligence scale (Book p51)"),
    q(21,"PEDS-U104",51,"Weschler",["Intelligence scale","Adaptive","Infant","Screening"],0,"3. Weschler Intelligence scale (Book p51)"),
    q(22,"PEDS-U104",51,"Vineland",["Adaptive behaviour scale II","Intelligence","Screening","Infant"],0,"4. Vineland adaptive behaviour scale II (Book p51)"),
    q(23,"PEDS-U105",52,"Congenital chromosomal Eg",["Down's syndrome","Fragile X","Rett","TORCH"],0,"Chromosomal (Eg : Down's syndrome) (Book p52)"),
    q(24,"PEDS-U105",52,"Genetic syndrome Eg",["Fragile X syndrome, Rett syndrome","Down only","TORCH","Brain anomalies"],0,"Genetic syndrome (Eg : Fragile X syndrome, Rett syndrome) (Book p52)"),
    q(25,"PEDS-U105",52,"Congenital other",["Congenital hypothyroidism + Brain anomalies + TORCH infections","Only hypothyroidism","Only TORCH","Only brain"],0,"Congenital hypothyroidism, Brain anomalies, TORCH infections (Book p52)"),
    q(26,"PEDS-U105",52,"Acquired severe head trauma etc",["Severe head trauma, meningitis, Perinatal asphyxia","Only trauma","Only meningitis","Only asphyxia"],0,"Acquired: Severe head trauma, meningitis, Perinatal asphyxia (Book p52 00:09:30)"),
    q(27,"PEDS-U106",52,"Developmental dissociation",["Variation in attainment of milestones between ≥2 domains","Out of sequence","Loss of milestone","Normal"],0,"Developmental dissociation Variation in attainment between ≥2 domains (Book p52)"),
    q(28,"PEDS-U106",52,"Dissociation Eg",["Isolated language delay due to hearing deficit","Early rolling","Rett","SSPE"],0,"Eg : Isolated language delay due to hearing deficit (Book p52)"),
    q(29,"PEDS-U106",52,"Developmental deviance",["Attainment of milestones out of normal sequence","Variation between domains","Loss","Normal"],0,"Developmental deviance Attainment out of normal sequence (Book p52)"),
    q(30,"PEDS-U106",52,"Deviance Eg",["Early rolling (Head control later) over due to increase tone of extensors in cerebral palsy","Isolated language","Rett","SSPE"],0,"Eg : Early rolling (Head control later) over due to increase tone of extensors in cerebral palsy (Book p52)"),
    q(31,"PEDS-U106",52,"Regression",["Loss of previously acquired milestone","Variation between domains","Out of sequence","Normal"],0,"Regression Loss of previously acquired milestone (Book p52)"),
    q(32,"PEDS-U106",52,"Regression graph",["No. of milestones increases then decreases with Age peak then fall","Linear increase","No change","Only decrease"],0,"No. of milestones vs Age Normal peak then Regression fall (Book p52)"),
    q(33,"PEDS-U106",52,"Regression Eg",["Rett syndrome, SSPE, Leukodystrophy","Isolated language","Early rolling","Down"],0,"Eg in : Rett syndrome, Subacute sclerosing panencephalitis (SSPE), Leukodystrophy (Book p52)"),
    q(34,"PEDS-U106",52,"SSPE full form",["Subacute sclerosing panencephalitis","Severe systemic","Not","None"],0,"Subacute sclerosing panencephalitis (SSPE) (Book p52)"),
]

RANGES = {102:(1,6),103:(7,13),104:(14,22),105:(23,26),106:(27,34)}
UNIT_RANGES = {1:(1,6),2:(7,13),3:(14,22),4:(23,26),5:(27,34)}
for u in UNITS:
    s,e = UNIT_RANGES[u["n"]]
    u["qs"] = [f"PEDS-C12-{i:03d}" for i in range(s,e+1)]

pages = [q["page"] for q in QUESTIONS]
assert pages == sorted(pages), f"Pages not sorted {pages[:10]}"
assert len(QUESTIONS)==34
assert len(UNITS)==5
for u in UNITS:
    s,e = UNIT_RANGES[u["n"]]
    assert len(u["qs"])==e-s+1
