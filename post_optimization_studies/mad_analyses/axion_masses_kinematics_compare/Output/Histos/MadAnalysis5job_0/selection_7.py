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
    xBinning = numpy.linspace(0.0,3000.0,161,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([9.375,28.125,46.875,65.625,84.375,103.125,121.875,140.625,159.375,178.125,196.875,215.625,234.375,253.125,271.875,290.625,309.375,328.125,346.875,365.625,384.375,403.125,421.875,440.625,459.375,478.125,496.875,515.625,534.375,553.125,571.875,590.625,609.375,628.125,646.875,665.625,684.375,703.125,721.875,740.625,759.375,778.125,796.875,815.625,834.375,853.125,871.875,890.625,909.375,928.125,946.875,965.625,984.375,1003.125,1021.875,1040.625,1059.375,1078.125,1096.875,1115.625,1134.375,1153.125,1171.875,1190.625,1209.375,1228.125,1246.875,1265.625,1284.375,1303.125,1321.875,1340.625,1359.375,1378.125,1396.875,1415.625,1434.375,1453.125,1471.875,1490.625,1509.375,1528.125,1546.875,1565.625,1584.375,1603.125,1621.875,1640.625,1659.375,1678.125,1696.875,1715.625,1734.375,1753.125,1771.875,1790.625,1809.375,1828.125,1846.875,1865.625,1884.375,1903.125,1921.875,1940.625,1959.375,1978.125,1996.875,2015.625,2034.375,2053.125,2071.875,2090.625,2109.375,2128.125,2146.875,2165.625,2184.375,2203.125,2221.875,2240.625,2259.375,2278.125,2296.875,2315.625,2334.375,2353.125,2371.875,2390.625,2409.375,2428.125,2446.875,2465.625,2484.375,2503.125,2521.875,2540.625,2559.375,2578.125,2596.875,2615.625,2634.375,2653.125,2671.875,2690.625,2709.375,2728.125,2746.875,2765.625,2784.375,2803.125,2821.875,2840.625,2859.375,2878.125,2896.875,2915.625,2934.375,2953.125,2971.875,2990.625])

    # Creating weights for histo: y8_M_0
    y8_M_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,2032.84407367,3252.55027788,2439.41280841,4065.68734735,2439.41280841,5285.39515155,7318.23882523,4878.82721682,4472.25528208,5691.96308629,4472.25528208,7724.80675996,4065.68734735,5285.39515155,3659.11941261,5285.39515155,5285.39515155,5691.96308629,4878.82721682,8131.37469469,4472.25528208,8537.94662943,4065.68734735,8131.37469469,5285.39515155,7724.80675996,6911.67089049,2845.98154314,5691.96308629,6911.67089049,6911.67089049,6505.09895576,5691.96308629,4065.68734735,5285.39515155,5691.96308629,4878.82721682,5285.39515155,7724.80675996,4878.82721682,4878.82721682,2845.98154314,4472.25528208,3659.11941261,2845.98154314,3252.55027788,6098.53102102,2845.98154314,2439.41280841,6098.53102102,6098.53102102,3659.11941261,4878.82721682,5285.39515155,4472.25528208,3659.11941261,3659.11941261,6098.53102102,2032.84407367,5691.96308629,1626.27533894,3659.11941261,1626.27533894,3252.55027788,1219.7066042,2032.84407367,3659.11941261,4065.68734735,813.137469469,3252.55027788,2845.98154314,2032.84407367,2439.41280841,0.0,1626.27533894,2845.98154314,813.137469469,1626.27533894,1626.27533894,2439.41280841,1219.7066042,3252.55027788,3252.55027788,3659.11941261,813.137469469,813.137469469,2439.41280841,406.568734735,813.137469469,1219.7066042,1219.7066042,1219.7066042,0.0,2845.98154314,813.137469469,1626.27533894,1626.27533894,1219.7066042,2032.84407367,813.137469469,1219.7066042,1626.27533894,1626.27533894,813.137469469,813.137469469,813.137469469,1219.7066042,406.568734735,1219.7066042,1219.7066042,406.568734735,406.568734735,813.137469469,406.568734735,406.568734735,813.137469469,0.0,1219.7066042,406.568734735,406.568734735,813.137469469,0.0,813.137469469,0.0,406.568734735,0.0,406.568734735,0.0,813.137469469,0.0,0.0,406.568734735,1219.7066042,406.568734735,406.568734735,0.0,406.568734735,0.0,0.0,813.137469469,406.568734735,406.568734735,406.568734735,0.0,0.0,0.0,406.568734735,0.0,0.0,0.0,406.568734735,406.568734735,0.0,406.568734735])

    # Creating weights for histo: y8_M_1
    y8_M_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,681.827334855,1022.74140228,1704.56873714,1363.65506971,3068.22380685,1022.74140228,4090.96480913,1363.65506971,2386.39647199,4090.96480913,3068.22380685,3068.22380685,2727.31013942,6136.44921369,3750.0515417,5113.70501141,1704.56873714,4431.88087656,5113.70501141,3750.0515417,3068.22380685,3409.13747427,2727.31013942,5454.62107884,3409.13747427,6818.27334855,3750.0515417,3750.0515417,4090.96480913,7500.1014834,5795.53314627,5454.62107884,4090.96480913,4090.96480913,4090.96480913,3409.13747427,4772.79294398,4431.88087656,7159.18941598,6136.44921369,4772.79294398,2727.31013942,3068.22380685,5795.53314627,3750.0515417,3409.13747427,3409.13747427,4090.96480913,3750.0515417,5113.70501141,4090.96480913,2727.31013942,3068.22380685,4090.96480913,2386.39647199,3068.22380685,5795.53314627,2045.48240456,1704.56873714,3750.0515417,3409.13747427,4431.88087656,1363.65506971,4090.96480913,3409.13747427,4090.96480913,3409.13747427,1022.74140228,1704.56873714,2386.39647199,1704.56873714,4431.88087656,1704.56873714,2045.48240456,1704.56873714,3068.22380685,3409.13747427,2045.48240456,2045.48240456,4431.88087656,340.913747427,1022.74140228,2045.48240456,3068.22380685,2045.48240456,1704.56873714,0.0,2386.39647199,1022.74140228,1022.74140228,681.827334855,681.827334855,1704.56873714,1022.74140228,1704.56873714,681.827334855,1022.74140228,1022.74140228,2045.48240456,1363.65506971,0.0,340.913747427,340.913747427,340.913747427,681.827334855,1022.74140228,0.0,340.913747427,681.827334855,681.827334855,681.827334855,1363.65506971,1704.56873714,1363.65506971,1022.74140228,681.827334855,340.913747427,1363.65506971,340.913747427,340.913747427,340.913747427,1022.74140228,340.913747427,340.913747427,340.913747427,681.827334855,0.0,1022.74140228,340.913747427,340.913747427,340.913747427,0.0,1022.74140228,681.827334855,0.0,0.0,340.913747427,0.0,0.0,0.0,0.0,340.913747427,340.913747427,340.913747427,340.913747427,0.0,0.0,0.0,681.827334855,1022.74140228,0.0,0.0,681.827334855,340.913747427])

    # Creating weights for histo: y8_M_2
    y8_M_2_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,142.164551459,291.437340491,355.411398648,483.359434961,469.143039815,405.169061659,760.580540306,753.472142733,852.987308755,732.147350015,973.827267495,924.069684484,902.744891766,881.420099047,1044.90964322,909.853289338,1016.47645293,909.853289338,1059.12603837,952.502474776,945.394477203,916.961286912,881.420099047,995.152060214,980.935265068,1030.69284808,995.152060214,924.069684484,1030.69284808,1158.64120439,860.095706328,945.394477203,924.069684484,909.853289338,753.472142733,909.853289338,845.878911182,980.935265068,1009.36845536,895.636494193,988.043662641,653.956976712,817.44612089,668.173371858,774.796935452,902.744891766,881.420099047,760.580540306,760.580540306,689.498164577,675.281769431,774.796935452,625.52418642,661.065374285,618.415788847,710.822957296,518.900622826,589.982998555,476.251437388,504.68422768,497.575830107,511.792225253,526.009020399,504.68422768,518.900622826,561.549808264,490.467832534,454.926644669,426.493854377,490.467832534,383.84430894,419.385456804,270.112667772,419.385456804,504.68422768,341.194923502,298.545578064,376.736071367,426.493854377,334.086685929,348.303161075,348.303161075,334.086685929,319.870250783,348.303161075,291.437340491,319.870250783,319.870250783,220.355044762,284.329102918,312.76201321,341.194923502,213.246847189,220.355044762,227.463282335,184.813936897,277.220865345,199.030372043,156.381026605,199.030372043,177.705699324,248.787955054,227.463282335,220.355044762,220.355044762,213.246847189,163.489224178,120.83987874,227.463282335,213.246847189,177.705699324,184.813936897,149.272789032,135.056313886,156.381026605,142.164551459,106.623403594,156.381026605,92.4069684484,135.056313886,127.948116313,199.030372043,113.731641167,127.948116313,99.5152060214,106.623403594,142.164551459,71.0822957296,149.272789032,85.2987308755,120.83987874,156.381026605,78.1904933025,170.597461751,85.2987308755,106.623403594,156.381026605,92.4069684484,106.623403594,56.8658205837,127.948116313,106.623403594,78.1904933025,49.7575830107,56.8658205837,78.1904933025,85.2987308755,56.8658205837,63.9740581566,42.6493854377,78.1904933025,85.2987308755,92.4069684484,49.7575830107])

    # Creating weights for histo: y8_M_3
    y8_M_3_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,16.4533981527,33.6221645728,33.6221645728,47.2140976554,70.8211464832,59.3753022031,77.2594288907,80.8362702283,77.2594288907,72.2518670182,97.2896763809,98.7203969159,108.735520661,106.589399859,118.750604406,113.743082534,99.4357571834,105.158679323,108.020160394,113.743082534,94.4281953109,120.181364941,95.1435555784,118.750604406,95.8589558459,101.581877986,100.866477718,102.297238253,88.7052731708,92.9974747759,95.1435555784,87.2745526358,104.443319056,91.5667542409,82.2669907633,91.5667542409,79.4055496933,77.2594288907,79.4055496933,72.2518670182,95.8589558459,82.9823510308,72.2518670182,75.8287083557,67.9597054131,82.2669907633,64.3828640756,63.6675038081,77.9747891582,60.0906624706,63.6675038081,67.2443451456,61.5214230056,82.2669907633,55.083100598,62.9521435406,62.2367832731,50.790938993,62.2367832731,49.360218458,57.2292214005,57.2292214005,50.0755787255,62.9521435406,42.2065357829,47.9294579229,37.1989899104,39.3450867129,37.1989899104,42.9218960504,43.6372963179,42.2065357829,49.360218458,44.3526565854,40.0604549804,36.4836256428,32.9068003053,37.1989899104,35.0528931078,33.6221645728,29.3299749678,25.7531456302,33.6221645728,30.7607035028,30.0453392353,28.6146067003,22.8916845602,32.1914320378,23.6070528277,35.7682613753,25.0377813627,25.0377813627,27.1838781653,14.3073053501,24.3224170952,17.1687664202,17.8841306877,20.0302274902,21.4609560252,22.8916845602,18.5994949552,24.3224170952,21.4609560252,17.1687664202,14.3073053501,24.3224170952,11.4458442801,16.4533981527,20.7455917577,15.0226696176,11.4458442801,16.4533981527,12.8765728151,13.5919370826,15.0226696176,17.8841306877,14.3073053501,15.7380338851,8.58438321008,17.1687664202,9.29974747759,10.7304760126,15.0226696176,12.8765728151,13.5919370826,6.43828640756,17.1687664202,9.29974747759,8.58438321008,12.8765728151,10.0151117451,10.0151117451,15.7380338851,8.58438321008,5.00755787255,10.7304760126,5.00755787255,7.15365067507,10.0151117451,7.15365067507,7.15365067507,6.43828640756,5.00755787255,7.15365067507,9.29974747759,9.29974747759,5.72292214005,7.86901894257,7.86901894257,10.0151117451,7.15365067507,7.86901894257,5.00755787255,5.00755787255])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights,\
             label="$signal100GeV4TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#0000ff", edgecolor="#0000ff", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights+y8_M_2_weights,\
             label="$signal100GeV1p5TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#59d354", edgecolor="#59d354", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights+y8_M_1_weights,\
             label="$signal100GeV1TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#ce5e60", edgecolor="#ce5e60", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y8_M_0_weights,\
             label="$signal1MeV$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"M [ j_{1} , j_{2} ]   ( GeV ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y8_M_0_weights+y8_M_1_weights+y8_M_2_weights+y8_M_3_weights) if x])/100. # log scale
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