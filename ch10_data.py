CH = 10
UNITS = [
    {"id": "PEDS-U085", "ch": 10, "n": 1, "title": "Short Stature — Definition and Types", "sec": "Short stature · p45", "qs": [], "guide": "Height <3rd %ile or <-2SD. Normal variant <-2 to -3SD (Constitutional delay m/c, Familial); Pathological <-3SD syndromic. Prepubertal growth velocity 4-6 cm/yr both per table."},
    {"id": "PEDS-U086", "ch": 10, "n": 2, "title": "Etiology 1-3 — Undernutrition, Systemic, Endocrine", "sec": "ETIOLOGY · p45", "qs": [], "guide": "1 Chronic undernutrition stunting. 2 Chronic systemic illness (heart/lung) hampers growth. 3 Endocrine a deficiency GH/thyroid, b excess Cushing/precocious puberty → premature epiphyseal fusion → short stature."},
    {"id": "PEDS-U087", "ch": 10, "n": 3, "title": "Etiology 4-5 — Bony and Genetic", "sec": "ETIOLOGY · p45", "qs": [], "guide": "4 Bony disorders achondroplasia rhizomelia (short proximal limbs). 5 Genetic Down, Turner."},
    {"id": "PEDS-U088", "ch": 10, "n": 4, "title": "Evaluation Steps 1-3 — Height, Charts, MPH", "sec": "STEPS OF EVALUATION · p45-46", "qs": [], "guide": "1 Accurate height stadiometer >2y infantometer <2y. 2 Growth charts percentiles. 3 Mid parental height MPH target height (mother+father)/2 ±6.5 cm boys+/girls-."},
    {"id": "PEDS-U089", "ch": 10, "n": 5, "title": "Body Proportion — US:LS Ratio Normal and Abnormal", "sec": "Assessment of body proportion · p46", "qs": [], "guide": "US trunk, LS below pubis. Normal 1.7:1 birth →1.3:1 3y →1:1 10y →0.9:1 adult (increasing LS). ↑US:LS short limbs (achondroplasia, rickets, congenital hypothyroidism). ↓US:LS short trunk vertebral spondyloepiphyseal dysplasia."},
    {"id": "PEDS-U090", "ch": 10, "n": 6, "title": "Bone Age and Normal Variant Table", "sec": "Bone age · p46", "qs": [], "guide": "Bone age X-Ray ossification centres: infancy shoulder, 1-13y left wrist carpal. Atlas Tanner Whitehouse, Greulich-Pyle + Bone expert software. BA<CA most cases, BA=CA familial, BA>CA precocious puberty. Normal variant D/t genetic potential: constitutional delay (Normal final height/Delyed puberty/Delyed BA/Normal parents) vs familial (Short/Normal/Normal/Short)."},
    {"id": "PEDS-U091", "ch": 10, "n": 7, "title": "Algorithmic Approach to Short Stature", "sec": "ALGORITHMIC APPROACH · p47", "qs": [], "guide": "Normal growth velocity→ Normal BA =Familial, Delayed BA=Constitutional. Abnormal velocity→ US:LS Normal=Proportionate (↓GH, malnutrition, genetic syndromes), Abnormal=Disproportionate ↑US:LS short limbs, ↓US:LS short trunk."},
    {"id": "PEDS-U092", "ch": 10, "n": 8, "title": "Tall Stature — Normal Variant", "sec": "Tall stature · p47", "qs": [], "guide": "Height >+2SD or 97th %ile. Normal variant m/c type: familial, constitutional acceleration of growth (CAG)."},
    {"id": "PEDS-U093", "ch": 10, "n": 9, "title": "Tall Stature — Pathological Causes", "sec": "Tall pathological · p47", "qs": [], "guide": "Syndromes Marfan superior lens dislocation, Klinefelter genetic, Sotos overgrowth/cerebral gigantism. Metabolic homocystinuria cystathionine-β synthase deficiency inferior lens dislocation marfanoid. Endocrine pituitary adenoma GH excess, hyperthyroidism."},
]

def q(num, sec, page, qtext, opts, ans, exp):
    assert len(opts)==4 and 0 <= ans <4
    return {"id": f"PEDS-C10-{num:03d}", "sec": sec, "page": page, "q": qtext, "opts": opts, "ans": ans, "exp": exp}

