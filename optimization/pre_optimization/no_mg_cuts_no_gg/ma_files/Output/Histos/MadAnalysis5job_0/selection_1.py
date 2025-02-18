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
    y2_ETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.534109117962,0.617641380894,0.822038647805,0.975227966832,1.33286572034,1.57432230158,1.8993894961,2.21526331675,2.80269264399,3.38330549105,3.82455625632,4.40740288776,5.3105865114,6.09339841845,7.07077102615,8.44077081345,9.28595519306,10.4075244188,12.3118375946,13.7331568591,15.0381298559,16.5707226029,18.4725413595,20.8155205386,22.4107495909,24.5028157816,26.1419490104,27.8792720132,29.7575336987,31.8670568264,33.9908189304,34.8080850027,36.2720372494,37.5680279386,39.3737116191,40.3732142023,41.1319733523,42.3389284663,42.4617306426,43.2633426354,43.1126781164,43.9695350987,43.6885931406,43.5742655936,44.8861941825,44.0872604923,44.0855815563,44.1155225817,43.4636956653,44.2411229847,43.6857149646,43.8828700211,43.738681398,44.094016211,44.2663469995,44.3851916838,44.7679491182,44.2737822875,43.608763731,43.4599780213,42.8824640104,42.6687594418,42.1269428084,41.2053668405,40.0720850375,39.2325930504,37.9971240067,36.8630027356,34.9060789009,33.7988166084,31.5437816962,30.0224977825,28.0257591796,25.7756691337,24.1776618421,21.925181311,20.8850884512,18.261167314,16.7612738444,15.1794802776,13.6767925789,11.859104506,10.7584180462,9.18177321651,8.07173668218,7.06854443721,6.26521353371,5.23610970973,4.30051062881,3.83169613155,3.18823871111,2.75174653017,2.34092048378,1.83918365047,1.61639883634,1.22596466696,1.05886576288,0.880045886762,0.692090200295,0.487608187089,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8,6),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights,\
             label="$signal$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\eta [ j_{1} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y2_ETA_0_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y2_ETA_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonposx="clip")

    # Log/Linear scale for Y-axis
    plt.gca().set_yscale("linear")
    #plt.gca().set_yscale("log",nonposy="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_1.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_1.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_1.eps')

# Running!
if __name__ == '__main__':
    selection_1()
