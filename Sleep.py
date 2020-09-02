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

class GraphPage_(tk.Frame):
    df_1 = 0
    df_2 = 0
    df_3 = 0
    df_4 = 0
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label= tk.Label(self, text='Graph page', font=MID_FONT)
        label.pack(pady=10,padx=10)       
        ttk.Button(self, text='Data page',
                   command=lambda: controller.show_frame(DataPage.DataPage_)).pack()

        self.bind("<<ShowGraph>>", self.plot_graph)

    def plot_graph(self, event):
        df_1 = self.controller.df_1
        df_2 = self.controller.df_2
        df_3 = self.controller.df_3
        df_4 = self.controller.df_4

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)

        a.plot(df_1['mean'])
        a.plot(df_2['mean'])
        a.plot(df_3['mean'])
        a.plot(df_4['mean'])
        a.legend(['bsl morning', '1st expo', 'bsl noon', '2nd expo'])
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    






