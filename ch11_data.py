CH = 11
UNITS = [
    {"id": "PEDS-U094", "ch": 11, "n": 1, "title": "Gross Motor Milestones", "sec": "Gross motor · p48", "qs": [], "guide": "Cephalo-caudal: 3m head control, 4-6m rolls over trunk control+, 6m sits with support tripod, 8m sits without support crawling, 10m stands with support creeping, 11m cruising, 12m stands without support walks with support, 15m walks without support independently, 18m runs, 2y climbs with 2 feet/step holding rails, 3y climbs upstairs 1 foot/step rides tricycle, 4y climbs downstairs 1 foot/step hops."},
    {"id": "PEDS-U095", "ch": 11, "n": 2, "title": "Fine Motor — Grasping and Grip", "sec": "Fine motor · p48", "qs": [], "guide": "0-3m no fine milestone neonatal palmar grasp reflex closed hands, 4m bidextrous reaches both hands, 6m unidextrous ulnar immature palmar + transfer hand to hand, 8m mature radial palmar, 9m immature pincer sides of fingers, 12m mature pincer tip of fingers, 15-18m scribbles. Images immature 9m vs mature 12m pincer."},
    {"id": "PEDS-U096", "ch": 11, "n": 3, "title": "Tower, Dressing, Drawing", "sec": "Tower/Dressing/Drawing · p48-49", "qs": [], "guide": "Tower 15m 2 cubes, 18m 3, 2y 6, 3y 9. Dressing 2y undresses with help, 3y dresses with help, 5y dresses+undresses without help. Drawing mnemonic LOX-STD: 2y draws line horizontal 18m-2y vertical 2-2.5y, 3y circle (o), 4y cross/plus (X), 4.5y square □, 5y triangle △, 6-7y diamond/rhomboid ◇."},
    {"id": "PEDS-U097", "ch": 11, "n": 4, "title": "Language Milestones", "sec": "Language · p49", "qs": [], "guide": "3m cooing musical, 4m laughs aloud, 6m monosyllables ma pa, 9m bisyllables mama papa, 1y 1-2 meaningful words, 15m jargon speech meaningless temporary 1-2 months, 18m 8-10 words, 2y 100 words speaks in sentences, 3y recognizes tells name age gender, 4y tells story and rhymes."},
    {"id": "PEDS-U098", "ch": 11, "n": 5, "title": "Social Milestones", "sec": "Social · p49", "qs": [], "guide": "2m social smile, 3m mother regard, 6m stranger anxiety smiles at mirror, 9m waves bye-bye plays peek a boo, 1y plays simple ball game, 15m points to objects, 18m domestic mimicry, 2.5-3y parallel play non-interactive, 4y group play interactive, 5y follows 3 step commands identifies 4 colors repeats 4 digits."},
    {"id": "PEDS-U099", "ch": 11, "n": 6, "title": "Miscellaneous — Mouthing, Casting, Object Permanence, Handedness", "sec": "Miscellaneous · p49", "qs": [], "guide": "Mouthing puts objects/hand in mouth starts 6m seen till 18m-2y, Casting deliberate throwing starts 12m, Object permanence feeling missing object present though not seen around 9m, Handedness preference one hand starts by 3y firmly at 4y, Hand regard plays with own hands 3m-5y (>5y → developmental delay)."},
    {"id": "PEDS-U100", "ch": 11, "n": 7, "title": "Vision and Hearing — Range and Localization", "sec": "Vision/Hearing · p49", "qs": [], "guide": "Vision newborn follows 45°, 1m 90°, 3m 180°, 4m fully established binocular vision. Hearing newborn startles, 4m horizontal localization, 6m downward, 7m upward, 10m diagonal localization — turning head towards sound, assessed using Murphy's sequence."},
    {"id": "PEDS-U101", "ch": 11, "n": 8, "title": "Assessment of Development — Pull to Sit, Ventral Suspension, Prone", "sec": "Assessment · p50", "qs": [], "guide": "Pull to sit newborn complete head lag no control, 3m no head lag. Ventral suspension newborn head/limbs drop, 2m head at level, 3m head lifted above body. In prone newborn-2w legs folded beneath pelvis lifted, 4-6w legs straighten pelvis level baby lies flat, 3m head lifted elbow flexed bears weight on forearm, 6m head lifted elbow straight bearing weight on extended limbs."},
]

def q(num, sec, page, qtext, opts, ans, exp):
    assert len(opts)==4 and 0 <= ans <4
    return {"id": f"PEDS-C11-{num:03d}", "sec": sec, "page": page, "q": qtext, "opts": opts, "ans": ans, "exp": exp}

