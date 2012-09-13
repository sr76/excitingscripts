import numpy as np
import os
import sys
from lxml import etree

def parse_plot2d(inputxmlpath,plot2dxmlpath):

    inputtree = etree.parse(inputxmlpath)
    plot2dtree = etree.parse(plot2dxmlpath)
    
    str2dbl_vec = lambda v :[float(v[0]),float(v[1]),float(v[2])]
    
    origin = str2dbl_vec(plot2dtree.xpath('/plot2d/grid/@origin')[0].split())

    print origin
    
    
rootdir = "/home1/srigamonti/projects/stm/runs/97/"
parse_plot2d(rootdir+"input.xml", rootdir+"STM2d2D.XML")