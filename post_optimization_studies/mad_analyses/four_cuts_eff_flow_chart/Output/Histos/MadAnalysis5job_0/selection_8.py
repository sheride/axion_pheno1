def selection_8():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(2.4,8.0,101,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([2.428,2.484,2.54,2.596,2.652,2.708,2.764,2.82,2.876,2.932,2.988,3.044,3.1,3.156,3.212,3.268,3.324,3.38,3.436,3.492,3.548,3.604,3.66,3.716,3.772,3.828,3.884,3.94,3.996,4.052,4.108,4.164,4.22,4.276,4.332,4.388,4.444,4.5,4.556,4.612,4.668,4.724,4.78,4.836,4.892,4.948,5.004,5.06,5.116,5.172,5.228,5.284,5.34,5.396,5.452,5.508,5.564,5.62,5.676,5.732,5.788,5.844,5.9,5.956,6.012,6.068,6.124,6.18,6.236,6.292,6.348,6.404,6.46,6.516,6.572,6.628,6.684,6.74,6.796,6.852,6.908,6.964,7.02,7.076,7.132,7.188,7.244,7.3,7.356,7.412,7.468,7.524,7.58,7.636,7.692,7.748,7.804,7.86,7.916,7.972])

    # Creating weights for histo: y9_sdETA_0
    y9_sdETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,9.77257965601,16.7939336611,16.1388782204,14.7755473844,14.0754599821,13.5432284366,13.1788567477,12.5934012475,12.1635216146,11.5002821809,10.689654873,10.243399254,9.8544595861,10.0509754183,8.90872839358,8.86369243203,8.03668513815,7.68050144226,7.80332533739,7.50854958908,6.94356607147,6.82893016935,6.5054984455,6.00192687546,5.77265907121,5.91185895236,5.69487113763,5.28136749068,5.02753570741,4.84329986471,4.49120816533,4.54443211989,4.12274447993,4.22918838905,3.93032064423,3.67648726095,3.50044181127,3.35714873361,3.38171351264,3.31620796857,3.01324582724,3.05009259578,2.85357636357,2.62840175583,2.45645030264,2.33362800751,2.4196035341,2.28040485295,2.2271816984,2.00200709065,2.02657146968,1.89146678503,1.7686440899,1.7686440899,1.76045609689,1.66629217729,1.52299909964,1.38380041849,1.34285965344,1.3019188884,1.3019188884,1.2118489653,1.08493227367,1.0194267296,0.986674357561,0.89251043796,0.908886823977,0.798346518359,0.773781739332,0.720558584775,0.642771051191,0.626394665174,0.700088202253,0.593642293138,0.597736289643,0.532230745573,0.491289980529,0.462631604998,0.405314453936])

    # Creating weights for histo: y9_sdETA_1
    y9_sdETA_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0121753363378,0.0,0.0,0.0,0.0,0.012124083239,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_2
    y9_sdETA_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0201171477175,0.0200587248488,0.0200523367198,0.0100184166588,0.0100609849022,0.0100407296577,0.0100369736362,0.0100184166588,0.0,0.0200856533328,0.0100702902491,0.0100367009218,0.0201104001013,0.0,0.0200884383256,0.0100309739187,0.0301231641338,0.010026284057,0.0200909423399,0.0,0.0,0.0100696704436,0.0,0.0,0.0100584808879,0.0,0.0200730712806,0.0200691458456,0.0100355646117,0.0100369736362,0.030120717968,0.0200670137146,0.0100329201081,0.0300712120348,0.0200818146706,0.0301384154817,0.0,0.0200591463165,0.0,0.0,0.0,0.0301656249442,0.0,0.0,0.0100153630836,0.0,0.0301271639454,0.0,0.0100153630836,0.0100355646117,0.0100407296577,0.0100532497293,0.0100584808879,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_3
    y9_sdETA_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0330022164742,0.0275039081427,0.0550204184001,0.0715304886826,0.0769084065992,0.0494438404549,0.0550100182023,0.0220258070706,0.0824719842972,0.0770172836701,0.0825303229068,0.0825615235003,0.0825312572996,0.0769656076872,0.0715463733598,0.0714786095709,0.115504068839,0.0824571152644,0.0880289399942,0.0879879485895,0.0385030923545,0.0879697482433,0.049491900744,0.0550275279103,0.0494987258738,0.0549652079749,0.0770483623863,0.0825302010295,0.0385245346374,0.0824432212501,0.0605180198431,0.0770323152061,0.0605063602464,0.0549869427634,0.0494744316617,0.0440079495606,0.0330035611873,0.0275322039934,0.0494630158196,0.0330570084539,0.0440075026771,0.066062665931,0.038471546442,0.0440181060038,0.0440188778934,0.0385077846313,0.0275095469999,0.0220166256459,0.0164932146495,0.0109798097808,0.0275078000917,0.0109969254189,0.00550043305941,0.0110251603309,0.0329898540515,0.0109818491946,0.0,0.0110268016121,0.00549598047472,0.00549710580862,0.0164732308318,0.0,0.0,0.0,0.0,0.00551630148624,0.0,0.00550877759313,0.0,0.00550972823621,0.0,0.0,0.0,0.0055142173841,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_4
    y9_sdETA_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0296093014719,0.0740006369071,0.0690581355745,0.0888119874986,0.0720588612207,0.0789811769054,0.0838799077184,0.0710551454879,0.0601752453266,0.077949483313,0.0740170308104,0.0740067695897,0.0631542861275,0.0740218808405,0.0572309163113,0.0631653089231,0.0740184337117,0.0513123564424,0.0621738986386,0.0493443264609,0.051313999841,0.0453781241622,0.0414593399262,0.0513091898938,0.065142958799,0.0444205037567,0.041453808487,0.0325669460243,0.042433755064,0.0384886884749,0.0315847507969,0.0286149972024,0.0226927857819,0.0246686199027,0.0355274524953,0.0187439433842,0.0207170117854,0.0236953751854,0.0148018309044,0.0148078914379,0.0187456388906,0.0148004199865,0.0108518461443,0.00789990939587,0.00789927608616,0.00986936232006,0.0108550167011,0.00493783568374,0.00986433191694,0.008879302829,0.00295951281608,0.0049387896566,0.00394801709087,0.00492756243817,0.00296082432835,0.000985635542116,0.000986290496594,0.0,0.00098390877107,0.00098843853885,0.0,0.00295772712318,0.0,0.0,0.0,0.0,0.00098843853885,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_5
    y9_sdETA_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0201671319655,0.0428538185517,0.0403297906764,0.0448718245108,0.0365551920727,0.0365467697107,0.0385565893739,0.0315090888698,0.0347782857311,0.0337771409555,0.036802737498,0.0320161310721,0.0254569835288,0.0282317257181,0.0289833005007,0.0272193457915,0.0249607083461,0.0214284016944,0.0196592495275,0.0156289432094,0.0191617219936,0.0186539315814,0.0146188279179,0.0153784369538,0.00983065305213,0.0120966285554,0.0100824636736,0.0118483629282,0.0100814233818,0.00831780876795,0.00907660557603,0.00831757270175,0.00604913650832,0.00781191088655,0.00503999348949,0.00554363473801,0.00176407834393,0.00353036090605,0.0047911036872,0.00327789970214,0.00100902818662,0.00176440083438,0.00151199444584,0.001512697443,0.00176417917221,0.00252110865659,0.0015116163398,0.000504345446014,0.00125959645965,0.0,0.000755526690956,0.000252130791247,0.0,0.0,0.0,0.0,0.0,0.000252082337658,0.0,0.0,0.000252305640284,0.0,0.000251938697373,0.00025204864821,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_6
    y9_sdETA_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00915122635347,0.0203298959025,0.0157372951425,0.0223471320523,0.0163174972141,0.0154613350138,0.0169053470723,0.0174656648991,0.0131724974739,0.0146018837655,0.0131663592504,0.0128770829759,0.00657674148862,0.00829787034096,0.00859625497926,0.010589944944,0.00687304272992,0.00802061058846,0.00715655367313,0.00486842592771,0.00572404628485,0.00372574165571,0.00688230404941,0.00429771210985,0.00457190974862,0.00371865370718,0.003434385983,0.00229007518177,0.00142972019498,0.00142837658386,0.00257383105408,0.00143290427341,0.000856673752252,0.00114437378301,0.0,0.000573715749006,0.0,0.000574087941282,0.000575049063104,0.0,0.000287772709722,0.00114313714093,0.00028645029247,0.0,0.000287772709722,0.0,0.000284774877387,0.0,0.0,0.000285168763384,0.0,0.0,0.0,0.0,0.000286315231561,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_7
    y9_sdETA_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00140389688565,0.00259179741679,0.00200890729009,0.00215963497413,0.00209495680919,0.00164173733398,0.00151016608455,0.00162028718988,0.00127460593465,0.000993968714699,0.000991965857471,0.0010153819784,0.000907562964458,0.000689484124594,0.000647966013243,0.000604451750192,0.000540240038499,0.000453415611888,0.00038733477633,0.000345491404989,0.000345496937049,0.000453389208874,8.64175687333e-05,0.000151208596088,0.00010804980981,8.65558283272e-05,8.47878321979e-05,0.000172854876863,4.31711495939e-05,8.63901179803e-05,2.16093752284e-05,6.47789154957e-05,6.48255608209e-05,2.16086166656e-05,0.0,2.16292026349e-05,0.0,8.63666486343e-05,0.0,2.16142032082e-05,0.0,2.15594567675e-05,0.0,4.31896317039e-05,2.15977872388e-05,0.0,2.16179960221e-05,0.0,0.0,0.0,2.15983655905e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_8
    y9_sdETA_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000311623078096,0.000595840713515,0.000197899555997,0.00022722862267,0.000226966843503,0.000311130107686,0.000142046439134,0.000198629508568,5.67977491387e-05,0.000170206349267,8.38794498328e-05,5.66030703722e-05,8.51951462817e-05,5.68173937126e-05,5.6826674029e-05,5.68373649536e-05,2.8397397143e-05,5.54501877952e-05,8.52544066704e-05,0.0,0.0,5.67472642172e-05,0.0,2.84292620376e-05,0.0,0.0,2.83684871011e-05,0.0,2.82164086993e-05,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_9
    y9_sdETA_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_10
    y9_sdETA_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0529581672,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0521138287,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_11
    y9_sdETA_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.230597157197,0.230360177931,0.230752248541,0.0,0.230360177931,0.230673165789,0.230428270563,0.691270862689,0.691406894245,0.690634127415,1.15196093808,0.690050421391,0.229952467535,0.46069776079,0.0,0.229982517444,0.230020175897,0.0,0.230186257361,0.459905011924,0.0,0.0,0.0,0.0,0.0,0.230673165789,0.0,0.230645229365,0.230364750743,0.460542515738,0.0,0.0,0.0,0.230465314184,0.0,0.0,0.229952467535,0.0,0.0,0.0,0.0,0.0,0.230838555567,0.0,0.0,0.0,0.0,0.0,0.0,0.230619675415,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_12
    y9_sdETA_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.360014592208,0.359811868228,0.471038591634,0.166185232799,0.24926001949,0.41523641197,0.332284298291,0.387679414358,0.415254491718,0.166084832498,0.332301147077,0.249093339603,0.249225244827,0.221683057221,0.304753497079,0.193884444938,0.110851626342,0.11081792877,0.138595883979,0.0553199120103,0.138550723077,0.110744148012,0.0554613956532,0.055246862136,0.055310487461,0.0277261663494,0.0830030831809,0.0554117725158,0.0554148883872,0.0554893615608,0.0553793443725,0.0829041831141,0.0553739204482,0.0276831134693,0.0,0.0554152730627,0.0,0.0553883842464,0.0552968314813,0.0,0.0,0.0277179112135,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_13
    y9_sdETA_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.120976979278,0.100886136205,0.0806370779249,0.131164048031,0.0706847527166,0.0706249137468,0.090728197985,0.0605411066643,0.14114865958,0.120910828693,0.0907840921951,0.0705687160937,0.0604932840393,0.0705420737937,0.0403480032828,0.040296939886,0.0403336018755,0.0403599468013,0.0201252656529,0.0100975166396,0.0302539823071,0.0201326453879,0.0201648285579,0.0302323407486,0.0101000473547,0.0201328456603,0.0100733686416,0.0,0.0100796984637,0.0100795224667,0.0,0.0403436337028,0.0100733686416,0.0,0.0,0.0101000473547,0.0100829695798,0.0,0.0100795224667,0.0100450209917,0.0,0.0,0.0,0.0,0.0,0.0100126436181,0.0100921881797,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_14
    y9_sdETA_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0311313336855,0.0593782688248,0.0537670784589,0.050937244374,0.0537533815556,0.0480915972913,0.0452789612844,0.0424463570394,0.0282997644031,0.0367983466273,0.0367745732662,0.0311056519918,0.0254442370822,0.00848934450933,0.0197930948501,0.0226399154035,0.00848375032467,0.0141540874587,0.0226202357236,0.011323614698,0.0141496513549,0.0,0.00283441331359,0.00565998366018,0.0113144462371,0.00848643199365,0.00283012110423,0.00566720531396,0.00282586005918,0.00566538932004,0.0,0.0,0.00283441331359,0.0,0.0,0.0,0.00283102910119,0.0,0.0,0.0,0.00282142741808,0.0,0.0,0.00282586005918,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_15
    y9_sdETA_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00304479137218,0.00610266039974,0.00456237615939,0.00761276616271,0.00303360356507,0.00152495980478,0.00306990779824,0.00608260720691,0.00456272127239,0.0015244965024,0.00153565712596,0.00152495980478,0.00306963123508,0.0,0.0,0.0,0.0,0.00152094963898,0.00151265392609,0.0,0.0,0.00151881868438,0.0,0.0,0.0,0.0,0.00153821474423,0.0,0.0,0.0,0.0,0.0,0.00152260665414,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y9_sdETA_16
    y9_sdETA_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000360556647444,0.000902637331643,0.000361270331388,0.000361288849134,0.00054152973313,0.000361627365852,0.000360629717469,0.000180547139028,0.0,0.000541688346672,0.0,0.0,0.000361042805651,0.000181168426734,0.0,0.0,0.0,0.000360556647444,0.0,0.000181168426734,0.0,0.0,0.0,0.0,0.000180755030564,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights+y9_sdETA_14_weights+y9_sdETA_15_weights+y9_sdETA_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights+y9_sdETA_14_weights+y9_sdETA_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights+y9_sdETA_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights+y9_sdETA_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y9_sdETA_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\Delta\eta ( j_{1} , j_{2} ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights+y9_sdETA_14_weights+y9_sdETA_15_weights+y9_sdETA_16_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y9_sdETA_0_weights+y9_sdETA_1_weights+y9_sdETA_2_weights+y9_sdETA_3_weights+y9_sdETA_4_weights+y9_sdETA_5_weights+y9_sdETA_6_weights+y9_sdETA_7_weights+y9_sdETA_8_weights+y9_sdETA_9_weights+y9_sdETA_10_weights+y9_sdETA_11_weights+y9_sdETA_12_weights+y9_sdETA_13_weights+y9_sdETA_14_weights+y9_sdETA_15_weights+y9_sdETA_16_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_8.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_8.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_8.eps')

# Running!
if __name__ == '__main__':
    selection_8()