QUESTIONS = [
    q(1,"PEDS-U085",45,"Short stature definition Height for age",["<3rd percentile or <-2 SD",">97th or >+2SD","<1st percentile","<-3SD only"],0,"Height for age <3rd percentile or <-2 SD (Book p45 00:00:18)"),
    q(2,"PEDS-U085",45,"Normal variant Height for age",["< -2 to -3 SD","<-3 SD",">+2 SD","Normal"],0,"Normal variant <-2 to -3 SD (Book p45)"),
    q(3,"PEDS-U085",45,"Pathological short stature Height for age",["<-3 SD","<-2 to -3",">+2","Normal"],0,"Pathological <-3 SD (Book p45)"),
    q(4,"PEDS-U085",45,"Normal variant seen in",["Constitutional delay (Overall m/c cause) + Familial short stature","Only syndromic","Only Down","Only Turner"],0,"Seen in Constitutional delay (Overall m/c cause), Familial short stature (Book p45)"),
    q(5,"PEDS-U085",45,"Pathological seen in",["Syndromic presentations","Familial","Constitutional","Normal"],0,"Syndromic presentations (Book p45)"),
    q(6,"PEDS-U085",45,"Overall m/c cause of short stature (normal variant)",["Constitutional delay","Familial","Pathological","Genetic"],0,"Constitutional delay (Overall m/c cause) (Book p45)"),
    q(7,"PEDS-U085",45,"Prepubertal growth velocity Normal variant vs Pathological per table",["Both 4-6 cm/yr (Normal)","4-6 vs <4","<4 both","Normal vs delayed"],0,"Table: Prepubertal growth velocity 4-6 cm/yr (Normal) for both columns per book (Book p45)"),
    q(8,"PEDS-U085",45,"Short stature TYPES header short stature 00:00:18 besides definition",["Height <3rd %ile or <-2SD","Height >97th","Weight","HC"],0,"00:00:18 Height for age <3rd percentile or <-2SD (Book p45)"),
    q(9,"PEDS-U086",45,"Etiology 1 Chronic undernutrition",["Stunting","Wasting","Normal","Tall"],0,"1. Chronic undernutrition : Stunting (Book p45)"),
    q(10,"PEDS-U086",45,"Chronic systemic illness Eg",["Chronic heart or lung diseases","Only heart","Only lung","Thyroid"],0,"Eg : Chronic heart or lung diseases (Book p45)"),
    q(11,"PEDS-U086",45,"Endocrine a Hormonal deficiency",["Growth hormone deficiency + Thyroid hormone deficiency","Only GH","Only thyroid","Cushing"],0,"a. Hormonal deficiency : GH deficiency, Thyroid hormone deficiency (Book p45)"),
    q(12,"PEDS-U086",45,"Endocrine b Hormone excess",["Cushing syndrome + Precocious puberty excess of sex steroids","Only Cushing","Only precocious","GH deficiency"],0,"b. Hormone excess : Cushing, Precocious puberty (Book p45)"),
    q(13,"PEDS-U086",45,"Precocious puberty excess sex steroids →",["Premature fusion of epiphysis (Arrests bone growth) → Short stature","Normal growth","Tall always","No effect"],0,"Precocious puberty : Excess of sex steroids → Premature fusion of epiphysis (Arrests bone growth) → Short stature (Book p45)"),
    q(14,"PEDS-U086",45,"Hormone excess arrests bone growth via",["Premature fusion of epiphysis","Delayed fusion","No fusion","Normal fusion"],0,"Premature fusion of epiphysis (Arrests bone growth) (Book p45)"),
    q(15,"PEDS-U086",45,"Which hormone deficiency causes short stature",["Growth hormone and Thyroid","Only GH","Only thyroid","Cushing"],0,"GH deficiency, Thyroid hormone deficiency (Book p45)"),
    q(16,"PEDS-U087",45,"Bony disorders Eg Achondroplasia",["Short proximal part of limbs → Rhizomelia","Short distal","Short trunk","Normal"],0,"Eg : Achondroplasia : Short proximal part of limbs → Rhizomelia (Book p45)"),
    q(17,"PEDS-U087",45,"Rhizomelia means",["Short proximal part of limbs","Short distal","Short trunk","Short head"],0,"Rhizomelia = Short proximal part of limbs (achondroplasia) (Book p45)"),
    q(18,"PEDS-U087",45,"Genetic disorders causing short stature",["Down syndrome, Turner syndrome","Marfan","Klinefelter","Sotos"],0,"5. Genetic disorders : Down's syndrome, Turner's syndrome (Book p45)"),
    q(19,"PEDS-U087",45,"Bony disorders affect",["Bone growth","Only hormone","Only nutrition","Systemic"],0,"4. Bony disorders : Bone growth affected (Book p45)"),
    q(20,"PEDS-U088",45,"Accurate assessment of height >2y vs <2y",[">2y stadiometer, <2y infantometer","Both stadiometer","Both infantometer",">2 infantometer"],0,"Use stadiometer/infantometer (>2 yrs old) (<2yrs old) (Book p45)"),
    q(21,"PEDS-U088",45,"Compare with growth charts",["Plot values and assess percentiles","Only height","Only weight","No"],0,"Compare with growth charts : Plot values and assess percentiles (Book p45)"),
    q(22,"PEDS-U088",46,"Mid parental height MPH is",["Target height of the child, Gives approximate of child's adult height","Only target","Not adult","Current height"],0,"Target height of the child, Gives an approximate of the child's adult height (Book p46)"),
    q(23,"PEDS-U088",46,"MPH formula",["[(Mother+s + Father+s) height /2] +6.5 boys -6.5 girls","(M+F)/2 only","+13 / -13","+3.5 / -3.5"],0,"mPH = [(mother's+Father's) height /2] +6.5 boys -6.5 girls (Book p46)"),
    q(24,"PEDS-U088",46,"MPH boys add",["+6.5 cm","-6.5","+13","+3"],0,"+6.5 cm (boys) (Book p46)"),
    q(25,"PEDS-U088",46,"MPH girls",["-6.5 cm","+6.5","-13","+6.5 girls"],0,"-6.5 cm (girls) (Book p46)"),
    q(26,"PEDS-U089",46,"Upper segment",["Height of the trunk","Below pubis","Only limbs","Pubis"],0,"Upper segment : Height of the trunk (Book p46)"),
    q(27,"PEDS-U089",46,"Lower segment",["Height/length below pubis","Trunk","Only head","Pubis to head"],0,"Lower segment : Height/length below pubis (Book p46)"),
    q(28,"PEDS-U089",46,"US:LS diagram Pubis line",["US:Trunk Pubis LS:Limbs","US:Limbs","Trunk head","No"],0,"US : Trunk → Pubis → LS : Limbs (Book p46)"),
    q(29,"PEDS-U089",46,"Normal US:LS At birth",["1.7:1","1.3:1","1:1","0.9:1"],0,"At birth :1.7:1 (Book p46)"),
    q(30,"PEDS-U089",46,"3 years",["1.3:1","1.7:1","1:1","0.9:1"],0,"3 years :1.3:1 (Book p46)"),
    q(31,"PEDS-U089",46,"At 10 yrs",["1:1","1.7:1","1.3:1","0.9:1"],0,"At 10 yrs :1:1 (Book p46)"),
    q(32,"PEDS-U089",46,"Adults",["0.9:1","1:1","1.3:1","1.7:1"],0,"Adults :0.9:1 (Book p46)"),
    q(33,"PEDS-U089",46,"Trend Increasing length of lower segment",["US:LS decreases with age","Increases","No change","US increases"],0,"Increasing length of lower segment → ratio decreases (Book p46)"),
    q(34,"PEDS-U089",46,"↑US:LS means",["Lower segment/limbs are short","Trunk short","Normal","Both short"],0,"1. ↑ US:LS Lower segment/limbs are short (Book p46)"),
    q(35,"PEDS-U089",46,"↑US:LS causes",["Achondroplasia, Rickets, Congenital hypothyroidism","Spondyloepiphyseal","Normal","Down"],0,"Achondroplasia, Rickets, Congenital hypothyroidism (Book p46)"),
    q(36,"PEDS-U089",46,"↓US:LS means",["Trunk is smaller → Pathology of vertebral column","Limbs short","Normal","Both"],0,"↓ US:LS Trunk is smaller → Pathology of vertebral Column (Book p46)"),
    q(37,"PEDS-U089",46,"↓US:LS Eg",["Spondyloepiphyseal dysplasia","Achondroplasia","Rickets","Hypothyroidism"],0,"Eg : Spondyloepiphyseal dysplasia (Book p46)"),
    q(38,"PEDS-U090",46,"Bone age Evaluated by",["X-Ray Depends on appearance of ossification centres","Only inspection","Growth chart","History"],0,"Bone age : Evaluated by X-Ray Depends on appearance of ossification centres (Book p46)"),
    q(39,"PEDS-U090",46,"Infancy X-Ray",["Shoulder X-Ray","Left wrist","Knee","Hand"],0,"Infancy Shoulder X-Ray (Book p46)"),
    q(40,"PEDS-U090",46,"1-13 yrs X-Ray",["Left wrist (Ossification centres of carpal bones)","Shoulder","Both","No"],0,"1-13 yrs Left wrist (Ossification centres of carpal bones) (Book p46)"),
    q(41,"PEDS-U090",46,"Atlas used",["Tanner Whitehouse method, Greulich & Pyle atlas (G&P), Bone expert software","Only TW","Only G&P","No"],0,"Tanner Whitehouse method, Greulich & Pyle atlas (G,P), Bone expert software (Book p46)"),
    q(42,"PEDS-U090",46,"Interpretation In most cases →",["Bone age (BA) < Chronological age (CA)","BA=CA","BA>CA","Normal"],0,"In most cases of short stature → BA < CA (Book p46)"),
    q(43,"PEDS-U090",46,"Exception BA = CA",["Familial short stature","Constitutional delay","Precocious puberty","Normal"],0,"Exception : BA = CA : Familial short stature (Book p46)"),
    q(44,"PEDS-U090",46,"BA > CA",["Precocious puberty (d/t ↑ sex steroids)","Familial","Constitutional","Normal"],0,"BA > CA : Precocious puberty (d/t ↑ sex steroids) (Book p46)"),
    q(45,"PEDS-U090",46,"Normal variant of short stature D/t",["Genetic potential","Only hormones","Only nutrition","Only bony"],0,"NORMAL VARIANT OF SHORT STATURE: D/t genetic potential (Book p46)"),
    q(46,"PEDS-U090",46,"Constitutional delay Final adult height",["Normal","Short","Tall","Very short"],0,"Constitutional delay Final (adult) height Normal (Book p46)"),
    q(47,"PEDS-U090",46,"Familial short stature Final adult height",["Short","Normal","Tall","Normal"],0,"Familial short stature Final height Short (Book p46)"),
    q(48,"PEDS-U090",46,"Constitutional delay Age at puberty",["Delayed","Normal","Early","Normal"],0,"Constitutional delay Age at puberty Delayed (Book p46)"),
    q(49,"PEDS-U090",46,"Familial Age at puberty",["Normal","Delayed","Early","Delayed"],0,"Familial Age at puberty Normal (Book p46)"),
    q(50,"PEDS-U090",46,"Constitutional delay Bone age",["Delayed","Normal","Advanced","Normal"],0,"Constitutional delay Bone age Delayed (Book p46)"),
    q(51,"PEDS-U090",46,"Familial Bone age",["Normal","Delayed","Advanced","Delayed"],0,"Familial Bone age Normal (Book p46)"),
    q(52,"PEDS-U090",46,"Constitutional delay Parents height",["Normal","Short","Tall","Short"],0,"Constitutional delay Parents' height Normal (Book p46)"),
    q(53,"PEDS-U090",46,"Familial Parents height",["Short","Normal","Tall","Normal"],0,"Familial Parents' height Short (Book p46)"),
    q(54,"PEDS-U091",47,"Algorithmic approach first branch",["Normal growth velocity vs Abnormal growth velocity","Normal BA vs Delayed","No","Height"],0,"Short stature → Normal growth velocity vs Abnormal growth velocity (Book p47)"),
    q(55,"PEDS-U091",47,"Normal growth velocity + Normal BA →",["Familial short stature","Constitutional delay","Proportionate","Disproportionate"],0,"Normal growth velocity → Normal BA → Familial short stature (Book p47)"),
    q(56,"PEDS-U091",47,"Normal growth velocity + Delayed BA →",["Constitutional delay","Familial","Proportionate","Disproportionate"],0,"Delayed BA → Constitutional delay (Book p47)"),
    q(57,"PEDS-U091",47,"Abnormal growth velocity next is",["US:LS ratio","Bone age","Parents height","Growth charts"],0,"Abnormal growth velocity → US : LS ratio (Book p47)"),
    q(58,"PEDS-U091",47,"Abnormal velocity + Normal US:LS →",["Proportionate short stature: ↓GH, malnutrition, Genetic syndromes","Disproportionate","Familial","Constitutional"],0,"Normal → Proportionate short stature: ↓GH, malnutrition, Genetic syndromes (Book p47)"),
    q(59,"PEDS-U091",47,"Proportionate causes",["↓GH, malnutrition, Genetic syndromes","↑US:LS","↓US:LS","Normal"],0,"Proportionate: ↓GH, malnutrition, Genetic syndromes (Book p47)"),
    q(60,"PEDS-U091",47,"Abnormal US:LS →",["Disproportionate short stature","Proportionate","Normal","Familial"],0,"Abnormal → Disproportionate short stature (Book p47)"),
    q(61,"PEDS-U091",47,"↑US:LS indicates",["Short limbs","Short trunk","Normal","Tall"],0,"↑US:LS (Short limbs) (Book p47)"),
    q(62,"PEDS-U091",47,"↓US:LS indicates",["Short trunk","Short limbs","Normal","Tall"],0,"↓US:LS (Short trunk) (Book p47)"),
    q(63,"PEDS-U092",47,"Tall stature Definition Height for age",[">+2 SD or 97th percentile","<-2SD","<-3SD",">+3SD only"],0,"Height for age >+2SD or 97th percentile (Book p47 00:22:35)"),
    q(64,"PEDS-U092",47,"NORMAL VARIANT m/c type",["m/c type","Rare","Pathological","No"],0,"NORMAL VARIANT: m/c type (Book p47)"),
    q(65,"PEDS-U092",47,"Normal variant Types",["Familial + Constitutional acceleration of growth (CAG)","Only familial","Only CAG","Marfan"],0,"Types → Familial, Constitutional acceleration of growth (CAG) (Book p47)"),
    q(66,"PEDS-U093",47,"Marfan lens dislocation",["Superior lens dislocation","Inferior","No","Central"],0,"Marfan syndrome : Superior lens dislocation (Book p47)"),
    q(67,"PEDS-U093",47,"Klinefelter syndrome is",["Genetic","Metabolic","Endocrine","Normal variant"],0,"Klinefelter's syndrome (Genetic) (Book p47)"),
    q(68,"PEDS-U093",47,"Overgrowth/cerebral gigantism",["Sotos syndrome","Marfan","Klinefelter","Homocystinuria"],0,"Overgrowth/cerebral gigantism : Sotos syndrome (Book p47)"),
    q(69,"PEDS-U093",47,"Homocystinuria deficiency",["Cystathionine -β synthase deficiency","Phenylalanine hydroxylase","GH","Thyroid"],0,"Homocystinuria : D/t cystathionine -β synthase deficiency (Book p47)"),
    q(70,"PEDS-U093",47,"Homocystinuria lens dislocation",["Inferior lens dislocation","Superior","No","Normal"],0,"Inferior lens dislocation (Book p47)"),
    q(71,"PEDS-U093",47,"Homocystinuria features",["Marfan like features","No marfanoid","Normal","Superior lens"],0,"Marfan like features (Book p47)"),
    q(72,"PEDS-U093",47,"Marfan vs Homocystinuria lens",["Marfan superior, Homocystinuria inferior","Both superior","Both inferior","No"],0,"Marfan superior vs Homocystinuria inferior (Book p47)"),
    q(73,"PEDS-U093",47,"Pituitary adenoma tall cause",["GH excess","GH deficiency","Thyroid","Low GH"],0,"Pituitary adenoma : GH excess (Book p47)"),
    q(74,"PEDS-U093",47,"Other endocrine tall",["Hyperthyroidism","Hypothyroidism","GH deficiency","Thyroid deficiency"],0,"Hyperthyroidism (Book p47)"),
    q(75,"PEDS-U093",47,"Tall stature time stamp",["00:22:35","00:00:18","00:02:47","00:00:14"],0,"Tall stature 00:22:35 (Book p47)"),
]

RANGES = {85:(1,8),86:(9,15),87:(16,19),88:(20,25),89:(26,37),90:(38,53),91:(54,62),92:(63,65),93:(66,75)}
UNIT_RANGES = {1:(1,8),2:(9,15),3:(16,19),4:(20,25),5:(26,37),6:(38,53),7:(54,62),8:(63,65),9:(66,75)}
for u in UNITS:
    s,e = UNIT_RANGES[u["n"]]
    u["qs"] = [f"PEDS-C10-{i:03d}" for i in range(s,e+1)]

pages = [q["page"] for q in QUESTIONS]
assert pages == sorted(pages), f"Pages not sorted {pages[:10]}"
assert len(QUESTIONS)==75
assert len(UNITS)==9
for u in UNITS:
    s,e = UNIT_RANGES[u["n"]]
    assert len(u["qs"])==e-s+1
