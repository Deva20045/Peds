CH = 13
UNITS = [
    {"id": "PEDS-U107", "ch": 13, "n": 1, "title": "Breath Holding Spells", "sec": "Breath holding · p53-54", "qs": [], "guide": "Reflex Begins 6m Peaks 2y Persists 5y Sequence anger/pain→cry→holds breath full expiration Types cyanotic m/c ↑sympathetic→cyanosis few sec if persistent tonic clonic vs pallid ↑parasympathetic→pale syncope if persistent ECG r/o long QT Management reassure benign, turn sideways during tonic clonic, avoid picking up ↓cerebral perfusion, treat iron deficiency, atropine long pallid."},
    {"id": "PEDS-U108", "ch": 13, "n": 2, "title": "Bruxism", "sec": "Bruxism · p54", "qs": [], "guide": "Teeth grinding >5y (<5 normal) During sleep Daytime associated anxiety Long term dental malocclusion jaw pain Treatment <5 no treatment >5 behavioural therapy."},
    {"id": "PEDS-U109", "ch": 13, "n": 3, "title": "Pica", "sec": "Pica · p54", "qs": [], "guide": "Inedible/non nutritive chalk/mud/paint For ≥1 month Inappropriate for development/cultural Age <5y Risk malnutrition iron deficiency anemia low SES psychosocial stress developmental delay cerebral palsy Complications lead poisoning (paint) parasitic (mud) Management behavioural deworming albendazole stat low dose iron 0.5-1 mg/kg/day."},
    {"id": "PEDS-U110", "ch": 13, "n": 4, "title": "Thumb Sucking", "sec": "Thumb sucking · p54", "qs": [], "guide": "Self soothing Begins after 6m Peak 18-21m Normal till 4y Management <4y reassurance >4y indicates emotional stress/social insecurity behavioural modifications positive reinforcement praise Avoid negative reinforcement oil on thumb."},
    {"id": "PEDS-U111", "ch": 13, "n": 5, "title": "Temper Tantrums", "sec": "Temper tantrums · p55", "qs": [], "guide": "Attention seeking Begins 18-36m Persists till 6y Physical/emotional crying/kicking/pushing/head banging Management reassure parents remain calm, leave alone safe place, distraction, time out."},
    {"id": "PEDS-U112", "ch": 13, "n": 6, "title": "Tics and Tourette", "sec": "Tics · p55-56", "qs": [], "guide": "Abrupt fast involuntary paroxysmal non rhythmic repetitive motor/verbal Begins 4-6y Peak10-12y Persists18-20y Types motor simple eye blinking neck jerking shoulder shrugging vs complex echopraxia; vocal simple throat clearing coughing sniffing vs complex echolalia other's speech palilalia own words. Tourette onset <18 motor+vocal ≥1y Management behavioural, long lasting neuroleptics haloperidol clonidine."},
    {"id": "PEDS-U113", "ch": 13, "n": 7, "title": "Nocturnal Enuresis — Definition and Types", "sec": "Nocturnal Enuresis · p56", "qs": [], "guide": "Nearly complete evacuation bladder at >5y (bladder maturation) wrong place&time ≥2/month for ≥3 months Incidence M>F Types etiology Primary m/c present since birth functional delayed maturation ↓ADH night vs Secondary previously dry ≥6m organic UTI DI/DM Stress bowel bladder dysfunction. Symptomatology monosymptomatic m/c night only vs polysymptomatic +LUTS hesitancy urgency dribbling m/c variety Primary monosymptomatic."},
    {"id": "PEDS-U114", "ch": 13, "n": 8, "title": "Nocturnal Enuresis — Management", "sec": "Enuresis management · p56", "qs": [], "guide": "Motivational+Alarm highest success 60-70% Non pharm reassurance behavioural void before bed restrict fluids evening avoid caffeine motivational verbal praising gifts if dry alarm conditioning sensors in underwear vs timed. Pharm short term desmopressin long term oxybutynin/tolterodine ↓uninhibited contractions Imipramine not used cardiovascular side effects."},
]

def q(num, sec, page, qtext, opts, ans, exp):
    assert len(opts)==4 and 0 <= ans <4
    return {"id": f"PEDS-C13-{num:03d}", "sec": sec, "page": page, "q": qtext, "opts": opts, "ans": ans, "exp": exp}

