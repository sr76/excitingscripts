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
    """
    rl=[]
    r=[]
    for i in range(grid[0]):
        for j in range(grid[1]):
            a = origin[0] + rows 
    """
rootdir = "/home1/srigamonti/projects/stm/runs/97/"
parse_plot2d(rootdir+"input.xml", rootdir+"STM2d2D.XML")







