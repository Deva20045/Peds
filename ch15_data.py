CH = 15
UNITS = [
    {"id": "PEDS-U123", "ch": 15, "n": 1, "title": "Terminology and WHO Classification", "sec": "TERMINOLOGY · p61", "qs": [], "guide": "Wasting Low weight for height W/H Acute severe weight loss Stunting Low height for age Chronic Underweight Low weight for age Can refer wasting and/or stunting WHO Moderate -2 to -3 SD Severe <-3 SD Symmetrical edema Absent vs Present."},
    {"id": "PEDS-U124", "ch": 15, "n": 2, "title": "Clinical Syndromes — Marasmus vs Kwashiorkor Overview", "sec": "Clinical Syndromes · p61", "qs": [], "guide": "Protein-energy malnutrition Marasmus vs Kwashiorkor Predominant Calorie <1yr vs Protein 1-4yrs Edema Absent vs Present +++ Anasarca Muscle wasting +++ vs + masked edema Appetite Good vs Poor."},
    {"id": "PEDS-U125", "ch": 15, "n": 3, "title": "General Appearance and Skin/Hair", "sec": "General appearance · p61", "qs": [], "guide": "Marasmus Alert Skin and bone Loose skin folds axilla & buttocks baggy pant Thin brittle hair Simian facies buccal fat loss wrinkles Loss muscle mass. Kwashiorkor Dull/lethargic/irritable Skin Flaky-paint hyperpigmented patches Flag sign grey & black hair ↓S Albumin ↓oncotic pressure Anasarca Crazy pavement cracks Bulging abdomen ascites Moon face."},
    {"id": "PEDS-U126", "ch": 15, "n": 4, "title": "Severe Acute Malnutrition — Criteria and Types", "sec": "SAM · p62", "qs": [], "guide": "Malnourished child Criteria Weight for Height <-3.5 SD (per book) Bipedal edema Diagnosis exclusion MAC <11.5 cm Any present = SAM Types Uncomplicated Good appetite No edema No complications Home supervised vs Complicated Poor Present Present Hospital."},
    {"id": "PEDS-U127", "ch": 15, "n": 5, "title": "Home Management of SAM", "sec": "HOME MANAGEMENT · p62", "qs": [], "guide": "Nutrition goal 175 Kcal/kg/day + Protein 4-6 g/kg/day Diets Home-made RUTF Ready-to-use therapeutic food Ingredients Milk solids Sugars Vegetable oil Peanut butter paste Advantages Good palatability Semi-solid Long shelf-life Nutrient 543 Kcal +15g protein per 100g Additional 3As Antibiotic Oral Amoxicillin x5d Albendazole <2y 200mg >2y 400mg Vitamin A <6m 50k 6-12m 1 Lakh >12m 2 Lakh."},
    {"id": "PEDS-U128", "ch": 15, "n": 6, "title": "Hospital Management and Phase I Stabilization Overview", "sec": "HOSPITAL MANAGEMENT · p62-63", "qs": [], "guide": "Management Stabilization phase management of complications mnemonic SHIELDED + Rehabilitation Phase I Stabilization complications details: Hypoglycemia <54, Hypothermia axillary <35 rectal <35.5, Infections etc."},
    {"id": "PEDS-U129", "ch": 15, "n": 7, "title": "Phase I — Hypoglycemia and Hypothermia", "sec": "Phase I · p63", "qs": [], "guide": "Hypoglycemia <54 mg/dl Symptomatic Eg Seizures IV 10% Dextrose 5ml/kg STAT Glucose infusion Asymptomatic Oral glucose 50mL Hypothermia axillary <35°C rectal <35.5°C Treatment Warming protective clothing Kangaroo mother care Rapid rewarming avoided dysequilibrium Drowsiness seizures coma."},
    {"id": "PEDS-U130", "ch": 15, "n": 8, "title": "Phase I — Infections, Electrolytes, Dehydration, Micronutrients", "sec": "Phase I · p63", "qs": [], "guide": "Infections ↓immunity usual signs absent Empirical treatment all SAM m/c Ampicillin+Amikacin Penicillin+Aminoglycoside If no improvement 48hrs 3rd gen cephalosporin Ceftriaxone m/c bacteria Gram-negative Electrolytes Na ↑ total body Excess Na avoided Serum Na Low/normal intracellular & dilution edema Hypokalemia Hypomagnesemia Supplementation Dehydration Thirst urine output Dryness Treated irrespective No shock ReSoMal Shock Ringers lactate 5% dextrose K+ First 2 hrs 15 ml/kg Oral fluids Micronutrient multivitamin Twice RDA Iron absorption first week ↓ Free radical bacterial proliferation."},
]

