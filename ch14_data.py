CH = 14
UNITS = [
    {"id": "PEDS-U115", "ch": 14, "n": 1, "title": "Introduction and Latching", "sec": "Introduction · p57", "qs": [], "guide": "Initiation as early as possible within minimum 1 hr after birth Exclusive breast milk upto 6 months Timeline 6m exclusive 1y breast feeding 2y. Correct latch 1 Mouth covers areola 2 Lips flanged out eversion 3 mouth wide open 4 chin touches breast Upper areola may be visible Reflexes rooting nipple touches mouth stimulus touch around mouth baby turns head, sucking/swallowing."},
    {"id": "PEDS-U116", "ch": 14, "n": 2, "title": "Feeding in Preterm Babies", "sec": "Feeding in Preterm · p57", "qs": [], "guide": "<28 weeks ↓↓↓ gut motility TPN 28-31 weeks expressed via NG/OG tube D/t ↑aspiration 32-34 weeks paladai/katori spoon D/t ↑aspiration >34 weeks direct breastfeeding."},
    {"id": "PEDS-U117", "ch": 14, "n": 3, "title": "Properties — Immunological and HMO", "sec": "Properties · p58", "qs": [], "guide": "PLABB: Para Amino Benzoic Acid malaria, Lactoferrin E.coli, IgA predominant colostrum, Bifidus factor lactobacillus bifidus, Bile salt stimulated lipase giardiasis, EGF intestinal maturation ↓bacterial. HMO most abundant solid non-digestible prebiotic ↑ favourable gut bacteria ↓ diarrhea NEC."},
    {"id": "PEDS-U118", "ch": 14, "n": 4, "title": "Nutritional Properties", "sec": "Nutritional · p58", "qs": [], "guide": "67 Kcal/100 mL Carbohydrates 6-7 g/dL >cow Lactose→Glucose+Galactose Galactocerebroside myelination Proteins 0.9-1.1 g/dL ↓solute Reno protective Whey:Casein 80:20 Easily digestible Taurine cysteine brain growth Fats 3.5-4 g/dL Rich PUFA DHA myelination Cow rich casein coagulates curd not digestible."},
    {"id": "PEDS-U119", "ch": 14, "n": 5, "title": "Composition — Colostrum, Transitional, Mature, Preterm", "sec": "Composition · p59", "qs": [], "guide": "Colostrum first 3-4 days thick lemon yellow rich 3As IgA VitA Lactoferrin anti-infective. Transitional 5-14 days ↑sugar ↑fat ↓Ig ↓proteins vs colostrum. Mature after 14 days. Preterm SIPS Sodium Iron Protein Sugars/Calories more."},
    {"id": "PEDS-U120", "ch": 14, "n": 6, "title": "Foremilk vs Hindmilk and Deficiencies", "sec": "Foremilk/Hindmilk · p59", "qs": [], "guide": "Foremilk initiation thin water quenches thirst white vs Hindmilk towards end thick fats satiety energy dense yellow. Deficiencies micronutrients VitK VitD VitB12 vegetarian/vegan mothers Supplementation VitK 1 mg IM anterolateral thigh (0.5 mg if <1Kg) VitD 400 IU/day upto 1y Iron Zinc not supplemented good bioavailability."},
    {"id": "PEDS-U121", "ch": 14, "n": 7, "title": "Supplementation in Preterm Breastfed", "sec": "Supplementation · p60", "qs": [], "guide": "1.5-2.5 Kg Iron 2 mg/kg/day upto1y D/t ↓iron stores ↓bioavailability + VitD + VitK. <1.5 Kg VLBW Human milk fortification HMF 32-40wks then VitD K iron till? Diagram."},
    {"id": "PEDS-U122", "ch": 14, "n": 8, "title": "Contraindications and Storage", "sec": "Contraindications · p60", "qs": [], "guide": "Absolute congenital lactose intolerance galactosemia mother on chemo/radiotherapy. Relative HIV SES High→Formula Low→Breastfeeding mixed contraindicated mother on ART Nevirapine prophylaxis neonate TB untreated/Rx <2wks Herpes active lesions on breast Infections. Storage Room 6-8 hrs Refrigerator 24 hrs Freezer -20°C 3 months."},
]

