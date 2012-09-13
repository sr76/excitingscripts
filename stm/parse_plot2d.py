import numpy as np
import os
import sys
from lxml import etree
import xml_parsing_tools as xpt

def parse_plot2d(inputxmlpath,plot2dxmlpath):

    inputtree = etree.parse(inputxmlpath)
    plot2dtree = etree.parse(plot2dxmlpath)
    
    # Parse plot2d file
    origin = xpt.attrib2float(plot2dtree,'/plot2d/grid/@origin')
    grid = xpt.attrib2int(plot2dtree,'/plot2d/grid/@gridticks')
    endpoint = []
    endpoint.append(xpt.attrib2float(plot2dtree,'/plot2d/grid/axis[1]/@endpoint'))
    endpoint.append(xpt.attrib2float(plot2dtree,'/plot2d/grid/axis[2]/@endpoint'))
    delta = []
    delta.append(xpt.attrib2float(plot2dtree,'/plot2d/grid/axis[1]/@deltas')[0])
    delta.append(xpt.attrib2float(plot2dtree,'/plot2d/grid/axis[2]/@deltas')[0])
    textrows =  plot2dtree.xpath('/plot2d/function/row')
    rows = []
    for row in textrows:
        rows.append(xpt.text2float(row))
    # Parse plot2d file
    """
    print grid
    print origin
    print endpoint[0]
    print endpoint[1]
    print delta
    print rows[0]
    """ 
    # Parse input.xml
    try:
        scale = xpt.attrib2float(inputtree,'/input/structure/crystal/@scale')[0]
    except:
        scale = 1.0
    try:
        stretch = xpt.attrib2float(inputtree,'/input/structure/crystal/@stretch')
    except:
        stretch = [1.0,1.0,1.0]
        
    textbasevects = inputtree.xpath('/input/structure/crystal/basevect')
    basevects = []
    for basevect in textbasevects:
        basevects.append(xpt.text2float(basevect))
        
    for i in range(3):
        for j in range(3):
            basevects[i][j] = scale * stretch[i] * basevects[i][j]   
    # Parse input.xml
    
    d = []
    for i in range(2):
        d.append([])
        for j in range(3):
            d[i].append(enpoint[i][j]-origin[j])
            
    rl=[]
    for i in range(grid[0]):
        rl.append([])
        for j in range(grid[1]):
            rl[i].append([])
            for lat in range(3):
                rl[i][j].append( origin[lat] +  i * d[0][lat]/(grid[0]*1.0-1.0) +  j * d[1][lat]/(grid[1]*1.0-1.0) )

    r=[]
    for i in range(grid[0]):
        r.append([])
        for j in range(grid[1]):
            r[i].append([])
            for k in range(3):
                for l in range(3):
                    x = rl[i][j][l]*basevects[l][k]
                r[i][j].append(x)
            print r[i][j]

rootdir = "/home1/srigamonti/projects/stm/runs/97/"
parse_plot2d(rootdir+"input.xml", rootdir+"STM2d2D.XML")