QUESTIONS = [
    q(1,"PEDS-U107",53,"Breath holding spells is",["Reflex event","Voluntary","Seizure","Normal"],0,"Reflex event (Book p53 00:00:30)"),
    q(2,"PEDS-U107",53,"Age begins by",["6 months","2 years","5 years","18 months"],0,"Begins by 6 months (Book p53)"),
    q(3,"PEDS-U107",53,"Peaks by",["2 years","6 months","5 years","10 years"],0,"Peaks by 2 years (Book p53)"),
    q(4,"PEDS-U107",53,"Persists till",["5 years","2 years","6 months","10 years"],0,"Persists till 5 years (Book p53)"),
    q(5,"PEDS-U107",53,"Sequence",["Provocative factors (Anger, pain) → Baby cries → Holds breath in full expiration","Holds breath then cries","No cry","Only pain"],0,"Sequence Provocative factors (Anger, pain) → Baby cries → Holds breath in full expiration (Book p53)"),
    q(6,"PEDS-U107",53,"Cyanotic type D/t",["↑sympathetic activity (m/c)","↑parasympathetic","Sympathetic low","No"],0,"Cyanotic breath holding spells : D/t ↑sympathetic activity (m/c) (Book p53)"),
    q(7,"PEDS-U107",53,"Cyanotic presents",["Cyanosis (Becomes normal after few seconds)","Pale","Syncope","No"],0,"Cyanosis (Becomes normal after few seconds) (Book p53)"),
    q(8,"PEDS-U107",53,"If persistent cyanotic",["May develop tonic clonic movement","No","Pale","Syncope"],0,"If persistent → may develop tonic clonic movement (Book p53)"),
    q(9,"PEDS-U107",53,"Pallid type D/t",["↑ parasympathetic activity","↑sympathetic","No","M/c"],0,"Pallid type : D/t ↑ parasympathetic activity (Book p53)"),
    q(10,"PEDS-U107",53,"Pallid presents",["Pale and develops a syncope like attack (Few seconds)","Cyanosis","Normal","No"],0,"Pale and develops a syncope like attack (Few seconds) (Book p53)"),
    q(11,"PEDS-U107",53,"If persistent pallid",["ECG done → to r/o long QT syndrome","No","Cyanosis","Normal"],0,"If persistent : ECG done → to r/o long QT syndrome (Book p53)"),
    q(12,"PEDS-U107",53,"Management reassure",["Benign condition with spontaneous resolution","Serious","No","Chronic"],0,"Reassure parents (Benign condition with spontaneous resolution) (Book p53)"),
    q(13,"PEDS-U107",53,"During tonic clonic episode",["Turn the child sideways (prevents aspiration)","Pick up","Supine","No"],0,"During tonic clonic episode : Turn the child sideways (prevents aspiration) (Book p53)"),
    q(14,"PEDS-U107",53,"Avoid picking the child up during event",["Causes sudden ↓cerebral perfusion","Prevents aspiration","Helps","No"],0,"Avoid picking the child up during event (causes sudden ↓cerebral perfusion) (Book p53)"),
    q(15,"PEDS-U107",53,"Evaluate and treat for",["Iron deficiency anaemia","Calcium","Normal","No"],0,"Evaluate and treat for Iron deficiency anaemia (Book p53)"),
    q(16,"PEDS-U107",53,"Atropine for",["Long duration pallid spells","Cyanotic only","All","No"],0,"Atropine : For long duration pallid spells (Book p53)"),
    q(17,"PEDS-U108",54,"Bruxism",["Teeth grinding","Breath holding","Pica","Thumb"],0,"Bruxism Teeth grinding (Book p54)"),
    q(18,"PEDS-U108",54,"Age onset",[">5 years (<5 yrs : normal)","<5 yrs pathological",">10","<1y"],0,"Age : >5 years (<5 yrs : normal) (Book p54)"),
    q(19,"PEDS-U108",54,"Occurs",["During sleep, Daytime bruxism Associated with anxiety disorders","Only day","Only night without anxiety","No"],0,"Occurs during sleep Daytime bruxism : Associated with anxiety disorders (Book p54)"),
    q(20,"PEDS-U108",54,"Long term problems",["Dental malocclusion, Jaw pain","No","Only jaw","Only dental"],0,"Long term problems : Dental malocclusion, Jaw pain (Book p54)"),
    q(21,"PEDS-U108",54,"Treatment <5 years",["No treatment required","Behavioural therapy","Drugs","No"],0,"Treatment <5 years → No treatment required (Book p54)"),
    q(22,"PEDS-U108",54,"Treatment >5 years",["Behavioural therapy","No treatment","Drugs","Surgery"],0,">5 years → Behavioural therapy (Book p54)"),
    q(23,"PEDS-U109",54,"Pica definition",["Consumption of inedible/non nutritive substances (chalk, mud, paint)","Teeth grinding","Thumb sucking","Breath holding"],0,"Consumption of inedible/non nutritive substances (chalk, mud, paint) (Book p54)"),
    q(24,"PEDS-U109",54,"For at least",["1 month","1 week","1 year","5 years"],0,"For atleast 1 month (Book p54)"),
    q(25,"PEDS-U109",54,"Inappropriate for",["Development or cultural practices","Only development","Only cultural","Normal"],0,"Inappropriate for development or cultural practices (Book p54)"),
    q(26,"PEDS-U109",54,"Age",["<5 years",">5 years","Adolescent","Adult"],0,"Age : <5 years (Book p54)"),
    q(27,"PEDS-U109",54,"Risk factors",["Malnutrition, Iron deficiency anemia, Low socioeconomic status, Psychosocial stress, Developmental delay (cerebral palsy)","Only malnutrition","Only iron","Only stress"],0,"Risk factors: malnutrition, Iron deficiency anemia, Low socioeconomic status, Psychosocial stress, Developmental delay (cerebral palsy) (Book p54)"),
    q(28,"PEDS-U109",54,"Complications Lead poisoning",["From paint","From mud","From thumb","No"],0,"Lead poisoning (From paint) (Book p54)"),
    q(29,"PEDS-U109",54,"Parasitic infestations",["From mud","From paint","From thumb","No"],0,"Parasitic infestations (From mud) (Book p54)"),
    q(30,"PEDS-U109",54,"Management of Pica",["Behavioural therapy, Deworming (Albendazole Stat), Low dose iron 0.5 to 1 mg/kg/day","Only behavioural","Only deworming","Only iron"],0,"Management: Behavioural therapy, Deworming (Albendazole Stat), Low dose iron supplements (0.5 to 1 mg/kg/day) (Book p54)"),
    q(31,"PEDS-U109",54,"Low dose iron for Pica",["0.5 to 1 mg/kg/day","5 mg","10 mg","No"],0,"Low dose iron supplements (0.5 to 1 mg/kg/day) (Book p54)"),
    q(32,"PEDS-U110",54,"Thumb sucking",["Self soothing behaviour for a child","Attention seeking","Reflex event","Pica"],0,"Thumb sucking Self soothing behaviour for a child (Book p54 00:14:05)"),
    q(33,"PEDS-U110",54,"Begins after",["6 months","18 months","4 years","Birth"],0,"Begins after 6 months (Book p54)"),
    q(34,"PEDS-U110",54,"Peak",["18 to 21 months","6 months","4 years","5 years"],0,"Peak : 18 to 21 months (Book p54)"),
    q(35,"PEDS-U110",54,"Normal till",["4 years","5 years","2 years","6 months"],0,"Normal till 4 years (Book p54)"),
    q(36,"PEDS-U110",54,"Management <4 years",["Reassurance","Behavioural modifications","Negative reinforcement","Oil"],0,"Management <4 years : Reassurance (Book p54)"),
    q(37,"PEDS-U110",54,">4 years indicates",["Emotional stress/ social insecurity","Normal","No","Reassurance only"],0,">4 years (Indicates emotional stress/ social insecurity) (Book p54)"),
    q(38,"PEDS-U110",54,">4 years Management",["Behavioural modifications (Positive reinforcement like praise)","Negative reinforcement","Oil","No"],0,"Behavioural modifications (Positive reinforcement like praise) (Book p54)"),
    q(39,"PEDS-U110",54,"Avoid",["Negative reinforcement (like applying oil on thumb)","Positive reinforcement","Reassurance","All"],0,"Note : Avoid negative reinforcement (like applying oil on thumb) (Book p54)"),
    q(40,"PEDS-U111",55,"Temper tantrums",["Attention seeking behavior","Self soothing","Reflex","Pica"],0,"Temper tantrums Attention seeking behavior (Book p55)"),
    q(41,"PEDS-U111",55,"Begins at",["18-36 months","6 months","4-6 years","5 years"],0,"Begins at 18-36 months (Book p55)"),
    q(42,"PEDS-U111",55,"Persists till",["6 years","5 years","4 years","10 years"],0,"Persists till 6 years (Book p55)"),
    q(43,"PEDS-U111",55,"Presentation Physical/emotional challenges →",["Crying/kicking/pushing/head banging","Only crying","Only head banging","Only pushing"],0,"Physical/emotional challenges → Crying/kicking/pushing/head banging (Book p55)"),
    q(44,"PEDS-U111",55,"Management Reassure & advice parents",["Remain calm during episode","Punish","Pick up","No"],0,"Reassure & advice parents to remain calm during episode (Book p55)"),
    q(45,"PEDS-U111",55,"Child to be left alone",["In a place where unlikely to get harmed","Anywhere","In danger","No"],0,"Child to be left alone in a place where unlikely to get harmed (Book p55)"),
    q(46,"PEDS-U111",55,"Distraction",["Taking the child away from that place","Time out","Reassure","No"],0,"Distraction (Taking the child away from that place) (Book p55)"),
    q(47,"PEDS-U111",55,"Time out technique",["Leaving the child alone for sometime to settle down","Punish","Negative reinforcement","No"],0,"Time out technique (Leaving the child alone for sometime to settle down) (Book p55)"),
    q(48,"PEDS-U112",55,"Tics definition",["Abrupt onset of fast, involuntary, paroxysmal, non rhythmic, repetitive motor/verbal manifestations","Slow voluntary","Normal","Breath holding"],0,"Abrupt onset of fast, involuntary, paroxysmal, non rhythmic, repetitive motor/verbal manifestations (Book p55)"),
    q(49,"PEDS-U112",55,"Begins by",["4-6 years","18-36 months","6 months","5 years"],0,"Begins by 4-6 years (Book p55)"),
    q(50,"PEDS-U112",55,"Peak",["10 to 12 years","4-6 years","18-20","6 months"],0,"Peak : 10 to 12 years (Book p55)"),
    q(51,"PEDS-U112",55,"Persists till",["18 to 20 years","12 years","6 years","5 years"],0,"Persists till 18 to 20 years (Book p55)"),
    q(52,"PEDS-U112",55,"Simple motor tics",["Eye blinking, Neck jerking, Shoulder shrugging","Echopraxia","Echolalia","Palilalia"],0,"Simple motor Eye blinking Neck jerking Shoulder shrugging (Book p55)"),
    q(53,"PEDS-U112",55,"Complex motor",["Echopraxia (repeating movements/postures or imitating others)","Eye blinking","Throat clearing","Echolalia"],0,"Complex motor Echopraxia (repeating movements/postures or imitating others) (Book p55)"),
    q(54,"PEDS-U112",55,"Simple vocal",["Repeated Throat clearing Coughing Sniffing","Echolalia","Palilalia","Echopraxia"],0,"Simple vocal Repeated Throat clearing Coughing Sniffing (Book p55)"),
    q(55,"PEDS-U112",55,"Complex vocal Echolalia",["Repeating other's speech","Repeating one's own words/sentences","Throat clearing","Eye blinking"],0,"Complex vocal Echolalia (repeating other's speech) (Book p55)"),
    q(56,"PEDS-U112",55,"Palilalia",["Repeating one's own words/sentences","Other's speech","Throat clearing","Echopraxia"],0,"Palilalia (repeating one's own words/sentences) (Book p55)"),
    q(57,"PEDS-U112",55,"Tourette's syndrome Age of onset",["<18 years","<5 years",">18","<6 months"],0,"Tourette's syndrome Age of onset <18 years (Book p55)"),
    q(58,"PEDS-U112",55,"Tourette requires",["Motor and vocal tics for ≥1 year","Only motor","Only vocal","<1 year"],0,"Motor and vocal tics for ≥1 year (Book p55)"),
    q(59,"PEDS-U112",55,"Management Behavioural therapy",["Yes for all tics","Only Tourette","No","Only motor"],0,"Management Behavioural therapy (Book p55)"),
    q(60,"PEDS-U112",55,"Long lasting tics Neuroleptics",["Haloperidol, Clonidine","Only haloperidol","Only clonidine","Imipramine"],0,"Long lasting tics : Neuroleptics (Haloperidol, Clonidine) (Book p55)"),
    q(61,"PEDS-U113",56,"Nocturnal Enuresis Definition Nearly complete evacuation bladder at",[">5 yrs (age of bladder maturation) At wrong place & time for ≥2 times a month for ≥3 months","<5 yrs","≥1/month","≥6 months"],0,"Definition: Nearly complete evacuation of bladder at >5 yrs (age of bladder maturation): At wrong place & time for ≥2 times a month for ≥3 months (Book p56 00:24:57)"),
    q(62,"PEDS-U113",56,"Incidence",["Males > Females","Females > Males","Equal","No"],0,"Incidence : Males > Females (Book p56)"),
    q(63,"PEDS-U113",56,"Primary (m/c)",["Present since birth","Previously dry ≥6 months","Secondary","No"],0,"Primary (m/c) Present since birth (Book p56)"),
    q(64,"PEDS-U113",56,"Primary Etiology Functional",["Delayed bladder maturation, Decreased ADH secretion at night","UTI","DI/DM","Stress"],0,"Etiology (Functional disorder): Delayed bladder maturation, Decreased ADH secretion at night (Book p56)"),
    q(65,"PEDS-U113",56,"Secondary",["Previously dry at night for at least preceding 6 months","Present since birth","Primary","No"],0,"Secondary Previously dry at night for at least preceding 6 months (Book p56)"),
    q(66,"PEDS-U113",56,"Secondary Etiology Organic",["UTI, DI/DM, Stress, Bowel bladder dysfunction","Only UTI","Only DI","Only stress"],0,"Etiology (Organic): UTI, DI/DM, Stress, Bowel bladder dysfunction (Book p56)"),
    q(67,"PEDS-U113",56,"Monosymptomatic (m/c)",["Passing urine at night time only","Plus LUTS","Both","No"],0,"Monosymptomatic (m/c): Passing urine at night time (Book p56)"),
    q(68,"PEDS-U113",56,"Polysymptomatic",["Passing urine at night + Lower urinary tract symptoms/LUTS (Hesitancy, urgency & dribbling)","Only night","No LUTS","Primary"],0,"Polysymptomatic: Passing urine at night time + Lower urinary tract symptoms/LUTS (Hesitancy, urgency & dribbling) (Book p56)"),
    q(69,"PEDS-U113",56,"m/c variety",["Primary monosymptomatic nocturnal enuresis","Secondary","Polysymptomatic","No"],0,"m/c variety: Primary monosymptomatic nocturnal enuresis (Book p56)"),
    q(70,"PEDS-U114",56,"Management motivational + Alarm therapy Highest success rate",["60-70%","30%","100%","10%"],0,"Motivational + Alarm therapy: Highest success rate (60-70%) (Book p56)"),
    q(71,"PEDS-U114",56,"Non pharmacological Reassurance",["Yes","No","Only pharm","No"],0,"Reassurance (Book p56)"),
    q(72,"PEDS-U114",56,"Behavioural modifications",["Voiding before going to bed, Restrict fluids in evening, Avoid caffeine drinks (tea, coffee and soda)","Only voiding","Only fluids","Only caffeine"],0,"Behavioural modifications: Voiding before going to bed, Restrict fluids in evening, Avoid caffeine drinks (Book p56)"),
    q(73,"PEDS-U114",56,"Motivational therapy",["Verbal praising, gifts : if dry at night","Punishment","Oil","No"],0,"Motivational therapy: Verbal praising, gifts : if dry at night (Book p56)"),
    q(74,"PEDS-U114",56,"Alarm therapy",["Conditioning a child to sensation of full bladder","Drug","Reassurance","No"],0,"Alarm therapy: Conditioning a child to sensation of full bladder (Book p56)"),
    q(75,"PEDS-U114",56,"Sensors put in underwear →",["Detects wetness & awakens child","No","Only timed","No"],0,"Sensors put in underwear → Detects wetness & awakens child (Book p56)"),
    q(76,"PEDS-U114",56,"Simple alarms",["Set to the time of usual bed wetting","Sensors","No","Only pharm"],0,"Simple alarms set to the time of usual bed wetting (Book p56)"),
    q(77,"PEDS-U114",56,"Short term Pharmacological",["Oral desmopressin","Oxybutynin","Imipramine","Clonidine"],0,"Short term: Oral desmopressin (Book p56)"),
    q(78,"PEDS-U114",56,"Long term usage",["Oxybutynin/Tolterodine (↓ uninhibited bladder contractions)","Desmopressin","Imipramine","Haloperidol"],0,"Long term usage: Oxybutynin/Tolterodine (↓ uninhibited bladder contractions) (Book p56)"),
    q(79,"PEDS-U114",56,"Imipramine",["Not used d/t adverse cardiovascular side effects","Used first line","Used short term","No"],0,"Imipramine not used d/t adverse cardiovascular side effects (Book p56)"),
]

RANGES = {107:(1,16),108:(17,22),109:(23,31),110:(32,39),111:(40,47),112:(48,60),113:(61,69),114:(70,79)}
UNIT_RANGES = {1:(1,16),2:(17,22),3:(23,31),4:(32,39),5:(40,47),6:(48,60),7:(61,69),8:(70,79)}
for u in UNITS:
    s,e = UNIT_RANGES[u["n"]]
    u["qs"] = [f"PEDS-C13-{i:03d}" for i in range(s,e+1)]

pages = [q["page"] for q in QUESTIONS]
assert pages == sorted(pages), f"Pages not sorted {pages[:10]}"
assert len(QUESTIONS)==79
assert len(UNITS)==8
for u in UNITS:
    s,e = UNIT_RANGES[u["n"]]
    assert len(u["qs"])==e-s+1
