def selection_1():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(-8.0,8.0,161,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([-7.95,-7.85,-7.75,-7.65,-7.55,-7.45,-7.35,-7.25,-7.15,-7.05,-6.95,-6.85,-6.75,-6.65,-6.55,-6.45,-6.35,-6.25,-6.15,-6.05,-5.95,-5.85,-5.75,-5.65,-5.55,-5.45,-5.35,-5.25,-5.15,-5.05,-4.95,-4.85,-4.75,-4.65,-4.55,-4.45,-4.35,-4.25,-4.15,-4.05,-3.95,-3.85,-3.75,-3.65,-3.55,-3.45,-3.35,-3.25,-3.15,-3.05,-2.95,-2.85,-2.75,-2.65,-2.55,-2.45,-2.35,-2.25,-2.15,-2.05,-1.95,-1.85,-1.75,-1.65,-1.55,-1.45,-1.35,-1.25,-1.15,-1.05,-0.95,-0.85,-0.75,-0.65,-0.55,-0.45,-0.35,-0.25,-0.15,-0.05,0.05,0.15,0.25,0.35,0.45,0.55,0.65,0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45,1.55,1.65,1.75,1.85,1.95,2.05,2.15,2.25,2.35,2.45,2.55,2.65,2.75,2.85,2.95,3.05,3.15,3.25,3.35,3.45,3.55,3.65,3.75,3.85,3.95,4.05,4.15,4.25,4.35,4.45,4.55,4.65,4.75,4.85,4.95,5.05,5.15,5.25,5.35,5.45,5.55,5.65,5.75,5.85,5.95,6.05,6.15,6.25,6.35,6.45,6.55,6.65,6.75,6.85,6.95,7.05,7.15,7.25,7.35,7.45,7.55,7.65,7.75,7.85,7.95])

    # Creating weights for histo: y2_ETA_0
    y2_ETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,7.778759289,14.1245898142,14.533997461,16.3763358716,25.1786182775,31.9338524496,41.9643637959,43.8067022065,53.427793906,70.2135394244,80.4487505941,85.3616463556,100.919172934,123.02721386,138.994140085,168.471554654,203.476024454,220.057010149,257.51797783,292.931747278,339.194907365,377.883873987,432.540026833,483.101983211,527.522744888,578.698700737,653.415836276,700.907195303,740.210361395,801.826308237,837.240077684,835.80727892,870.607048897,877.362243069,862.418855962,874.496245542,832.736681569,763.341941439,727.518772345,663.241627799,618.002066828,552.906122989,485.967780739,419.848237782,355.980692883,295.592944982,242.369790899,197.334849752,153.732847369,126.097791211,119.956656509,162.125720129,199.58658781,232.339199553,297.844543039,341.651305246,429.469429482,471.228993455,542.466131996,608.176075306,669.178022677,710.118787356,771.734734198,814.518097287,855.049462319,878.59044201,883.093838125,876.748043599,881.046839891,799.369910356,789.95351848,742.666759276,688.829605723,669.178022677,593.028088374,523.42854842,489.65237756,416.777840431,379.112272927,323.637320787,291.498748514,258.336777124,220.671209619,194.878391872,159.669282248,150.048170548,128.144829445,101.32857258,91.9121807042,72.6699973051,59.3642087845,54.0419133762,45.649040617,33.1620713899,28.8632950986,26.4068372179,18.6280819289,13.7151821674,11.4634341101,10.2352091697,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_1
    y2_ETA_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.608524689202,0.0,0.0,0.0,0.0,0.0,0.606569232146,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.606204111962,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.60876676669,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_2
    y2_ETA_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.501848647982,0.501704646508,0.502036449043,0.502924010493,0.0,0.0,1.50662089325,1.00413219281,1.50479288028,1.50636512019,1.00420078462,0.502732697201,2.00683180855,1.50928481721,1.00320248459,1.50562383283,1.00359750728,0.502036449043,1.50534368076,0.501497838079,1.50800863773,0.0,1.00281200713,1.00312005046,1.00413529184,0.0,1.50609571141,0.501704646508,1.00451110056,0.0,0.501778196758,0.0,0.0,0.0,0.0,0.0,0.500935261303,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.503483488241,0.502286643856,0.501645971589,0.500768120424,0.501645971589,0.502036449043,0.502924010493,0.502036449043,0.501835012261,1.00488422346,1.50779645765,2.00514469803,1.00454601627,1.5075303545,3.00900273021,2.00793878114,0.501848647982,1.50538706714,2.51175758415,0.0,0.501835012261,1.50553974589,2.00643947168,0.501622212379,1.00482720136,1.00377807728,1.00574719929,2.00727517607,0.0,0.0,0.0,0.5030492112,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_3
    y2_ETA_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.27511570108,0.274721427956,1.37391142682,0.549817831794,1.37603493595,2.20317424515,2.75099857028,3.57683724537,5.22908945023,3.84910101721,6.32456747224,6.60177133804,7.42766485792,8.25064347861,6.60149711407,10.7226770559,8.24933939131,6.87175803532,6.60019505806,7.97422369023,4.39963508138,7.14979066688,5.77521968064,5.50332560333,4.95007570626,4.39769113815,3.30319625984,3.57099322798,3.02213294564,1.92323504609,2.20140296147,1.65007547596,1.10097387654,1.37689010847,2.19925588938,0.274618644751,0.550881820779,0.824664184001,0.549649641095,0.27489754068,0.274950963572,0.550685395169,0.275121591817,0.823835011981,0.275401909648,1.92613105429,1.10073459074,1.92400835767,1.92695677312,2.75003777076,3.5765467711,4.67449687138,4.12654863764,5.50115009321,4.39679940244,3.84880038649,6.59544590524,8.52388836286,9.07433508162,8.25014987547,10.4502365619,11.2797945265,6.87651125072,5.50042898574,7.70383682909,5.22544734971,5.77431981978,6.32231274186,4.67646925264,3.57810883205,4.67693238645,1.92453832087,3.02696335001,0.825826893614,0.0,1.10069091803,0.275901403523,0.274855289877,0.0,0.0,0.0,0.273960507234,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_4
    y2_ETA_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0987187343842,0.345265623444,0.44437618815,0.937842095849,0.986775892944,1.38145410364,1.67833847267,2.12243127477,3.20746516928,4.09558583919,4.78610185457,6.31621619367,6.66084489994,6.3155848881,6.95645423214,6.21802513053,5.97005431674,6.56269792799,7.39978505844,5.67294788848,6.81014766417,3.94801064765,4.39107492271,3.94732923847,2.71355173608,3.10805759034,2.12139914027,1.9248314302,1.52977203119,1.23441682453,0.937477742351,0.937514819027,0.29605765936,0.740566521885,0.542563042584,0.493709611689,0.493504387277,0.394962598824,0.641296427266,0.690909028156,1.23305901653,1.57832804702,1.52935476827,2.02274912801,2.96000340823,2.95991522586,3.01101690623,4.44126872555,5.08171719921,5.08317220823,5.87132413869,5.2299858248,6.61268730807,5.87099946725,7.20438095476,5.57582503444,5.37910621186,6.71012080453,5.82434698802,4.88408248252,4.34179100154,3.79859765546,2.91156323196,1.67717566794,1.33262552414,1.23378632062,0.888369384256,0.394645943969,0.0491954381802,0.098477214912,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_5
    y2_ETA_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0126179212887,0.0251744813659,0.163831014104,0.151311822508,0.516658721208,0.529409497762,0.882441122065,1.27327695033,1.43684463057,2.19294111335,2.55893177262,2.21814218217,2.52103714329,2.94924525437,2.70959203237,2.96214087155,2.39486775316,2.34418153583,2.36948663383,1.9915840333,1.82773367377,1.39945534299,1.1720871669,1.19743687742,0.85722364864,0.604982095647,0.428736859392,0.453752276141,0.252047298505,0.226859033272,0.163821951562,0.226919050107,0.100811417298,0.126018147709,0.188914329898,0.352873780028,0.428703450021,0.541846186216,0.667866534542,0.78134696546,1.00801554531,1.10919612616,1.42423949487,1.82747500121,1.78961298103,2.23080973538,2.44541993289,2.75994215542,2.78531927363,2.65881979091,2.82332193326,2.72221957435,2.48324654314,2.16805213206,2.11721187152,1.73930226902,1.32317294601,0.781539819555,0.718526944634,0.403273116889,0.214160471364,0.163795004003,0.050426344437,0.0252171333296,0.0125885470494,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_6
    y2_ETA_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0143638188769,0.0,0.0,0.028554287912,0.0858015236152,0.114744049192,0.372476875058,0.415038809904,0.472253954893,0.500846081856,0.944989070563,0.887855601942,1.13085129195,1.31736332531,1.1876663527,0.987689715274,1.24555860177,0.973063947191,1.01752358294,0.916333861852,0.686734795577,0.686839765204,0.443950244477,0.486198420108,0.458394365119,0.171934201412,0.299993897766,0.15771261638,0.071606430918,0.0859243380793,0.0715841873541,0.0858671546251,0.114563751361,0.0574110383075,0.171351719951,0.243650400569,0.171726461521,0.286477558674,0.386403895321,0.458290045304,0.572735780812,0.715441989246,0.715981833044,1.04527955185,1.11632249581,0.91546211409,0.916921691766,1.2165389985,0.972836013143,1.15909511969,0.801817496781,0.744919959893,0.615945778143,0.444017974879,0.37193423207,0.30052594382,0.200372322936,0.0286795766601,0.0569437235235,0.0,0.0286946772908,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_7
    y2_ETA_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00108128831986,0.00107991829676,0.00216419015728,0.0129619649641,0.0237609949618,0.0334701168936,0.0506749080226,0.0864002195597,0.0906443365387,0.10260898839,0.113392000559,0.113419409403,0.0907243418643,0.115556796309,0.105812135082,0.098143526138,0.0691294628034,0.0496788019052,0.0614796293369,0.047523163391,0.0388699525005,0.0356459348547,0.0367110869512,0.0161994460519,0.0248478142942,0.0129622373761,0.0118052509844,0.0183598161539,0.0118828905161,0.00864083500119,0.0193646143115,0.0356604355581,0.0269213520054,0.0464370565209,0.0367079856447,0.0485895099095,0.0626557160047,0.0691271787331,0.0711909515199,0.0852168406307,0.116549759211,0.0907169238745,0.0928869373633,0.0982744096538,0.0874840004499,0.0701944472617,0.0626390988693,0.0529410620127,0.0388908025002,0.0259165287021,0.0129509092255,0.00432302217895,0.00215933493624,0.00107991829676,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_8
    y2_ETA_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0014198700204,0.0,0.00283829453854,0.00426135104876,0.00568020320393,0.00424137460847,0.0028314397248,0.00708182218067,0.00710327085053,0.0113554856123,0.0169550732964,0.0127832216298,0.00851752739246,0.00565799800258,0.00425743178506,0.00566853079176,0.0085277580145,0.00568114459934,0.0113609869845,0.00140997645949,0.00142040456669,0.0014198700204,0.00283988778345,0.00141842451814,0.00424410079455,0.0014198700204,0.00985090114142,0.00708939714705,0.00710321962318,0.00849469781136,0.00850724480065,0.00567246935852,0.00994551583463,0.00567962782424,0.009942048708,0.0141252149377,0.0113575421307,0.0183828018897,0.00425961080362,0.00992222594977,0.0085145354181,0.0014198700204,0.00283988778345,0.00283736353708,0.00281850741673,0.00142146326531,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_9
    y2_ETA_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_10
    y2_ETA_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,52.7314194359,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,52.6056914349,0.0,0.0,0.0,0.0,52.64790836,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_11
    y2_ETA_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,11.5010083094,0.0,11.5298573732,0.0,11.4991253868,0.0,11.5214130418,23.0270863879,0.0,11.5010083094,0.0,34.5830818007,23.0555223616,11.5293866425,23.0273169499,34.5845228128,23.0294688614,46.1043776401,11.53761194,46.035804674,11.5064265152,0.0,0.0,11.5093123822,11.5293866425,11.4739499434,34.5424068303,11.5180084104,11.4851648608,0.0,0.0,0.0,11.4991253868,11.53761194,11.5336578026,0.0,23.0275859388,46.0905247098,0.0,11.4976228914,23.0505076392,22.9967482782,34.5420994143,23.0354442586,23.0741978794,34.5770295495,23.0608444999,23.0121382883,34.5560484122,11.528454788,11.5214130418,0.0,23.0362512254,23.0048371599,0.0,11.4851648608,11.5010083094,23.0542542709,11.5010083094,0.0,0.0,23.0395559467,11.4976228914,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_12
    y2_ETA_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.38815964354,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.76621886236,4.15385111579,0.0,4.15857108423,4.15728242129,5.54116985868,5.53969462812,15.2387277681,15.2267489729,20.7686304812,13.8418921532,9.69436317935,16.6112961288,12.4535097826,12.4464221364,11.0693838464,22.1552702719,15.2325210288,6.92478802321,17.9975743244,17.9916964827,11.0834321958,11.0793911796,6.9216490711,11.0786641429,11.0714437837,8.30580193458,12.4604531754,4.15498975528,8.31225871293,5.54472041358,13.8498049284,9.68734477477,16.6052432597,11.0728959337,22.1739462676,8.30698481176,15.2342770725,9.69367845695,9.70082188107,18.0007979051,16.6119000693,22.1466343068,19.3811828721,16.6140254015,11.0728478493,19.3803750535,11.0734825639,9.68850072467,4.15712855109,6.92343973557,4.15216239032,1.38202560795,2.77088882299,0.0,1.38348083538,2.76873271678,2.76883850255,1.3844840691,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_13
    y2_ETA_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.504237726954,0.0,0.0,1.00953538056,1.0087297392,0.0,3.02449357772,2.51810959791,4.53569106043,4.53827942984,4.03218796915,3.02122579926,5.54766764051,3.02240771003,6.04927724701,5.0405566111,5.04321173799,4.02821893376,2.52224340289,4.03433634611,3.5299016846,5.55092358469,4.53532996317,6.0507277049,4.02691716297,2.52308940218,4.53578512778,1.51183896137,3.02054699711,2.52469734702,3.02845108228,4.53500831351,5.04375793552,3.5277684798,6.05280932438,4.03567756449,5.03640550986,5.54429031911,5.54628697453,4.53195264177,4.03581714831,3.01903554716,3.52980458282,4.53569409486,3.02404144754,3.52839660696,1.51398976587,2.5165787276,1.51382105152,1.00843630975,1.51120537223,2.01840591735,2.01864503049,1.0087297392,0.504767842003,0.503357438599,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_14
    y2_ETA_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.141173973061,0.141373847829,0.141506065278,0.566554939202,0.141625201413,0.566002253724,0.424616151783,0.706899345404,2.12124456578,2.12302208538,1.69707471762,0.848790809249,2.26218801917,1.97863132125,1.83824228468,1.69647682466,1.69856598731,3.25315134812,1.13163207477,2.40399907141,1.69847999691,1.41508989336,1.55572266556,2.40359124224,2.26122231047,1.41649459553,2.12290666203,1.98154383713,1.69766491568,0.849049742299,2.6873730157,1.55722297675,0.990150940937,1.83867492987,1.41509547215,2.26351923515,1.69832225167,1.98066469594,1.97969706352,2.68828678389,1.27311917214,0.9903827495,1.41438234822,0.990297528593,1.27287466701,0.707019962806,1.13191774756,1.13169017119,0.99003147777,0.566052462882,0.283029213211,0.141507046376,0.141506065278,0.0,0.141095273573,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_15
    y2_ETA_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.153937303482,0.0,0.0,0.152706301922,0.30300266315,0.0,0.0758636991624,0.229546068137,0.303543379595,0.0769107389413,0.0,0.2290219573,0.303192711684,0.0,0.0768147691591,0.0,0.0760964140653,0.227905067594,0.227559186353,0.0760474836591,0.304831703007,0.0,0.227890175731,0.0767828580246,0.22823641154,0.152272369588,0.457892395806,0.0,0.227346859119,0.0,0.075424802874,0.0761527904028,0.152211797527,0.152695369404,0.0763837915596,0.0,0.0,0.0,0.153039655088,0.0,0.153062761113,0.152748259154,0.0760474836591,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_16
    y2_ETA_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00902765199907,0.0,0.00903130742547,0.0,0.0,0.0270947365183,0.00903130742547,0.0,0.00899993505085,0.00902010245598,0.0,0.00903834878921,0.0180572077457,0.0,0.0360836975903,0.0360716090817,0.0180640739416,0.0271353716164,0.0,0.036116690749,0.0270904824412,0.00903775206347,0.027063110054,0.00902516885002,0.0180785262541,0.0180868611652,0.0451340444167,0.0,0.0271006075296,0.009007729059,0.00903285698747,0.00902669146312,0.0,0.00902765199907,0.0,0.00900018144083,0.0,0.00903130742547,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights+y2_ETA_14_weights+y2_ETA_15_weights+y2_ETA_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights+y2_ETA_14_weights+y2_ETA_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights+y2_ETA_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\eta [ j_{1} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 2000.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights+y2_ETA_14_weights+y2_ETA_15_weights+y2_ETA_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y2_ETA_0_weights+y2_ETA_1_weights+y2_ETA_2_weights+y2_ETA_3_weights+y2_ETA_4_weights+y2_ETA_5_weights+y2_ETA_6_weights+y2_ETA_7_weights+y2_ETA_8_weights+y2_ETA_9_weights+y2_ETA_10_weights+y2_ETA_11_weights+y2_ETA_12_weights+y2_ETA_13_weights+y2_ETA_14_weights+y2_ETA_15_weights+y2_ETA_16_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_1.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_1.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_1.eps')

# Running!
if __name__ == '__main__':
    selection_1()