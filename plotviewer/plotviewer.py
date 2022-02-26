import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.figure import Figure

def show(figure, width=800, heigtht=500):
  root = tk.Tk()
  root.minsize(width, heigtht)
  root.wm_title("Plot Viewer")

  canvas = FigureCanvasTkAgg(figure, master=root)  # A tk.DrawingArea.
  canvas.draw()
  canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

  toolbar = NavigationToolbar2Tk(canvas, root)
  toolbar.update()

  def _quit():
      root.quit()  
      root.destroy()
      
  button = tk.Button(master=root, text="Close", command=_quit)
  button.pack(side=tk.BOTTOM)
  
  root.mainloop()
