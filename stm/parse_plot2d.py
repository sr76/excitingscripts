import numpy as np
import os
import sys
from lxml import etree
import xml_parsing_tools as xpt

def parse_plot2d(inputxmlpath,plot2dxmlpath):

    inputtree = etree.parse(inputxmlpath)
    plot2dtree = etree.parse(plot2dxmlpath)
    
    origin = xpt.attrib2float(plot2dtree,'/plot2d/grid/@origin')
    grid = xpt.attrib2int(plot2dtree,'/plot2d/grid/@gridticks')

    print origin, grid
    
    
rootdir = "/home1/srigamonti/projects/stm/runs/97/"
parse_plot2d(rootdir+"input.xml", rootdir+"STM2d2D.XML")