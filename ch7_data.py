CH = 7
UNITS = [
    {"id": "PEDS-U057", "ch": 7, "n": 1, "title": "Neonatal Reflexes — Primitive Reflexes Table", "sec": "Neonatal reflexes · p30", "qs": [], "guide": "Primitive (immature) reflexes disappear after birth. Palmar grasp 28w→32w→2-3m, Rooting 28-32w→34-36w→<1m prominent (finds nipple), Moro 28-32w→37w→5-6m, ATNR 35w→1m postnatal→6-7m."},
    {"id": "PEDS-U058", "ch": 7, "n": 2, "title": "Moro Reflex — Abnormalities", "sec": "Moro reflex – Abnormalities · p30", "qs": [], "guide": "Absent in term = brain structural/functional (anencephaly, HIE). Sluggish = hypotonia (metabolic, Down, SMA). Unilateral = limb pathology: nerve (Erb’s/Klumpke) vs bone (clavicle fracture m/c)."},
    {"id": "PEDS-U059", "ch": 7, "n": 3, "title": "Postnatal Reflexes — SPL", "sec": "Postnatal reflexes · p31", "qs": [], "guide": "Appear after birth; mnemonic SPL (Special). STNR 4-6m→8-12m, Parachute 7-8m→never disappears (forward protective extension), Landau 3m→≤9m; ventral suspension, prone and tilt tests."},
    {"id": "PEDS-U060", "ch": 7, "n": 4, "title": "Birth Asphyxia and HIE — Definitions", "sec": "Birth asphyxia and HIE · p31", "qs": [], "guide": "WHO: failure to initiate/sustain breathing. NNF: APGAR 1-min moderate 4-6/10, severe 0-3/10. AAP essential: cord pH<7, APGAR 0-3 at 5-min, neurologic HIE signs, multi-organ (oliguria, ↑LFT). AKA perinatal asphyxia/depression."},
    {"id": "PEDS-U061", "ch": 7, "n": 5, "title": "Hypoxic Ischemic Encephalopathy — Sarnat Staging", "sec": "Hypoxic ischemic encephalopathy · p31", "qs": [], "guide": "HIE = leading neonatal brain injury worldwide; Birth asphyxia→Hypoxia→Ischemia. Sarnat & Sarnat staging: Stage1 99% normal (irritable, mydriasis, normal EEG), Stage2 80% recovery (lethargic, miosis, seizures), Stage3 50% death (comatose, burst-suppression)."},
    {"id": "PEDS-U062", "ch": 7, "n": 6, "title": "HIE — Complications and Investigations", "sec": "Complications · p32", "qs": [], "guide": "Term: parasagittal→spastic quadriplegia, focal necrosis→hemiplegic CP, basal ganglia→dystonic/extrapyramidal (chorea/athetosis). Preterm: PVL→spastic diplegia (lower limbs). IOC: DWI MRI. + intellectual disability."},
    {"id": "PEDS-U063", "ch": 7, "n": 7, "title": "HIE — Management and Therapeutic Hypothermia", "sec": "Management · p32", "qs": [], "guide": "Supportive: temp, vitals, glucose 75-100 mg/dL neuroprotective, phenobarbitone for seizures. Therapeutic hypothermia: 33.5-34.5°C, start ≤6h stop ≤72h, Stage2/3 >36wks; preterm <36w C/I; whole-body better than selective head; ↓metabolism→↓free radicals."},
    {"id": "PEDS-U064", "ch": 7, "n": 8, "title": "Neonatal Seizures — Types and Etiology", "sec": "Neonatal seizures · p34", "qs": [], "guide": "Types: Subtle m/c (minimal: blinking/finger rolling/lip chewing), focal clonic best prognosis, myoclonic worst. Etiology: HIE m/c (<24h onset), metabolic (hypoglycemia m/c, hypocalcemia 2nd in IDM), sepsis, bleeds, kernicterus, PVH/germinal matrix."},
    {"id": "PEDS-U065", "ch": 7, "n": 9, "title": "Neonatal Seizures — Management and Pyridoxine Trial", "sec": "Management · p34", "qs": [], "guide": "Stabilize ABC + correct reversible (hypoglycemia <45 → 2mL/kg 10% dextrose). Drugs: phenobarbitone → phenytoin/levetiracetam → midazolam infusion; pyridoxine therapeutic trial ↑GABA via GAD + pyridoxal phosphate."},
]

def q(num, sec, page, qtext, opts, ans, exp):
    assert len(opts)==4 and 0 <= ans <4
    return {"id": f"PEDS-C7-{num:03d}", "sec": sec, "page": page, "q": qtext, "opts": opts, "ans": ans, "exp": exp}

