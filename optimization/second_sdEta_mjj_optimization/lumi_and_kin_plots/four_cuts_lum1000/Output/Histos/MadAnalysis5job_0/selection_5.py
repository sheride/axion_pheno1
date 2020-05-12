def selection_5():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(-3.2,3.2,65,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([-3.15,-3.05,-2.95,-2.85,-2.75,-2.65,-2.55,-2.45,-2.35,-2.25,-2.15,-2.05,-1.95,-1.85,-1.75,-1.65,-1.55,-1.45,-1.35,-1.25,-1.15,-1.05,-0.95,-0.85,-0.75,-0.65,-0.55,-0.45,-0.35,-0.25,-0.15,-0.05,0.05,0.15,0.25,0.35,0.45,0.55,0.65,0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45,1.55,1.65,1.75,1.85,1.95,2.05,2.15,2.25,2.35,2.45,2.55,2.65,2.75,2.85,2.95,3.05,3.15])

    # Creating weights for histo: y6_PHI_0
    y6_PHI_0_weights = numpy.array([125.585994017,300.403446487,299.686947092,301.631645451,313.402135518,305.0092426,309.717438627,311.866836813,312.788036036,297.844648647,308.182139923,308.182139923,303.371643982,307.2610407,308.591539577,294.774051238,312.07153664,304.599842946,311.866836813,301.017545969,301.119845883,311.559837072,307.2610407,306.851641046,314.835034308,306.749241132,297.742248733,304.497543032,317.803231803,304.906942687,311.866836813,310.536237936,309.103339145,305.930441823,299.789347005,301.529245537,289.963455298,306.646941218,300.19874666,308.182139923,304.906942687,310.229238195,300.608146314,305.418642255,303.371643982,291.396454088,301.733945364,300.096346746,310.63863785,316.165633185,300.812846142,304.497543032,298.561048042,308.796239404,297.639948819,299.891646919,302.45044476,303.269244069,305.623342082,302.655144587,309.308038973,305.213942428,310.126838282,126.50719324])

    # Creating weights for histo: y6_PHI_1
    y6_PHI_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.303284616073,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.607364400582,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.304383383345,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y6_PHI_2
    y6_PHI_2_weights = numpy.array([0.0,0.501747425547,0.250748925267,1.25625793763,0.251018230755,0.250748925267,0.0,0.251462011492,0.0,1.0033939261,0.250917512362,0.0,0.753781001008,1.0037889488,0.250460405808,0.501740504386,0.502516087665,1.25531686628,0.501402297186,0.250657090752,0.752123744409,0.501870560239,0.251741750373,0.502140898737,0.0,0.251148596512,0.250460405808,0.501747425547,0.250467636872,0.251462011492,0.250748925267,0.50289096669,0.501616130083,0.502681679034,0.0,0.752546038555,1.25386962044,0.0,0.501574603114,0.502568357929,0.251462011492,0.0,0.251462011492,0.752145747504,1.00407922438,0.250460405808,0.250917512362,0.251421414231,0.501769841846,0.250384066431,0.501942664279,0.753043329165,0.753555185205,0.502609574994,0.501988219983,0.250822992024,0.502439644987,0.501897521778,0.501666437629,1.00357067397,0.502697587375,1.00478167061,0.251524611847,0.501985017654])

    # Creating weights for histo: y6_PHI_3
    y6_PHI_3_weights = numpy.array([1.37360104222,2.33795836478,3.84988406863,1.92463277062,2.74978689922,3.5756763543,2.61296742247,2.7503180812,1.78869893571,1.37407331683,2.74968228786,3.0239753163,2.33730225855,1.92584037171,2.20109521532,2.47618958713,2.61024549571,2.20004300781,3.02386867365,2.47519324006,2.75104121995,2.19927416507,1.78678749311,2.33780804942,2.88714974568,2.06223023092,2.33698131495,2.47624443192,3.43625378118,2.2015624117,2.47368196132,2.74963353693,1.78715921893,2.47621497824,1.6510415524,2.47522980325,1.51232180513,2.06254812759,3.16315718173,2.06242421898,3.29910320437,2.88798765224,2.61189998029,2.33884299098,2.063877606,2.06307930957,1.78741109872,2.33860837714,2.33993277733,3.16174645178,2.61384392351,1.92537825355,2.19923353929,2.0618585051,1.51292814479,1.6515229678,2.61417299227,2.33837274766,2.61288210834,2.19970378261,3.30097706813,2.47455643107,1.92425901351,0.550495569766])

    # Creating weights for histo: y6_PHI_4
    y6_PHI_4_weights = numpy.array([1.06140703818,1.77633554295,1.97377986682,2.171006741,1.48037849026,1.75183086616,2.14630064767,1.6038909196,1.89914752373,2.02302771362,2.19513463859,1.80103261763,1.7268471988,1.38148196774,1.67810940682,2.0233253291,1.60293794882,1.75167354081,1.94860179743,1.67810439646,1.60356825231,1.99851602232,1.82583791612,2.09704979466,1.77641370459,1.72660770351,1.52994098777,1.97398328751,1.67738190231,1.52959427074,1.45556417312,1.82574572546,2.24522121993,1.99847293321,1.80117892019,1.60388089888,1.60410035272,1.77649888074,1.48033540115,1.62828035807,1.70253592197,1.75189399672,1.72677605166,1.5542342273,1.60326161818,1.60358228132,1.92387065229,1.72718690132,2.0972111283,1.72694239567,1.35689311688,1.89966158684,1.5788832025,1.97409151132,1.57898641595,1.06043502802,1.50487114219,2.09673013358,1.85007704374,1.99858817153,1.67747709918,1.77605295855,1.35683700083,0.962288556642])

    # Creating weights for histo: y6_PHI_5
    y6_PHI_5_weights = numpy.array([0.283587558105,0.63010757138,0.731002476598,0.686797175172,0.693122449675,0.573411165681,0.57351339436,0.554520366026,0.605090553066,0.699534448507,0.655355954602,0.636439347707,0.750048019665,0.649087496039,0.636503165611,0.567203624207,0.573299034223,0.67428786579,0.75612022317,0.756318978929,0.592360781836,0.567186519408,0.6806117399,0.655423773628,0.687081254868,0.598694658752,0.68062414338,0.617515338735,0.573481185324,0.705814610354,0.579867977085,0.667900673917,0.523160668326,0.674389294245,0.699494737366,0.680566927328,0.749904079283,0.693220677231,0.642651990612,0.649135309452,0.730930256337,0.573438873454,0.699298882421,0.70586642489,0.680578630612,0.636502365386,0.554609591057,0.636438547482,0.642945572974,0.69949143644,0.668032110791,0.686937514543,0.693312903105,0.617613766348,0.737258831765,0.649092497442,0.617679584813,0.718412744654,0.67458724978,0.586120131074,0.55456557871,0.617663880408,0.699457827011,0.308756218961])

    # Creating weights for histo: y6_PHI_6
    y6_PHI_6_weights = numpy.array([0.142939481439,0.264760124947,0.228957111808,0.271789090672,0.343472844453,0.293519801519,0.214863415709,0.27198328447,0.243480733482,0.1861277072,0.229145507284,0.250481507366,0.300530772452,0.307691699986,0.257519470487,0.250528993623,0.279111971334,0.265001555074,0.214368383978,0.229242654169,0.250448766841,0.307673455266,0.229065205525,0.250604471778,0.27190505711,0.229073303181,0.257645184104,0.293383091085,0.229167900803,0.2576541815,0.236054957599,0.157324168322,0.264874091963,0.200574326159,0.250857898433,0.207634182944,0.214839572609,0.271833577797,0.200254793636,0.257881865605,0.279509856181,0.2291371597,0.221980280995,0.293738738156,0.286644791237,0.250542989572,0.185817971841,0.264780369088,0.250466261778,0.264889587479,0.178931114988,0.2216233343,0.229015020049,0.293213390198,0.272018524271,0.293352349982,0.243326578096,0.17153348096,0.221905877528,0.236141407579,0.265188500969,0.279330158188,0.178998945357,0.0786758051899])

    # Creating weights for histo: y6_PHI_7
    y6_PHI_7_weights = numpy.array([0.00702448636907,0.0215976972454,0.0215903106878,0.0286160480568,0.0248317521929,0.0232252440154,0.0237559131735,0.00972171564604,0.0226818238777,0.0232300636132,0.0232162125081,0.0253844133857,0.0237637712135,0.0205195951105,0.0216005261398,0.0259267438751,0.019993902711,0.0237530633243,0.0291202932457,0.0237638236004,0.0275458353941,0.0248509886748,0.020527358854,0.0140422232056,0.0210595262784,0.0210217343446,0.0231847489158,0.0145710169115,0.0237553054851,0.028614507881,0.0210562992433,0.0291602016116,0.0221262290166,0.0204879848348,0.019980083038,0.0237594126206,0.0231779281371,0.022134610926,0.0237565208619,0.0172787508164,0.019395685841,0.0221424899208,0.0253741874563,0.0188611295724,0.0178252722606,0.0167331828144,0.0162009001388,0.0221407925841,0.0253505923814,0.0178180428638,0.0226795712395,0.0253800024059,0.0204835843324,0.0231828944184,0.0199778199225,0.0188960611796,0.0216016786523,0.0188969203253,0.0226751602597,0.0172833294344,0.0221406459007,0.0242675658748,0.0189062975864,0.00863265206917])

    # Creating weights for histo: y6_PHI_8
    y6_PHI_8_weights = numpy.array([0.00212455757871,0.00283856182619,0.00282012517609,0.00425664409346,0.00425978455293,0.00141868177579,0.00212835953921,0.00707631267792,0.00213139865761,0.00212009671566,0.00141479406515,0.00141987039886,0.00213215704516,0.00141004996681,0.000709212262694,0.00350873624741,0.0021313604227,0.00354545697919,0.00212941341208,0.00355031392619,0.000710731636286,0.000709935013826,0.00280619838912,0.00212822516022,0.000710202286972,0.00283782905231,0.00283829455304,0.00281288764202,0.00353844885457,0.000710731636286,0.00284182478584,0.00284014504836,0.00213317713767,0.00213021003454,0.000709212262694,0.00283944791091,0.00213017179963,0.00142195438698,0.00284160094458,0.00141868177579,0.00212440278301,0.00208744744481,0.00284057231418,0.000709212262694,0.00283566376861,0.00212908229035,0.00355103667732,0.00568329246507,0.00142040494516,0.00141554242996,0.000710202286972,0.0028411016635,0.000710731636286,0.000710202286972,0.00425955811318,0.00141054108122,0.000710731636286,0.00567592018079,0.00284061054909,0.00212869066094,0.00141914727652,0.00142115776452,0.00141868177579,0.0])

    # Creating weights for histo: y6_PHI_9
    y6_PHI_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y6_PHI_10
    y6_PHI_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,26.365709718,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,26.3028457174,0.0,0.0,0.0,26.32395418,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y6_PHI_11
    y6_PHI_11_weights = numpy.array([5.74956283208,5.76492882563,0.0,5.76549178107,11.4921492437,11.5074239732,17.2775731057,23.0287585175,5.75900434409,11.4921492437,0.0,5.76613062982,5.76682904041,5.76910103633,11.5126212239,0.0,11.5206332518,11.5196821837,5.76492882563,0.0,0.0,11.5121408865,11.5192690935,11.5220166235,11.5135050447,11.5174438114,5.75321339635,11.5181258905,0.0,0.0,0.0,17.2580137666,5.74881158438,5.76682904041,5.75465632991,0.0,0.0,5.77096378478,0.0,5.75465632991,5.75050429339,17.2732981028,11.5121408865,5.76880610916,0.0,23.0393643674,0.0,17.2523361785,5.77096378478,0.0,0.0,23.0461467316,11.5150517311,5.76613062982,11.5232366805,5.76613062982,5.76245797003,11.526839211,23.0212748608,0.0,0.0,5.76492882563,0.0,11.5197782512])

    # Creating weights for histo: y6_PHI_12
    y6_PHI_12_weights = numpy.array([3.46322488898,3.46014844665,4.15033996409,3.46072738328,5.53810876862,4.15310770433,3.45860782126,3.45951373207,2.76783352043,5.53945417119,9.00626519753,5.54122464018,3.46267095625,4.84367428039,5.5396753596,7.61843388323,8.99966801267,4.15404054242,4.84571402224,4.15218832988,6.92048634598,4.15279323211,4.84836347476,7.61882432887,6.23265769781,6.23062853454,4.84550533578,4.8463756641,4.8434078926,2.76431470128,2.76959533423,3.46200065919,4.15328369337,0.69101279964,3.45834528023,4.15073329479,4.15361739937,5.54038893266,8.31401566615,8.30117038945,6.92686522749,2.77006079159,4.84628815042,4.15105449884,7.6155372767,5.53619404631,2.07697843775,5.53854826038,5.54046009762,3.46259979128,6.23159214667,4.1506640532,3.45886651554,4.84414069943,2.07255082272,6.92582756533,4.84736139507,4.84755373282,6.23137095826,4.15546480347,2.76929528734,5.53431971492,4.84960501494,1.38290939125])

    # Creating weights for histo: y6_PHI_13
    y6_PHI_13_weights = numpy.array([0.251834218163,2.01726970063,1.76463666863,0.504805892615,1.00750740765,1.2553460394,1.2594155142,1.76535431145,0.757389615122,2.01645040439,1.00651150754,1.26042871055,1.26141596253,1.2612797166,1.2593062747,1.51294036534,2.01647012819,0.756770743013,3.7813738267,1.5124876283,1.26180361103,1.51198891964,0.756617655992,0.504505483991,1.51377832333,1.25768376469,1.76416936633,2.01623495982,0.755744498603,1.51099590224,1.00634749657,0.756773322279,1.25940049376,1.00837267552,1.51120391246,2.01482091519,1.2594000386,1.26053188119,2.01702998062,2.01746390419,2.52023111464,0.756484596213,1.51260718486,1.00780918177,1.26090724025,1.51094188938,1.2617166746,2.01760803964,1.76204981659,1.00820123019,0.50366980182,2.01729701051,1.51318433355,1.76553030842,0.754382797898,1.51241707779,2.52248569654,1.51397692681,0.756785156558,0.756617807713,1.76379764859,2.01687370745,1.76365503035,1.008559293])

    # Creating weights for histo: y6_PHI_14
    y6_PHI_14_weights = numpy.array([0.282987957504,0.565520666063,0.49504470515,0.494810395741,0.0707530346741,0.565758630544,0.566026316539,0.63661164108,0.636916070176,0.424507088928,0.283065098779,0.49494111269,0.21227624439,0.919850067262,0.636608274565,0.707886043044,0.707163011918,0.565569720988,0.212313660794,0.565790371966,0.707345477003,0.636700613249,0.495488219387,0.49477317171,0.565725157771,0.42423228516,0.495099435057,0.424251233827,0.990241961499,0.495400882383,0.636335683078,1.06148510297,0.636378293533,0.707135887429,0.494908409406,0.636617508434,0.990201563325,0.778316315546,0.566126253926,0.707369619721,0.4242715291,0.566432318186,0.565723522607,0.919340473154,0.353515089437,0.495256795563,0.565720444651,0.424648674909,0.494655343703,0.49504345473,0.494986801101,0.565594537009,0.212341362399,1.27300897947,0.282990458343,0.353714675653,1.20233814546,0.636284512058,0.424189963264,0.565737084851,0.849237041116,0.635934490737,0.706679868995,0.283046246298])

    # Creating weights for histo: y6_PHI_15
    y6_PHI_15_weights = numpy.array([0.0381124151314,0.0381239976918,0.0377124031333,0.0,0.0,0.113901215179,0.0761046316509,0.0,0.038040733265,0.0380237435399,0.0759555948272,0.0,0.0383333997476,0.152256686795,0.114178251114,0.0758196474788,0.152147804818,0.0,0.038040733265,0.0383333997476,0.0383333997476,0.0381918974977,0.0,0.0767477001341,0.0377124031333,0.0380237435399,0.0380482087441,0.0379318512874,0.0377789142138,0.0,0.0770426417625,0.0,0.0380237435399,0.0,0.0,0.114219321928,0.038040733265,0.0761046316509,0.114089904544,0.0377124031333,0.0764289433432,0.0380237435399,0.0377124031333,0.0384073863071,0.0,0.0383914307392,0.114569014792,0.0,0.0,0.0,0.0,0.0760185306786,0.0384073863071,0.0,0.038040733265,0.0,0.0,0.0,0.0,0.0,0.0380482087441,0.0380813017739,0.1143979061,0.0379704696713])

    # Creating weights for histo: y6_PHI_16
    y6_PHI_16_weights = numpy.array([0.0,0.00451258424683,0.0,0.00451917421617,0.00902922526609,0.00450009054273,0.00451258424683,0.0,0.00902933113678,0.00902647936532,0.00903300003748,0.00451642831541,0.00451917421617,0.0,0.0135495140119,0.00902750438611,0.0,0.00903990954382,0.00903203757665,0.0,0.0,0.00903990954382,0.00451835804938,0.00451887585331,0.0090448642922,0.00450859292175,0.0045136785648,0.0,0.00902395098071,0.0,0.0,0.00451917421617,0.0,0.00451258424683,0.0,0.00902973537033,0.0,0.00900005789048,0.0,0.0,0.00904255631111,0.0,0.0,0.0,0.0,0.0,0.00450009054273,0.00451565353444,0.0,0.0,0.00901610884982,0.0,0.00451601926955,0.0,0.00902812036105,0.0,0.00451005104991,0.00451642831541,0.00451835804938,0.00901720990502,0.0,0.00450009054273,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights+y6_PHI_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights+y6_PHI_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y6_PHI_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\phi [ j_{2} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 1000.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights+y6_PHI_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y6_PHI_0_weights+y6_PHI_1_weights+y6_PHI_2_weights+y6_PHI_3_weights+y6_PHI_4_weights+y6_PHI_5_weights+y6_PHI_6_weights+y6_PHI_7_weights+y6_PHI_8_weights+y6_PHI_9_weights+y6_PHI_10_weights+y6_PHI_11_weights+y6_PHI_12_weights+y6_PHI_13_weights+y6_PHI_14_weights+y6_PHI_15_weights+y6_PHI_16_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonposx="clip")

    # Log/Linear scale for Y-axis
    plt.gca().set_yscale("linear")
    #plt.gca().set_yscale("log",nonposy="clip")

    # Legend
    plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.)

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_5.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_5.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_5.eps')

# Running!
if __name__ == '__main__':
    selection_5()