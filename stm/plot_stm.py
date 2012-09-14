import parse_plot2d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.cm as cm # color map library
import os
import sys

args = sys.argv[1:]

rootdir = "/home1/srigamonti/projects/stm/runs/1347622007185/"
r, rl, func = parse_plot2d.parse_plot2d(rootdir+"input.xml", rootdir+"STM2d2D.XML")

nx = len(r)
ny = len(r[0])
x=[]
y=[]
#f=[]
for i in range(nx):
    x.append([])
    y.append([])
#    f.append([])
    for j in range(ny):
        x[i].append(r[i][j][0])
        y[i].append(r[i][j][1])
#        f[i].append(func[i][j])
xnp=np.array(x)
ynp=np.array(y)
fnp=np.array(func)

# Make plot
gray=1.00

cdict0 = {'red':   ((0.0,  gray, gray),
                   (1.0,  1.0, 1.0)),

         'green': ((0.0,  gray, gray),
                   (1.0,  0.0, 0.0)),

         'blue':  ((0.0,  gray, gray),
                   (1.0,  0.0, 0.0))}

cdict1 = {'red':   ((0.0,  gray, gray),
                   (1.0,  0.35, 0.35)),

         'green': ((0.0,  gray, gray),
                   (1.0,  0.5, 0.5)),

         'blue':  ((0.0,  gray, gray),
                   (1.0,  0.8, 0.8))}

white_red = LinearSegmentedColormap('whiteRed', cdict1)


fig=plt.figure(1,figsize=(8,5.5))

params = {'font.size':15,
          'xtick.major.size': 5,
          'ytick.major.size': 5,
          'patch.linewidth': 1.5,
          'axes.linewidth': 2.,
          'axes.formatter.limits': (-4, 6),
          'lines.linewidth': 1.0,
          'lines.markeredgewidth':2.0,
          'lines.markersize':18,
          'legend.fontsize':11,
          'legend.borderaxespad':1,
          'legend.borderpad':0.5,
          'savefig.dpi':80}

plt.rcParams.update(params)


ax=fig.add_subplot(111)

#ax.contour(x,y,func,cmap='whiteRed')
zmin=0.001
zmax=0.0035
ncontours = 10
levels=[]
for i in range(ncontours):
    levels.append(zmin+(zmax-zmin)/ncontours*i)

#cm.copper.set_under('yellow')
#cm.copper.set_over('cyan')
#ax.contourf(x,y,func,levels=levels,cmap=white_red,linewidths=0.1,antialiased=True, extend='both')
#ax.contourf(x,y,func,levels=levels,cmap=cm.copper,antialiased=True,extend='none')
#ax.imshow(func,cmap=cm.copper)
ax.pcolor(xnp,ynp,fnp,cmap=cm.copper)
#ax.contourf(x,y,func,ncontours)
#ax.set_zlim(zmin,zmax)

if "-png" in args:
    plt.savefig('PLOT.png', orientation='portrait',format='png')
else:
    plt.show()












