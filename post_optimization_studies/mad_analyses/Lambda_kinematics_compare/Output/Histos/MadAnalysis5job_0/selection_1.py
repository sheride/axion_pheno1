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
    y2_ETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,406.568743944,0.0,406.568743944,0.0,0.0,1219.70663183,0.0,813.137487888,0.0,1219.70663183,1219.70663183,0.0,1626.27537578,1626.27537578,1626.27537578,0.0,4878.82732733,1219.70663183,1219.70663183,2439.41286366,1626.27537578,2439.41286366,4472.25538338,8131.37487888,5691.96321522,5285.39527127,8537.94682282,7724.80693493,10164.2185986,10164.2185986,8131.37487888,8131.37487888,11790.4943744,4878.82732733,6505.0991031,10570.7905425,5691.96321522,8537.94682282,8131.37487888,6911.67104705,4878.82732733,4878.82732733,6098.53115916,8537.94682282,4472.25538338,2439.41286366,4065.68743944,4878.82732733,2439.41286366,4472.25538338,6505.0991031,4065.68743944,6098.53115916,9351.08271071,10164.2185986,7724.80693493,6911.67104705,8537.94682282,5691.96321522,4065.68743944,6098.53115916,10977.3584865,9757.65065465,8131.37487888,8537.94682282,6098.53115916,6505.0991031,9757.65065465,8131.37487888,6505.0991031,3252.55035155,6505.0991031,5285.39527127,3659.1194955,3659.1194955,4878.82732733,3659.1194955,1219.70663183,1626.27537578,813.137487888,1626.27537578,813.137487888,1626.27537578,1219.70663183,1626.27537578,406.568743944,813.137487888,406.568743944,0.0,406.568743944,0.0,406.568743944,406.568743944,813.137487888,406.568743944,0.0,406.568743944,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating weights for histo: y2_ETA_1
    y2_ETA_1_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,141.959877152,0.0,0.0,141.959877152,0.0,0.0,0.0,0.0,141.959877152,141.959877152,141.959877152,141.959877152,141.959877152,425.879687011,141.959877152,425.879687011,141.959877152,0.0,0.0,141.959877152,425.879687011,141.959877152,283.919809859,283.919809859,283.919809859,0.0,141.959877152,425.879687011,0.0,0.0,0.0,283.919809859,141.959877152,0.0,0.0,0.0,283.919809859,0.0,0.0,0.0,141.959877152,0.0,0.0,0.0,141.959877152,283.919809859,141.959877152,141.959877152,0.0,0.0,709.799385759,0.0,141.959877152,141.959877152,0.0,141.959877152,141.959877152,0.0,141.959877152,283.919809859,425.879687011,283.919809859,141.959877152,141.959877152,141.959877152,283.919809859,141.959877152,0.0,141.959877152,0.0,141.959877152,0.0,0.0,141.959877152,283.919809859,0.0,0.0,0.0,141.959877152,141.959877152,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,6),dpi=80)
    frame = gridspec.GridSpec(1,1,right=0.7)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights+y2_ETA_1_weights,\
             label="$signal4TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#ce5e60", edgecolor="#ce5e60", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData, bins=xBinning, weights=y2_ETA_0_weights,\
             label="$signal1TeV$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"\eta [ j_{1} ] ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y2_ETA_0_weights+y2_ETA_1_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y2_ETA_0_weights+y2_ETA_1_weights) if x])/100. # log scale
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
