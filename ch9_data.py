CH = 9
UNITS = [
    {"id": "PEDS-U076", "ch": 9, "n": 1, "title": "Microcephaly — Definitions and Primary Etiology", "sec": "Microcephaly · p41", "qs": [], "guide": "Small brain. HC <-2SD low, <-3SD severe/pathological. Primary: defective brain development—Trisomy 21/18/13, Cornelia de Lange (synorphys), Rubinstein-Taybi (broad thumb), familial AR."},
    {"id": "PEDS-U077", "ch": 9, "n": 2, "title": "Secondary Microcephaly and PKU Pathway", "sec": "Secondary · p41", "qs": [], "guide": "External factors: maternal TORCH/alcohol/Phenytoin/radiation, perinatal asphyxia, trauma/infection, PKU (phenylalanine hydroxylase deficiency → ↓tyrosine→↓melanin→hypopigmentation; phenylacetate etc → mousy urine → brain damage/microcephaly)."},
    {"id": "PEDS-U078", "ch": 9, "n": 3, "title": "Microcephaly d/t Teratogens", "sec": "Microcephaly d/t Teratogens · p42", "qs": [], "guide": "Fetal alcohol syndrome: microcephaly, FAS facies (small eyes, smooth philtrum, thin upper lip), m/c VSD. Fetal hydantoin (phenytoin): cleft lip/palate, microcephaly, cardiac defects, hypoplasia nails/phalanges."},
    {"id": "PEDS-U079", "ch": 9, "n": 4, "title": "Late Onset Acquired Syndromes and Macrocephaly Definition", "sec": "Late onset syndromes · p42", "qs": [], "guide": "Rett (X-linked dominant MECP2, normal → microcephaly after 1y, regression, hand-wringing midline, ataxia), Seckel (bird/beak nose), Angelman. Macrocephaly: HC >+2SD. Causes: fluid/hydrocephalus, hydranencephaly transillumination+."},
    {"id": "PEDS-U080", "ch": 9, "n": 5, "title": "Macrocephaly — Thick Skull and Brain Volume Introduction", "sec": "Macrocephaly · p43", "qs": [], "guide": "Thick skull: hemolytic anemia→extramedullary hematopoiesis (β-thal major) + achondroplasia/osteopetrosis. Brain volume ↑ megalencephaly introduction → lysosomal, leukodystrophy, genetic."},
    {"id": "PEDS-U081", "ch": 9, "n": 6, "title": "Megalencephaly — Metabolic and Genetic Causes", "sec": "Megalencephaly · p43", "qs": [], "guide": "Lysosomal: Tay-Sachs (Hex A, cherry spot, no HSM) vs Sandhoff (Hex A&B, +HSM). Leukodystrophies: Alexander/Canavan. Genetic: Sotos/cerebral gigantism, NF1, Fragile X CGG repeats (long face, large ears, macroorchidism). Familial m/c cause."},
    {"id": "PEDS-U082", "ch": 9, "n": 7, "title": "Craniosynostosis — Basics and Sutures", "sec": "Craniosynostosis · p43", "qs": [], "guide": "Cranio=skull, synostosis=fusion → premature. Normal: metopic <2y, coronal/sagittal/lambdoid <2nd decade. Rule: growth arrests perpendicular to fused suture, proceeds parallel."},
    {"id": "PEDS-U083", "ch": 9, "n": 8, "title": "Craniosynostosis — Types", "sec": "Types · p44", "qs": [], "guide": "1 Dolico/scapho m/c sagittal → AP expansion. 2 Brachy B/L coronal → transverse elongation. 3 Plagio U/L coronal → flat side + U/L elongation. 4 Trigono metopic → anterior elongation. 5 Oxy/Turri multiple → irregular."},
    {"id": "PEDS-U084", "ch": 9, "n": 9, "title": "Craniosynostosis — Syndromes", "sec": "Associated syndromes · p44", "qs": [], "guide": "Crouzon (AD, brachy, shallow orbit→exophthalmos/hypertelorism/maxillary hypoplasia, normal IQ, tower skull) vs Apert (AD, turricephaly, syndactyly mitten hand, low IQ, exophthalmos not prominent). Carpenter AR similar to Apert + obesity/hypogonadism."},
]

