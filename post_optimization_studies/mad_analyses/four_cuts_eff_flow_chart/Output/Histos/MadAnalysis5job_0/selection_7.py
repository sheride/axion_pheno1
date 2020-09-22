def selection_7():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(120.0,2000.0,161,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([125.875,137.625,149.375,161.125,172.875,184.625,196.375,208.125,219.875,231.625,243.375,255.125,266.875,278.625,290.375,302.125,313.875,325.625,337.375,349.125,360.875,372.625,384.375,396.125,407.875,419.625,431.375,443.125,454.875,466.625,478.375,490.125,501.875,513.625,525.375,537.125,548.875,560.625,572.375,584.125,595.875,607.625,619.375,631.125,642.875,654.625,666.375,678.125,689.875,701.625,713.375,725.125,736.875,748.625,760.375,772.125,783.875,795.625,807.375,819.125,830.875,842.625,854.375,866.125,877.875,889.625,901.375,913.125,924.875,936.625,948.375,960.125,971.875,983.625,995.375,1007.125,1018.875,1030.625,1042.375,1054.125,1065.875,1077.625,1089.375,1101.125,1112.875,1124.625,1136.375,1148.125,1159.875,1171.625,1183.375,1195.125,1206.875,1218.625,1230.375,1242.125,1253.875,1265.625,1277.375,1289.125,1300.875,1312.625,1324.375,1336.125,1347.875,1359.625,1371.375,1383.125,1394.875,1406.625,1418.375,1430.125,1441.875,1453.625,1465.375,1477.125,1488.875,1500.625,1512.375,1524.125,1535.875,1547.625,1559.375,1571.125,1582.875,1594.625,1606.375,1618.125,1629.875,1641.625,1653.375,1665.125,1676.875,1688.625,1700.375,1712.125,1723.875,1735.625,1747.375,1759.125,1770.875,1782.625,1794.375,1806.125,1817.875,1829.625,1841.375,1853.125,1864.875,1876.625,1888.375,1900.125,1911.875,1923.625,1935.375,1947.125,1958.875,1970.625,1982.375,1994.125])

    # Creating weights for histo: y8_M_0
    y8_M_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.78092644877,4.19643634479,4.34791621285,4.6672559347,4.63450396322,4.58946800245,4.58946800245,4.72047988834,4.83920778492,5.04391160662,4.98249966011,5.07666357809,4.90061973143,5.29774338553,5.28136739979,5.13397952817,5.10532355313,5.01115963515,5.07666357809,5.39600329994,5.51063520009,5.44513125715,5.54339117156,5.21176746041,5.38371931064,5.33459135343,5.64574308241,5.56795515016,5.73171900752,5.21586345684,5.3427793463,5.50654320365,5.53520317869,5.42465927498,5.39190730351,5.39600329994,5.76037498256,5.37143932133,5.44513125715,5.38781530707,5.39600329994,5.62527110024,5.66211906814,5.73990700039,5.53929517513,5.28955539266,5.51473119652,5.17082749607,5.55157916443,5.72762301109,5.5843311359,5.28955539266,5.13397952817,5.36325132847,4.98659565654,5.22405144971,5.10941554956,5.20357946754,5.10941554956,5.05619559592,5.16673549964,5.20767546398,5.33459135343,4.85967576709,4.99068765298,5.00706363871,4.72047988834,4.96612367437,4.63859595966,4.78598383128,4.80645581345,4.79826782058,4.88424374569,4.79417182415,4.83101979205,4.52805605594,4.4871160916,4.63040796679,4.58946800245,4.6549719454,4.45845611657,4.43798813439,4.31926023781,4.42980014153,4.56899602028,4.44208013083,4.26603628417,4.2332843127,4.16368437332,4.44208013083,4.27831627347,4.33154022711,4.02448449457,4.01220050527,3.99992011596,3.92213258372,3.97535533736,3.75836912636,3.90575619798,3.88528581581,3.94260296589,3.72152235846,3.64782882264,3.75427512993,3.7993098907,3.40627783304,3.49225375815])

    # Creating weights for histo: y8_M_1
    y8_M_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0121240822392,0.0,0.0,0.0,0.0,0.0121313846429,0.012170493784,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0121753353338,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y8_M_2
    y8_M_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0201069897442,0.0200520625826,0.0200902467322,0.0301386860576,0.0,0.0401901996181,0.0301534291639,0.0401373219466,0.0401354749263,0.0,0.0,0.0100187051905,0.0,0.0200525088425,0.0,0.0100340928946,0.010029956726,0.0100340928946,0.0201069236316,0.010030973207,0.0,0.0100187051905,0.0,0.020059913452,0.0100546539083,0.0,0.0200717021522,0.0100355638996,0.0301035100306,0.0301212943158,0.0,0.020081296741,0.0100329193962,0.0100459435753,0.0100702895346,0.0200800364699,0.0200909202541,0.0200976843979,0.0100187051905,0.0,0.0,0.0,0.0,0.0,0.0200856932279,0.0301465658512,0.0200554012681,0.0100262833455,0.0,0.0301023365322,0.0301327565851,0.0200707931042,0.0,0.0,0.0,0.0100602900062,0.0,0.0200628802542,0.0,0.0,0.0,0.0100568562838,0.0,0.010018415948,0.0200878294908,0.0100609841883,0.0100584801742,0.010036972924,0.0100407289452,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0200899492255,0.0100546539083,0.0,0.0100329193962,0.0,0.0,0.0100696697291,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0200968290664,0.0,0.0,0.0,0.0200913995704,0.0100546539083,0.0100407289452,0.0,0.0,0.0,0.0100229529241,0.0100271593373,0.0200494552675])

    # Creating weights for histo: y8_M_3
    y8_M_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.016467068046,0.033020819304,0.0660267939506,0.022005470001,0.0605417458234,0.0549595614727,0.0330115119394,0.0385177017189,0.0495202173402,0.0274719724628,0.0439881245678,0.0329905937288,0.0550531226281,0.0330729624838,0.0384914493443,0.0329847558053,0.0770149280482,0.0769908775905,0.0550048185839,0.0494478222126,0.0384611993937,0.0550147718983,0.0495028701351,0.0660128999362,0.0494861323166,0.0494600911961,0.0604524097483,0.0549908839438,0.054978127451,0.0440215595791,0.044014409443,0.0440062842884,0.0220022768152,0.0495135140877,0.0605064014008,0.0495056326877,0.0549466424769,0.0605267142873,0.0880243500509,0.0769583363463,0.0384865458135,0.0825579491536,0.0714909198046,0.0494663881909,0.0385217805465,0.093498672974,0.0494654131723,0.027476477861,0.0385032308185,0.0275048671512,0.0440315535192,0.0605509678738,0.0385348864209,0.0440292378502,0.0660262251897,0.0109989608662,0.0495139609712,0.033022789654,0.0440291565986,0.0660339034608,0.0495150578671,0.0274811335746,0.0440349254584,0.0330179226864,0.0494890167465,0.0440275721935,0.0660108280217,0.0220213424905,0.0165016040157,0.0274971766924,0.0440586509099,0.0329953266314,0.0274735812434,0.0604587473689,0.0659462736683,0.0330062224637,0.0385075696511,0.0385122172395,0.0549511113119,0.0384953697315,0.0330256943968,0.0385095725017,0.0550025435406,0.0329908252958,0.0439449799968,0.0440170501182,0.0164954248356,0.0164961114112,0.00551630153443,0.0384828529308,0.0275246153395,0.0110027024999,0.0495168047753,0.0110260298188,0.0109935170126,0.0329819810649,0.0219834630197,0.0219787341797,0.0165017908942,0.021995618251,0.0165183743348,0.0110160968173,0.027530579203,0.0110268870226,0.0110078538479,0.0275157670462,0.00549901933056])

    # Creating weights for histo: y8_M_4
    y8_M_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00197027550081,0.00394952315682,0.00394805331706,0.00197208323937,0.00394731619262,0.00591465602221,0.0049318955883,0.00789053831836,0.00295908284024,0.00690804643985,0.00492704555802,0.00789948081221,0.00887485797688,0.00690768569379,0.00592003915499,0.00690746924616,0.00887773592873,0.00987371970967,0.0118414852196,0.00691111278131,0.00986770326714,0.0118350198487,0.0138150146498,0.00887579992491,0.0167695168168,0.010855918983,0.00690918479406,0.0108539148383,0.0177644183596,0.020733422518,0.0167638170292,0.0138102888765,0.0138146498955,0.0167698214468,0.0118430484525,0.0236884617958,0.0167671719675,0.0128264021133,0.0236846138379,0.0207369417962,0.0384858120008,0.0246552251464,0.019740096233,0.0226995726873,0.0286270632524,0.0227092967976,0.0315806274797,0.0295947725593,0.0187597087065,0.0404452843598,0.0345472547224,0.0375002056814,0.0246604319144,0.0217110002336,0.0286303580664,0.0315931173097,0.025667294193,0.035510599002,0.037488389244,0.0236896803158,0.0296010094577,0.0355199463331,0.0365179222339,0.0355182428101,0.0305913575837,0.0236793028543,0.0315771522927,0.0325532148749,0.0463906599127,0.0305928967668,0.0246773148297,0.0296191028765,0.0463764705679,0.0305930891647,0.0414399413969,0.0256571492123,0.0345520326035,0.0404506955506,0.031575536952,0.0424380054801,0.0404769899297,0.0434100557645,0.0286233796344,0.0266487839992,0.0296034024066,0.0375073364284,0.0355257543446,0.0246621955618,0.0325592032594,0.0305981436178,0.0315898305124,0.0345392982678,0.0236820525409,0.0286232834354,0.0365091601131,0.0355226399037,0.0305958508762,0.0246805214613,0.0345343841049,0.0325702020057,0.0404531806901,0.0236774911075,0.0325773407693,0.0197404609873,0.0266355245775,0.0226978972223,0.0365152527131])

    # Creating weights for histo: y8_M_5
    y8_M_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000251938705986,0.0,0.000252305648909,0.0002524496493,0.000252082346275,0.000505256118684,0.000251550317047,0.0,0.00100821879408,0.000252565441778,0.000504063784247,0.00100804954661,0.00176381272972,0.0012601130476,0.000504233431831,0.000503640065399,0.000503908940815,0.0010087493429,0.0005055806097,0.000757268405308,0.00176452332904,0.000504453493556,0.000504129402652,0.00277454102769,0.00176529874653,0.00100816998039,0.00151229698237,0.00226877236524,0.00151225977193,0.00125991859306,0.00176589811465,0.0017634390249,0.00226803415819,0.0030252505489,0.00227000351057,0.00100852648038,0.00126088086296,0.00151354973375,0.00151175403008,0.00403113468814,0.00251986759464,0.00353011215693,0.00302553582892,0.00302505929526,0.00378131901764,0.00226734436471,0.00151308280278,0.0015113947293,0.00353056508397,0.00579873448009,0.00403280715725,0.00352975885784,0.00403183088342,0.00428482584567,0.00504358666959,0.0035289166216,0.00428863091295,0.00327555475643,0.00428580612063,0.00554881237974,0.00579692597282,0.0025199840273,0.00504172214661,0.00453653644768,0.00428524196239,0.00605145336491,0.00630244776603,0.00302364129753,0.00378220246544,0.00378109975614,0.00655375025356,0.00403377942996,0.00579619776857,0.00554580753691,0.00655393030406,0.00604913671511,0.00529495317508,0.0047889152371,0.00479140393515,0.00579921061364,0.00857274455886,0.00806881121119,0.00756044061894,0.00781866104687,0.00806541425839,0.00831917743612,0.00755932830694,0.00881756522831,0.00781524408846,0.00831736892885,0.00957568187154,0.00781375567097,0.00604803240537,0.0100857049273,0.00831910941704,0.0133673373885,0.0131095930941,0.0141151511418,0.00957541379635,0.0146184042987,0.00882085415082,0.00957963498034,0.0108400685178,0.0103367473419,0.00932927675767,0.0136076367897])

    # Creating weights for histo: y8_M_6
    y8_M_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000571674400031,0.0,0.000286439425776,0.0,0.00114685418586,0.0,0.000570006782515,0.0,0.0002863152617,0.000284909568403,0.000574595954751,0.000286450322624,0.000286764731657,0.0,0.000574212165791,0.000284852384948,0.0002863152617,0.000287128726344,0.0,0.000286439425776,0.000287128726344,0.0,0.000570397169566,0.0,0.0,0.0,0.0002863152617,0.000573312626051,0.00114767194926,0.000855710321202,0.0,0.00114175666071,0.0,0.000287276383623,0.000573726606275,0.000284468995872,0.000284540475191,0.00114194260691,0.0002863152617,0.00085747571043,0.000286183799735,0.000860014575872,0.00114628535044,0.000287772740014,0.000574099498388,0.00171888568258,0.0,0.000573215054281,0.000859751651942,0.000855365820875,0.000287128726344,0.00114753198976,0.000861860741729,0.00114346816553,0.000858949384059,0.00143494383419,0.000858809024669,0.00143481187237,0.00114442988728,0.000859505523154,0.000859800337856,0.00114721908029,0.000287772740014,0.000286823114765,0.0017229295126,0.000572128768571,0.00171794695418,0.00114786489344,0.000574257552659,0.00057395194108,0.000571234027442,0.000287772740014,0.00142779090371,0.000858079435757,0.00315403945603,0.00200631252267,0.00143411307455,0.00171937953969,0.00114571851444,0.00171905863254,0.00114306128325,0.00142758196417,0.00114167868327,0.00257856595517,0.00257476605458,0.00171679028883,0.00286293168092,0.000573893557972,0.00171545767439,0.00171991238553,0.00171669531631,0.00171834183993,0.00401011677105,0.00171878471179])

    # Creating weights for histo: y8_M_7
    y8_M_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.16142075517e-05,0.0,0.0,0.0,0.0,0.0,0.0,2.15983699309e-05,0.0,0.0,2.16751901451e-05,0.0,6.48229754557e-05,2.15259544109e-05,2.1608621008e-05,0.0,0.0,4.31871677194e-05,4.31500777633e-05,0.0,6.48842053155e-05,0.0,4.32972641202e-05,4.32010816917e-05,2.1608621008e-05,0.0,4.31777380696e-05,0.0,4.32343997878e-05,2.16142075517e-05,2.1655333398e-05,4.32154985786e-05,0.0,6.48049962567e-05,6.4709107195e-05,2.15933994577e-05,0.000108047903684,6.47796409759e-05,0.0,2.15259544109e-05,0.0,4.32198571723e-05,8.64498145473e-05,0.0,6.47386953407e-05,4.32177616945e-05,6.47944350488e-05,0.000129524958026,4.32275685304e-05,4.31157957474e-05,4.31698590732e-05,2.15789867617e-05,6.48095224886e-05,2.15259544109e-05,2.15774067715e-05,4.31813003817e-05,6.47836642932e-05,4.32141155632e-05,0.0,4.32269817966e-05,6.47637991641e-05,2.15912704523e-05,4.3124303387e-05,6.48629571711e-05,4.31932026953e-05,6.48075108299e-05,6.48050381662e-05,6.47414194618e-05,8.64146943402e-05,4.31736728427e-05,6.47325765457e-05,4.31823481206e-05,4.32195218958e-05,8.63922308188e-05,8.64066477057e-05,8.63133570364e-05,0.000108139434152,0.000151167974206,4.31120238874e-05,8.64006965489e-05,0.000107929760649,0.00015134743092,0.000108003270008,0.000108111270931,6.48057087191e-05,6.48629571711e-05])

    # Creating weights for histo: y8_M_8
    y8_M_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.83974019316e-05,0.0,0.0,0.0,0.0,0.0,0.0,2.83974019316e-05,0.0,0.0,2.83974019316e-05,0.0,0.0,0.0,0.0,0.0,0.0,2.84292668315e-05,0.0,0.0,0.0,2.83684918849e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.84489114087e-05,0.0,0.0,2.83974019316e-05,0.0,2.83498718548e-05,0.0,0.0,2.67506280594e-05,0.0,0.0,0.0,2.82532080623e-05,0.0,0.0,2.84292668315e-05,0.0,0.0,2.84080928579e-05,5.67658938165e-05,2.84080928579e-05])

    # Creating weights for histo: y8_M_9
    y8_M_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y8_M_10
    y8_M_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0521138287,0.0,0.0,0.0,0.0,0.0,1.0529581672,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.05462838872,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y8_M_11
    y8_M_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.230020174047,0.230597155343,0.230551273514,0.0,0.0,0.23018625551,0.460704673945,0.461024770794,0.690790519723,0.229982515595,0.92256484756,0.691531007872,0.459685974368,0.229952465686,0.921662581772,0.230020174047,0.23018625551,0.461233045094,0.0,0.0,0.0,0.691049133384,0.229982515595,0.229952465686,0.0,0.230128538167,0.230465312331,0.461073957345,0.460063327437,0.460617444671,0.690580324073,0.229703305066,0.0,0.229479006709,0.690811654569,0.459964954335,0.230673163934,0.230114128045,0.0,0.229932022526,0.23042826871,0.230619673561,0.0,0.0,0.230673163934,0.460930624662,0.230673163934,0.0,0.0,0.0,0.230752246685,0.0,0.230645227511,0.0,0.230020174047,0.460488714246,0.460933698821,0.23058774073,0.230551273514,0.0,0.0,0.229952465686,0.0,0.0,0.230764043772,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.23018625551,0.0,0.0,0.0,0.0,0.230645227511,0.0,0.230645227511,0.0,0.0,0.0,0.0,0.0,0.0,0.23042826871,0.0,0.229952465686,0.0,0.0,0.0,0.0,0.230020174047,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y8_M_12
    y8_M_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.1384016717,0.138443216656,0.193985782999,0.0830623678981,0.193914271821,0.0553889654108,0.249327202516,0.0553995439874,0.0,0.110761389775,0.0830144373293,0.166014641665,0.13852719132,0.138417289526,0.0554480900371,0.276708559354,0.0830847175454,0.13863259241,0.110806050602,0.193944199576,0.221602676653,0.138488839171,0.166332229768,0.110769506428,0.0276929401566,0.0831032973727,0.221554361409,0.0553778482885,0.138307541602,0.138455103129,0.138503572244,0.304717206551,0.166303263702,0.165999177709,0.0830418646933,0.249127940601,0.138598702498,0.138450871698,0.138508919233,0.22168095812,0.0554508597007,0.0830207844753,0.13835108687,0.166090538143,0.110701880473,0.166112079972,0.138369743633,0.166070535017,0.0,0.138488146755,0.138542616808,0.16611227231,0.0829216535957,0.0554893657195,0.0831335713355,0.166173281846,0.16598894534,0.0831337636732,0.0553688468815,0.0554876731473,0.138561735181,0.138537539091,0.166128851824,0.0552076293743,0.0830163607069,0.193842375968,0.166046800537,0.083064522081,0.0277373240172,0.0830550590634,0.0830507506977,0.193846491996,0.0,0.055405237185,0.138359819005,0.0830155913558,0.138498263721,0.0277244643148,0.0553541522769,0.055427009819,0.027640512731,0.027640512731,0.0276622122767,0.0554012365597,0.0553334567344,0.0553302254601,0.0,0.0,0.027683115544,0.0552821025535,0.055481095196,0.0277205483181,0.110737001347,0.055328263615,0.0277631934454,0.0,0.0554069297572,0.0,0.11093630173,0.0,0.0554069297572,0.110733231527,0.0,0.083088948976,0.0,0.0])

    # Creating weights for histo: y8_M_13
    y8_M_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0100450214151,0.0202018191175,0.020154633721,0.0201706251705,0.0201565514812,0.0100975170653,0.0100829700048,0.0201646655487,0.0302947299171,0.0100796988885,0.0100533236174,0.0503771563265,0.0202008723751,0.0403626188016,0.0,0.0100953565507,0.0100671484834,0.0302972606322,0.0705522117657,0.0302903906813,0.0403309818277,0.0,0.0,0.0201751586099,0.0302794424555,0.02018709606,0.0,0.0504437620791,0.0302832415627,0.0100671484834,0.020144614031,0.0,0.0605195101389,0.0302102088859,0.0201372160891,0.0302955856265,0.0504043630316,0.0504252520522,0.0504063475493,0.0201157626644,0.0201972128518,0.0202033970214,0.0100921886051,0.0504656221175,0.0302368026361,0.0100996957865,0.0403580307424,0.0100796988885,0.0302258301349,0.0201121759674,0.0302450805629,0.0201806145162,0.0403226614188,0.0302305820533,0.0201734168467,0.0403646943521,0.0201509438533,0.0201718874936,0.0201687620301,0.0502923379211,0.0302623282667,0.0503909447793,0.0302358741003,0.0100712388959,0.0100953565507,0.0201602656243,0.0100533236174,0.0201530679548,0.0100671484834,0.0302263702635,0.0,0.0201717114967,0.0201792186781,0.0,0.0100796988885,0.0403124111121,0.0201975648457,0.0403432834095,0.0201530679548,0.0100712388959,0.0,0.0201997435669,0.0100450214151,0.0,0.0302386839831,0.0201514657754,0.0504735844635,0.0302405653301,0.0201426537888,0.0,0.0403559794673,0.0302626923983,0.0504655614288,0.0503821024484,0.0201326462365,0.0100592771703,0.0201847413418,0.010103349241,0.0302577523452,0.0302652049069,0.0201010760201,0.0,0.0100733690662,0.0201624868275,0.0100953565507,0.0302478176193])

    # Creating weights for histo: y8_M_14
    y8_M_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00283355094161,0.0,0.0,0.0028258606674,0.0,0.0,0.00849404406756,0.0,0.0,0.00283301960937,0.00566026189448,0.00848628376984,0.00566853005501,0.00849465581141,0.00282513619339,0.00565291712087,0.00848269410312,0.0,0.00849725668462,0.0112963041191,0.00566429016999,0.011320377586,0.00848864225398,0.00849404406756,0.00566748354982,0.00283250443641,0.00848682241222,0.0113195465378,0.00848361364261,0.0056608043843,0.022631921437,0.00565841896805,0.00283102971052,0.011334166831,0.00848161297091,0.00849407099968,0.0141481000323,0.0113287688648,0.0282809334006,0.0,0.0113106320064,0.00283301960937,0.0112983047908,0.00565440992976,0.0084840176244,0.00847707683258,0.0113231939162,0.0113078195237,0.0169835481493,0.00566144306027,0.00283201542608,0.0169662769662,0.00282930990235,0.0113075271178,0.00565759946214,0.0113145871804,0.0084839753025,0.0113278685626,0.0169713017301,0.0113231708315,0.00848760729112,0.0113201275021,0.0056624587859,0.00566242031144,0.00283198118381,0.00566600997816,0.0141461686146,0.0056529363581,0.00849297063025,0.005657891868,0.00283622837898,0.0113069038316,0.00565444840421,0.0141587343719,0.0141420480004,0.0113181922369,0.00566055430034,0.00849807234308,0.00566200863477,0.005657891868,0.00849126621186,0.0113077156426,0.00283250443641,0.00282930990235,0.0113202198408,0.0,0.00564705746127,0.0084891001,0.0,0.00565548336707,0.00565157051492,0.0169864991401,0.0028258606674,0.00282544052634,0.00282513619339,0.00848646459978,0.00565943084623,0.00283102971052,0.00282347986807,0.00564901581106,0.00848026636496,0.0084916663462,0.0028309785395,0.0169567814705])

    # Creating weights for histo: y8_M_15
    y8_M_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00151881882101,0.0,0.0,0.0,0.0,0.00152260679112,0.0,0.00152162936482,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00303299398069,0.0,0.0,0.00151115660254,0.0,0.0,0.0,0.0,0.00151448717969,0.00152495994197,0.0,0.00151265406217,0.00150849615926,0.00153629548684,0.0,0.0,0.0,0.0,0.00151115660254,0.0,0.0030566070399,0.0,0.0,0.0,0.0,0.00153821488261,0.0,0.0,0.0,0.00152162936482,0.00152162936482,0.0,0.0,0.0,0.0,0.0,0.0,0.00304287815979,0.00150849615926,0.0,0.0030419007335,0.0,0.0,0.0,0.0,0.0,0.00152449663954,0.0,0.0015356572641,0.0,0.0,0.00304599008656,0.0,0.0,0.0,0.00153153127233,0.0])

    # Creating weights for histo: y8_M_16
    y8_M_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180734341243,0.0,0.0,0.0,0.000180766987918,0.0,0.0,0.0,0.0,0.000180657151876,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000180003640899,0.0,0.0,0.0,0.000361281541581,0.0,0.0,0.0,0.000180970259668,0.0,0.0,0.0,0.0,0.000180154593273,0.0,0.0,0.0,0.0,0.0,0.000180970259668,0.0,0.0,0.000180003640899,0.0,0.0,0.0,0.000361441117605,0.0,0.0,0.0,0.000180003640899,0.0,0.0,0.000180657151876,0.0,0.000180612801676,0.0,0.0,0.000180503389116,0.0,0.0,0.0,0.0,0.0,0.000180766987918,0.0,0.0,0.0,0.0,0.0,0.000361110724014,0.00018054716184])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights+y8_M_11_weights+y8_M_12_weights+y8_M_13_weights+y8_M_14_weights+y8_M_15_weights+y8_M_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights+y8_M_11_weights+y8_M_12_weights+y8_M_13_weights+y8_M_14_weights+y8_M_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights+y8_M_11_weights+y8_M_12_weights+y8_M_13_weights+y8_M_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights+y8_M_11_weights+y8_M_12_weights+y8_M_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights+y8_M_11_weights+y8_M_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights+y8_M_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"M [ j_{1} , j_{2} ]   ( GeV ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights+y8_M_11_weights+y8_M_12_weights+y8_M_13_weights+y8_M_14_weights+y8_M_15_weights+y8_M_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights+y8_M_4_weights+y8_M_5_weights+y8_M_6_weights+y8_M_7_weights+y8_M_8_weights+y8_M_9_weights+y8_M_10_weights+y8_M_11_weights+y8_M_12_weights+y8_M_13_weights+y8_M_14_weights+y8_M_15_weights+y8_M_16_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_7.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_7.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_7.eps')

# Running!
if __name__ == '__main__':
    selection_7()