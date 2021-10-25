import sys
from matplotlib import figure
sys.path.append("..")
import numpy as np
from matplotlib.figure import Figure
from plotviewer import PlotViewer

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

fig2 = Figure()
fig2.add_subplot(111).plot([5,1,9,2,4,8,3])

view = PlotViewer(fig2)
view.show()