def q(num, sec, page, qtext, opts, ans, exp):
    assert len(opts)==4 and 0 <= ans <4
    return {"id": f"PEDS-C9-{num:03d}", "sec": sec, "page": page, "q": qtext, "opts": opts, "ans": ans, "exp": exp}

QUESTIONS = [
    # U076 1-12
    q(1,"PEDS-U076",41,"Microcephaly is indicative of",["Small brain size (Head size)","Large brain size","Fluid in brain","Thick skull"],0,"Indicative of small brain size (Head size) (Book p41)"),
    q(2,"PEDS-U076",41,"Definition: Head circumference for age < -2 SD →",["Low value","Pathological","Normal","High value"],0,"Head circumference (HC) for age < -2 SD → Low value (Book p41)"),
    q(3,"PEDS-U076",41,"True/severe/significant microcephaly HC <-3 SD →",["Pathological","Low value only","Normal","High"],0,"True/severe/significant microcephaly: HC for age < -3 SD → Pathological (Book p41)"),
    q(4,"PEDS-U076",41,"Etiology Primary is",["Defective brain development","External factors","Maternal toxins","Perinatal asphyxia"],0,"Primary: Defective brain development (Book p41)"),
    q(5,"PEDS-U076",41,"Primary Genetic defects: Trisomy",["21, 18, 13","Only 21","Only 18","Only 13"],0,"Trisomy (21, 18, 13) (Book p41)"),
    q(6,"PEDS-U076",41,"Cornelia de Lange syndrome feature",["Eyebrows joined in middle → Synorphys","Broad thumb","Bird face","Beak nose"],0,"Cornelia de Lange: Eyebrows are joined in the middle → Synorphys (Book p41)"),
    q(7,"PEDS-U076",41,"Rubinstein Taybi syndrome associated with",["Broad thumb","Synorphys","Bird face","Thin lip"],0,"Rubinstein taybi: A/w broad thumb (Book p41)"),
    q(8,"PEDS-U076",41,"Familial microcephaly inheritance",["Autosomal recessive","Autosomal dominant","X-linked recessive","X-linked dominant"],0,"Familial microcephaly: Autosomal recessive inheritance (Book p41)"),
    q(9,"PEDS-U076",41,"Synorphys meaning",["Eyebrows joined in middle","Broad thumb","Small eyes","Smooth philtrum"],0,"Synorphys = Eyebrows are joined in the middle (Book p41)"),
    q(10,"PEDS-U076",41,"Low value vs Pathological cutoffs",["<-2 SD low, <-3 SD pathological","<-2 pathological, <-3 low","Both low","Both pathological"],0,"<-2 SD Low value, <-3 SD Pathological (Book p41)"),
    q(11,"PEDS-U076",41,"Microcephaly definitions header timestamp",["00:00:14","00:16:23","00:25:28","00:00:30"],0,"Microcephaly 00:00:14 (Book p41)"),
    q(12,"PEDS-U076",41,"Primary defective brain development includes",["Genetic defects + Familial","Maternal TORCH","Radiation","PKU"],0,"Primary: 1 Genetic defects, 2 Familial (Book p41)"),
    # U077 13-26
    q(13,"PEDS-U077",41,"Secondary microcephaly due to",["External factors affecting brain growth","Defective brain development","Genetic only","Familial only"],0,"Secondary: External factors affecting brain growth (Book p41)"),
    q(14,"PEDS-U077",41,"Maternal factors include",["TORCH infections, Toxins Alcohol, Drugs Phenytoin, Radiation","Only TORCH","Only alcohol","Only radiation"],0,"Maternal factors: TORCH, Toxins Alcohol, Drugs Phenytoin, Radiation exposure during pregnancy (Book p41)"),
    q(15,"PEDS-U077",41,"Perinatal factor",["Birth asphyxia","TORCH","Alcohol","Phenytoin"],0,"Perinatal factors: Birth asphyxia (Book p41)"),
    q(16,"PEDS-U077",41,"Other CNS insults",["Trauma/injury, Infections","Only trauma","Only infections","PKU"],0,"Other CNS insults: Trauma/injury, Infections (Book p41)"),
    q(17,"PEDS-U077",41,"Phenylketonuria deficiency",["Deficiency of phenylalanine hydroxylase","Deficiency of tyrosine","Deficiency of melanin","Not enzyme"],0,"Phenylketonuria: Deficiency of phenylalanine hydroxylase (Book p41)"),
    q(18,"PEDS-U077",41,"Phenylalanine hydroxylase converts",["Phenylalanine → Tyrosine","Tyrosine→Melanin directly","Phenylalanine→Melanin","Tyrosine→Phenylalanine"],0,"Phenylalanine hydroxylase ↓ → Phenylalanine → Tyrosine ↓ (Book p41)"),
    q(19,"PEDS-U077",41,"Downstream: Tyrosine ↓ → melanin ↓ →",["Hypopigmentation (Hair, skin, eyes)","Hyperpigmentation","No change","Jaundice"],0,"Tyrosine ↓ → melanin ↓ → Hypopigmentation (Hair, skin, eyes) (Book p41)"),
    q(20,"PEDS-U077",41,"Phenylalanine converted to metabolites",["Phenylacetate, phenyl lactate, phenylpyruvate → mousy/musty urine odour","Only phenylacetate","Only tyrosine","Only melanin"],0,"Converted to its metabolites → Phenylacetate, phenyl lactate, phenylpyruvate → mousy/musty urine odour (Book p41)"),
    q(21,"PEDS-U077",41,"Phenylalanine accumulation leads to ↑ phenylalanine →",["Brain damage, microcephaly, seizure","No brain damage","Only skin","Only urine"],0,"↑ Phenylalanine → Brain damage, microcephaly, seizure (Book p41)"),
    q(22,"PEDS-U077",41,"PKU shows hypopigmentation due to",["↓ Tyrosine→↓ melanin","↑ Tyrosine","Normal melanin","↑ phenylalanine directly"],0,"↓ Tyrosine → ↓ melanin → Hypopigmentation (Book p41)"),
    q(23,"PEDS-U077",41,"Mousy/musty urine odour is due to",["Phenylacetate etc metabolites","Tyrosine","Melanin","Phenylalanine hydroxylase"],0,"Phenylacetate, phenyl lactate, phenylpyruvate → mousy/musty urine odour (Book p41)"),
    q(24,"PEDS-U077",41,"Secondary 4th point other than maternal/perinatal/CNS is",["Phenylketonuria","Genetic defects","Familial","TORCH"],0,"4. Phenylketonuria (Book p41)"),
    # U078 25-36
    q(25,"PEDS-U078",42,"Microcephaly d/t Teratogens: Fetal alcohol syndrome shows",["Microcephaly","Macrocephaly","Normal HC","No effect"],0,"Fetal alcohol syndrome: microcephaly (arrow) (Book p42)"),
    q(26,"PEDS-U078",42,"FAS Facial characteristics include",["Small eye openings, Smooth philtrum, Thin upper lip","Broad thumb","Bird face","Beak nose"],0,"FAS Facial Characteristics: small eye openings, smooth philtrum, thin upper lip (Book p42)"),
    q(27,"PEDS-U078",42,"Fetal alcohol syndrome most commonly cardiac",["Ventricular septal defect","ASD","PDA","Tetralogy"],0,"Most commonly: Ventricular septal defect (Book p42)"),
    q(28,"PEDS-U078",42,"Phenytoin (Diphenyl hydantoin) exposure causes",["Fetal hydantoin syndrome","Fetal alcohol","Rett","Seckel"],0,"Phenytoin exposure: Fetal hydantoin syndrome (Book p42)"),
    q(29,"PEDS-U078",42,"Fetal hydantoin features: Cleft lip & palate",["Yes + Microcephaly + Cardiac defects + Hypoplasia nails/phalanges","Only cleft","Only microcephaly","Only cardiac"],0,"Fetal hydantoin: Cleft lip & palate, Microcephaly, Cardiac defects, Hypoplasia of nails and phalanges (Book p42)"),
    q(30,"PEDS-U078",42,"Hydantoin microcephaly image shows",["Microcephaly with cleft and cardiac","Only microcephaly","Only cardiac","Normal"],0,"Microcephaly diagram with cleft lip/palate and cardiac defects (Book p42)"),
    q(31,"PEDS-U078",42,"VSD in Fetal alcohol vs hydantoin both can have cardiac defects but hydantoin additional is",["Hypoplasia nails/phalanges","Only VSD","Only microcephaly","No"],0,"Hydantoin: Hypoplasia of nails and phalanges (Book p42)"),
    q(32,"PEDS-U078",42,"Teratogen section header",["MICROCEPHALY D/T TERATOGENS","LATE ONSET","MACROCEPHALY","CRANIOSYNOSTOSIS"],0,"MICROCEPHALY D/T TERATOGENS (Book p42)"),
    # U079 37-52
    q(33,"PEDS-U079",42,"Late onset/acquired syndromes noticed",["During development of child (Not at birth)","At birth","Prenatal","Perinatal"],0,"Noticed during development of the child (Not at birth) (Book p42)"),
    q(34,"PEDS-U079",42,"Rett syndrome inheritance",["X-linked dominant","Autosomal recessive","X-linked recessive","Autosomal dominant"],0,"Rett: X-linked dominant inheritance (Book p42)"),
    q(35,"PEDS-U079",42,"Rett gene defect",["MECP-2 gene defect","CGG repeats","PHEX","SMN"],0,"MECP-2 gene defect (Book p42)"),
    q(36,"PEDS-U079",42,"Rett head size course",["Normal head size → microcephaly after 1 yr","Microcephaly at birth","Macrocephaly","Normal always"],0,"Normal head size → microcephaly after 1 yr (Book p42)"),
    q(37,"PEDS-U079",42,"Rett features: Developmental regression",["Loss of previously acquired milestones","No regression","Only ataxia","Only hand"],0,"Developmental regression: Loss of previously acquired milestones (Book p42)"),
    q(38,"PEDS-U079",42,"Rett characteristic hand movements",["Hand wringing stereotypic movements: Characteristic (Abnormal hand movements in the midline)","Normal","Bird face","Broad thumb"],0,"Hand wringing stereotypic movements: Characteristic (Abnormal hand movements in the midline) (Book p42)"),
    q(39,"PEDS-U079",42,"Rett also has",["Speech defects, Progressive ataxia → wheelchair dependent by adolescence","No speech","No ataxia","Normal speech"],0,"Speech defects, Progressive ataxia → wheelchair dependent by adolescence (Book p42)"),
    q(40,"PEDS-U079",42,"Seckel syndrome face",["Bird like face + beak like nose","Smooth philtrum","Thin lip","Broad thumb"],0,"Seckel: Bird like face + beak like nose (Book p42)"),
    q(41,"PEDS-U079",42,"Angelman syndrome listed under",["Late onset/acquired syndromes (with Rett, Seckel)","Teratogens","Primary","Macrocephaly"],0,"3. Angelman syndrome (listed) (Book p42)"),
    q(42,"PEDS-U079",42,"Macrocephaly definition",["HC for age > +2 SD","HC < -2SD","HC <-3SD","HC <-2"],0,"Macrocephaly Definition: HC for age > +2 SD (Book p42)"),
    q(43,"PEDS-U079",42,"Macrocephaly 00:16:23 etiology: ↑ fluid in brain",["Hydrocephalus, Hydranencephaly: Complete replacement brain tissue with fluids – Transillumination positive","Only hydrocephalus","Only hydranencephaly","No fluid"],0,"↑ fluid: Hydrocephalus, Hydranencephaly: Complete replacement ... Transillumination positive (Book p42)"),
    q(44,"PEDS-U079",42,"Hydranencephaly transillumination",["Positive","Negative","Not done","Unknown"],0,"Transillumination positive (Book p42)"),
    q(45,"PEDS-U079",42,"Abnormal midline hand movements image corresponds to",["Rett syndrome","Seckel","Fetal alcohol","Hydantoin"],0,"Abnormal midline hand movements (Rett) (Book p42)"),
    q(46,"PEDS-U079",42,"Seckel syndrome image shows",["Bird like face beak nose","Hand wringing","Microcephaly alcohol","Hydantoin"],0,"Seckel syndrome (image) (Book p42)"),
    # U080
    q(47,"PEDS-U080",43,"Thick skull causes: Hemolytic anemia →",["Extramedullary hematopoiesis → Expansion of the skull","No expansion","Thin skull","Normal"],0,"Hemolytic anemia → Extramedullary hematopoiesis → Expansion of the skull (Book p43)"),
    q(48,"PEDS-U080",43,"Example for thick skull hemolytic anemia",["β-thalassemia major","Sickle cell trait","Iron deficiency","Normal"],0,"Eg: β-thalassemia major (Book p43)"),
    q(49,"PEDS-U080",43,"Other thick skull causes",["Achondroplasia, Osteopetrosis","Only thalassemia","Only achondroplasia","Only osteopetrosis"],0,"Achondroplasia, Osteopetrosis (Book p43)"),
    q(50,"PEDS-U080",43,"↑ Brain volume is called",["Megalencephaly","Microcephaly","Macrocephaly","Plagiocephaly"],0,"3. ↑ Brain volume: megalencephaly (Book p43)"),
    q(51,"PEDS-U080",43,"Megalencephaly introduction includes",["Metabolic disorders, Genetic syndromes, Non syndromic Familial","Only metabolic","Only genetic","Only familial"],0,"Megalencephaly includes metabolic, genetic, non syndromic (Book p43)"),
    # U081
    q(52,"PEDS-U081",43,"Lysosomal disorders under megalencephaly",["Mucopolysaccharoidosis and Gm gangliosidoses","Only mucopoly","Only gangliosidoses","No"],0,"Lysosomal disorders: mucopolysaccharoidosis, Gm gangliosidoses (Book p43)"),
    q(53,"PEDS-U081",43,"Tay Sachs",["Hexosaminidase A deficiency, Cherry red spot in macula, No hepatosplenomegaly","Hex A&B, +HSM","No spot","HSM +"],0,"Tay Sach's: Hexosaminidase A deficiency, Cherry red spot, No hepatosplenomegaly (Book p43)"),
    q(54,"PEDS-U081",43,"Sandhoff",["Hexosaminidase A & B deficiency, Cherry red spot, Hepatosplenomegaly +","Hex A only, No HSM","No spot","Only HSM"],0,"Sandhoff: Hexosaminidase A & B deficiency, Cherry red spot, Hepatosplenomegaly + (Book p43)"),
    q(55,"PEDS-U081",43,"Both Tay-Sachs and Sandhoff have",["Cherry red spot in macula","No spot","No HSM both","Only Tay has HSM"],0,"Both: Cherry red spot in macula (Book p43)"),
    q(56,"PEDS-U081",43,"Tay vs Sandhoff HSM difference",["Tay No HSM, Sandhoff +HSM","Both +HSM","Both no HSM","Tay +HSM Sandhoff no"],0,"Tay No hepatosplenomegaly vs Sandhoff + (Book p43)"),
    q(57,"PEDS-U081",43,"Leukodystrophies",["Alexander disease, Canavan disease","Only Alexander","Only Canavan","Neither"],0,"Leukodystrophies: Alexander, Canavan (Book p43)"),
    q(58,"PEDS-U081",43,"Genetic syndromes megalencephaly: Sotos",["Sotos/cerebral gigantism","NF","Fragile X","Familial"],0,"Sotos syndrome/cerebral gigantism (Book p43)"),
    q(59,"PEDS-U081",43,"NF type",["NF type 1","NF type 2","NF type 3","No"],0,"NF type 1 (Book p43)"),
    q(60,"PEDS-U081",43,"Fragile X due to",["CGG trinucleotide repeats","CAG","CTG","GAA"],0,"Fragile X: D/t CGG trinucleotide repeats (Book p43)"),
    q(61,"PEDS-U081",43,"Fragile X features",["Long face, large ears, macroorchidism (Enlarged testis)","Bird face","Broad thumb","Synorphys"],0,"Long face, large ears, macroorchidism (Enlarged testis) (Book p43)"),
    q(62,"PEDS-U081",43,"Non syndromic megalencephaly",["Familial megalencephaly → m/c type & cause of megalencephaly","Rare","Not m/c","Only genetic"],0,"Familial megalencephaly → m/c type & cause of megalencephaly (Book p43)"),
    q(63,"PEDS-U081",43,"Which is m/c cause of megalencephaly",["Familial megalencephaly","Tay Sachs","Sotos","NF"],0,"Familial megalencephaly m/c (Book p43)"),
    # U082
    q(64,"PEDS-U082",43,"Craniosynostosis definition",["Abnormalities of head shape: Cranio=Skull, Synostosis=Fusion of sutures → Premature fusion","Normal fusion","No fusion","Suture + brain"],0,"Cranio Skull Synostosis Fusion → Premature fusion of the sutures (Book p43)"),
    q(65,"PEDS-U082",43,"Normal fusion metopic suture",["Fuses before 2 yrs of age","Fuses before 2nd decade","Never fuses","Fuses at puberty"],0,"Metopic suture → Fuses before 2 yrs of age (Book p43)"),
    q(66,"PEDS-U082",43,"Coronal, Sagittal, Lambdoid sutures fuse",["Fuses before 2nd decade of life","Before 2 yrs","At birth","Never"],0,"Coronal/Sagittal/Lambdoid → Fuses before 2nd decade of life (Book p43)"),
    q(67,"PEDS-U082",43,"Rule: Suture fusion →",["Skull growth arrests perpendicular to suture line, Skull growth occurs parallel to fused suture","Arrests parallel, grows perpendicular","No effect","Both perpendicular"],0,"Rule: Suture fusion → Skull growth arrests perpendicular to suture line, Skull growth occurs parallel to fused suture (Book p43)"),
    q(68,"PEDS-U082",43,"Craniosynostosis header time",["00:25:28","00:16:23","00:00:14","00:00:30"],0,"Craniosynostosis 00:25:28 (Book p43)"),
    # U083
    q(69,"PEDS-U083",44,"Dolicochephaly/scaphocephaly suture",["Sagittal suture (Premature fusion) m/c suture involved","Coronal","Metopic","Lambdoid"],0,"1. Dolicocephaly/scaphocephaly: m/c suture, Sagittal suture (Premature fusion) (Book p44)"),
    q(70,"PEDS-U083",44,"Dolicocephaly shape",["AP expansion of skull","Transverse elongation","Flat side","Anterior elongation"],0,"AP expansion of skull (Book p44)"),
    q(71,"PEDS-U083",44,"Brachycephaly suture",["B/L fusion of coronal suture","Sagittal","U/L coronal","Metopic"],0,"2. Brachycephaly: B/L fusion of coronal suture (Book p44)"),
    q(72,"PEDS-U083",44,"Brachy shape",["Transverse elongation","AP expansion","Flat side","Anterior elongation"],0,"Brachycephaly Transverse elongation (Book p44)"),
    q(73,"PEDS-U083",44,"Plagiocephaly suture",["U/L fusion of coronal suture","B/L coronal","Sagittal","Metopic"],0,"3. Plagiocephaly: U/L fusion of coronal suture (Book p44)"),
    q(74,"PEDS-U083",44,"Plagio additionally",["U/L elongation, Normal side appears flat","AP expansion","Transverse elongation","Anterior elongation"],0,"U/L elongation, Normal side appears flat (Book p44)"),
    q(75,"PEDS-U083",44,"Trigonocephaly suture",["Metopic suture, Elongation in anterior aspect","Coronal","Sagittal","Lambdoid"],0,"4. Trigonocephaly: Elongation in anterior aspect, metopic suture (Book p44)"),
    q(76,"PEDS-U083",44,"Oxycephaly/Turricephaly",["Premature fusion of multiple sutures → Irregular shape of skull","Single sagittal","B/L coronal","U/L coronal"],0,"5. Oxycephaly/Turricephaly: Premature fusion of multiple sutures → Irregular shape (Book p44)"),
    # U084
    q(77,"PEDS-U084",44,"Crouzon inheritance",["Autosomal dominant","Autosomal recessive","X-linked","Sporadic"],0,"Crouzon: Autosomal dominant (Book p44)"),
    q(78,"PEDS-U084",44,"Apert inheritance",["Autosomal dominant","Autosomal recessive","X-linked","Sporadic"],0,"Apert: Autosomal dominant (Book p44)"),
    q(79,"PEDS-U084",44,"Crouzon craniosynostosis type",["Brachycephaly","Turricephaly","Dolicocephaly","Plagiocephaly"],0,"Crouzon: Brachycephaly (Book p44)"),
    q(80,"PEDS-U084",44,"Apert craniosynostosis",["Turricephaly (Tower shaped skull)","Brachycephaly","Dolico","Plagio"],0,"Apert: Turricephaly (Tower shaped skull) (Book p44)"),
    q(81,"PEDS-U084",44,"Crouzon features",["Exophthalmos, Hypertelorism D/t shallow orbit, Maxillary hypoplasia","Syndactyly","Mitten hand","Low IQ"],0,"Crouzon Features: Exophthalmos, Hypertelorism D/t shallow orbit, Maxillary hypoplasia (Book p44)"),
    q(82,"PEDS-U084",44,"Apert features Syndactyly",["Syndactyly (Fused fingers), mitten hand deformity, Exophthalmos (Not prominent)","Only exophthalmos","Only hypertelorism","Normal IQ always"],0,"Apert: Syndactyly (Fused fingers), mitten hand deformity, Exophthalmos (Not prominent) (Book p44)"),
    q(83,"PEDS-U084",44,"IQ: Crouzon vs Apert",["Crouzon Normal IQ, Apert Low IQ","Both normal","Both low","Crouzon low Apert normal"],0,"Crouzon Normal IQ, Apert Low IQ (Book p44)"),
    q(84,"PEDS-U084",44,"Tower shaped skull image corresponds to",["Apert syndrome","Crouzon syndrome","Carpenter","Normal"],0,"Tower shaped skull (Apert) (Book p44)"),
    q(85,"PEDS-U084",44,"Syndactyly (Apert) image shows",["Fused fingers mitten hand","Normal hand","Broad thumb","Bird face"],0,"Syndactyly (Apert syndrome) mitten hand (Book p44)"),
    q(86,"PEDS-U084",44,"Carpenter syndrome inheritance",["Autosomal recessive","Autosomal dominant","X-linked","Not"],0,"Carpenter: Autosomal recessive (Book p44)"),
    q(87,"PEDS-U084",44,"Carpenter similar to",["Apert syndrome, A/w obesity & hypogonadism","Crouzon","Normal","Rett"],0,"Similar to Apert syndrome, A/w obesity & hypogonadism (Book p44)"),
    q(88,"PEDS-U084",44,"Exophthalmos arrow in Crouzon due to",["Shallow orbit","Deep orbit","Normal orbit","No"],0,"Exophthalmos D/t shallow orbit (Book p44)"),
]

RANGES = {76:(1,12),77:(13,24),78:(25,32),79:(33,46),80:(47,51),81:(52,63),82:(64,68),83:(69,76),84:(77,88)}
UNIT_RANGES = {1:(1,12),2:(13,24),3:(25,32),4:(33,46),5:(47,51),6:(52,63),7:(64,68),8:(69,76),9:(77,88)}
for u in UNITS:
    s,e = UNIT_RANGES[u["n"]]
    u["qs"] = [f"PEDS-C9-{i:03d}" for i in range(s,e+1)]

pages = [q["page"] for q in QUESTIONS]
assert pages == sorted(pages), f"Pages not sorted {pages[:10]}"
assert len(QUESTIONS)==88
assert len(UNITS)==9
for u in UNITS:
    s,e = UNIT_RANGES[u["n"]]
    assert len(u["qs"])==e-s+1
