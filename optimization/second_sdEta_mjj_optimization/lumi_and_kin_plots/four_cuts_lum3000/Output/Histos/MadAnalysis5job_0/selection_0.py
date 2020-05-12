def selection_0():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(0.0,2000.0,201,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([5.0,15.0,25.0,35.0,45.0,55.0,65.0,75.0,85.0,95.0,105.0,115.0,125.0,135.0,145.0,155.0,165.0,175.0,185.0,195.0,205.0,215.0,225.0,235.0,245.0,255.0,265.0,275.0,285.0,295.0,305.0,315.0,325.0,335.0,345.0,355.0,365.0,375.0,385.0,395.0,405.0,415.0,425.0,435.0,445.0,455.0,465.0,475.0,485.0,495.0,505.0,515.0,525.0,535.0,545.0,555.0,565.0,575.0,585.0,595.0,605.0,615.0,625.0,635.0,645.0,655.0,665.0,675.0,685.0,695.0,705.0,715.0,725.0,735.0,745.0,755.0,765.0,775.0,785.0,795.0,805.0,815.0,825.0,835.0,845.0,855.0,865.0,875.0,885.0,895.0,905.0,915.0,925.0,935.0,945.0,955.0,965.0,975.0,985.0,995.0,1005.0,1015.0,1025.0,1035.0,1045.0,1055.0,1065.0,1075.0,1085.0,1095.0,1105.0,1115.0,1125.0,1135.0,1145.0,1155.0,1165.0,1175.0,1185.0,1195.0,1205.0,1215.0,1225.0,1235.0,1245.0,1255.0,1265.0,1275.0,1285.0,1295.0,1305.0,1315.0,1325.0,1335.0,1345.0,1355.0,1365.0,1375.0,1385.0,1395.0,1405.0,1415.0,1425.0,1435.0,1445.0,1455.0,1465.0,1475.0,1485.0,1495.0,1505.0,1515.0,1525.0,1535.0,1545.0,1555.0,1565.0,1575.0,1585.0,1595.0,1605.0,1615.0,1625.0,1635.0,1645.0,1655.0,1665.0,1675.0,1685.0,1695.0,1705.0,1715.0,1725.0,1735.0,1745.0,1755.0,1765.0,1775.0,1785.0,1795.0,1805.0,1815.0,1825.0,1835.0,1845.0,1855.0,1865.0,1875.0,1885.0,1895.0,1905.0,1915.0,1925.0,1935.0,1945.0,1955.0,1965.0,1975.0,1985.0,1995.0])

    # Creating weights for histo: y1_PT_0
    y1_PT_0_weights = numpy.array([0.0,0.0,189.760787293,461.198604554,588.01269582,660.478233686,778.694632323,817.076899413,889.849037016,991.484749871,1032.01621512,1131.80962955,1150.53981349,1190.764379,1269.06371187,1260.1591195,1277.96830423,1275.2047066,1243.57813372,1254.93912398,1268.14241266,1244.80633267,1249.41192872,1159.75160559,1179.40338874,1126.89653376,1130.5814306,1083.29457115,1064.87128695,1032.93751433,1017.89162723,950.032285413,908.886720693,892.612634647,882.172643598,854.84476703,846.861173875,803.873310734,760.885447594,751.366755755,716.362485769,717.283484979,648.81004369,647.274645007,631.614658434,607.050379496,565.904814776,545.946131889,529.05794637,505.107466905,505.721866379,507.256965062,471.638595603,462.426803501,436.32712588,428.343532725,389.961565635,395.795660633,371.845181169,352.807797492,344.210104864,342.67470618,315.039629875,313.197331455,307.056336721,273.587165418,280.956509099,266.83192121,256.084940425,249.02264648,245.33798964,233.976909381,206.034783339,203.578325446,213.404127021,206.648882813,188.22550861,190.681966503,167.038626776,158.748103885,159.669283095,159.362233358,153.52813836,148.615252573,156.598725727,142.474107838,123.129584425,125.893092055,118.523718374,109.926145746,105.013259958,112.38260364,99.1791949607,95.1874583834,109.619096009,88.7392639122,93.6521796998,84.7475273349,76.7640841801,93.9592294365,81.3699202309,72.465297866,74.9217257598,78.9134623372,59.8759886605,56.4983515566,63.8676952379,56.8054012933,60.1830383972,52.5066149792,62.9465460277,45.1372712979,46.3655002448,42.9878931409,45.1372712979,44.8302215612,37.4608778799,44.5231718245,39.9173057737,42.0667139307,35.6185194596,37.7679276166,31.3197331455,38.6891068268,28.8632932517,33.1620915658,28.2491787783,26.0997856212,28.556234515,30.0915041986,18.73043294,18.4233772032,28.2491787783,18.4233772032,23.6433337275,21.4939405704,16.5810397829,19.9586588868,18.4233772032,14.1245908891,19.9586588868,18.1163214665,18.4233772032,13.8175321524,13.5104764157,14.7387023626,11.6681389954,12.5893092055,12.8963649423,12.5893092055,7.67640841801,11.3610832587,8.59757562818,11.6681389954,10.4399130485,12.5893092055,8.9046313649,9.21169010162,11.0540275219,7.98346415473,7.98346415473,8.29051989145,7.67640841801,5.83407099769,7.67640841801,7.36934968129,7.06229394457,6.14112673441,4.29878931409,8.9046313649,4.60584505081,6.44818247113,3.68467484065,4.60584505081,4.29878931409,4.60584505081,4.91290078753,4.29878931409,5.52701226097,3.99173057737,4.29878931409,3.99173057737,3.37761910393,5.52701226097,2.76350673048,2.14939405704,1.5352813836,2.45645039376,3.68467484065,3.37761910393,3.68467484065,2.76350673048,3.37761910393,3.99173057737,2.14939405704,2.76350673048,1.22822504688,3.07056336721,1.84233772032,0.614112673441])

    # Creating weights for histo: y1_PT_1
    y1_PT_1_weights = numpy.array([0.0,0.0,0.0,1.82209320175,0.909853848219,0.913150150035,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_2
    y1_PT_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.752246786476,2.25808254825,7.52808020362,10.5435951411,12.8113767158,15.0565508847,9.04294994055,10.5332102999,7.52683439455,5.27341371341,3.76431126672,1.5053095469,0.752773001351,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_3
    y1_PT_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,3.30199476371,5.35642587437,14.4365115646,18.977544663,18.1487910859,23.9266717741,30.1229390145,27.2192271395,31.7644589114,30.9401721381,28.8846806947,30.1162113865,27.2303697733,19.7963256284,16.9138173598,17.7378908479,14.4375170525,19.3888135799,16.0853958985,14.0286095086,13.614872576,8.66453887946,7.42314831259,6.60056477477,2.88769201565,4.12459353619,0.825650580535,0.411927968511,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_4
    y1_PT_4_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.813660897617,3.10960083369,5.69984761328,6.88240320638,7.47622726875,8.58604142838,8.58644426146,10.0653046299,11.9908647993,12.9497548391,14.1370963298,14.9517029833,14.6547638961,17.0235576982,17.0973002019,17.4672452696,18.2811214124,14.6553290649,14.9493040221,15.9149821,14.5066445768,12.0636753758,10.3621234684,9.69366405579,8.43840911625,6.43853826811,6.73450634715,6.43890202037,5.40161885903,4.14475258716,4.07126861808,2.07339239494,2.14719652613,2.36822803202,1.3322014694,0.887930992453,0.296119321819,0.0739603342326,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_5
    y1_PT_5_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.359232884497,0.623997465461,1.05875343832,1.39933308956,1.94681148724,1.92817175777,1.96665755514,2.55207949806,2.64688659664,3.02504669126,3.5356309381,2.96802469347,3.1570567273,2.89229994853,3.91289078015,3.74359828433,3.95124454048,4.27223559605,4.31036429323,4.49950735822,5.00989054866,4.08353365482,4.8579339165,5.2186681222,4.61382142958,4.99070616639,4.34798884898,4.61332028898,3.83742860888,4.00850060394,3.2706145865,2.81686028357,2.53348027996,2.26872650203,2.00408045432,1.85312580327,1.53133682384,1.26700586453,1.32372537746,0.945462053883,0.850786992343,0.567242242513,0.567185826685,0.3402141487,0.18914795636,0.207992313234,0.0755909974144,0.0378915706606,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_6
    y1_PT_6_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.043018425228,0.150496745403,0.192911895222,0.258092406619,0.23638836289,0.322209200861,0.364725346452,0.536773104871,0.450598294342,0.643690062508,0.558589016225,0.72998611295,0.75228803365,0.751108624977,0.922688968669,0.85887343724,0.707985829954,0.730918618078,0.881414163828,1.01015865445,0.966317342375,1.07338860535,0.987856358863,0.837770794462,1.05254013902,1.15866142692,1.35201771854,1.26717077371,0.966039172879,1.18058208296,1.13812936902,1.41749701846,1.09599231372,1.20224331408,1.35237836416,1.13806038898,1.43866564214,1.24471552239,0.966659243427,1.1157355999,1.02987494845,1.13804314397,1.13832131347,0.924070068971,0.644251425047,0.70886105166,0.686758198349,0.643975130008,0.473134297297,0.558501516548,0.321945652134,0.622651076308,0.343307869789,0.322017256411,0.321628044051,0.278937049063,0.321958323467,0.215130590008,0.21456480375,0.15061955986,0.171926968377,0.172199514501,0.2146420314,0.150533034901,0.107354605979,0.236446096182,0.0860456978954,0.0429234877034,0.12846722087,0.0858267612569,0.0428375700684,0.0213476568691,0.0430565966809,0.0215457270465,0.0429275740208,0.0431176140222,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_7
    y1_PT_7_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0016221902017,0.00484954537566,0.0161990822689,0.0129446750064,0.0226939094826,0.0307866691285,0.043745111421,0.0324039480552,0.0340246845195,0.0437337015469,0.0372542132273,0.0372588337548,0.0356307107329,0.0696514976646,0.0421082816908,0.0421354076448,0.032397818784,0.0664133879771,0.0664336302881,0.0485974511157,0.0583202354292,0.056712889065,0.045371285649,0.0501933247414,0.035628950532,0.0615726153173,0.0632012412537,0.0648157855825,0.0581841027444,0.0486102125726,0.0534584346543,0.0533285255372,0.0664387537302,0.051837289572,0.0485880214677,0.0615944606685,0.0387301417307,0.0485836523975,0.0405149855021,0.0534540341519,0.0421097904345,0.0372554705137,0.0648014210854,0.0615395172528,0.0518582548227,0.0550436527779,0.0615433834085,0.053451299554,0.055075902174,0.0583279363084,0.0679330700471,0.0776320916477,0.0680318613259,0.0648032127185,0.0680389964262,0.0776506051899,0.0826374430971,0.0972007486131,0.0923432854763,0.076146073421,0.0566865174828,0.0726933449453,0.0842170977283,0.0534488164134,0.0583297279415,0.0551020222989,0.0356337282203,0.0518470964059,0.0518536971595,0.0421182456855,0.0486040204371,0.0421299070168,0.0485987712664,0.02755331827,0.017815072477,0.024298408093,0.0371556734058,0.0178230059542,0.0129544755539,0.0178089589219,0.0194423656899,0.0145765227393,0.0129546861494,0.0128413009188,0.0226857685531,0.0128412694866,0.0113516962826,0.0048656857898,0.0113417417175,0.00485778374479,0.0097249059843,0.00810587314306,0.00323514877802,0.00324547424257,0.00648264096526,0.00485933020706,0.00323357088359,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_8
    y1_PT_8_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.00212624021527,0.0,0.00638724665889,0.00638607177072,0.00212763671741,0.00638585015675,0.00212763671741,0.0,0.00212980497074,0.0,0.0,0.00852190820525,0.00213219483804,0.00212624021527,0.00849543257374,0.00213366818121,0.00426200092241,0.00213219483804,0.00848550003578,0.00426347315194,0.00639566910362,0.00213366818121,0.0,0.00425149486085,0.0,0.00638228540128,0.00212763671741,0.00212763671741,0.0,0.0,0.00424438205449,0.00424990681296,0.00213366818121,0.00212980497074,0.00213060679015,0.0,0.0,0.00639021784526,0.0,0.00213219483804,0.0,0.00426586301925,0.00425983155545,0.00213219483804,0.00213366818121,0.0,0.00638904184346,0.00424557253358,0.0,0.00212763671741,0.00213060679015,0.00213060679015,0.00636142918748,0.00212763671741,0.00212624021527,0.00426733636241,0.00426200092241,0.00212763671741,0.0,0.00425744168815,0.0085248025506,0.00631221529382,0.00426438967608,0.00425387581904,0.0085137073745,0.00213219483804,0.00639180589315,0.00425744168815,0.00852547407436,0.0085233047074,0.00424438205449,0.0042412995043,0.014906201496,0.00212980497074,0.0106467396684,0.00638824002405,0.0106494680816,0.00851226966775,0.0,0.0042524793169,0.00638588022497,0.00426438967608,0.00841561145133,0.00426733636241,0.00639497307983,0.00213060679015,0.00426427497136,0.00426438967608,0.00212763671741,0.00638082764904,0.0,0.00213366818121,0.00851307148716,0.00413849177846,0.00425961105511,0.00639260771256,0.00202509626471,0.0,0.00212763671741,0.00212763671741,0.0,0.0021149646298,0.0,0.0,0.00419598445754,0.00212624021527,0.00635995584431,0.00212624021527,0.00212763671741,0.0,0.00211218721645,0.00212763671741,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_9
    y1_PT_9_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_10
    y1_PT_10_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,78.9085371523,0.0,0.0,0.0,0.0,0.0,79.0971291539,78.97186254,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_11
    y1_PT_11_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,17.2486885309,34.5412068894,17.3128913891,0.0,0.0,69.0993600824,86.4336994973,51.7898925383,51.7837826465,86.3385350506,69.1008587351,103.724866186,86.3937546387,86.3570664677,120.954645755,120.972860149,17.2639690244,69.1551848956,86.3425987051,17.2947865117,69.0817220929,51.7349899729,86.4209321291,17.2639690244,0.0,17.2277477414,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_12
    y1_PT_12_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.07914487411,0.0,4.15234016472,8.31073608337,10.3938750431,10.3852458101,10.3754798611,16.593192748,8.30942914839,12.4546085788,24.911845453,14.5362184535,18.6924101816,20.7451290034,29.0705039126,45.7056512931,49.8392587231,64.405005829,66.445353487,37.3762632568,56.0831189648,39.4567998869,47.7701758058,37.3952469923,29.0750046159,22.8610596254,39.472234991,20.764332004,35.3058820598,18.6940719797,12.4577359906,16.617167648,29.0776877274,24.9293635749,12.456270377,14.5276815426,4.15933933529,4.14988785846,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_13
    y1_PT_13_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.755502653215,0.0,0.754445761059,2.26861400616,1.51350825646,3.02717900667,5.2887666372,2.27085114007,3.02721633017,2.26860535803,2.26829038414,3.02635424845,2.26422257829,3.02039159245,3.78571897313,3.01780170598,6.04311544821,4.53384022235,3.02829324957,6.80937136464,9.8245454055,3.02502380238,3.78201393345,6.0455096139,15.1262250619,15.1277407599,15.8763772554,11.3429562397,13.6164805613,15.1137899655,15.1304034727,12.0979149712,12.8520771647,12.8468837369,9.83099053596,6.80745512175,6.8102316257,6.05069393847,2.26911150105,3.02774932789,2.271921232,3.77917689262,4.54253659682,1.50869944267,2.26635684501,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_14
    y1_PT_14_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.212260573394,0.21271710161,0.636445232254,0.424589996818,0.0,0.0,0.63675802954,0.0,0.212398562012,0.84967862252,0.636867104608,1.2729660668,0.0,0.636410605248,2.54598984528,0.849176530936,0.212327201525,0.424608175996,0.424440235018,1.0614371909,0.848768509384,1.90799043759,1.06199439713,1.69740601326,0.636335580069,0.848015372008,1.91032256643,1.90861949486,2.12054600421,1.06016926537,2.12162954094,2.12314043262,2.33545245598,2.33402091785,1.69700953405,1.48685708162,4.87837088585,4.66640744102,2.9694677381,3.18355208703,3.81928948558,5.5191695984,4.03371721898,2.75912137444,1.91048560191,3.81896630019,3.18268929747,3.18361268429,2.12084899051,1.69660728366,1.48612558612,0.423536470167,2.33388904667,1.69627544152,1.27324914258,0.636621829983,2.33420040116,1.0613734195,1.48595158542,1.27187069919,1.27276811575,1.69808412546,0.636602496572,1.06130993665,1.06075994438,0.211885187796,0.636559501373,0.636069240683,0.849186630479,0.424501409395,0.0,0.634892788161,0.637174707843,0.424415996114,0.211760963412,0.636796407804,0.212159260546,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_15
    y1_PT_15_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.115000199243,0.115905766366,0.115000199243,0.114122199795,0.0,0.115222158921,0.0,0.227821045187,0.0,0.11407123062,0.0,0.114144626232,0.0,0.0,0.0,0.0,0.0,0.0,0.229559492958,0.113795553862,0.0,0.0,0.1131372094,0.0,0.0,0.1131372094,0.0,0.0,0.11407123062,0.114914836954,0.0,0.0,0.115174292217,0.0,0.114483327483,0.0,0.0,0.0,0.0,0.0,0.228697892288,0.0,0.0,0.0,0.0,0.114144626232,0.114122199795,0.114337245394,0.114122199795,0.571100480343,0.342754851538,0.342408172504,0.342197559007,0.113449052111,0.113911409014,0.0,0.113449052111,0.11407123062,0.343505561011,0.113795553862,0.228215856852,0.230243100402,0.113795553862,0.1131372094,0.228451378763,0.226586261511,0.0,0.0,0.114337245394,0.0,0.0,0.341274618043,0.229488313396,0.0,0.11407123062,0.0,0.0,0.23017449146,0.0,0.0,0.0,0.227786297506,0.0,0.0,0.0,0.0,0.114195506766,0.115366113601,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y1_PT_16
    y1_PT_16_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0135414770362,0.0135377523129,0.0,0.0,0.0,0.0135469601754,0.0,0.0,0.0135469601754,0.0135002712018,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0135469601754,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.01355507372,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0135459582537,0.0,0.0135727675994,0.0135410352667,0.0271028596867,0.0270260466524,0.0270483256951,0.0406357207738,0.0135400362324,0.0,0.0406291664157,0.040596943228,0.0270608771464,0.0406263945286,0.0,0.0270870368311,0.0,0.01355507372,0.0,0.0270114971324,0.0,0.0,0.0135410352667,0.0,0.0135377523129,0.0,0.0,0.0,0.0135575222203,0.0,0.0135575222203,0.0,0.0135514529424,0.0135727675994,0.0,0.0,0.0135876318441,0.0,0.0135480573807,0.0135002712018,0.0,0.0,0.0,0.0,0.0,0.0135727675994,0.0271187258531])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights+y1_PT_10_weights+y1_PT_11_weights+y1_PT_12_weights+y1_PT_13_weights+y1_PT_14_weights+y1_PT_15_weights+y1_PT_16_weights,\
             label="$bg\_dip\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#e5e5e5", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights+y1_PT_10_weights+y1_PT_11_weights+y1_PT_12_weights+y1_PT_13_weights+y1_PT_14_weights+y1_PT_15_weights,\
             label="$bg\_dip\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#f2f2f2", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights+y1_PT_10_weights+y1_PT_11_weights+y1_PT_12_weights+y1_PT_13_weights+y1_PT_14_weights,\
             label="$bg\_dip\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights+y1_PT_10_weights+y1_PT_11_weights+y1_PT_12_weights+y1_PT_13_weights,\
             label="$bg\_dip\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ccc6aa", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights+y1_PT_10_weights+y1_PT_11_weights+y1_PT_12_weights,\
             label="$bg\_dip\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#c1bfa8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights+y1_PT_10_weights+y1_PT_11_weights,\
             label="$bg\_dip\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#bab5a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights+y1_PT_10_weights,\
             label="$bg\_dip\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b2a596", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights,\
             label="$bg\_dip\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#b7a39b", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights,\
             label="$bg\_vbf\_1600\_inf$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#ad998c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights,\
             label="$bg\_vbf\_1200\_1600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#9b8e82", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights,\
             label="$bg\_vbf\_800\_1200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#876656", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights,\
             label="$bg\_vbf\_600\_800$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#afcec6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights,\
             label="$bg\_vbf\_400\_600$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#84c1a3", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights,\
             label="$bg\_vbf\_200\_400$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#89a8a0", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights,\
             label="$bg\_vbf\_100\_200$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#829e8c", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights+y1_PT_1_weights,\
             label="$bg\_vbf\_0\_100$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#adbcc6", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y1_PT_0_weights,\
             label="$signal$", histtype="step", rwidth=1.0,\
             color=None, edgecolor="#7a8e99", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"p_{T} [ j_{1} ]   ( GeV ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 3000.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights+y1_PT_10_weights+y1_PT_11_weights+y1_PT_12_weights+y1_PT_13_weights+y1_PT_14_weights+y1_PT_15_weights+y1_PT_16_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y1_PT_0_weights+y1_PT_1_weights+y1_PT_2_weights+y1_PT_3_weights+y1_PT_4_weights+y1_PT_5_weights+y1_PT_6_weights+y1_PT_7_weights+y1_PT_8_weights+y1_PT_9_weights+y1_PT_10_weights+y1_PT_11_weights+y1_PT_12_weights+y1_PT_13_weights+y1_PT_14_weights+y1_PT_15_weights+y1_PT_16_weights) if x])/100. # log scale
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
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_0.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_0.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_0.eps')

# Running!
if __name__ == '__main__':
    selection_0()