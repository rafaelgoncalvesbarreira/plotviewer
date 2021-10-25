from matplotlib.figure import Figure
import plotviewer.plotviewer as pv

fig = Figure()
fig.add_subplot(111).plot([5,1,9,2,4,8,3])

pv.show(fig)