def q(num, sec, page, qtext, opts, ans, exp):
    assert len(opts)==4 and 0 <= ans <4
    return {"id": f"PEDS-C15-{num:03d}", "sec": sec, "page": page, "q": qtext, "opts": opts, "ans": ans, "exp": exp}

QUESTIONS = [
    q(1,"PEDS-U123",61,"Malnutrition condition",["Under-nutrition or over-nutrition","Only under","Only over","Only protein"],0,"Condition of undernutrition or overnutrition (Book p61)"),
    q(2,"PEDS-U123",61,"Wasting parameter",["Low weight for height (W/H)","Low height for age","Low weight for age","HC"],0,"Wasting Low weight for height (W/H) (Book p61)"),
    q(3,"PEDS-U123",61,"Wasting implication",["Acute severe weight loss","Chronic undernutrition","Wasting and/or stunting","Normal"],0,"Acute severe weight loss (Book p61)"),
    q(4,"PEDS-U123",61,"Stunting",["Low height for age","Low weight for height","Low weight for age","Normal"],0,"Stunting Low height for age (Book p61)"),
    q(5,"PEDS-U123",61,"Stunting implication",["Chronic undernutrition","Acute severe","Wasting and/or stunting","Normal"],0,"Chronic undernutrition (Book p61)"),
    q(6,"PEDS-U123",61,"Underweight",["Low weight for age","Low weight for height","Low height for age","Normal"],0,"Underweight Low weight for age (Book p61)"),
    q(7,"PEDS-U123",61,"Underweight can refer",["To wasting and/or stunting","Only wasting","Only stunting","Normal"],0,"Can refer to wasting and/or stunting (Book p61)"),
    q(8,"PEDS-U123",61,"WHO moderate wasting",["-2 to -3 S.D.","<-3 S.D.","Normal","<-3.5"],0,"Moderate -2 to -3 S.D. (Book p61)"),
    q(9,"PEDS-U123",61,"Severe wasting",["<-3 S.D.","-2 to -3","Normal","<-3.5"],0,"Severe <-3 S.D. (Book p61)"),
    q(10,"PEDS-U123",61,"Moderate stunting",["-2 to -3 S.D.","<-3","Normal","<-3.5"],0,"Moderate -2 to -3 S.D. (Book p61)"),
    q(11,"PEDS-U123",61,"Severe stunting",["<-3 S.D.","-2 to -3","Normal","<-3.5"],0,"Severe <-3 S.D. (Book p61)"),
    q(12,"PEDS-U123",61,"Symmetrical edema moderate vs severe",["Absent vs Present","Present vs Absent","Both absent","Both present"],0,"Symmetrical edema Absent vs Present (Book p61)"),
    q(13,"PEDS-U124",61,"Marasmus predominant deficiency",["Calorie","Protein","Both","None"],0,"Marasmus Predominant deficiency Calorie (Book p61 00:05:02)"),
    q(14,"PEDS-U124",61,"Kwashiorkor predominant",["Protein","Calorie","Both","None"],0,"Kwashiorkor Protein (Book p61)"),
    q(15,"PEDS-U124",61,"Marasmus onset",["<1 yr","1-4 yrs","4-6 yrs","Normal"],0,"Marasmus Onset <1 yr (Book p61)"),
    q(16,"PEDS-U124",61,"Kwashiorkor onset",["1-4 yrs","<1 yr","4-6 yrs","Normal"],0,"1-4 yrs (Book p61)"),
    q(17,"PEDS-U124",61,"Marasmus edema",["Absent","Present +++ Anasarca","Present +","No"],0,"Marasmus Edema Absent (Book p61)"),
    q(18,"PEDS-U124",61,"Kwashiorkor edema",["Present (+++); Anasarca","Absent","No","Only +"],0,"Present (+++); Anasarca (Book p61)"),
    q(19,"PEDS-U124",61,"Marasmus muscle wasting",["Present (+++)","Present (+) masked by edema","Absent","No"],0,"Present (+++) (Book p61)"),
    q(20,"PEDS-U124",61,"Kwashiorkor muscle wasting",["Present (+) but masked by edema","Present +++","Absent","No"],0,"Present (+) but masked by edema (Book p61)"),
    q(21,"PEDS-U124",61,"Marasmus appetite",["Good","Poor","No","Low"],0,"Good (Book p61)"),
    q(22,"PEDS-U124",61,"Kwashiorkor appetite",["Poor","Good","Normal","No"],0,"Poor (Book p61)"),
    q(23,"PEDS-U125",61,"Marasmus general Alert",["Alert","Dull/lethargic/irritable","Poor","No"],0,"Marasmus Alert (Book p61)"),
    q(24,"PEDS-U125",61,"Skin and bone appearance",["Marasmus Skin and bone Loose skin folds axilla & buttocks Baggy pant appearance","Kwashiorkor","Normal","No"],0,"Skin and bone appearance Loose skin folds in axilla & buttocks Baggy pant appearance (Book p61)"),
    q(25,"PEDS-U125",61,"Thin and brittle hair Marasmus plus",["Simian facies d/t buccal fat loss + wrinkles Loss of muscle mass","Flag sign","Anasarca","Crazy pavement"],0,"Thin and brittle hair Simian facies d/t buccal fat loss + wrinkles Loss of muscle mass (Book p61 image Marasmus)"),
    q(26,"PEDS-U125",61,"Kwashiorkor general",["Dull/lethargic/irritable","Alert","Normal","Good appetite"],0,"Kwashiorkor Dull/lethargic/irritable (Book p61)"),
    q(27,"PEDS-U125",61,"Skin changes Kwashiorkor",["Flaky-paint appearance; Hyperpigmented patches","Baggy pant","Normal","Thin hair only"],0,"Skin changes : Flaky-paint appearance; Hyperpigmented patches (Book p61)"),
    q(28,"PEDS-U125",61,"Flag sign",["Alternating grey & black patches in the hair","Cracks on skin","Baggy pant","Simian facies"],0,"Flag sign (Alternating grey & black patches in the hair) (Book p61)"),
    q(29,"PEDS-U125",61,"↓ S. Albumin → ↓ oncotic pressure →",["Anasarca","No edema","Baggy pant","Crazy pavement"],0,"↓ S. Albumin ↓ oncotic pressure Anasarca (Book p61 arrow)"),
    q(30,"PEDS-U125",61,"Crazy pavement appearance",["Cracks on skin","Flag sign","Flaky paint","Baggy pant"],0,"Crazy pavement appearance (Cracks on skin) (Book p61)"),
    q(31,"PEDS-U125",61,"Bulging abdomen",["Kwashiorkor (ascites)","Marasmus","Normal","No"],0,"Bulging abdomen (ascites) Kwashiorkor image (Book p61)"),
    q(32,"PEDS-U125",61,"Moon face",["Kwashiorkor","Marasmus","Normal","No"],0,"Moon face Kwashiorkor (Book p61)"),
    q(33,"PEDS-U126",62,"SAM Criteria Weight for Height",["<-3.5 S.D. (per book)","<-3 S.D.","-2 to -3","Normal"],0,"1. Weight for Height : <-3.5 S.D. (Book p62 00:13:36)"),
    q(34,"PEDS-U126",62,"Bipedal edema",["Diagnosis of exclusion","Not exclusion","Normal","No"],0,"2. Bipedal edema : Diagnosis of exclusion (Book p62)"),
    q(35,"PEDS-U126",62,"MAC",["<11.5 cm","<12.5","<13.5","<11"],0,"3. Mean Arm Circumference (MAC) : <11.5 cm (Book p62)"),
    q(36,"PEDS-U126",62,"Presence of any of above",["SAM","Not SAM","Normal","Moderate"],0,"Presence of any of the above : SAM (Book p62)"),
    q(37,"PEDS-U126",62,"Uncomplicated SAM Appetite",["Good","Poor","Absent","No"],0,"Uncomplicated SAM Appetite Good (Book p62)"),
    q(38,"PEDS-U126",62,"Complicated Appetite",["Poor","Good","Absent","No"],0,"Complicated SAM Poor (Book p62)"),
    q(39,"PEDS-U126",62,"Uncomplicated Generalized edema",["Absent","Present","No","Both"],0,"Absent (Book p62)"),
    q(40,"PEDS-U126",62,"Complicated edema",["Present","Absent","No","Both"],0,"Present (Book p62)"),
    q(41,"PEDS-U126",62,"Medical Complications uncomplicated vs complicated",["Absent vs Present","Present vs Absent","Both absent","Both present"],0,"Medical Complications Absent vs Present (Book p62)"),
    q(42,"PEDS-U126",62,"Intervention Uncomplicated vs Complicated",["Supervised Home management vs Hospital management","Both home","Both hospital","No"],0,"Intervention Supervised Home management vs Hospital management (Book p62)"),
    q(43,"PEDS-U127",62,"Nutrition goal",["175 Kcal/kg/day + Protein: 4-6 g/kg/day","100 Kcal","50 Kcal","543 Kcal"],0,"Nutrition goal : 175 Kcal/kg/day + Protein: 4-6 g/Kg/day (Book p62)"),
    q(44,"PEDS-U127",62,"Diets",["Home-made foods + Ready-to-use therapeutic food (RUTF)","Only home-made","Only RUTF","No"],0,"Diets: Home-made foods, Ready-to-use therapeutic food (RUTF) (Book p62)"),
    q(45,"PEDS-U127",62,"Ingredients",["Milk Solids, Sugars, Vegetable oil, Peanut butter & paste","Only milk","Only sugar","Only oil"],0,"Ingredients: 1. Milk Solids 2.Sugars 3.Vegetable oil 4.Peanut butter & paste (Book p62)"),
    q(46,"PEDS-U127",62,"Advantages",["Good palatability, Semi-solid consistency, Long shelf-life","Only palatability","Only shelf-life","No"],0,"Advantages: 1. Good palatability 2.Semi-solid consistency 3.Long shelf-life (Book p62)"),
    q(47,"PEDS-U127",62,"Nutrient Value",["543 Kcal + 15g protein (Per 100g)","175 Kcal","100 Kcal","No"],0,"Nutrient Value : 543 Kcal + 15g protein (Per 100g) (Book p62)"),
    q(48,"PEDS-U127",62,"Antibiotic",["Oral Amoxicillin x 5d","Only albendazole","Only Vit A","No"],0,"Antibiotic: Oral Amoxicillin x 5d (Book p62 Additional Interventions 3 As)"),
    q(49,"PEDS-U127",62,"Albendazole Dosage",["<2y : 200mg >2y : 400mg","Only 200","Only 400","No"],0,"Albendazole (Deworming) : Dosage <2y : 200mg >2y : 400mg (Book p62)"),
    q(50,"PEDS-U127",62,"Vitamin A <6 months",["50,000 IU","1 Lakh IU","2 Lakh IU","No"],0,"Vitamin A <6 months - 50,000 IU (Book p62)"),
    q(51,"PEDS-U127",62,"6-12 months",["1 Lakh IU","50,000","2 Lakh","No"],0,"6-12 months - 1 Lakh IU (Book p62)"),
    q(52,"PEDS-U127",62,">12 months",["2 Lakh IU","1 Lakh","50,000","No"],0,">12 months - 2 Lakh IU (Book p62)"),
    q(53,"PEDS-U128",62,"Hospital management phases",["Stabilization phase : management of complications mnemonic SHIELDED + Rehabilitation","Only stabilization","Only rehabilitation","No"],0,"Hospital management management Stabilization phase: management of complications mnemonic [SHIELDED] Rehabilitation (Book p62)"),
    q(54,"PEDS-U129",63,"Hypoglycemia definition",["Blood glucose : <54 mg/dl","<70","<50","<60"],0,"Definition : Blood glucose : <54 mg/dl (Book p63 Phase I: Stabilization)"),
    q(55,"PEDS-U129",63,"Symptomatic Hypoglycemia Treatment",["IV 10% Dextrose : 5ml/kg STAT → Glucose infusion","Oral glucose 50mL","No","Only infusion"],0,"Symptomatic (Eg : Seizures) IV 10% Dextrose : 5ml/Kg STAT Glucose infusion (Book p63)"),
    q(56,"PEDS-U129",63,"Asymptomatic",["Oral glucose : 50mL","IV Dextrose","No","Glucose infusion"],0,"Asymptomatic Oral glucose : 50mL (Book p63)"),
    q(57,"PEDS-U129",63,"Hypothermia definition",["Axillary temp : <35°C / Rectal temperature : <35.5°C","<36","<37","<34"],0,"Definition : Axillary temp : <35°C / Rectal temperature : <35.5°C (Book p63)"),
    q(58,"PEDS-U129",63,"Treatment hypothermia",["Warming child using protective clothing Kangaroo mother care in infants","Only warming","Only Kangaroo","No"],0,"Treatment: Warming child using protective clothing Kangaroo mother care in infants (Book p63)"),
    q(59,"PEDS-U129",63,"Rapid rewarming",["Should be avoided as it causes dysequilibrium syndrome Causes Drowsiness, seizures, coma","Should be done","No effect","Promote"],0,"Note Rapid rewarming should be avoided as it causes dysequilibrium syndrome Causes : Drowsiness, seizures, coma (Book p63)"),
    q(60,"PEDS-U130",63,"Infections immunity",["↓ immunity (Usual signs may be absent) Empirical treatment is started in all children of SAM","Normal immunity","No empirical","No"],0,"↓ immunity (Usual signs may be absent) Empirical treatment is started in all children of SAM (Book p63)"),
    q(61,"PEDS-U130",63,"m/c antibiotics",["Ampicillin + Amikacin (Penicillin + Aminoglycoside)","Only Ampicillin","Only Amikacin","Ceftriaxone first"],0,"m/c antibiotics : Ampicillin + Amikacin (Penicillin + Aminoglycoside) (Book p63)"),
    q(62,"PEDS-U130",63,"If no improvement in 48hrs",["3rd generation cephalosporins (Eg : Ceftriaxone)","Continue same","No","Only Ampicillin"],0,"If no improvement in 48hrs 3rd generation cephalosporins (Eg : Ceftriaxone) (Book p63)"),
    q(63,"PEDS-U130",63,"m/c bacteria",["Gram-negative","Gram-positive","No","Both"],0,"m/c bacteria : Gram-negative (Book p63)"),
    q(64,"PEDS-U130",63,"Sodium levels",["↑ total body overall (Excess Na+ avoided)","↓ total body","Normal","Low"],0,"Sodium levels : ↑ total body overall (Excess Na+ avoided) (Book p63)"),
    q(65,"PEDS-U130",63,"Serum sodium",["Low/normal: (D/t intracellular sodium & dilution effect of edema)","High","Normal always","High due edema"],0,"Serum sodium : Low/normal: (D/t intracellular sodium & dilution effect of edema) (Book p63)"),
    q(66,"PEDS-U130",63,"Hypokalemia Hypomagnesemia Treatment",["Supplementation","No","Only Na","Only fluids"],0,"Hypokalemia Hypomagnesemia Treatment : Supplementation (Book p63)"),
    q(67,"PEDS-U130",63,"Dehydration Clinical Symptoms",["Thirst, urine output, Dryness of oral mucosa Treatment Started irrespective of symptoms","Only thirst","Only urine","Only dryness"],0,"Clinical Symptoms : Thirst, urine output, Dryness of oral mucosa Treatment : Started irrespective of symptoms (Book p63)"),
    q(68,"PEDS-U130",63,"No shock symptoms",["Oral fluids : Rehydration Solution for malnutrition (ReSomal)","Ringer lactate","No","IV"],0,"No shock symptoms : Oral fluids : Rehydration Solution for malnutrition (ReSomal) (Book p63)"),
    q(69,"PEDS-U130",63,"Shock symptoms present",["Ringer's lactate with 5% dextrose Contains K+ ions First 2 hours : 15 ml/kg → Resolution Oral fluids","ReSomal","No","Only oral"],0,"Shock symptoms present : Ringer's lactate with 5% dextrose Contains K+ ions First 2 hours : 15 ml/kg Resolution Oral fluids (Book p63)"),
    q(70,"PEDS-U130",63,"First 2 hours shock",["15 ml/kg","5 ml/kg","50 mL","No"],0,"First 2 hours : 15 ml/kg (Book p63)"),
    q(71,"PEDS-U130",63,"Multivitamin supplement",["Recommended for all SAM Dose : Twice RDA value","Not recommended","Once RDA","No"],0,"Multivitamin supplement recommended for all SAM Dose : Twice RDA value (Book p63)"),
    q(72,"PEDS-U130",63,"Iron absorption in first week",["↓ Iron absorption unabsorbed iron → Free radical damage Promote bacterial proliferation","↑ absorption","Normal","No"],0,"Iron absorption in first week ↓ Unabsorbed iron Free radical damage Promote bacterial proliferation (Book p63)"),
]

RANGES = {123:(1,12),124:(13,22),125:(23,32),126:(33,42),127:(43,52),128:(53,53),129:(54,59),130:(60,72)}
UNIT_RANGES = {1:(1,12),2:(13,22),3:(23,32),4:(33,42),5:(43,52),6:(53,53),7:(54,59),8:(60,72)}
for u in UNITS:
    s,e = UNIT_RANGES[u["n"]]
    u["qs"] = [f"PEDS-C15-{i:03d}" for i in range(s,e+1)]

pages = [q["page"] for q in QUESTIONS]
assert pages == sorted(pages), f"Pages not sorted {pages[:10]}"
assert len(QUESTIONS)==72
assert len(UNITS)==8
for u in UNITS:
    s,e = UNIT_RANGES[u["n"]]
    assert len(u["qs"])==e-s+1
