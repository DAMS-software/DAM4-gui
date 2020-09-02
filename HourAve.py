import tkinter as tk
from tkinter import ttk

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
#from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT
from matplotlib.figure import Figure

import DataPage
from DataEdit import DataEdit_

LARGE_FONT = ('Verdana', 12)
MID_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)

class HourAve_(tk.Frame):
    df_1 = 0

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label= tk.Label(self, text='Graph page', font=MID_FONT)
        label.pack(pady=10,padx=10)       
        ttk.Button(self, text='Back to Data page ',
                   command=lambda: controller.show_frame(DataPage.DataPage_)).pack()

        self.bind("<<ShowHourGraph>>", self.plot_ave_hour_graph)

    def plot_ave_hour_graph(self, event):
        try:
            self.canvas.get_tk_widget().pack_forget()
        except AttributeError:
            pass

        df = self.controller.df_hour_ave


        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)

        a.plot(df['mean'])

        a.legend(['hour average'])
        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas.draw()


    






