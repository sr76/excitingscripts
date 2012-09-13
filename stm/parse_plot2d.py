import numpy as np
import os
import sys
from lxml import etree

def parse_plot2d(inputxmlpath,plot2dxmlpath):

    inputtree = etree.parse(inputxmlpath)
    plot2dtree = etree.parse(plot2dxmlpath)
    
    bands = bandstree.xpath('/bandstructure/band')
    nbands = len(bands)
    
    vertex_x = bandstree.xpath('/bandstructure/vertex//@distance')
    vertex_ymax = bandstree.xpath('/bandstructure/vertex//@upperboundary')
    vertex_ymin = bandstree.xpath('/bandstructure/vertex//@lowerboundary')
    nvertex = len(vertex_x)
    
    xdata = []
    ydata = []
    legends = []
    for band in bands:
        xdata.append(band.xpath("point/@distance"))
        ydata.append(band.xpath("point/@eval"))
    
    
    #convert the data from strings to floats
    for band in range(nbands):
        for i, x in enumerate(xdata[band]):
            xdata[band][i] = float(xdata[band][i])
        for i, x in enumerate(ydata[band]):
            ydata[band][i] = float(ydata[band][i])
    
    for i in range(nvertex):
        vertex_x[i] = float(vertex_x[i])
        vertex_ymax[i] = float(vertex_ymax[i])
        vertex_ymin[i] = float(vertex_ymin[i])
    
    #-------------------------------------------------------------------------------
    #Plot BANDS
     
    #colors=['k','r','g','b','y','c','m']
    fig = plt.figure(1, figsize=(8, 5.5))
    
    params = {'font.size':15,
              'xtick.major.size': 5,
              'ytick.major.size': 5,
              'patch.linewidth': 1.5,
              'axes.linewidth': 2.,
              'axes.formatter.limits': (-4, 6),
              'lines.linewidth': 1.8,
              'lines.markeredgewidth':2.0,
              'lines.markersize':18,
              'legend.fontsize':11,
              'legend.borderaxespad':1,
              'legend.borderpad':0.5,
              'savefig.dpi':80}
    
    plt.rcParams.update(params)
    
    ax = fig.add_subplot(111)
    
    for band in range(nbands):
        ax.plot(xdata[band], ydata[band], 'k')
    
    ax.plot(xdata[band], [0] * len(xdata[band]), 'r:')
    
    for i in range(1, nvertex - 1):
        #ax.axvline(vertex_x[i],vertex_ymin[i],vertex_ymax[i])
        ax.axvline(vertex_x[i], linewidth=1, color='0.8')
    
    ax.set_xlim(0.0, xdata[band][-1])
    
    ax.legend(loc=2)
    
    
    ymin = None
    ymax = None
    if "-ymin" in args:
        iymin = int(args.index("-ymin")) + 1
        ymin = float(args[iymin])
    if "-ymax" in args:
        iymax = int(args.index("-ymax")) + 1
        ymax = float(args[iymax])
    xmin = None
    xmax = None
    if "-xmin" in args:
        ixmin = int(args.index("-xmin")) + 1
        xmin = float(args[ixmin])
    if "-xmax" in args:
        ixmax = int(args.index("-xmax")) + 1
        xmax = float(args[ixmax])
    
    ax.set_ylim(ymin, ymax)
    ax.set_xlim(xmin, xmax)
    
    #ax.legend()
    
    #ax.set_xlim(0.0,54.0)
    #ax.set_ylim(0)
    #ax.set_xlabel(str.capitalize(labels[0]["xlabel"])+" [eV]")
    #ax.set_ylabel(str.capitalize(labels[0]["ylabel"]))
    
    #plt.savefig('PLOT.ps',  orientation='portrait',format='eps')
    
    if "-png" in args:
        plt.savefig('PLOT.png', orientation='portrait', format='png')
    else:
        plt.show()
