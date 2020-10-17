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
    y4_PT_0_weights = numpy.array([0.0,0.0,448.050871682,368.975376679,338.990078575,311.52598031,279.41818234,247.840994336,220.774846046,193.17799779,174.603198964,142.760660977,117.950032545,107.203163224,92.210634172,80.6677449015,70.5842655388,61.1641761342,48.4271669392,37.149627652,34.6287578113,32.7712779287,29.4543371384,21.0956746667,17.9114208679,19.1055167925,16.1866189769,11.2775602872,11.6755942621,8.3586624717,7.4299225304,6.89921356394,5.30708666457,4.37834672327,4.6437027065,5.17441167296,2.91889811551,3.18425379874,2.7862210239,1.8574807826,2.25551235744,1.59212629937,1.32677181614,1.45944920776,0.9287402413,0.663386058072,0.796063149686,1.06141763291,0.663386058072,0.9287402413,0.265354393229,0.398031574843,0.265354393229,0.132677181614,0.132677181614,0.0,0.132677181614,0.265354393229,0.132677181614,0.398031574843,0.265354393229,0.0,0.0,0.132677181614,0.132677181614,0.0,0.0,0.132677181614,0.132677181614,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_1
    y4_PT_1_weights = numpy.array([0.0,0.0,287.312073263,243.798885885,218.392529566,201.553000721,182.644637058,157.000809581,149.543909468,123.900831395,109.635415561,103.069047278,82.7094776454,66.6794850401,59.7044217603,48.6480740058,44.3197559773,36.5465174237,32.6156833075,28.2907136164,23.1636627574,20.437441707,16.0290213776,13.9442572269,12.2628013567,9.85784083306,8.65558689123,8.33555538717,6.89258686675,6.17169913218,4.80744501638,4.96886065519,3.52617990594,3.36573249716,2.96531092101,2.24387132529,1.68301043392,2.48438956001,1.84333404114,1.76277790112,1.28267009317,1.12217412301,0.641195207787,1.2020315187,0.721077483684,0.560918445594,0.961258786349,0.400759407504,0.0802192978898,0.721077483684,0.080079519045,0.320540199543,0.24037833598,0.160298816935,0.481036169697,0.080022084718,0.24037833598,0.240518114825,0.0,0.16015903809,0.0,0.0802192978898,0.0802192978898,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0802192978898,0.0802192978898,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_2
    y4_PT_2_weights = numpy.array([0.0,0.0,196.567581548,168.389774159,150.680979515,142.712017425,120.419791579,109.742428779,100.627616389,80.7833311847,75.9915499281,65.0537570598,53.1784639456,45.9907620607,39.5843503806,32.6049985504,28.0215583484,25.9902548157,21.9276507503,16.2504192615,16.3545912888,14.6878808518,11.4065459913,10.0523426361,7.76061803515,8.22938015808,5.46889043417,5.31263839319,4.01052105172,4.42719716099,3.48967291514,2.96882687855,2.70840341025,2.29172610098,1.92713330537,1.45837118244,1.61462502342,1.30211704147,1.04169357317,1.14586290049,0.885439732199,0.520846936587,0.677100777564,0.260423408294,0.208338714635,0.260423408294,0.208338714635,0.208338714635,0.208338714635,0.208338714635,0.104169357317,0.104169357317,0.260423408294,0.104169357317,0.208338714635,0.0,0.156254050976,0.0520846936587,0.0520846936587,0.0520846936587,0.0520846936587,0.0,0.0520846936587,0.0520846936587,0.0,0.0,0.0,0.0,0.0,0.104169357317,0.0,0.0,0.0,0.0,0.0,0.0520846936587,0.0520846936587,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_3
    y4_PT_3_weights = numpy.array([0.0,0.0,140.966470672,121.62090509,107.96523115,94.1672971694,85.3835646351,77.5955623881,67.6738695255,55.867396119,54.0537455957,44.4165128152,37.9798609581,33.605769696,27.3824869005,24.0041259257,18.5631923559,17.9942061917,13.2645038271,13.1222557861,9.74389781134,9.03266360613,9.03266360613,6.79227795973,5.86767469296,4.90750941593,5.12088147749,3.84066110812,3.73397507734,2.77381010031,2.56044013875,1.84920683354,1.5291517412,1.13797352833,1.45802832067,1.20909664885,1.20909664885,0.533425053905,0.924603266769,0.782356725728,0.320055092343,0.533425053905,0.355616802604,0.426739923124,0.284493352083,0.177808341302,0.248931701823,0.106685010781,0.248931701823,0.0711233305207,0.177808341302,0.0355616802604,0.0,0.177808341302,0.0355616802604,0.0,0.0,0.0355616802604,0.0711233305207,0.0,0.0,0.0355616802604,0.0,0.0,0.0,0.0355616802604,0.0,0.0,0.0355616802604,0.0355616802604,0.0355616802604,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0355616802604,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_4
    y4_PT_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_5
    y4_PT_5_weights = numpy.array([0.0,0.0,79.0971291539,0.0,78.9085371523,0.0,78.97186254,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_6
    y4_PT_6_weights = numpy.array([0.0,0.0,86.4011892197,310.922590593,155.352700617,172.742662894,190.060574561,103.726017745,51.7445000294,51.7772398266,69.099589811,34.5700267167,103.78097795,17.2983917156,51.8014200112,17.3004869473,17.2596400156,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_7
    y4_PT_7_weights = numpy.array([0.0,0.0,176.541933258,95.5647890812,118.376517189,91.3858283688,64.4067086643,39.4564829255,33.2292406025,43.6029289416,29.0534246123,29.0616470511,35.2906492644,20.7724767543,18.7008953489,18.6877019411,16.6110745549,12.4623349111,18.6940433166,14.5383189276,10.3939732397,6.2198536684,4.15369618751,16.6027338285,2.0744012691,4.1530989788,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_8
    y4_PT_8_weights = numpy.array([0.0,0.0,55.9532928362,43.1132315618,26.4785176646,15.1222611138,11.3375538375,8.30775980306,9.83549701357,9.83379014633,5.29433803914,6.80093740577,9.07770713151,3.77614745088,5.29255379392,3.78273459292,5.28628617742,6.04602416396,4.53634287784,2.2632385926,3.02597565867,3.02454553151,3.02161836798,4.53661005946,6.80269889276,2.26997184248,2.27025495486,0.753999271304,2.27222854855,0.755502679967,2.26702510688,2.26997184248,0.0,0.0,0.757751193074,2.26503558243,0.757151741301,0.0,0.0,0.756398443893,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_9
    y4_PT_9_weights = numpy.array([0.0,0.0,23.7674343961,14.6405087644,8.91044047609,6.15365179535,3.81934144307,4.45546262709,3.18444951776,2.33413519734,2.54683244708,2.54656408778,1.69643848455,1.27313920749,1.69562878973,1.27251332436,1.90997688198,1.48488940862,1.48360041832,1.27332388486,2.12264325597,1.27222159184,1.06087854659,0.849298883466,0.848617885682,1.06072993902,1.48590080575,0.423367953954,0.84894482233,1.69853428409,1.2726247079,1.27345777595,0.849662755587,0.211760964354,0.42432337076,1.06204951651,1.06050803762,1.27395034511,1.27262413078,1.06099195003,0.848647318637,0.637179039051,0.637099108379,0.635627172068,0.0,0.0,0.0,0.0,0.212437806897,0.212281033127,0.849012056433,0.0,0.0,0.0,0.212060776514,0.0,0.0,0.0,0.211908013706,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_10
    y4_PT_10_weights = numpy.array([0.0,0.0,1.48145933214,1.02773175815,0.913812555037,0.230039122125,0.571482938632,0.341581832162,0.113137203039,0.0,0.343819689084,0.114071224206,0.114864836383,0.0,0.0,0.0,0.113137203039,0.0,0.0,0.0,0.0,0.0,0.0,0.343041057412,0.0,0.0,0.0,0.0,0.0,0.115905759849,0.0,0.114914830493,0.0,0.0,0.114337238966,0.0,0.34382775551,0.0,0.0,0.11422918432,0.0,0.114144619814,0.0,0.0,0.0,0.0,0.0,0.0,0.229372179422,0.114122193378,0.0,0.0,0.0,0.0,0.113795547464,0.228137395816,0.0,0.0,0.115905759849,0.113137203039,0.113449045733,0.0,0.115222152443,0.114071224206,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_11
    y4_PT_11_weights = numpy.array([0.0,0.0,0.162605602178,0.121873470418,0.0947348178819,0.06764164162,0.0270516297151,0.0135876322733,0.027095275389,0.0541827144219,0.0,0.0135400366601,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0135152253822,0.0135469606033,0.0,0.0,0.0,0.0,0.0135727680281,0.0,0.0,0.0,0.0,0.0,0.0135492849462,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0135550741481,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0135469606033,0.0,0.0,0.0,0.0,0.0,0.0,0.0135469606033,0.0,0.0,0.0,0.0,0.0135469606033,0.0,0.0,0.0135414774639,0.0135377527405,0.0135002716282,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_12
    y4_PT_12_weights = numpy.array([0.0,0.0,0.912787033803,1.81916001616,0.913150150035,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_13
    y4_PT_13_weights = numpy.array([0.0,0.0,9.03876615718,14.3000564189,12.8016704253,17.3227331768,16.5649496758,11.2956205368,5.27149226024,0.753445792208,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_14
    y4_PT_14_weights = numpy.array([0.0,0.0,14.8559620956,23.5128565693,33.4114494002,35.0706872792,41.6621785534,41.2548950084,49.9204336313,37.5395562166,36.3045123613,32.5797585463,32.5970041875,21.8638411509,21.0363520176,13.2018247826,9.90207547543,4.94335946635,2.06216552844,1.64844503259,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_15
    y4_PT_15_weights = numpy.array([0.0,0.0,8.06773951744,11.4694905207,15.7648365263,18.0599629707,19.6151602019,20.4277586991,19.985478039,19.5384174939,17.6129655561,16.5048709572,18.0592444849,16.2814248587,15.4683002735,16.2833668748,14.9508972563,15.6930059769,12.5830985217,12.7298289681,11.4718383762,8.06757718172,7.25323808485,5.77328345942,3.84893179711,3.035434441,1.92420736389,1.48061599318,0.518508403149,0.296202322267,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_16
    y4_PT_16_weights = numpy.array([0.0,0.0,1.98520664078,2.76083543994,3.47885497709,4.36822048457,4.57526056873,4.72688710688,4.70792778793,5.27467278568,4.7451202221,5.19959472287,4.85838399774,4.93370812958,4.63180543214,5.12282718608,4.650557693,4.55613920432,4.34802181793,4.23457499093,4.10239390812,4.12158129106,3.38377030151,3.64899670958,3.42176996214,3.30863222186,3.04361887356,3.02438047631,2.8168308492,2.79897253913,2.60929172504,2.06127168048,1.38007397353,1.30416587786,0.907631031796,0.718306417629,0.585807245583,0.264645535112,0.22687985012,0.0944662320757,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_17
    y4_PT_17_weights = numpy.array([0.0,0.0,0.880926044487,1.20383059022,1.20151975902,1.09497409521,1.31032601857,1.24538506363,1.69603313814,1.84686773395,1.48109284564,1.58894013274,1.43859064653,1.33080709099,1.1594854245,1.50232819976,1.28826365381,1.24532733034,1.33089706495,1.095309998,1.11736711428,1.09536248281,1.00963604355,0.773454398675,1.07269504316,1.05274631667,0.665614834344,0.881270194884,1.18044410868,0.793935471091,1.11647562229,1.00927614771,0.793924974129,0.880071291868,0.988191499975,0.966535517598,0.773048766072,0.600648461756,0.902253621911,0.580388350389,0.558027497014,0.708427668556,0.49457681076,0.407801125172,0.408065798571,0.343790800887,0.257956317898,0.214864039563,0.279192496774,0.17203800917,0.236497678407,0.0857799737648,0.0427792889203,0.0427693093086,0.0641474146084,0.107100053358,0.0,0.0641858334893,0.0212968213248,0.0215439423037,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_18
    y4_PT_18_weights = numpy.array([0.0,0.0,0.0939633949117,0.126374698649,0.139312395938,0.137681978341,0.110036261618,0.130970489133,0.106837410644,0.0971007960125,0.0988517245135,0.0939811540823,0.0938545139077,0.102055573202,0.0712685263583,0.0824750345434,0.0808946569453,0.0890838348826,0.0745356165535,0.0550748658589,0.0745386969052,0.0680569453587,0.0648158809925,0.0518185254627,0.0404785877563,0.0567118213458,0.0388850715151,0.0583254227375,0.043744232072,0.0421359112833,0.029187709366,0.0403724413503,0.0517026036547,0.0615929529829,0.0436066535055,0.0502176855281,0.0404902176557,0.0583105238935,0.0599251311143,0.0647839144853,0.0356373120987,0.0356562656915,0.0534745288389,0.0550742686478,0.0372410752242,0.0421144745498,0.0615596034606,0.0437515243332,0.0583280944712,0.0631650639227,0.0550754316378,0.0615762625057,0.043736594057,0.04858245881,0.0631755308322,0.0583313005516,0.0453435003985,0.043755201896,0.0453509812527,0.0485824273778,0.0372615689929,0.0453472408256,0.0291467186855,0.0340059829685,0.0291682214265,0.0388617174199,0.0113483458093,0.0162010376275,0.0113408869576,0.0129638299874,0.0097293192267,0.00324230279333,0.00161444628819,0.00324402841894,0.0016198774512,0.006482166451,0.0,0.0,0.00162193248585,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y4_PT_19
    y4_PT_19_weights = numpy.array([0.0,0.0,0.019051396408,0.0255568357526,0.0170323594326,0.0127713462745,0.0169406513367,0.0127830172016,0.0105960224445,0.0191430599584,0.0149063018377,0.0106548047169,0.00638585020569,0.0106519348716,0.0149184961746,0.00424989905007,0.00635183190326,0.00426200095508,0.0042612147266,0.0105419653385,0.00637643216845,0.00426733639512,0.00635995589306,0.00632726281994,0.00638804852726,0.00213219485438,0.00212624023157,0.0042598315881,0.00213219485438,0.00841264032944,0.00850301317327,0.00213060680648,0.00425744172078,0.00213219485438,0.0,0.00213366819756,0.00426427500404,0.0,0.0,0.00426586305194,0.0,0.00213219485438,0.00212980498706,0.00213219485438,0.0,0.00212624023157,0.00425149489344,0.00639408110474,0.0,0.0042458554302,0.00213219485438,0.00426041290718,0.00426200095508,0.0,0.00426130493128,0.00212763673372,0.00851974001723,0.0,0.00426200095508,0.00425744172078,0.0,0.00213366819756,0.0,0.0084835634842,0.00213366819756,0.00637891001318,0.00639180594214,0.00212763673372,0.0,0.0,0.00425387585165,0.00212624023157,0.0106495450043,0.0,0.0,0.0042598315881,0.00212624023157,0.0,0.00423014979236,0.0,0.00851209043726,0.0,0.00212624023157,0.0,0.00425744172078,0.00212980498706,0.0,0.00212763673372,0.0,0.00213219485438,0.00213219485438,0.00213366819756,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights+y4_PT_15_weights+y4_PT_16_weights+y4_PT_17_weights+y4_PT_18_weights+y4_PT_19_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights+y4_PT_15_weights+y4_PT_16_weights+y4_PT_17_weights+y4_PT_18_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights+y4_PT_15_weights+y4_PT_16_weights+y4_PT_17_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights+y4_PT_15_weights+y4_PT_16_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights+y4_PT_15_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#758991", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#688296", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights,\
             label="$signal\_2pt4TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#6d7a84", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights,\
             label="$signal\_2pt2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7c99d1", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights+y4_PT_1_weights,\
             label="$signal\_2TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7f7f9b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights,\
             label="$signal\_1pt8TeVL$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#aaa5bf", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"p_{T} [ j_{2} ]   ( GeV ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 3000.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights+y4_PT_15_weights+y4_PT_16_weights+y4_PT_17_weights+y4_PT_18_weights+y4_PT_19_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y4_PT_0_weights+y4_PT_1_weights+y4_PT_2_weights+y4_PT_3_weights+y4_PT_4_weights+y4_PT_5_weights+y4_PT_6_weights+y4_PT_7_weights+y4_PT_8_weights+y4_PT_9_weights+y4_PT_10_weights+y4_PT_11_weights+y4_PT_12_weights+y4_PT_13_weights+y4_PT_14_weights+y4_PT_15_weights+y4_PT_16_weights+y4_PT_17_weights+y4_PT_18_weights+y4_PT_19_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_3.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_3.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_3.eps')

# Running!
if __name__ == '__main__':
    selection_3()