QUESTIONS = [
    # U057 p30 1-18 (18Q)
    q(1,"PEDS-U057",30,"Neonatal reflexes are AKA",["Mature reflexes","Immature/primitive reflexes","Postnatal reflexes","Conditioned reflexes"],1,"AKA immature or primitive reflex; disappear sometime after birth (Book p30)"),
    q(2,"PEDS-U057",30,"Involuntary palmar grasp image corresponds to",["Rooting reflex","Palmar grasp","Moro reflex","ATNR"],1,"Involuntary palmar grasp with hand grasping finger (Book p30)"),
    q(3,"PEDS-U057",30,"Palmar grasp onset",["28 wks of gestation","32 wks of gestation","35 wks of gestation","37 wks of gestation"],0,"Onset 28 wks of gestation (Book p30)"),
    q(4,"PEDS-U057",30,"Palmar grasp fully developed by",["30 wks gestation","32 wks gestation","34 wks gestation","37 wks gestation"],1,"Fully developed by 32 wks of gestation (Book p30)"),
    q(5,"PEDS-U057",30,"Palmar grasp duration after birth",["1-2 months","2-3 months","5-6 months","6-7 months"],1,"Duration 2-3 months (Book p30)"),
    q(6,"PEDS-U057",30,"Rooting reflex stimulus and response",["Stimulus near mouth → face turns ipsilaterally","Neck turned → I/L extension","Loud noise → abduction","Tilt forward → arm extension"],0,"Stimulus near mouth → Face turns ipsilaterally (Book p30)"),
    q(7,"PEDS-U057",30,"Rooting reflex onset",["28-32 wks gestation","28 wks gestation","35 wks gestation","37 wks gestation"],0,"Onset 28-32 wks of gestation (Book p30)"),
    q(8,"PEDS-U057",30,"Rooting reflex fully developed by",["32 wks","34-36 wks gestation","37 wks","1 month after birth"],1,"Fully developed by 34-36 wks of gestation (Book p30)"),
    q(9,"PEDS-U057",30,"Rooting reflex after birth",["Persists 5-6 months","Less prominent after 1 month","Disappears at 8-12 months","Does not disappear"],1,"Less prominent after 1 month (Book p30)"),
    q(10,"PEDS-U057",30,"Note: Rooting reflex helps baby to",["Maintain temperature","Find and latch to nipple during breastfeeding","Protect airway","Extend limbs"],1,"Rooting helps baby to find and latch to nipple during breastfeeding (Book p30)"),
    q(11,"PEDS-U057",30,"Moro reflex movement sequence",["Extension+Abduction → Flexion+adduction","Flexion+adduction → Extension+Abduction","I/L extension → C/L flexion","B/L LL flexion → extension"],0,"Extension + Abduction of hands → Flexion + adduction (Book p30)"),
    q(12,"PEDS-U057",30,"Moro reflex onset",["28 wks","28-32 wks gestation","34-36 wks","35 wks"],1,"Onset 28-32 wks of gestation (Book p30)"),
    q(13,"PEDS-U057",30,"Moro reflex fully developed by",["32 wks","34 wks","37 wks of gestation","40 wks"],2,"Fully developed by 37 wks of gestation (Book p30)"),
    q(14,"PEDS-U057",30,"Moro reflex duration",["2-3 months","5-6 months","6-7 months","8-12 months"],1,"Duration 5-6 months (Book p30)"),
    q(15,"PEDS-U057",30,"ATNR stimulus",["Neck turned to one side","Stimulus near mouth","Baby tilted forward","Baby held prone below"],0,"Neck turned to one side → I/L extension, C/L flexion (Book p30)"),
    q(16,"PEDS-U057",30,"ATNR response",["I/L extension + C/L flexion","B/L UL extension + LL flexion","Extension of arms","Flexion+adduction"],0,"I/L extension + C/L flexion (Book p30)"),
    q(17,"PEDS-U057",30,"ATNR onset",["28 wks","35 wks of gestation","37 wks","28-32 wks"],1,"Onset 35 wks of gestation (Book p30)"),
    q(18,"PEDS-U057",30,"ATNR fully developed and duration",["Fully 1 month after birth; lasts 6-7 months","Fully 32 wks; lasts 2-3 months","Fully 37 wks; lasts 5-6 months","Fully 34-36 wks; lasts <1 month"],0,"Fully developed 1 month after birth; duration 6-7 months (Book p30)"),
    # U058 p30 19-30 (12Q)
    q(19,"PEDS-U058",30,"Absent Moro in term newborn indicates",["Physiologic","Structural/functional disorders in brain","Peripheral nerve injury","Bone fracture"],1,"Absent response in term newborn D/t structural/functional disorders in brain (Book p30)"),
    q(20,"PEDS-U058",30,"Cause of absent Moro: Brain anomalies e.g.",["Anencephaly","Clavicle fracture","Erb’s palsy","Down syndrome"],0,"Brain anomalies: Eg Anencephaly (Book p31)"),
    q(21,"PEDS-U058",30,"Absent Moro due to ↓ brain function e.g.",["Hypoxic ischemic encephalopathy (HIE)","Brachial plexus injury","Metabolic disorder","Fracture"],0,"↓ brain function: Eg Hypoxic ischemic encephalopathy (HIE) (Book p31)"),
    q(22,"PEDS-U058",30,"Sluggish Moro response is due to",["Hypotonia","Hypertonia","Fracture","Nerve injury"],0,"Sluggish response D/t hypotonia (Book p31)"),
    q(23,"PEDS-U058",30,"Sluggish Moro e.g. hypotonia seen in",["Metabolic disorders, Down syndrome, Spinomuscular atrophy","Anencephaly, HIE","Erb’s palsy","Clavicle fracture"],0,"Eg: metabolic disorders, Down syndrome, Spinomuscular atrophy etc. (Book p31)"),
    q(24,"PEDS-U058",30,"Unilateral Moro response indicates",["Brain disorder","Hypotonia","Pathology in limbs","Normal variant"],2,"Unilateral response D/t pathology in limbs (Book p31)"),
    q(25,"PEDS-U058",30,"Unilateral Moro: Nerve injury e.g.",["Brachial plexus injury (Erb’s palsy, Klumpke’s paralysis)","Clavicle fracture","Anencephaly","HIE"],0,"Nerve injury Eg: Brachial plexus injury (Erb’s palsy, Klumpke’s paralysis) (Book p31)"),
    q(26,"PEDS-U058",30,"Unilateral Moro: Bone injury e.g. (m/c)",["Clavicle fracture (D/t fracture/dislocation)","Femur fracture","Skull fracture","Rib fracture"],0,"Bone injury D/t fracture/dislocation (m/c: Clavicle fracture) (Book p31)"),
    q(27,"PEDS-U058",30,"Sluggish vs absent vs unilateral Moro triad is classified under",["Abnormal Moro reflex","Postnatal reflexes","Neonatal seizures","HIE staging"],0,"Abnormal Moro reflex flowchart (Book p31)"),
    q(28,"PEDS-U058",30,"Clavicle fracture as cause of unilateral Moro is",["Bone injury","Nerve injury","Brain anomaly","Metabolic"],0,"Bone injury side (Book p31)"),
    q(29,"PEDS-U058",30,"Erb’s palsy is due to",["Brachial plexus injury","Clavicle fracture","HIE","Metabolic disorder"],0,"Brachial plexus injury (Erb’s/Klumpke’s) (Book p31)"),
    q(30,"PEDS-U058",30,"Moro abnormalities flowchart heading",["Abnormal Moro reflex","Normal Moro","ATNR","STNR"],0,"Abnormal Moro reflex (Book p31)"),
    # U059 p31 31-48 (18Q)
    q(31,"PEDS-U059",31,"Postnatal reflexes appear",["Before birth","After birth","At 28 wks gestation","At 35 wks"],1,"Appear after birth (Book p31)"),
    q(32,"PEDS-U059",31,"Mnemonic for postnatal reflexes",["SPL (Special)","MRS","ABC","KMC"],0,"Mnemonic: SPL (Special) (Book p31)"),
    q(33,"PEDS-U059",31,"Symmetric tonic neck reflex: baby held from below in prone, extension of neck →",["B/L UL extension + LL flexion","B/L UL flexion + LL extension","I/L extension C/L flexion","Extension of arms"],0,"Extension of neck → B/L UL extension + LL flexion (Book p31)"),
    q(34,"PEDS-U059",31,"STNR: flexion of neck →",["B/L UL flexion + LL extension","B/L UL extension + LL flexion","B/L LL flexion","Extension of arms"],0,"Flexion of neck → B/L UL flexion + LL extension (Book p31)"),
    q(35,"PEDS-U059",31,"STNR appearance",["4-6 months","7-8 months","3 months","At birth"],0,"Appearance 4-6 months (Book p31)"),
    q(36,"PEDS-U059",31,"STNR disappearance",["8-12 months","Does not disappear","≤9 months","6-7 months"],0,"Disappearance 8-12 months (Book p31)"),
    q(37,"PEDS-U059",31,"Parachute reflex elicited by",["Baby tilted forward (mimic falling)","Baby held prone below","Ventral suspension","Neck turned"],0,"Baby tilted forward (mimic falling) (Book p31)"),
    q(38,"PEDS-U059",31,"Parachute reflex response",["Extension of arms","Flexion of LL","I/L extension","Abduction of hands"],0,"Extension of arms (Book p31)"),
    q(39,"PEDS-U059",31,"Parachute reflex also called",["Forward Parachute Reflex / Protective Extension Reaction Forward","Moro","Landau","ATNR"],0,"Forward Parachute Reflex (Protective Extension Reaction Forward) (Book p31)"),
    q(40,"PEDS-U059",31,"Parachute appearance",["7-8 months","4-6 months","3 months","5-6 months"],0,"Appearance 7-8 months (Book p31)"),
    q(41,"PEDS-U059",31,"Parachute disappearance",["8-12 months","Does not disappear","≤9 months","6-7 months"],1,"Does not disappear (Book p31)"),
    q(42,"PEDS-U059",31,"Landau reflex: baby held in ventral suspension in prone, flexion of neck →",["B/L LL flexion","B/L LL extension","B/L UL extension","Extension of arms"],0,"Flexion of neck → B/L LL flexion (Book p31)"),
    q(43,"PEDS-U059",31,"Landau: extension of neck →",["B/L LL extension","B/L LL flexion","B/L UL flexion","I/L extension"],0,"Extension of neck → B/L LL extension (Book p31)"),
    q(44,"PEDS-U059",31,"Landau appearance",["3 months","4-6 months","7-8 months","1 month"],0,"Appearance 3 months (Book p31)"),
    q(45,"PEDS-U059",31,"Landau disappearance",["≤9 months","8-12 months","Does not disappear","6-7 months"],0,"Disappearance ≤9 months (Book p31)"),
    q(46,"PEDS-U059",31,"Landau vs STNR difference is",["Landau: LL; STNR: UL+LL with neck flex/extend in prone from below","Same","Landau tilts forward","STNR ventral suspension"],0,"Landau ventral suspension LL; STNR from below UL+LL (Book p31)"),
    q(47,"PEDS-U059",31,"Postnatal reflex table header Duration title",["Disappearance (Age)","Onset","Fully developed by","Duration after birth"],0,"Columns: Reflex, method to elicit, Appearance (Age), Disappearance (Age) (Book p31)"),
    q(48,"PEDS-U059",31,"SPL mnemonic stands for",["Special (mnemonic for postnatal)","Spinal","Supine","Symmetric"],0,"Mnemonic: SPL (Special) (Book p31)"),
    # U060 p31 49-64 (16Q)
    q(49,"PEDS-U060",31,"Birth asphyxia and HIE AKA",["Perinatal asphyxia/perinatal depression","Neonatal sepsis","RDS","TTN"],0,"AKA perinatal asphyxia/perinatal depression (Book p31)"),
    q(50,"PEDS-U060",31,"Impaired gas exchange in birth asphyxia leads to",["Hypoxia + Complications → Brain HIE, multiorgan dysfunction, lactic acidosis (↑ anaerobic metabolism)","Hyperoxia","Hypoglycemia alone","Hyperthermia"],0,"Impaired gas exchange → Hypoxia + Complications → Brain: HIE, multiorgan dysfunction, Lactic acidosis (↑ anaerobic) (Book p31)"),
    q(51,"PEDS-U060",31,"Brain manifestation of impaired gas exchange",["HIE","Sepsis","Jaundice","Anemia"],0,"Brain: HIE (Book p31)"),
    q(52,"PEDS-U060",31,"WHO definition of birth asphyxia",["Failure to initiate and sustain breathing after birth","APGAR 0-3 at 5 min","Cord pH <7","Seizures"],0,"WHO definition: Failure to initiate and sustain breathing after birth (Book p32)"),
    q(53,"PEDS-U060",31,"NNF criteria for birth asphyxia is based on",["APGAR score 1 minute after birth","Cord pH","EEG","Birth weight"],0,"Based on APGAR score 1 minute after birth (Book p32)"),
    q(54,"PEDS-U060",31,"NNF moderate asphyxia APGAR",["4 to 6/10","0 to 3/10","7-10/10","<7"],0,"Moderate: 4 to 6/10 (Book p32)"),
    q(55,"PEDS-U060",31,"NNF severe asphyxia APGAR",["0 to 3/10","4 to 6/10","7-10",">7"],0,"Severe: 0 to 3/10 (Book p32)"),
    q(56,"PEDS-U060",32,"Essential criteria (AAP) most important includes",["Profound metabolic/mixed acidosis Umbilical cord pH <7","APGAR 7-10","Normal cord pH","No organ involvement"],0,"AAP essential: Profound metabolic or mixed acidosis: Umbilical cord pH <7 (Book p32)"),
    q(57,"PEDS-U060",32,"AAP: Persistence of low APGAR",["0-3 at 5 min","4-6 at 1 min","7-10 at 5 min","0-3 at 1 min"],0,"Persistence of low APGAR score: 0-3 at 5 min (Book p32)"),
    q(58,"PEDS-U060",32,"AAP: Signs of neonatal neurologic dysfunction",["Features of HIE","Normal reflexes","Mydriasis alone","No seizures"],0,"Signs of neonatal neurologic dysfunction: Features of HIE (Book p32)"),
    q(59,"PEDS-U060",32,"AAP: Evidence of multiple organ involvement e.g.",["Kidney (Oliguria), liver (↑ liver enzymes)","Only brain","Only lung","Skin"],0,"Eg: Kidney (Oliguria), liver (↑ liver enzymes) (Book p32)"),
    q(60,"PEDS-U060",32,"AAP essential criteria number of items",["4 items a-d","2 items","3 items","5 items"],0,"a-d = 4 items (Book p32)"),
    q(61,"PEDS-U060",32,"Who definition vs NNF vs AAP: which is most important",["AAP essential criteria","WHO definition","NNF criteria","All equal"],0,"Essential criteria: American association of pediatrics (AAP) criteria: most important (Book p32)"),
    q(62,"PEDS-U060",32,"HIE full form",["Hypoxic ischemic encephalopathy","Hyperbilirubinemia induced","Hypertrophic","Hepatic"],0,"Hypoxic ischemic encephalopathy (Book p32)"),
    q(63,"PEDS-U060",32,"Birth asphyxia → ? → Ischemia pathogenesis",["Hypoxia","Hyperoxia","Hypoglycemia","Hypocalcemia"],0,"Birth asphyxia → Hypoxia → Ischemia (Book p32)"),
    q(64,"PEDS-U060",32,"Sarnat and Sarnat staging indicates",["Clinical features and prognosis of HIE","Etiology of seizures","Metabolic disorders","Growth chart"],0,"Indicates clinical features and prognosis of HIE (Book p32)"),
    # U061 p32 Sarnat 65-82 (18Q)
    q(65,"PEDS-U061",32,"HIE leading cause of",["Neonatal brain injury worldwide","Neonatal jaundice","Sepsis","RDS"],0,"Leading cause of neonatal brain injury worldwide (Book p32)"),
    q(66,"PEDS-U061",32,"Sarnat Stage I Consciousness",["Normal/slightly irritable","Lethargic","Comatose","Stupor"],0,"Stage1: Normal/slightly irritable (Book p32)"),
    q(67,"PEDS-U061",32,"Sarnat Stage II Consciousness",["Lethargic","Normal","Comatose","Irritable"],0,"Stage2: Lethargic (Book p32)"),
    q(68,"PEDS-U061",32,"Sarnat Stage III Consciousness",["Comatose","Lethargic","Normal","Irritable"],0,"Stage3: Comatose (Book p32)"),
    q(69,"PEDS-U061",32,"Sarnat Tone Stage1 vs 2 vs 3",["Normal → Hypotonia → Flaccidity","Flaccidity → Hypotonia → Normal","Normal all","Hypotonia all"],0,"Tone: Normal – Hypotonia – Flaccidity (Book p32)"),
    q(70,"PEDS-U061",32,"Sarnat neonatal reflexes",["Easily elicitable → Sluggish → Absent reflexes","Absent → Sluggish → Normal","Normal all","Absent all"],0,"Neonatal reflexes: Easily elicitable → Sluggish → Absent reflexes (Book p32)"),
    q(71,"PEDS-U061",32,"Sarnat Pupil Stage1",["Mydriasis (D/t sympathetic overactivity)","Miosis (parasympathetic)","Poor/no reaction","Normal"],0,"Stage1: Mydriasis (D/t sympathetic overactivity) (Book p32)"),
    q(72,"PEDS-U061",32,"Sarnat Pupil Stage2",["Miosis (D/t parasympathetic overactivity)","Mydriasis","Poor reaction","Normal"],0,"Stage2: Miosis (D/t parasympathetic overactivity) (Book p32)"),
    q(73,"PEDS-U061",32,"Sarnat Pupil Stage3",["Poor/no reaction to light","Mydriasis","Miosis","Easily reactive"],0,"Stage3: Poor/no reaction to light (Book p32)"),
    q(74,"PEDS-U061",32,"Sarnat Convulsions",["Absent → Largely present → Absent","Present all","Absent all","Present → Absent → Present"],0,"Convulsions: Absent → Largely present → Absent (Book p32)"),
    q(75,"PEDS-U061",32,"Sarnat EEG Stage1",["Normal","Seizure spikes: Low voltage complexes","Burst suppression","Abnormal"],0,"EEG Stage1: Normal (Book p32)"),
    q(76,"PEDS-U061",32,"Sarnat EEG Stage2",["Seizure spikes: Low voltage complexes","Normal","Burst suppression","Triphasic"],0,"Stage2: Seizure spikes: Low voltage complexes (Book p32)"),
    q(77,"PEDS-U061",32,"Sarnat EEG Stage3",["Burst suppression pattern (Burst/Suppression)","Normal","Low voltage","Seizure spikes"],0,"Stage3: Burst suppression pattern (Book p32)"),
    q(78,"PEDS-U061",32,"Sarnat Outcome Stage1",["99%: Normal outcome Good outcome","80%: Complete recovery 20%: complications","50%: Death 50%: Complications","100% death"],0,"Stage1: 99%: Normal outcome Good outcome (Book p32)"),
    q(79,"PEDS-U061",32,"Sarnat Outcome Stage2",["80%: Complete recovery 20%: complications","99% normal","50% death","100% normal"],0,"Stage2: 80%: Complete recovery 20%: complications (Book p32)"),
    q(80,"PEDS-U061",32,"Sarnat Outcome Stage3",["50%: Death 50%: Complications","99% normal","80% recovery","10% death"],0,"Stage3: 50%: Death 50%: Complications (Book p32)"),
    q(81,"PEDS-U061",32,"Which stage has seizures largely present",["Stage 2","Stage 1","Stage 3","None"],0,"Largely present in Stage2 (Book p32)"),
    q(82,"PEDS-U061",32,"Which stages have absent convulsions",["Stage1 and Stage3","Stage2","All","None"],0,"Absent in Stage1 and Stage3 (Book p32)"),
    # U062 p32 complications 83-92 (10Q)
    q(83,"PEDS-U062",32,"Complications: Term babies a. Parasagittal infarction B/L →",["Spastic quadriplegia","Spastic diplegia","Hemiplegic CP","Dystonic CP"],0,"Parasagittal infarction: B/L → Spastic quadriplegia (Book p33)"),
    q(84,"PEDS-U062",32,"Focal ischemic necrosis →",["Hemiplegic cerebral palsy (Stroke-like condition)","Diplegia","Quadriplegia","Athetosis"],0,"Focal ischemic necrosis: Hemiplegic cerebral palsy (Stroke-like condition) (Book p33)"),
    q(85,"PEDS-U062",32,"Selective neuronal necrosis (Eg: Basal ganglia) →",["Dystonic/extrapyramidal cerebral palsy","Spastic quadriplegia","Hemiplegic","Diplegia"],0,"Selective neuronal necrosis (Eg: Basal ganglia) → Dystonic/extrapyramidal cerebral palsy (Book p33)"),
    q(86,"PEDS-U062",32,"Extrapyramidal manifestations",["Chorea, athetosis","Spasticity","Quadriplegia","Diplegia"],0,"Extrapyramidal manifestations: Chorea, athetosis (Book p33)"),
    q(87,"PEDS-U062",32,"Pre-term babies: Periventricular leukomalacia B/L AKA",["Zone of periventricular ischemia hemorrhages AKA leukomalacia Intraventricular bleed in lateral ventricle","Parasagittal infarction","Basal ganglia necrosis","Subarachnoid bleed"],0,"Zone of periventricular ischemia hemorrhages AKA leukomalacia Intraventricular bleed in lateral ventricle (Book p33)"),
    q(88,"PEDS-U062",32,"PVL → thinning/infarction of periventricular matter → affects",["Motor cortex of lower limbs","Upper limbs","Face","Trunk"],0,"Affects motor cortex of lower limbs (Book p33)"),
    q(89,"PEDS-U062",33,"PVL result",["Spastic diplegia","Spastic quadriplegia","Hemiplegic","Dystonic"],0,"Spastic diplegia (Book p33)"),
    q(90,"PEDS-U062",33,"Other HIE complication",["Intellectual disability and cognitive dysfunction","Jaundice","Anemia","Rash"],0,"Intellectual disability and cognitive dysfunction (Book p33)"),
    q(91,"PEDS-U062",33,"Investigations: Diffusion weighted imaging (DWI) MRI",["IOC (Investigation of choice)","Not useful","Second line","Only for infection"],0,"Investigations: Diffusion weighted imaging (DWI) MRI: IOC (Book p33)"),
    q(92,"PEDS-U062",33,"Parasagittal injury diagram shows motor homunculus with parasagittal cerebral injury arrow to",["Spastic quadriplegia","Spastic diplegia","Hemiplegia","Ataxia"],0,"Spreads to parasagittal cerebral injury → Spastic quadriplegia (Book p33)"),
    # U063 p32-33 management 93-105 (13Q)
    q(93,"PEDS-U063",33,"HIE supportive management maintain: Normal temperature, Stable vitals, Blood glucose",["Between 75-100mg/dL (Neuroprotective range)","<45",">150","20-30"],0,"Blood glucose level between 75-100mg/dL (Neuroprotective range) (Book p33)"),
    q(94,"PEDS-U063",33,"Treat seizures initial drug in HIE management",["Phenobarbitone","Phenytoin","Midazolam","Levetiracetam"],0,"Initial drug: Phenobarbitone (Book p33)"),
    q(95,"PEDS-U063",33,"Therapeutic (Induced) hypothermia gaining popularity as",["An established treatment modality d/t improved outcome","Experimental only","Not recommended","Harmful"],0,"Gaining popularity as an established treatment modality d/t improved outcome (Book p33)"),
    q(96,"PEDS-U063",33,"Induced hypothermia mechanism",["↓ metabolism (esp. brain) → ↓ free radicals generation → Prevents further brain damage","↑ metabolism","↑ free radicals","Increases damage"],0,"Induced hypothermia → ↓ metabolism → ↓ free radicals → Prevents further brain damage (Book p33)"),
    q(97,"PEDS-U063",33,"Therapeutic hypothermia method: Cooling crystals used →",["Selective head cooling and Whole body cooling (better method)","Only head","Only body","No cooling"],0,"Method: Cooling crystals used → Selective head cooling; Whole body cooling (better method) (Book p33)"),
    q(98,"PEDS-U063",33,"Better method of cooling",["Whole body cooling","Selective head cooling","No cooling","Ice bath"],0,"Whole body cooling (better method) (Book p33)"),
    q(99,"PEDS-U063",33,"Temperature range for therapeutic hypothermia",["33.5°C to 34.5°C","30-32°C","36-37°C","35-36°C"],0,"Temperature range: 33.5°C to 34.5°C (Book p33)"),
    q(100,"PEDS-U063",33,"Start therapeutic hypothermia",["Within 6 hours after birth","After 24 hours","After 72 hours","At 1 week"],0,"Start: within 6 hours after birth (Book p34)"),
    q(101,"PEDS-U063",33,"Termination of hypothermia",["≤72 hours after birth","≤24 hours","≤48 hours","≤96 hours"],0,"Termination: ≤72 hours after birth (Book p34)"),
    q(102,"PEDS-U063",33,"Indication for therapeutic hypothermia",["Stage 2/ Stage 3 HIE who are >36 weeks","Stage 1 HIE","Preterm <36 wks","All HIE"],0,"Indication: Stage 2/ Stage 3 HIE who are >36 weeks (Book p34)"),
    q(103,"PEDS-U063",33,"Contraindication for therapeutic hypothermia",["Preterm <36 wks (↑ morbidity)","Term >36 wks","Stage 2 HIE","Stage 3 HIE"],0,"C/I: Preterm <36 wks (↑ morbidity) (Book p34)"),
    q(104,"PEDS-U063",33,"Free radicals generation is primarily in",["Brain (esp. brain)","Liver","Kidney","Heart"],0,"Esp. brain (Book p33)"),
    q(105,"PEDS-U063",33,"HIE management includes supportive plus",["Therapeutic hypothermia","Antibiotics","Phototherapy","Exchange transfusion"],0,"Therapeutic (Induced) hypothermia (Book p33)"),
    # U064 p34 types etiology 106-120 (15Q)
    q(106,"PEDS-U064",34,"Neonatal seizures Types — Subtle (m/c) manifestations",["Minimal manifestations e.g. Blinking, rolling of fingers, chewing movement of lip","Generalized tonic-clonic","Only myoclonic","Only tonic"],0,"Subtle (m/c) minimal manifestations Eg: Blinking, rolling of fingers, chewing movement of lip (Book p34)"),
    q(107,"PEDS-U064",34,"Focal clonic neonatal seizure prognosis",["Best prognosis","Worst prognosis","Intermediate","No prognosis"],0,"Focal clonic • Best prognosis (Book p34)"),
    q(108,"PEDS-U064",34,"Worst prognosis neonatal seizure type",["Myoclonic","Subtle","Focal clonic","Tonic"],0,"Myoclonic • Worst prognosis (Book p34)"),
    q(109,"PEDS-U064",34,"Neonatal seizures types include",["Subtle, Focal clonic, Tonic, myoclonic","Only tonic and myoclonic","Only subtle","Grand mal"],0,"Subtle (m/c), Focal clonic, Tonic, myoclonic (Book p34)"),
    q(110,"PEDS-U064",34,"Etiology m/c HIE onset of seizure",["<24h","48h","72h","1 week"],0,"HIE (m/c) Onset <24h (Book p34)"),
    q(111,"PEDS-U064",34,"Metabolic conditions causing neonatal seizures listed: Hypermagnesemia, Hyponatremia, Hypernatremia (rare),",["Hypoglycemia (m/c) and Hypocalcemia (2nd m/c) in infants of diabetic mother","Only hypoglycemia","Only hypermagnesemia","Only hypocalcemia"],0,"Hypoglycemia (m/c) and Hypocalcemia (2nd m/c) In infants of diabetic mother (Book p34)"),
    q(112,"PEDS-U064",34,"In infants of diabetic mother most common metabolic seizure cause",["Hypoglycemia (m/c)","Hypermagnesemia","Hypernatremia","Hyponatremia"],0,"Hypoglycemia (m/c) In infants of diabetic mother (Book p34)"),
    q(113,"PEDS-U064",34,"Second most common metabolic in IDM",["Hypocalcemia (2nd m/c)","Hypernatremia","Hypermagnesemia","Hypoglycemia"],0,"Hypocalcemia (2nd m/c) (Book p34)"),
    q(114,"PEDS-U064",34,"Hypernatremia in neonatal seizures is",["Rare","Common","m/c","2nd m/c"],0,"Hypernatremia (rare) (Book p34)"),
    q(115,"PEDS-U064",34,"Infections causing neonatal seizures e.g.",["Neonatal sepsis, meningitis","Pneumonia only","UTI only","Otitis media"],0,"Infections: Eg: Neonatal sepsis, meningitis (Book p34)"),
    q(116,"PEDS-U064",34,"Intracranial bleeds e.g.",["Subarachnoid hemorrhage, Intraventricular hemorrhage (d/t germinal matrix bleed)","Subdural only","Epidural only","No bleeds"],0,"Intracranial bleeds: Eg: Subarachnoid hemorrhage, Intraventricular hemorrhage (d/t germinal matrix bleed) (Book p34)"),
    q(117,"PEDS-U064",34,"Germinal matrix bleed leads to",["Intraventricular hemorrhage","Subarachnoid","Epidural","Normal"],0,"Intraventricular hemorrhage (d/t germinal matrix bleed) (Book p34)"),
    q(118,"PEDS-U064",34,"Bilirubin encephalopathy / Kernicterus is",["Etiology of neonatal seizures","Treatment","Investigation","Not related"],0,"Bilirubin encephalopathy / Kernicterus (Book p34)"),
    q(119,"PEDS-U064",34,"Overall m/c etiology of neonatal seizures",["HIE (m/c)","Metabolic","Infections","Trauma"],0,"HIE (m/c) (Book p34)"),
    q(120,"PEDS-U064",34,"Metabolic m/c overall in neonatal seizures",["Hypoglycemia","Hypernatremia","Hypermagnesemia","Hyponatremia"],0,"Hypoglycemia (m/c) (in metabolic box) (Book p34)"),
    # U065 p34 management 121-135 (15Q)
    q(121,"PEDS-U065",34,"Management first step: Stabilize the baby",["Vitals & Airway, Breathing, Circulation: ABC","Only breathing","Only circulation","Only temperature"],0,"Stabilize the baby (Vitals & Airway, Breathing, Circulation: ABC) (Book p34)"),
    q(122,"PEDS-U065",34,"Next step after ABC",["Identify and correct reversible causes","Start anti-epileptic directly","Do EEG","Do MRI"],0,"Identify and correct reversible causes (Book p34)"),
    q(123,"PEDS-U065",34,"Eg reversible: Hypoglycemia (<45 mg/dL) →",["IV 2mL/kg of 10% dextrose followed by infusion","Oral feeds only","No treatment","Only observation"],0,"Eg: Hypoglycemia (<45 mg/dL) → IV 2mL/kg of 10% dextrose followed by infusion (Book p34)"),
    q(124,"PEDS-U065",34,"If seizures continue first anti-epileptic",["IV Phenobarbitone","IV Phenytoin","Oral valproate","IV midazolam"],0,"If seizures continue Anti-epileptic medication: IV Phenobarbitone (Book p34)"),
    q(125,"PEDS-U065",34,"If no response to phenobarbitone next",["IV Phenytoin or Levetiracetam","IV midazolam","Oral pyridoxine","No drug"],0,"If no response IV Phenytoin or Levetiracetam (Book p34)"),
    q(126,"PEDS-U065",34,"If refractory next",["IV infusion midazolam","Oral phenytoin","IM pyridoxine","Only ABC"],0,"If refractory IV infusion midazolam (Book p34)"),
    q(127,"PEDS-U065",34,"IM Pyridoxine therapeutic trial effect",["↑GABA levels","↓GABA","↑ glutamate","No effect"],0,"IM Pyridoxine (Therapeutic trial): ↑GABA levels (Book p34)"),
    q(128,"PEDS-U065",34,"Pyridoxine is involved in",["Glutamate metabolism","Glucose metabolism","Fatty acid","Protein"],0,"Pyridoxine is involved in glutamate metabolism (Book p34)"),
    q(129,"PEDS-U065",34,"Enzyme + co-factor: Glutamate acid decarboxylase +",["Pyridoxal phosphate (co-factor)","Thiamine","NAD","FAD"],0,"Glutamate acid decarboxylase + Pyridoxal phosphate (co-factor) (Book p34)"),
    q(130,"PEDS-U065",34,"Glutamate → (?) inhibitory neurotransmitter",["GABA","Glutamate","Dopamine","Serotonin"],0,"Glutamate → ↑ GABA (Inhibitory neurotransmitter) (Book p34)"),
    q(131,"PEDS-U065",34,"GABA full form role",["Inhibitory neurotransmitter","Excitatory","No role","Enzyme"],0,"GABA (Inhibitory neurotransmitter) (Book p34)"),
    q(132,"PEDS-U065",34,"Correct order of anti-epileptic escalation",["Phenobarbitone → Phenytoin/Levetiracetam → Midazolam infusion","Midazolam → Phenytoin → Phenobarbitone","Levetiracetam → Phenobarbitone → Midazolam","Pyridoxine → Phenobarbitone → Phenytoin"],0,"IV Phenobarbitone → IV Phenytoin or Levetiracetam → IV infusion midazolam (Book p34)"),
    q(133,"PEDS-U065",34,"Pyridoxine route in trial",["IM Pyridoxine","IV Pyridoxine","Oral","Subcutaneous"],0,"IM Pyridoxine (Therapeutic trial) (Book p34)"),
    q(134,"PEDS-U065",34,"Reversible cause must be corrected before",["Anti-epileptic medication if seizures continue","Direct midazolam","No correction needed","Only glucose"],0,"Identify and correct reversible causes → If seizures continue → Anti-epileptic (Book p34)"),
    q(135,"PEDS-U065",34,"Seizure spikes low voltage vs burst suppression correspond to",["Stage2 vs Stage3 EEG","Stage1 vs Stage2","Normal vs abnormal","Stage1 vs Stage3"],0,"Stage2 low voltage seizure spikes; Stage3 burst suppression (Book p32)"),
]

# Assign qs to UNITS and set RANGES
RANGES = {57: (1,18), 58: (19,30), 59: (31,48), 60: (49,64), 61: (65,82), 62: (83,92), 63: (93,105), 64: (106,120), 65: (121,135)}
# Build mapping ch7 n -> range
UNIT_RANGES = {1:(1,18),2:(19,30),3:(31,48),4:(49,64),5:(65,82),6:(83,92),7:(93,105),8:(106,120),9:(121,135)}
for u in UNITS:
    s,e = UNIT_RANGES[u["n"]]
    u["qs"] = [f"PEDS-C7-{i:03d}" for i in range(s,e+1)]

# Validate strict page order within file (non-decreasing)
pages = [q["page"] for q in QUESTIONS]
assert pages == sorted(pages), f"Pages not sorted: {pages[:20]}"
assert len(QUESTIONS)==135
assert len(UNITS)==9
# Check counts
for u in UNITS:
    s,e = UNIT_RANGES[u["n"]]
    assert len(u["qs"])==e-s+1
