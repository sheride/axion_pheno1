def selection_2():

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

    # Creating weights for histo: y3_PHI_0
    y3_PHI_0_weights = numpy.array([27.0168611273,64.6046653051,64.5186653779,65.9515841648,65.0795449031,64.9649450001,65.4971445495,65.4071046258,65.0754649065,65.5258245253,64.2402656136,65.8492642514,65.0877448961,64.7561451769,64.8666650833,64.4081454715,65.6077044559,65.4275446085,64.8748650764,64.6128252982,64.772505163,66.1153440262,64.5227453745,65.5381045149,65.3947846362,66.160383988,65.7919443,64.2935055686,64.76430517,64.2730255859,64.887145066,64.5186653779,65.0631849169,64.7602251734,65.9352241787,66.2341039256,64.9403450209,65.5872244733,65.4685045738,66.0949040435,64.5104653849,64.5391453606,65.4685045738,65.0836648996,66.1685839811,65.5995044629,64.9280650313,65.0631849169,65.1205048684,64.7192652081,65.8574242445,65.1737048234,65.1983048025,66.0826240539,65.1655448303,63.9495858597,65.6199844455,64.4981853953,64.4163054646,65.0795449031,65.6035844594,65.2105847921,65.4234646119,27.1110250476])

    # Creating weights for histo: y3_PHI_1
    y3_PHI_1_weights = numpy.array([25.0914018284,62.4863638576,61.2116902788,62.2225526519,62.8429455998,62.4762696542,62.2695788218,61.0185785535,63.558312184,63.4150706304,63.0477537831,62.4421816894,62.574167405,63.1714077752,62.3269795898,62.574167405,62.9747710899,63.2170319725,63.2054556836,63.1813016968,62.5122803244,62.392351574,62.8345337636,61.7967134583,62.2563602221,60.5349380284,62.0759063074,62.8773139591,62.3220126008,64.1680501394,62.8644558666,60.6903567162,62.5756094341,63.0362976633,62.1721617474,61.1746781995,62.9863073224,63.0731495171,62.5970796446,63.9457373256,63.2105428417,63.0745915462,62.3404785841,63.3373612865,64.0208029496,63.5739742219,63.2540440518,61.7848567749,61.5434771324,62.9342340507,63.3510205062,61.0841508195,63.0680223027,62.0872022018,61.8824741312,62.9401223361,63.5338778027,62.2936126396,62.1252156901,62.5276619677,63.325384434,63.084285186,64.0665473159,26.0984067737])

    # Creating weights for histo: y3_PHI_2
    y3_PHI_2_weights = numpy.array([57.5096593038,138.82595135,141.73656548,141.282157786,139.046895057,140.35123563,139.275813728,139.638364707,139.364860612,140.719984768,139.457419786,137.918706162,141.461697791,139.870713026,140.171406378,138.693971885,137.537147496,137.144597428,136.979313188,137.74747169,139.776707615,137.570369628,139.877572322,139.541756069,139.968767901,139.026193206,138.613726387,140.331277558,140.641474754,138.270637628,139.806128209,139.436841898,139.779269521,140.812626584,140.442348567,140.309460039,137.981555493,140.601021436,140.538585315,140.019882052,137.569460564,137.989943669,140.469992356,139.638447349,140.755727484,139.205650569,140.087565948,139.074621488,138.752730432,139.207675301,138.010810804,139.709808819,140.952167803,137.950812625,139.66695888,138.815083911,138.562529594,139.31606044,138.099692403,140.038269923,138.865660889,139.666008496,137.600657964,58.8952370805])

    # Creating weights for histo: y3_PHI_3
    y3_PHI_3_weights = numpy.array([35.8453154105,85.7279630449,84.9489661989,85.1713916347,85.0370426089,85.5341786926,84.4030387091,85.7676949309,84.625220391,84.4675928676,84.9683446341,84.5351939498,84.2040136479,85.9373476469,84.9664758542,85.7245911159,85.0582491984,85.1723666503,85.6399678862,84.8484177142,84.8346862444,85.4856310404,85.1674509466,84.7340565084,86.3627794577,85.4963562121,85.3656228692,84.2712490993,85.2014952416,86.36761391,86.4089301965,84.430826654,85.3932076858,84.7096811182,87.0688532612,85.0367176037,85.7837826885,85.5383631346,85.3696854342,85.5819950831,83.8676738885,84.4092544336,86.296275268,85.7317006047,86.2063707037,86.1251600286,84.6623116098,84.6008043752,85.348681973,85.3202440177,85.7392569757,84.7360471653,84.3152466787,85.3092344664,85.3419787406,85.5414100583,85.8672277744,86.4433401223,84.4476050476,85.0946904068,85.4447616361,85.5085032815,85.2705994729,35.978677233])

    # Creating weights for histo: y3_PHI_4
    y3_PHI_4_weights = numpy.array([6.51622640869,15.3554202684,15.6837099349,15.5503730719,15.7037876246,15.8657078386,15.811623537,15.582259281,15.8537149363,15.817283289,15.5556359999,15.7412173443,15.6829603785,15.6880228904,15.786379119,15.6800543444,15.6997873183,15.8993617181,15.6168430914,15.7264386576,15.532067061,15.7787673138,15.6681696668,15.6564493305,15.7035631585,15.7471817289,15.8024284441,15.5369892815,15.702080079,15.6689232315,15.6582610925,15.747121604,15.6120371122,15.7106659068,15.665155408,15.7701454111,15.2851463504,15.7720012646,15.5802390862,15.781897814,15.6071269166,15.684976565,15.9285984257,15.630651764,15.5012831407,15.4538807134,15.5723827732,15.39019247,15.7579761426,15.4866086703,15.658305184,15.4769365871,15.5944205328,15.8440308281,15.6169673494,15.5112317982,15.7836815177,15.6485970258,15.4521972178,15.653154489,15.6818260231,15.5903160101,15.6033150014,6.49719088298])

    # Creating weights for histo: y3_PHI_5
    y3_PHI_5_weights = numpy.array([1.61956898424,3.99293241203,3.98174044381,4.0520622372,4.01982626396,3.97251736257,4.04988969985,3.98456594267,4.02540764446,3.98579664707,4.04359214221,4.01965022041,4.05064188589,3.99736790911,3.964384551,4.03376571174,4.03374570679,4.01536115956,4.02211483001,4.00672702399,3.9485270288,4.0118442897,4.03076496954,4.05793168895,3.96742970419,4.07509593436,4.04257188986,3.99815570396,4.00829141093,4.04239184533,3.99192136196,3.95684628649,3.99522737967,4.03396976221,4.01485703487,4.05535505165,4.0345499057,4.00381030257,4.01069600568,3.98743625261,4.04486045591,4.02819233322,4.02814032036,3.97724973308,3.98357369725,3.98121191308,3.98584946013,3.94853703128,3.96737128974,4.03076897053,3.9654636179,4.02342315361,3.97170916267,4.01917010166,4.01968622932,4.03194526147,4.07202717533,4.02263495866,4.01328464595,3.99034817285,4.03144513777,3.97928943758,3.95261844077,1.68262177972])

    # Creating weights for histo: y3_PHI_6
    y3_PHI_6_weights = numpy.array([0.759567477618,1.84410633269,1.80732867099,1.81238597435,1.83321198756,1.82945624755,1.81545694409,1.78548499918,1.84796503816,1.88884132484,1.84387840915,1.83988974728,1.82827164497,1.84525594701,1.81743528039,1.84404535315,1.80127970032,1.8651952577,1.80518838902,1.84613465222,1.84233192797,1.81472518958,1.82788577442,1.84141023718,1.82716601589,1.87045449331,1.79737800927,1.81184015746,1.83219232964,1.80156160574,1.81760922203,1.85464579687,1.80579318612,1.79937733853,1.82962918953,1.82815168521,1.80620304862,1.83878111921,1.80964989226,1.82344726347,1.81241696395,1.78105448555,1.80364990515,1.85099402198,1.864067636,1.84130827139,1.82256555926,1.82816068219,1.8036938904,1.84505701375,1.83549022325,1.84187308191,1.82901439579,1.8254925773,1.8427747794,1.84269380657,1.83459452374,1.78762528115,1.78873790788,1.8506401407,1.82782279555,1.78972757587,1.80453660768,0.747547310186])

    # Creating weights for histo: y3_PHI_7
    y3_PHI_7_weights = numpy.array([0.132483912607,0.325598517704,0.325424383705,0.329682431467,0.325503341215,0.325436495552,0.328770145331,0.329997507136,0.33262003641,0.325116851746,0.329738087291,0.325127999675,0.327314753901,0.326830405736,0.327717881444,0.322923098633,0.330316145113,0.326613398311,0.325633009228,0.328024114207,0.327110780334,0.325381929375,0.328472462107,0.329020386994,0.328921690106,0.320135068718,0.327703464573,0.329606700989,0.328842229682,0.333818690203,0.326955966617,0.327641564232,0.328218113312,0.329707283804,0.330778909883,0.328657492578,0.328509845386,0.32632057659,0.328019001247,0.326735941708,0.329378797093,0.329941055031,0.32973142368,0.32692260665,0.332644050557,0.329758497221,0.32531952612,0.32973310006,0.329189324214,0.329164974791,0.32460962099,0.327255284312,0.326956888626,0.325512016483,0.324031353621,0.329130147991,0.32999122071,0.328809330719,0.328955804444,0.328512485685,0.327339773877,0.32677311544,0.326214629358,0.137706591479])

    # Creating weights for histo: y3_PHI_8
    y3_PHI_8_weights = numpy.array([0.0524432420583,0.121522465867,0.121998634972,0.123048119638,0.119830228644,0.119193430798,0.120553095102,0.11992826608,0.122101231253,0.122897915356,0.125718578023,0.120190511024,0.123611738373,0.120397307349,0.121569836274,0.120983898504,0.124616406774,0.119013601451,0.121940305519,0.123131931102,0.121898577982,0.119521266678,0.121136894521,0.12304887697,0.12147601614,0.125066707776,0.120735211296,0.119789139642,0.119791901679,0.120021714972,0.119526746201,0.126084948763,0.11978579847,0.124062856106,0.120001831281,0.121787190704,0.127030782822,0.12281503942,0.124052669241,0.116459193136,0.11923490589,0.12525011589,0.121642822338,0.122345359616,0.123174846611,0.12352440754,0.127096938045,0.12138984358,0.122063914065,0.121211306152,0.118166740356,0.123374158709,0.119970943994,0.120715461252,0.121961288084,0.121015632221,0.124935035866,0.120720955625,0.125744861916,0.119314485203,0.123726570771,0.120404004544,0.122586681393,0.0501002631612])

    # Creating weights for histo: y3_PHI_9
    y3_PHI_9_weights = numpy.array([4809.1009488,11645.8829898,11432.44672,11218.4336683,11184.7842043,11649.1475761,11711.3439056,11385.508198,11333.4863035,10981.7569277,11291.5427139,11369.6582276,11612.0297295,11166.6424866,11297.6796748,11156.1565892,11630.3291009,11528.876986,11708.9752541,11445.5973505,11177.0130277,11294.1843756,11427.3018243,11508.3320099,11348.9133004,11181.8541515,11427.2941339,11278.7727596,11404.0459726,11463.3968441,11380.4286708,11327.7377093,11216.6264179,11125.0488114,11276.4041081,11433.0619542,11221.2522098,11155.8489721,11260.4733882,11367.5625862,11189.8137436,11534.3910223,11456.0947835,11513.4499892,11421.6685864,11411.7633162,11387.6192202,11260.1196286,11659.191274,11226.6547349,11516.0455083,11596.6834821,11278.7535336,11458.4480542,11565.7448937,11111.5328857,11299.5676746,11529.3230308,11364.9132341,11009.8769745,11270.7977867,11750.888082,11278.2075132,4764.92329007])

    # Creating weights for histo: y3_PHI_10
    y3_PHI_10_weights = numpy.array([5533.69833308,13789.9117447,13542.5065642,13557.0543782,13691.0974207,13710.0199675,13600.2130213,13537.1660813,13429.7523486,13737.4341898,13650.0203347,13510.9561609,13543.2799338,13226.3946091,13678.7273541,13499.3017498,13469.7097801,13536.004103,13698.3116898,13941.7461366,13611.9790131,13618.4006745,13759.1385587,13651.8710352,13648.7313853,13516.2658629,13561.6214914,13643.7795111,13619.4010531,13668.019455,13643.3024074,13455.9776594,13723.782869,13843.8321534,13564.7265128,13536.2272644,13645.5417165,13656.1534253,13562.5910892,13666.9921431,13453.8961023,13635.2301213,13673.9332318,13669.6046704,13641.1785266,13430.3987471,13780.4812522,13589.812931,13593.2296088,13608.9855724,13496.723851,13564.5649132,13602.6216252,13624.6376505,13627.8196241,13607.7966609,13604.4684781,13652.2250153,13790.1272109,13751.2009389,13628.7045745,13498.9900933,13784.805966,5686.32148507])

    # Creating weights for histo: y3_PHI_11
    y3_PHI_11_weights = numpy.array([1571.77132189,3751.01351807,3699.42018662,3752.35333015,3742.04519178,3750.58510096,3790.55814656,3696.15038426,3666.64762234,3684.67725873,3724.05320999,3743.61131568,3740.44871366,3745.77107585,3693.22562098,3684.4897542,3791.57866302,3692.69307738,3797.78821364,3696.17459079,3789.26059984,3708.14337379,3791.5909584,3761.16066382,3757.49203011,3720.35230091,3724.92963997,3788.13403574,3717.68189828,3748.21247704,3730.31847405,3767.85319231,3770.54011685,3718.10685732,3767.65608201,3795.22962212,3705.83914292,3736.0296776,3690.46876647,3727.46978843,3712.75606207,3728.94292853,3755.25119729,3753.32620201,3730.93631685,3682.59933968,3762.08704378,3770.36798154,3681.21649377,3762.75637348,3715.61166384,3759.49963497,3711.82199749,3723.82958778,3743.86759748,3725.86524147,3702.74992894,3725.00494917,3745.96780191,3710.87371639,3719.21536258,3727.1139909,3741.14263411,1503.3936454])

    # Creating weights for histo: y3_PHI_12
    y3_PHI_12_weights = numpy.array([190.61715853,459.894265786,455.355400196,458.256150031,450.790373998,453.169065805,451.334360771,458.570462049,450.059031102,457.869511624,450.757673237,461.313863517,456.735757014,452.251136216,457.598287668,457.345145308,457.586361508,452.335004049,451.831027619,463.026613949,459.273720762,454.77371137,461.139587698,461.831304966,459.501856657,453.363346796,455.432343163,457.984541359,448.62019763,456.903877396,451.580578263,459.284492777,453.774991666,466.430186069,456.819624848,454.050447486,454.651756768,458.679336346,453.38758383,453.139442763,449.782036423,456.537628876,456.706903402,453.718438586,452.700867855,456.844246597,456.569175492,454.914516999,452.481195685,452.833209757,453.154446642,451.101608297,461.742051125,456.787693516,449.198808738,455.02531487,457.176640212,450.091347148,451.396299859,460.529045259,450.197528442,456.184845374,455.323468865,187.934542006])

    # Creating weights for histo: y3_PHI_13
    y3_PHI_13_weights = numpy.array([44.0473690302,107.436519229,107.039894698,106.398899454,104.506073207,107.231774558,104.338405891,106.897168123,105.479126197,105.560138093,105.267949122,105.727684043,104.448788391,105.669185565,104.209939837,104.843774479,106.374626227,107.614502666,105.227776931,104.955431323,106.232931264,107.75601558,106.092510646,108.1777629,105.75729738,105.971265876,105.638479933,105.434342093,105.455095703,105.91950322,105.16405971,105.406063784,106.080980863,106.817127157,105.537442625,108.026480013,106.716514631,105.168671623,105.962770247,105.860519278,106.331723298,104.510260339,105.680169201,106.011862849,106.698734492,104.349632259,106.888975909,105.860215862,106.517534852,106.404846395,106.133835815,107.405388815,104.640971667,106.680044107,105.467292999,105.072549644,106.840611504,105.293860792,105.626282637,105.508739534,106.458732959,106.807842647,106.850138746,44.4938750422])

    # Creating weights for histo: y3_PHI_14
    y3_PHI_14_weights = numpy.array([19.2808597511,46.8793601918,47.0792718474,47.0860048227,46.7438927284,46.8425404353,46.6338182006,46.4268273023,47.0728466652,46.8941727374,46.8467725912,46.6449757025,46.890325323,46.5623717139,46.7010325313,46.6999937294,46.8682796381,47.2500970496,46.8398857193,46.6672137581,46.7705937848,47.0086333178,46.2004454352,46.4396007184,47.2343995986,46.5515220052,46.8906715903,47.0551485587,46.6634048178,46.613465378,46.5569468596,46.7198848622,46.636857658,46.3532262636,47.3603254741,46.7401992105,46.7746720441,46.7237707508,47.0653826812,46.3155985501,46.4661478782,47.1788429337,47.2895715221,47.1913470308,45.7898493634,46.6378964599,46.7328506489,47.1560662401,46.783405675,46.7009171088,47.003093041,46.9702361214,46.8175322413,47.0746164759,46.5481362804,46.1583931951,46.8253809668,47.0945845569,46.6669444391,47.1172458281,47.0721541306,46.9333778908,46.621429526,19.5801347327])

    # Creating weights for histo: y3_PHI_15
    y3_PHI_15_weights = numpy.array([3.46854497399,8.19706676083,8.02234779874,8.09997821955,8.1192531853,8.20592081418,8.17539896737,8.2120677227,8.29427582972,8.33628088625,8.30684260636,8.10062694173,7.99533425093,8.21490839323,8.16474527125,8.23777791793,8.21406942647,8.10486667794,8.22741254278,8.12864961293,8.18467841232,8.05639566919,8.20991358694,7.99100234654,8.11321498796,8.22427527978,8.05470828254,8.25576961903,8.05037519651,8.26954285351,8.20581682957,8.1432440895,8.17285134439,8.24170806359,8.25498973445,8.15184408955,8.11737673571,8.35524035323,8.0652130916,8.16512457875,8.08586821674,8.25145543929,8.23442323256,8.16169781314,8.09705956057,8.09968517201,8.26442279302,7.9222484303,8.25362729971,8.21438847017,8.08356519392,8.08989525715,8.19087849479,8.33050855866,8.25397824777,8.37092784987,8.19330795344,8.19397676356,8.20304942093,8.10477569141,8.11287349304,8.06909242661,8.04512633691,3.51620064886])

    # Creating weights for histo: y3_PHI_16
    y3_PHI_16_weights = numpy.array([1.2904453641,2.98663201716,2.98592530915,2.96430928703,2.97515869924,2.97539978873,2.98216685493,2.9808389371,2.9700311186,3.00851300665,2.97328582672,2.96230431596,2.98290706899,2.95905307397,2.98008177745,2.9715269518,3.04111092467,2.99359973452,2.94063168016,2.97945787174,3.00349403182,3.04302616115,2.97309826988,2.99517297825,2.99983108909,2.94763636972,3.01850897747,3.00003097,3.02480156723,2.99904234903,2.98780858009,3.03774876612,2.93374214358,2.99929922873,3.00889274186,2.98088669284,2.99083413766,2.98520589195,2.96783242866,2.99963197844,2.98424808114,2.97212158786,2.97244278376,2.99439232585,2.99971401049,2.95004495386,2.99331435543,2.96281769022,2.97855012744,2.97729923501,2.9967908967,2.9931183258,2.99850163075,2.99714328789,3.00653229858,2.96010485576,2.98971457353,3.00886539784,2.98896511642,2.98669941438,3.03126245749,2.96928820865,3.01014671531,1.2585071686])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights+y3_PHI_14_weights+y3_PHI_15_weights+y3_PHI_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights+y3_PHI_14_weights+y3_PHI_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights+y3_PHI_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights+y3_PHI_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=4, linestyle="dashdot",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y3_PHI_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=3, linestyle="dashed",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\phi [ j_{1} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights+y3_PHI_14_weights+y3_PHI_15_weights+y3_PHI_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y3_PHI_0_weights+y3_PHI_1_weights+y3_PHI_2_weights+y3_PHI_3_weights+y3_PHI_4_weights+y3_PHI_5_weights+y3_PHI_6_weights+y3_PHI_7_weights+y3_PHI_8_weights+y3_PHI_9_weights+y3_PHI_10_weights+y3_PHI_11_weights+y3_PHI_12_weights+y3_PHI_13_weights+y3_PHI_14_weights+y3_PHI_15_weights+y3_PHI_16_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_2.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_2.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_2.eps')

# Running!
if __name__ == '__main__':
    selection_2()