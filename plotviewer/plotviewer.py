import tkinter as tk
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

root = tk.Tk()

def show(figure, width=800, heigtht=500):
  root.minsize(width, heigtht)
  root.wm_title("Plot Viewer")

  canvas = FigureCanvasTkAgg(figure, master=root)  # A tk.DrawingArea.
  canvas.draw()
  canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

  toolbar = NavigationToolbar2Tk(canvas, root)
  toolbar.update()

  button = tk.Button(master=root, text="Close", command=_quit)
  button.pack(side=tk.BOTTOM)
  
  root.mainloop()

def _quit():
    root.quit()  
    root.destroy()