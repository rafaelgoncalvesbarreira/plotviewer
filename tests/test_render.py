from matplotlib.figure import Figure
import plotviewer.plotviewer as pv

fig = Figure()
ax = fig.add_subplot(111)
ax.plot([5,1,9,2,4,8,3])
pv.show(fig)

ax.plot([1,9,2,4,8,3,5])
pv.show(fig)