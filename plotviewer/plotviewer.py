import tkinter as tk
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

class PlotViewer():
  def __init__(self, figure, width=800, heigtht=500):
    self.root = tk.Tk()
    self.root.minsize(width, heigtht)
    self.root.wm_title("Plot Viewer")
    self.create_widgets(figure)
  
  def create_widgets(self, figure):
    canvas = FigureCanvasTkAgg(figure, master=self.root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, self.root)
    toolbar.update()

    button = tk.Button(master=self.root, text="Close", command=self._quit)
    button.pack(side=tk.BOTTOM)
  
  def show(self):
    self.root.mainloop()

  def _quit(self):
    self.root.quit()     # stops mainloop
    self.root.destroy() 
