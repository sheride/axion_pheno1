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
    y4_PT_0_weights = numpy.array([0.0,0.0,284.308335112,221.128691754,217.040611536,198.086730529,182.105969679,198.830010568,156.834128336,166.12524883,147.914647862,137.136967289,120.4129264,107.777005729,121.52788646,102.202325432,99.6008452941,91.4246448595,85.8499645632,72.0991238323,64.2945634174,69.1259636742,73.5856839113,57.9766030816,60.2064832001,46.0839624495,44.5974023705,47.1988825088,47.5705625285,31.9614576988,28.9883015408,30.4748816198,26.0151413828,27.130077442,19.697177047,21.5554011457,23.7852732643,15.2374408099,20.4404690865,20.4404690865,21.9270491655,18.2105969679,14.8657967902,12.6359246716,13.0075686914,8.9194764741,11.5209926124,9.6627685136,9.6627685136,8.17618843459,10.0344125334,10.7777005729,8.17618843459,4.8313842568,4.8313842568,4.8313842568,5.94631631606,4.08809221729,4.45974023705,3.71644859754,3.34480377779,3.71644859754,1.48657967902,2.60151413828,1.85822449877,1.11493445926,2.22986931852,0.743289639508,2.22986931852,2.60151413828,1.11493445926,1.48657967902,1.11493445926,2.22986931852,1.48657967902,1.11493445926,0.371644859754,0.0,0.371644859754,0.371644859754,0.743289639508,1.11493445926,0.0,0.0,0.371644859754,0.371644859754,0.371644859754,0.743289639508,0.0,0.0,0.743289639508,0.0,0.0,0.371644859754,0.0,0.371644859754,0.371644859754,0.0,0.371644859754,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8,6),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y4_PT_0_weights,\
             label="$signal$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"p_{T} [ j_{2} ]   ( GeV ) ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 40.0\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y4_PT_0_weights).max()*1.1
    ymin=0 # linear scale
    #ymin=min([x for x in (y4_PT_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonposx="clip")

    # Log/Linear scale for Y-axis
    plt.gca().set_yscale("linear")
    #plt.gca().set_yscale("log",nonposy="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_3.png')
    plt.savefig('../../PDF/MadAnalysis5job_0/selection_3.png')
    plt.savefig('../../DVI/MadAnalysis5job_0/selection_3.eps')

# Running!
if __name__ == '__main__':
    selection_3()
