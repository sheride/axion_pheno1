def selection_3():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,1000.0,101,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([5.0,15.0,25.0,35.0,45.0,55.0,65.0,75.0,85.0,95.0,105.0,115.0,125.0,135.0,145.0,155.0,165.0,175.0,185.0,195.0,205.0,215.0,225.0,235.0,245.0,255.0,265.0,275.0,285.0,295.0,305.0,315.0,325.0,335.0,345.0,355.0,365.0,375.0,385.0,395.0,405.0,415.0,425.0,435.0,445.0,455.0,465.0,475.0,485.0,495.0,505.0,515.0,525.0,535.0,545.0,555.0,565.0,575.0,585.0,595.0,605.0,615.0,625.0,635.0,645.0,655.0,665.0,675.0,685.0,695.0,705.0,715.0,725.0,735.0,745.0,755.0,765.0,775.0,785.0,795.0,805.0,815.0,825.0,835.0,845.0,855.0,865.0,875.0,885.0,895.0,905.0,915.0,925.0,935.0,945.0,955.0,965.0,975.0,985.0,995.0])

    # Creating weights for histo: y4_PT_0
    y4_PT_0_weights = numpy.array([0.0,0.0,3857.85473566,3520.70702093,3273.42523017,3008.12745466,2792.16563739,2528.30186066,2301.49005258,2079.59024034,1852.16363278,1616.13963249,1433.33878717,1216.5569706,1099.46626968,958.01558937,822.501504036,764.774952882,664.674637582,570.101117606,504.391173207,407.566055136,377.269880771,333.872517492,288.837555599,251.78618695,221.694612412,198.563071985,175.636211384,161.102203683,134.081246546,115.862581962,100.1003553,92.7310015352,82.4957901957,71.8511792027,61.6159678633,51.9948760043,49.9478177364,38.689087263,38.8938070898,31.3197334986,27.2256569629,26.4068376557,20.8798223324,18.423378411,13.3057727412,11.6681401269,13.1010689145,9.00698437869,6.34583063044,9.62109785906,7.57405559117,5.3223094965,3.07056340183,2.04704226788,2.86585957504,3.27526722862,2.86585957504,3.27526722862,2.86585957504,1.43292938752,2.04704226788,1.8423378411,1.02352093394,0.818816707154,0.818816707154,0.0,0.0,0.614112680365,0.409408453577,0.409408453577,0.614112680365,0.0,0.204704226788,0.0,0.204704226788,0.204704226788,0.204704226788,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_1
    y4_PT_1_weights = numpy.array([0.0,0.0,0.608524689202,1.21277334411,0.60876676669,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_2
    y4_PT_2_weights = numpy.array([0.0,0.0,6.02584410478,9.53337094592,8.53444695023,11.5484887846,11.0432997839,7.5304136912,3.51432817349,0.502297194805,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_3
    y4_PT_3_weights = numpy.array([0.0,0.0,9.90397473038,15.6752377129,22.2742996002,23.3804581861,27.7747857023,27.5032633389,33.2802890875,25.0263708111,24.2030082408,21.7198390308,21.731336125,14.5758941006,14.0242346784,8.80121652174,6.60138365029,3.29557297757,1.37477701896,1.09896335506,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_4
    y4_PT_4_weights = numpy.array([0.0,0.0,5.37849301162,7.64632701381,10.5098910175,12.0399753138,13.0767734679,13.6185057994,13.323652026,13.0256116626,11.7419770374,11.0032473048,12.0394963232,10.8542832391,10.3122001823,10.8555779166,9.96726483754,10.4620039846,8.3887323478,8.48655264542,7.6478922508,5.37838478781,4.83549205657,3.84885563961,2.56595453141,2.02362296067,1.28280490926,0.987077328785,0.345672268766,0.197468214845,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_5
    y4_PT_5_weights = numpy.array([0.0,0.0,1.32347109385,1.84055695996,2.31923665139,2.91214698971,3.05017371249,3.15125807125,3.13861852528,3.51644852379,3.1634134814,3.46639648191,3.23892266516,3.28913875306,3.08787028809,3.41521812405,3.10037179534,3.03742613621,2.89868121195,2.82304999395,2.73492927208,2.74772086071,2.25584686767,2.43266447306,2.28117997476,2.20575481457,2.02907924904,2.01625365088,1.8778872328,1.86598169276,1.73952781669,1.37418112032,0.920049315689,0.869443918573,0.605087354531,0.478870945086,0.390538163722,0.176430356742,0.151253233413,0.0629774880505,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_6
    y4_PT_6_weights = numpy.array([0.0,0.0,0.587284029658,0.802553726816,0.80101317268,0.729982730141,0.873550679048,0.830256709085,1.13068875876,1.23124515597,0.98739523043,1.05929342183,0.95906043102,0.887204727326,0.772990282998,1.00155213317,0.858842435873,0.830218220225,0.887264709966,0.73020666533,0.744911409518,0.730241655204,0.673090695698,0.515636265783,0.715130028774,0.701830877783,0.443743222896,0.587513463256,0.786962739123,0.529290314061,0.744317081527,0.672850765138,0.529283316086,0.586714194579,0.658794333317,0.644357011732,0.515365844048,0.400432307837,0.601502414607,0.386925566926,0.372018331343,0.47228511237,0.32971787384,0.271867416781,0.272043865714,0.229193867258,0.171970878599,0.143242693042,0.186128331183,0.114692006113,0.157665118938,0.0571866491765,0.0285195259469,0.0285128728724,0.0427649430723,0.0714000355722,0.0,0.0427905556595,0.0141978808832,0.0143626282024,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_7
    y4_PT_7_weights = numpy.array([0.0,0.0,0.0626422632744,0.0842497990994,0.0928749306255,0.0917879855605,0.0733575077455,0.087313659422,0.0712249404291,0.0647338640083,0.0659011496757,0.0626541027216,0.0625696759384,0.0680370488011,0.0475123509056,0.0549833563623,0.0539297712969,0.0593892232551,0.0496904110356,0.0367165772392,0.0496924646035,0.0453712969058,0.0432105873283,0.0345456836418,0.0269857251709,0.0378078808972,0.0259233810101,0.0388836151584,0.0291628213813,0.0280906075222,0.0194584729107,0.0269149609002,0.0344684024365,0.0410619686553,0.029071102337,0.0334784570187,0.0269934784371,0.0388736825956,0.0399500874095,0.0431892763235,0.0237582080658,0.0237708437944,0.0356496858926,0.0367161790985,0.0248273834828,0.0280763163665,0.0410397356404,0.0291676828888,0.0388853963141,0.0421100426152,0.0367169544252,0.0410508416704,0.0291577293713,0.0323883058733,0.0421170205548,0.038887533701,0.0302290002657,0.0291701345973,0.0302339875018,0.0323882849185,0.0248410459952,0.0302314938837,0.0194311457903,0.0226706553123,0.019445480951,0.0259078116133,0.00756556387287,0.0108006917517,0.00756059130508,0.00864255332496,0.0064862128178,0.00216153519555,0.00107629752546,0.00216268561263,0.0010799183008,0.00432144430067,0.0,0.0,0.0010812883239,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_8
    y4_PT_8_weights = numpy.array([0.0,0.0,0.0127009309387,0.0170378905017,0.0113549062884,0.00851423084965,0.0112937675578,0.0085220114677,0.00706401496302,0.0127620399723,0.00993753455844,0.00710320314463,0.00425723347046,0.00710128991441,0.00994566411642,0.00283326603338,0.00423455460218,0.00284133397005,0.00284080981773,0.00702797689233,0.00425095477897,0.00284489093008,0.00423997059537,0.00421817521329,0.00425869901818,0.00142146323625,0.00141749348771,0.0028398877254,0.00142146323625,0.00560842688629,0.00566867544885,0.00142040453765,0.00283829448052,0.00142146323625,0.0,0.00142244546504,0.00284285000269,0.0,0.0,0.0028439087013,0.0,0.00142146323625,0.00141986999137,0.00142146323625,0.0,0.00141749348771,0.00283432992896,0.00426272073649,0.0,0.0028305702868,0.00142146323625,0.00284027527145,0.00284133397005,0.0,0.00284086995419,0.00141842448915,0.00567982667816,0.0,0.00284133397005,0.00283829448052,0.0,0.00142244546504,0.0,0.00565570898947,0.00142244546504,0.00425260667545,0.00426120396143,0.00141842448915,0.0,0.0,0.00283591723443,0.00141749348771,0.00709969666953,0.0,0.0,0.0028398877254,0.00141749348771,0.0,0.00282009986157,0.0,0.00567472695817,0.0,0.00141749348771,0.0,0.00283829448052,0.00141986999137,0.0,0.00141842448915,0.0,0.00142146323625,0.00142146323625,0.00142244546504,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_9
    y4_PT_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_10
    y4_PT_10_weights = numpy.array([0.0,0.0,52.7314194359,0.0,52.6056914349,0.0,52.64790836,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_11
    y4_PT_11_weights = numpy.array([0.0,0.0,57.6007928132,207.281727062,103.568467078,115.161775263,126.707049707,69.1506784967,34.496333353,34.5181598844,46.0663932073,23.0466844778,69.1873186336,11.5322611437,34.5342800075,11.5336579649,11.5064266771,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_12
    y4_PT_12_weights = numpy.array([0.0,0.0,117.694622172,63.7098593874,78.9176781259,60.9238855792,42.9378057762,26.3043219503,22.1528270684,29.0686192944,19.3689497416,19.3744313674,23.5270995096,13.8483178362,12.4672635659,12.4584679607,11.0740497033,8.30822327409,12.4626955444,9.69221261837,6.9293154931,4.14656911227,2.76913079167,11.068489219,1.3829341794,2.76873265254,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_13
    y4_PT_13_weights = numpy.array([0.0,0.0,37.3021952242,28.7421543745,17.6523451098,10.0815074092,7.55836922502,5.53850653538,6.55699800905,6.55586009756,3.52955869276,4.53395827052,6.05180475434,2.51743163392,3.52836919594,2.52182306195,3.52419078495,4.03068277597,3.02422858523,1.5088257284,2.01731710578,2.01636368767,2.01441224532,3.0244067063,4.53513259518,1.51331456165,1.51350330324,0.502666180869,1.51481903237,0.503668453311,1.51135007125,1.51331456165,0.0,0.0,0.50516746205,1.51002372162,0.504767827534,0.0,0.0,0.504265629262,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_14
    y4_PT_14_weights = numpy.array([0.0,0.0,15.8449562641,9.76033917624,5.94029365072,4.10243453023,2.54622762871,2.97030841806,2.12296634517,1.55609013156,1.69788829805,1.69770939186,1.1309589897,0.848759471662,1.13041919315,0.84834221624,1.27331792132,0.989926272413,0.989066945548,0.848882589905,1.41509550398,0.84814772789,0.707252364392,0.566199255644,0.565745257121,0.70715329268,0.990600537167,0.282245302636,0.565963214887,1.13235618939,0.848416471931,0.848971850632,0.566441837058,0.141173976236,0.282882247173,0.708033011004,0.707005358416,0.849300230072,0.848416087186,0.707327966688,0.565764879091,0.424786026034,0.424732738919,0.423751448045,0.0,0.0,0.0,0.0,0.141625204598,0.141520688752,0.566008037622,0.0,0.0,0.0,0.141373851009,0.0,0.0,0.0,0.141272009137,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_15
    y4_PT_15_weights = numpy.array([0.0,0.0,0.987639554758,0.68515450543,0.609208370024,0.15335941475,0.380988625755,0.227721221441,0.0754248020258,0.0,0.229213126056,0.0760474828039,0.0765765575886,0.0,0.0,0.0,0.0754248020258,0.0,0.0,0.0,0.0,0.0,0.0,0.228694038274,0.0,0.0,0.0,0.0,0.0,0.0772705065662,0.0,0.0766098869953,0.0,0.0,0.076224825977,0.0,0.229218503673,0.0,0.0,0.0761527895465,0.0,0.0760964132096,0.0,0.0,0.0,0.0,0.0,0.0,0.152914786281,0.0760814622523,0.0,0.0,0.0,0.0,0.0758636983093,0.15209159721,0.0,0.0,0.0772705065662,0.0754248020258,0.0756326971551,0.0,0.0768147682953,0.0760474828039,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_16
    y4_PT_16_weights = numpy.array([0.0,0.0,0.108403734785,0.0812489802789,0.0631565452546,0.0450944277467,0.01803441981,0.00905842151552,0.018063516926,0.0361218096146,0.0,0.00902669110671,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00901015025479,0.00903130706887,0.0,0.0,0.0,0.0,0.00904851201876,0.0,0.0,0.0,0.0,0.0,0.00903285663082,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00903671609877,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00903130706887,0.0,0.0,0.0,0.0,0.0,0.0,0.00903130706887,0.0,0.0,0.0,0.0,0.00903130706887,0.0,0.0,0.00902765164262,0.00902516849367,0.00900018108546,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights+y4_PT_15_weights+y4_PT_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights+y4_PT_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"p_{T} [ j_{2} ]   ( GeV ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 2000.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights+y4_PT_15_weights+y4_PT_16_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights+y4_PT_15_weights+y4_PT_16_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonposx="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonposy="clip")

    # Legend
    plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.)

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_3.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_3.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_3.eps')

# Running!
if __name__ == '__main__':
    selection_3()