def q(num, sec, page, qtext, opts, ans, exp):
    assert len(opts)==4 and 0 <= ans <4
    return {"id": f"PEDS-C14-{num:03d}", "sec": sec, "page": page, "q": qtext, "opts": opts, "ans": ans, "exp": exp}

QUESTIONS = [
    q(1,"PEDS-U115",57,"Initiation of breastfeeding",["As early as possible within minimum 1 hr after birth","After 1 day","After 1 week","After 1 month"],0,"Initiation As early as possible within (minimum : 1 hr after birth) (Book p57 00:00:34)"),
    q(2,"PEDS-U115",57,"Exclusive breastfeeding",["Infant only receives breast milk upto 6 months of age","Upto 1 year exclusive","Upto 2 years","No"],0,"Exclusive breastfeeding : Infant only receives breast milk upto 6 months of age (Book p57)"),
    q(3,"PEDS-U115",57,"Timeline Exclusive 6m Breast feeding upto",["1 yr with complementary, upto 2 yr","Only 6m","Only 1yr","Only 2yr"],0,"Diagram Exclusive breast 6m feeding Breast feeding 1yr 2yr (Book p57)"),
    q(4,"PEDS-U115",57,"Correct latching 1",["Mouth covers areola","Mouth not open","Chin not touching","Upper areola not visible"],0,"1 Mouth covers areola (Book p57 Correct Latch-on image)"),
    q(5,"PEDS-U115",57,"2",["Lips are flanged out (Eversion)","Closed lips","Pursed","No"],0,"2 Lips are flanged out (Eversion) (Book p57)"),
    q(6,"PEDS-U115",57,"3",["Mouth wide open","Mouth closed","Small open","No"],0,"3. mouth wide open (Book p57)"),
    q(7,"PEDS-U115",57,"4",["Chin touches the breast","Chin away","Cheek touches","No"],0,"4. Chin touches the breast (Book p57)"),
    q(8,"PEDS-U115",57,"Note upper areola",["May be visible","Not visible","Must be fully covered","No"],0,"Note : upper areola may be visible (Book p57)"),
    q(9,"PEDS-U115",57,"Rooting reflex",["Nipple touches the mouth & initiates reflex Stimulus touch around the mouth Baby turns head towards touch","Sucking","Swallowing","No"],0,"Rooting reflex : Nipple touches the mouth & initiates Rooting reflex image Baby turns head towards touch (Book p57)"),
    q(10,"PEDS-U115",57,"Second reflex assisting breastfeeding",["Sucking and swallowing reflex","Rooting only","No","Grasping"],0,"2. Sucking and swallowing reflex (Book p57)"),
    q(11,"PEDS-U116",57,"<28 weeks feeding",["Total Parenteral Nutrition (TPN) D/t ↓↓↓ gut motility","Expressed via NG tube","Paladai","Direct"],0,"<28 weeks (↓↓↓ gut motility) Total Parenteral Nutrition (TPN) (Book p57 00:04:30)"),
    q(12,"PEDS-U116",57,"28-31 weeks",["Expressed breastmilk via nasogastric or orogastric tube (D/t ↑risk of aspiration)","TPN","Paladai","Direct"],0,"28-31 weeks Expressed breastmilk via nasogastric or orogastric tube (D/t ↑risk of aspiration) (Book p57)"),
    q(13,"PEDS-U116",57,"32-34 weeks",["Feeding breastmilk by paladai or Katori spoon (D/t ↑risk of aspiration)","TPN","NG tube","Direct"],0,"32-34 weeks Feeding breastmilk by paladai or Katori spoon (D/t ↑risk of aspiration) (Book p57)"),
    q(14,"PEDS-U116",57,">34 weeks",["Direct breastfeeding","TPN","NG tube","Paladai"],0,">34 weeks Direct breastfeeding (Book p57)"),
    q(15,"PEDS-U117",58,"Immunological mnemonic",["PLABB","SIPS","LOX-STD","Good Doctor"],0,"Mnemonic : PLABB (Book p58 00:07:47)"),
    q(16,"PEDS-U117",58,"Para Amino Benzoic Acid",["Protection from malaria","E.coli","Giardiasis","Bacterial"],0,"Low levels of Para Amino Benzoic Acid : Protection from malaria (Book p58)"),
    q(17,"PEDS-U117",58,"Lactoferrin",["Protection from E.coli","Malaria","Giardiasis","Bifidus"],0,"Lactoferrin : Protection from E.coli (Book p58)"),
    q(18,"PEDS-U117",58,"IgA",["Predominant immunoglobulin in colostrum","Malaria","E.coli","Giardiasis"],0,"IgA : Predominant immunoglobulin in colostrum (Book p58)"),
    q(19,"PEDS-U117",58,"Bifidus factor",["Promotes lactobacillus bifidus growth","Malaria","E.coli","Giardiasis"],0,"Bifidus factor : Promotes lactobacillus bifidus growth (Book p58)"),
    q(20,"PEDS-U117",58,"Bile salt stimulated lipase",["Protection from giardiasis","Malaria","E.coli","Bifidus"],0,"Bile salt stimulated lipase : Protection from giardiasis (Book p58)"),
    q(21,"PEDS-U117",58,"Epidermal Growth Factor EGF →",["Promotes intestinal maturation → ↓ risk of bacterial infection","Malaria","E.coli","Giardiasis"],0,"Epidermal Growth Factor (EGF) → Promotes intestinal maturation → ↓ risk of bacterial infection (Book p58)"),
    q(22,"PEDS-U117",58,"Human milk Oligosaccharides HMO",["Most abundant solid in breast milk Non-digestible prebiotic → ↑es favourable gut bacteria → ↓es risk of diarrhea & necrotizing enterocolitis","Least abundant","Digestible","No"],0,"Most abundant solid in breast milk Non-digestible substance prebiotic → ↑es favourable gut bacteria → ↓es risk of diarrhea & necrotizing enterocolitis (Book p58)"),
    q(23,"PEDS-U118",58,"Nutritive value",["67 Kcal/100 mL","100 Kcal","50 Kcal","120 Kcal"],0,"Nutritive value : 67 Kcal/100 mL (Book p58)"),
    q(24,"PEDS-U118",58,"Carbohydrates",["6-7 g/dL (more than in cow milk) Lactose → Glucose + Galactose Galactocerebroside : Promotes myelination","Less than cow","No lactose","No myelination"],0,"Carbohydrates (Breast milk > cow milk) 6-7 g/dL Lactose → Glucose + Galactose Galactocerebroside : Promotes myelination (Book p58)"),
    q(25,"PEDS-U118",58,"Proteins",["0.9-1.1 g/dL Cow milk > breast milk by 3 times ↓protein → ↓ solute load → Reno protective Whey:Casein 80:20 Easily digestible Taurine & cysteine → Promote brain growth","More than cow","Equal",">>"],0,"Proteins (Cow milk > breast milk by 3 times) 0.9-1.1 g/dL ↓protein → ↓solute load Reno protective Whey:Casein 80:20 Easily digestible Amino acids Taurine & cysteine → Promote brain growth (Book p58)"),
    q(26,"PEDS-U118",58,"Whey:Casein ratio",["80:20 → Easily digestible","20:80","50:50","No"],0,"Whey : Casein ratio is 80:20 → Easily digestible (Book p58)"),
    q(27,"PEDS-U118",58,"Taurine & cysteine",["Promote brain growth","Myelination","E.coli protection","Malaria"],0,"Amino acids : Taurine & cysteine → Promote brain growth (Book p58)"),
    q(28,"PEDS-U118",58,"Fats",["3.5-4 g/dL Cow milk = breast milk Rich in PUFA (Eg DHA : Docosa Hexanoic Acid) : Promotes myelination","Less than cow","No PUFA","No myelination"],0,"Fats (Cow milk = breast milk) 3.5-4 g/dL Rich in PUFA (Eg DHA) : Promotes myelination (Book p58)"),
    q(29,"PEDS-U118",58,"Cow milk rich in casein →",["Coagulates in intestine → Curd → Not easily digestible","Easily digestible","No curd","No"],0,"Note Cow milk rich in casein → Coagulates in intestine → Curd → Not easily digestible (Book p58)"),
    q(30,"PEDS-U119",58,"Colostrum secreted during",["First 3-4 days","5-14 days","After 14 days","Preterm"],0,"Colostrum Secreted during first 3-4 days (Book p58 00:18:13)"),
    q(31,"PEDS-U119",58,"Thick & lemon yellow-coloured",["Colostrum","Transitional","Mature","Preterm"],0,"Thick & lemon yellow-coloured Colostrum (Book p58)"),
    q(32,"PEDS-U119",58,"Rich in mnemonic 3As",["IgA, Vitamin A, Anti-infective protein (Lactoferrin)","Only IgA","Only VitA","No"],0,"Rich in : (mnemonic → 3As) Ig A, Vitamin A, Anti-infective protein (Lactoferrin) (Book p58)"),
    q(33,"PEDS-U119",59,"Transitional milk",["Secreted after 5-14 days ↑sugar, ↑fat ↓Ig, ↓proteins Compared to colostrum","After 3-4 days","After 14 days","Preterm"],0,"2. Transitional milk Secreted after 5-14 days ↑sugar, ↑fat ↓Ig, ↓proteins Compared to colostrum (Book p59)"),
    q(34,"PEDS-U119",59,"Mature milk",["Secreted after 14 days","5-14 days","3-4 days","Preterm"],0,"3. Mature milk Secreted after 14 days (Book p59)"),
    q(35,"PEDS-U119",59,"Preterm milk mnemonic",["SIPS Sodium Iron Protein Sugars (Calories)","PLABB","LOX-STD","3As"],0,"PRETERM MILK Contains more : (mnemonic : SIPS) Sodium Iron Protein Sugars (Calories) (Book p59)"),
    q(36,"PEDS-U120",59,"Foremilk production",["At the initiation of feeding","Towards end","Middle","No"],0,"Foremilk Production At the initiation of feeding (Book p59)"),
    q(37,"PEDS-U120",59,"Hindmilk production",["Towards the end of feeding","At initiation","Middle","No"],0,"Hindmilk Towards the end of feeding (Book p59)"),
    q(38,"PEDS-U120",59,"Foremilk consistency",["Thin","Thick","Equal","No"],0,"Consistency Thin (Book p59)"),
    q(39,"PEDS-U120",59,"Hindmilk consistency",["Thick","Thin","Equal","No"],0,"Thick (Book p59)"),
    q(40,"PEDS-U120",59,"Main component foremilk",["Water","Fats","Proteins","Sugar"],0,"Main component Water (Book p59)"),
    q(41,"PEDS-U120",59,"Hindmilk main",["Fats","Water","Proteins","Sugar"],0,"Fats (Book p59)"),
    q(42,"PEDS-U120",59,"Function foremilk",["Quenches thirst","Satiety","Energy dense","No"],0,"Function Quenches thirst (Book p59)"),
    q(43,"PEDS-U120",59,"Hindmilk function",["Satiety (Energy dense)","Quenches thirst","Water","No"],0,"Satiety (Energy dense) (Book p59)"),
    q(44,"PEDS-U120",59,"Appearance foremilk",["White","Yellow","Clear","Brown"],0,"Appearance White (Book p59 image)"),
    q(45,"PEDS-U120",59,"Hindmilk appearance",["Yellow","White","Clear","Brown"],0,"Yellow (Book p59 image)"),
    q(46,"PEDS-U120",59,"Deficiencies Vitamin K, B12, D",["Vitamin K, Vitamin B12 (In vegetarian/vegan mothers), Vitamin D","Only K","Only D","Only B12"],0,"Vitamins : Vitamin K, Vitamin B12 (In vegetarian/vegan mothers), Vitamin D (Book p59 00:22:34)"),
    q(47,"PEDS-U120",59,"Vitamin K dose",["1 mg IM on anterolateral aspect of thigh (0.5 mg if birth weight <1Kg)","0.5 mg always","2 mg","No"],0,"Vitamin K 1 mg IM on anterolateral aspect of thigh (0.5 mg dose given : If birth weight <1Kg) (Book p59)"),
    q(48,"PEDS-U120",59,"Vitamin D dose",["400 IU/day orally upto 1 yr of age","800 IU","200 IU","No"],0,"Vitamin D 400 IU/day orally upto 1 yr of age (Book p59)"),
    q(49,"PEDS-U120",59,"Iron Zinc",["Not supplemented d/t good bioavailability","Supplemented high dose","No need","Supplemented"],0,"Others Iron Zinc Not supplemented d/t good bioavailability (Book p59)"),
    q(50,"PEDS-U121",60,"1.5-2.5 Kg supplements",["Iron 2 mg/kg/day upto 1 yr D/t ↓iron stores & ↓bioavailability + Vit D + Vit K","Only iron","Only Vit D","No"],0,"1.5-2.5 Kg Iron (2 mg/kg/day) upto 1 yr D/t ↓iron stores & ↓bioavailability Vit D Vit K (Book p60)"),
    q(51,"PEDS-U121",60,"<1.5 Kg VLBW",["Human milk fortification (HMF) 32-40 wks then Vit D K & iron","Only iron","Only Vit D","No"],0,"<1.5 Kg (very low birth weight) Human milk fortification (HMF) 32-40 wks Vit D K & iron (Book p60 diagram)"),
    q(52,"PEDS-U122",60,"Absolute contraindications",["Congenital lactose intolerance, Galactosemia, mother on chemo/radiotherapy","HIV","TB","Herpes"],0,"Absolute: Congenital lactose intolerance, Galactosemia, mother on chemo/radiotherapy (Book p60 00:27:02)"),
    q(53,"PEDS-U122",60,"HIV Relative High SES →",["Formula feeds","Breastfeeding","Mixed","No"],0,"HIV High SES → Formula feeds (Book p60)"),
    q(54,"PEDS-U122",60,"HIV Low →",["Breastfeeding","Formula","Mixed","No"],0,"Low → Breastfeeding (Book p60)"),
    q(55,"PEDS-U122",60,"Mixed feeding",["Contraindicated","Allowed","Preferred","No"],0,"Mixed feeding is contraindicated (Book p60)"),
    q(56,"PEDS-U122",60,"Mother should be on",["Anti-retroviral therapy","No","Only Nevirapine","No ART"],0,"Mother should be on anti-retroviral therapy (Book p60)"),
    q(57,"PEDS-U122",60,"Neonate prophylaxis",["Nevirapine prophylaxis for neonate","No","Only ART mother","No"],0,"Nevirapine prophylaxis for neonate (Book p60)"),
    q(58,"PEDS-U122",60,"Tuberculosis if",["Mother is untreated/Rx <2 weeks","Always contraindicated","Never","Only if treated"],0,"Tuberculosis : If mother is untreated/Rx <2 weeks (Book p60)"),
    q(59,"PEDS-U122",60,"Herpes only if",["Active lesions are present on breast","Always","Never","Only if not"],0,"Herpes (Only if active lesions are present on breast) (Book p60)"),
    q(60,"PEDS-U122",60,"Expressed storage Room temperature",["6-8 hrs","24 hrs","3 months","No"],0,"Room temperature 6-8 hrs (Book p60 00:31:28)"),
    q(61,"PEDS-U122",60,"Refrigerator",["24 hrs","6-8 hrs","3 months","No"],0,"Refrigerator 24 hrs (Book p60)"),
    q(62,"PEDS-U122",60,"Freezer -20°C",["3 months","24 hrs","6-8 hrs","No"],0,"In a freezer (-20°C) 3 months (Book p60)"),
]

RANGES = {115:(1,10),116:(11,14),117:(15,22),118:(23,29),119:(30,35),120:(36,49),121:(50,51),122:(52,62)}
UNIT_RANGES = {1:(1,10),2:(11,14),3:(15,22),4:(23,29),5:(30,35),6:(36,49),7:(50,51),8:(52,62)}
for u in UNITS:
    s,e = UNIT_RANGES[u["n"]]
    u["qs"] = [f"PEDS-C14-{i:03d}" for i in range(s,e+1)]

pages = [q["page"] for q in QUESTIONS]
assert pages == sorted(pages), f"Pages not sorted {pages[:10]}"
assert len(QUESTIONS)==62
assert len(UNITS)==8
for u in UNITS:
    s,e = UNIT_RANGES[u["n"]]
    assert len(u["qs"])==e-s+1