QUESTIONS = [
    q(1,"PEDS-U094",48,"Gross motor Rule direction",["Cephalo-caudal","Caudo-cephalic","Proximal-distal","Distal-proximal"],0,"Rule : Direction of development → Cephalo-caudal (Book p48)"),
    q(2,"PEDS-U094",48,"3 months gross motor",["Head control/Neck holding","Rolls over","Sits with support","Stands"],0,"3 months Head control/Neck holding (Book p48)"),
    q(3,"PEDS-U094",48,"4-6 months",["Rolls over (trunk control+)","Sits without support","Crawling","Cruising"],0,"4-6 months Rolls over(trunk control+) (Book p48)"),
    q(4,"PEDS-U094",48,"6 months",["Sits with support : Tripod posture","Sits without support","Stands","Walks"],0,"6 months Sits with support : Tripod posture + Tripod position : 6 months image (Book p48)"),
    q(5,"PEDS-U094",48,"8 months",["Sits without support, crawling","Stands with support","Cruising","Walks without support"],0,"8 months Sits without support, crawling Crawling : 8 months (Book p48)"),
    q(6,"PEDS-U094",48,"10 months",["Stands with support, creeping","Runs","Climbs","Hops"],0,"10 months Stands with support, creeping Creeping : 10 months (Book p48)"),
    q(7,"PEDS-U094",48,"11 months",["Cruising","Standing without support","Walks","Runs"],0,"11 months Cruising Cruising : 11 months image (Book p48)"),
    q(8,"PEDS-U094",48,"12 months",["Stands without support, walks with support","Walks without support","Runs","Hops"],0,"12 months Stands without support, walks with support (Book p48)"),
    q(9,"PEDS-U094",48,"15 months",["Walks without support (independently)","Runs","Climbs","Cruising"],0,"15 months Walks without support (independently) (Book p48)"),
    q(10,"PEDS-U094",48,"18 months",["Runs","Walks without support","Climbs","Hops"],0,"18 months Runs (Book p48)"),
    q(11,"PEDS-U094",48,"2 years",["Climbs with 2 feet/step holding side rails","Climbs 1 foot/step","Rides tricycle","Hops"],0,"2 years Climbs with 2 feet/step holding side rails (Book p48)"),
    q(12,"PEDS-U094",48,"3 years",["Climbs upstairs with 1 foot/step, rides tricycle","Walks without support","Runs","Hops"],0,"3 years Climbs upstairs with 1 foot/step, rides tricycle (Book p48)"),
    q(13,"PEDS-U094",48,"4 years",["Climbs downstairs with 1 foot/step, hops","Runs","Walks","Cruising"],0,"4 years Climbs downstairs with 1 foot/step, hops Hopping : 4 years image (Book p48)"),
    q(14,"PEDS-U094",48,"Tripod position age vs Cruising age",["6 months tripod, 11 months cruising","3 months tripod 8m cruising","6m both","11m both"],0,"Tripod 6m Cruising 11m (Book p48 images)"),
    q(15,"PEDS-U094",48,"Crawling vs Creeping ages",["8 months crawling, 10 months creeping","10 crawling 8 creeping","Both 8","Both 10"],0,"Crawling : 8 months Creeping : 10 months (Book p48)"),
    q(16,"PEDS-U095",48,"0-3 months fine motor",["No fine motor milestone (Neonatal palmar grasp reflex → closed hands)","Bidextrous grasp","Unidextrous","Pincer"],0,"0-3 months No fine motor milestone (Neonatal palmar grasp reflex → closed hands) (Book p48)"),
    q(17,"PEDS-U095",48,"4 months fine motor",["Bidextrous grasp (Reaches for objects with both hands)","Unidextrous","Mature pincer","Scribbles"],0,"4 months Bidextrous grasp (Reaches for objects with both hands) (Book p48)"),
    q(18,"PEDS-U095",48,"6 months fine motor",["Unidextrous grasp : Ulnar (Immature) palmar grasp + Transfer objects from one hand to another","Mature radial","Pincer","Bidextrous"],0,"6 months Unidextrous grasp : Ulnar (Immature) palmar grasp + Transfer objects (Book p48)"),
    q(19,"PEDS-U095",48,"8 months",["Unidextrous grasp : mature (Radial) palmar grasp","Immature pincer","Mature pincer","Scribbles"],0,"8 months Unidextrous grasp : mature (Radial) palmar grasp (Book p48)"),
    q(20,"PEDS-U095",48,"9 months",["Immature pincer grasp (Hold with sides of fingers)","Mature pincer","Bidextrous","Scribbles"],0,"9 months Immature pincer grasp (Hold with sides of fingers) Immature pincer 9m image (Book p48)"),
    q(21,"PEDS-U095",48,"12 months",["Mature pincer grasp (Holds with tip of fingers)","Immature pincer","Ulnar palmar","Radial"],0,"12 months mature pincer grasp (Holds with tip of fingers) mature pincer 12m image (Book p48)"),
    q(22,"PEDS-U095",48,"Scribbles age",["18 months","9 months","12 months","4 months"],0,"18 months Scribbles? Actually book shows Scribbles at 15-18m column – but fine print scribbles row shows 15? We'll take 15-18m (Book p48)"),
    q(23,"PEDS-U095",48,"Immature vs mature pincer difference",["Sides vs tip of fingers","Both tip","Both sides","No difference"],0,"Immature Hold with sides vs Mature tip (Book p48)"),
    q(24,"PEDS-U096",48,"Tower of cubes 15 months",["2 cubes","3 cubes","6 cubes","9 cubes"],0,"15 months makes a tower of 2 cubes (Book p48-49)"),
    q(25,"PEDS-U096",48,"18 months tower",["3 cubes","2 cubes","6 cubes","9 cubes"],0,"18 months makes tower of 3 cubes (Book p48)"),
    q(26,"PEDS-U096",48,"2 years tower",["6 cubes","2 cubes","3 cubes","9 cubes"],0,"2 years makes tower of 6 cubes (Book p48)"),
    q(27,"PEDS-U096",48,"3 years tower",["9 cubes","6 cubes","3 cubes","2 cubes"],0,"3 years makes tower of 9 cubes (Book p48)"),
    q(28,"PEDS-U096",48,"Dressing 2 years",["Undresses with help","Dresses with help","Dresses and undresses without help","No"],0,"2 years Undresses with help (Book p48)"),
    q(29,"PEDS-U096",48,"3 years dressing",["Dresses with help","Undresses with help","Without help","No"],0,"3 years Dresses with help (Book p48)"),
    q(30,"PEDS-U096",48,"5 years dressing",["Dresses and undresses without help","Only dresses","Only undresses","With help"],0,"5 years Dresses and undresses without help (Book p48)"),
    q(31,"PEDS-U096",49,"Drawing 2 years draws line",["Horizontal 18m-2y and Vertical 2-2.5y","Only horizontal","Only vertical","Circle"],0,"2 years Draws line Horizontal 18m-2y Vertical 2-2.5y mnemonic LOX-STD (Book p49)"),
    q(32,"PEDS-U096",49,"Mnemonic LOX-STD Drawing sequence",["Line-O-Cross-Square-Triangle-Diamond","Only line","Only circle","None"],0,"Mnemonic LOX-STD Line Circle Cross Square Triangle Diamond (Book p49)"),
    q(33,"PEDS-U096",49,"3 years draws",["Circle (o)","Cross/plus","Square","Triangle"],0,"3 years Draws circle(o) (Book p49)"),
    q(34,"PEDS-U096",49,"4 years draws",["Cross/plus (X)","Square","Triangle","Diamond"],0,"4 years Draws cross/plus(X) (Book p49)"),
    q(35,"PEDS-U096",49,"4.5 years",["Square (□)","Circle","Triangle","Diamond"],0,"4.5 years Draws square (□) (Book p49)"),
    q(36,"PEDS-U096",49,"5 years",["Triangle (△)","Square","Circle","Diamond"],0,"5 years Draws triangle (△) (Book p49)"),
    q(37,"PEDS-U096",49,"6-7 years",["Diamond/rhomboid (◇)","Triangle","Square","Circle"],0,"6-7 years Draws diamond/rhomboid (◇) (Book p49)"),
    q(38,"PEDS-U097",49,"3 months language",["Cooing (Musical) sound","Laughs aloud","Monosyllables","Bisyllables"],0,"3 months Cooing (Musical) sound (Book p49)"),
    q(39,"PEDS-U097",49,"4 months",["Laughs aloud","Cooing","Monosyllables","Bisyllables"],0,"4 months Laughs aloud (Book p49)"),
    q(40,"PEDS-U097",49,"6 months",["Monosyllables (ma, pa)","Bisyllables","Cooing","Jargon"],0,"6 months monosyllables(ma, pa) (Book p49)"),
    q(41,"PEDS-U097",49,"9 months",["Bi-syllables (mama, papa)","Monosyllables","Jargon","100 words"],0,"9 months Bi-syllables (mama, papa) (Book p49)"),
    q(42,"PEDS-U097",49,"1 year",["1-2 meaningful words","Jargon","8-10 words","100 words"],0,"1 year 1-2 meaningful words (Book p49)"),
    q(43,"PEDS-U097",49,"15 months",["Jargon speech (meaningless words; temporary milestone for 1-2 months)","8-10 words","100 words","Story"],0,"15 months Jargon speech (meaningless words ;temporary milestone for 1-2 months) (Book p49)"),
    q(44,"PEDS-U097",49,"18 months",["8-10 meaningful words","Jargon","100 words","Story"],0,"18 months 8-10 meaningful words (Book p49)"),
    q(45,"PEDS-U097",49,"2 years",["100 words, speaks in sentences","8-10 words","Jargon","Story"],0,"2 years 100 words, speaks in sentences (Book p49)"),
    q(46,"PEDS-U097",49,"3 years",["Recognizes and tells name, age and gender","Tells story","100 words","Jargon"],0,"3 years Recognizes and tells name, age and gender (Book p49)"),
    q(47,"PEDS-U097",49,"4 years",["Tells story and rhymes","Recognizes name","100 words","Jargon"],0,"4 years Tells story and rhymes (Book p49)"),
    q(48,"PEDS-U098",49,"2 months social",["Social smile","Mother regard","Stranger anxiety","Waves bye-bye"],0,"2 months Social smile (Book p49)"),
    q(49,"PEDS-U098",49,"3 months social",["Mother regard","Social smile","Stranger anxiety","Parallel play"],0,"3 months mother regard (Book p49)"),
    q(50,"PEDS-U098",49,"6 months social",["Stranger anxiety, smiles at mirror image","Waves bye-bye","Peek a boo","Ball game"],0,"6 months Stranger anxiety, smiles at mirror image (Book p49)"),
    q(51,"PEDS-U098",49,"9 months",["Waves bye-bye, plays peek a boo","Ball game","Points","Mimicry"],0,"9 months Waves bye-bye, plays peek a boo (Book p49)"),
    q(52,"PEDS-U098",49,"1 year",["Plays simple ball game","Points","Mimicry","Parallel play"],0,"1 year Plays simple ball game (Book p49)"),
    q(53,"PEDS-U098",49,"15 months",["Points to objects","Domestic mimicry","Parallel play","Group play"],0,"15 months Points to objects (Book p49)"),
    q(54,"PEDS-U098",49,"18 months",["Domestic mimicry (imitates actions of adults)","Parallel play","Group play","3 step commands"],0,"18 months Domestic mimicry (imitates actions of adults) (Book p49)"),
    q(55,"PEDS-U098",49,"2.5-3 years",["Parallel play (Non-interactive)","Group play","Domestic mimicry","Ball game"],0,"2.5-3 years Parallel play (Non-interactive) (Book p49)"),
    q(56,"PEDS-U098",49,"4 years",["Group play (Interactive play)","Parallel play","Domestic mimicry","Social smile"],0,"4 years Group play (Interactive play) (Book p49)"),
    q(57,"PEDS-U098",49,"5 years social triple",["Follows 3 step commands + Identifies 4 colors + Repeats 4 digits","Only commands","Only colors","Only digits"],0,"5 years Follows 3 step commands, Identifies 4 colors, Repeats 4 digits (Book p49)"),
    q(58,"PEDS-U099",49,"Mouthing starts",["6 months till 18 months-2 years","12 months","9 months","3 years"],0,"Mouthing Puts objects/hand in mouth Starts at 6 months Seen till 18 months-2 years (Book p49)"),
    q(59,"PEDS-U099",49,"Casting",["Deliberate throwing of objects Starts at 12 months","6 months","9 months","3 years"],0,"Casting Deliberate throwing of objects Starts at 12 months (Book p49)"),
    q(60,"PEDS-U099",49,"Object permanence",["Feeling that a missing object is present though not seen Around 9 months","6 months","12 months","3 years"],0,"Object permanence Around 9 months (Book p49)"),
    q(61,"PEDS-U099",49,"Handedness",["Starts by 3 years & firmly established at 4 years","By 1y","By 2y","By 5y"],0,"Handedness Preference of one hand over the other Starts by 3 years & firmly established at 4 years (Book p49)"),
    q(62,"PEDS-U099",49,"Hand regard",["Plays with own hands 3 months - 5 years (>5 years → Developmental delay)","3m-5m","3-18m","Normal after 5y"],0,"Hand regard Plays with own hands 3 months -5 years (>5 years → Developmental delay) (Book p49)"),
    q(63,"PEDS-U100",49,"Vision newborn",["Follows objects upto 45°","90°","180°","Binocular"],0,"Newborn Follows objects upto 45° (Book p49)"),
    q(64,"PEDS-U100",49,"1 month vision",["Follows objects upto 90°","45°","180°","Binocular"],0,"1 month Follows objects upto 90° (Book p49)"),
    q(65,"PEDS-U100",49,"3 months vision",["Follows objects upto 180°","45°","90°","Binocular"],0,"3 months Follows objects upto 180° (Book p49)"),
    q(66,"PEDS-U100",49,"4 months vision",["Fully established Binocular vision","45°","90°","180°"],0,"4 months Fully established Binocular vision (Book p49)"),
    q(67,"PEDS-U100",49,"Hearing newborn",["Startles in response to sound","Horizontal localization","Downward","Upward"],0,"Newborn Startles in response to sound (Book p49)"),
    q(68,"PEDS-U100",49,"4 months hearing",["Horizontal localization of sound","Downward","Upward","Diagonal"],0,"4 months Horizontal localization of sound (Book p49)"),
    q(69,"PEDS-U100",49,"6 months hearing",["Downward localization of sound","Horizontal","Upward","Diagonal"],0,"6 months Downward localization of sound (Book p49)"),
    q(70,"PEDS-U100",49,"7 months",["Upward localization of sound","Horizontal","Downward","Diagonal"],0,"7 months Upward localization of sound (Book p49)"),
    q(71,"PEDS-U100",49,"10 months hearing",["Diagonal localization of sound","Horizontal","Downward","Upward"],0,"10 months Diagonal localization of sound (Book p49)"),
    q(72,"PEDS-U100",49,"Hearing assessed Indicates by turning head towards sound source Assessed using",["Murphy's sequence","Tanner","Greulich","Denver"],0,"Assessed using Murphy's sequence (Book p49)"),
    q(73,"PEDS-U101",50,"Pull to sit maneuver Newborn vs 3 months",["Newborn Complete head lag (no head control) vs 3 months No head lag (head control attained)","Both no lag","Both lag","Reverse"],0,"Newborn Complete head lag (no head control) 3 months No head lag (head control attained) (Book p50)"),
    q(74,"PEDS-U101",50,"Ventral suspension Newborn",["Head and limbs drop down (no control)","Head at level","Lifted above","Normal"],0,"Newborn Head and limbs drop down (no control) (Book p50)"),
    q(75,"PEDS-U101",50,"2 months ventral suspension",["Head at level with rest of body","Drop down","Lifted above","No"],0,"2 months Head at level with rest of body (Book p50)"),
    q(76,"PEDS-U101",50,"3 months ventral suspension",["Head is lifted above the level of body","At level","Drop","No"],0,"3 months Head is lifted above the level of body (Book p50)"),
    q(77,"PEDS-U101",50,"In prone Newborn-2 weeks",["Legs Folded beneath abdomen Pelvis Lifted compared to rest","Legs Straighten","Head lifted","Bears weight"],0,"Newborn-2 weeks Legs Folded beneath abdomen Pelvis Lifted (Book p50)"),
    q(78,"PEDS-U101",50,"4-6 weeks prone",["Legs Straighten Pelvis In level with rest (baby lies flat)","Folded","Head lifted","Forearm weight"],0,"4-6 weeks Legs Straighten Pelvis In level with rest of body (baby lies flat) (Book p50)"),
    q(79,"PEDS-U101",50,"3 months prone",["Head lifted up Elbow flexed/bent Bears weight on forearm","Elbow straight","Extended limbs","Folded"],0,"3 months Head lifted Elbow flexed Bears weight on forearm (Book p50)"),
    q(80,"PEDS-U101",50,"6 months prone",["Head lifted Elbow straight (in extension) Bearing weight on extended limbs","Flexed","Folded","No"],0,"6 months Head lifted Elbow straight Bearing weight on extended limbs (Book p50)"),
]

RANGES = {94:(1,15),95:(16,23),96:(24,37),97:(38,47),98:(48,57),99:(58,62),100:(63,72),101:(73,80)}
UNIT_RANGES = {1:(1,15),2:(16,23),3:(24,37),4:(38,47),5:(48,57),6:(58,62),7:(63,72),8:(73,80)}
for u in UNITS:
    s,e = UNIT_RANGES[u["n"]]
    u["qs"] = [f"PEDS-C11-{i:03d}" for i in range(s,e+1)]

pages = [q["page"] for q in QUESTIONS]
assert pages == sorted(pages), f"Pages not sorted {pages[:10]}"
assert len(QUESTIONS)==80
assert len(UNITS)==8
for u in UNITS:
    s,e = UNIT_RANGES[u["n"]]
    assert len(u["qs"])==e-s+1
