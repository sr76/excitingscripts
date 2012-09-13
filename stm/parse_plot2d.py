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
    textrows =  plot2dtree.xpath('/plot2d/function/row')
    rows = []
    for row in textrows:
        rows.append(xpt.text2float(row))
    # Parse plot2d file

    print grid
    print origin
    print endpoint[0]
    print endpoint[1]
    print rows[0]
    
    
    
rootdir = "/home1/srigamonti/projects/stm/runs/97/"
parse_plot2d(rootdir+"input.xml", rootdir+"STM2d2D.XML")