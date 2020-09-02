import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg

from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT
from matplotlib.figure import Figure

import DataPage
from datetime import datetime
#import seaborn as sns; sns.set()
import pandas as pd

LARGE_FONT = ('Verdana', 12)
MID_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)

class GraphPage_(tk.Frame):
    #df_1 = 0
    #df_2 = 0
    #df_3 = 0
    #df_4 = 0
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label= tk.Label(self, text='Graph page', font=MID_FONT)
        label.pack(pady=10,padx=10)       
        ttk.Button(self, text='Back to Data page ',
                   command=lambda: controller.show_frame(DataPage.DataPage_)).pack()

        self.bind("<<ShowGraph>>", self.plot_graph)


    def plot_graph(self,event):


        df = self.controller.df
        df.to_csv('df_prije.csv')
        print(df.shape)

        df_C = df[df.name.str.contains('^C')]
        df_C = df_C.groupby(['datetime']).mean()
        df_C = df_C.resample('H').sum().mean(axis=1)

        df_D = df[df.name.str.contains('^D')]
        df_D = df_D.set_index('datetime')

        df_D1 = df_D[df_D.name == 'D1'].drop(['name'], axis=1)
        df_D1 = df_D1.resample('H').mean().mean(axis=1)

        df_D2 = df_D[df_D.name == 'D2'].drop(['name'], axis=1)
        df_D2 = df_D2.resample('H').mean().mean(axis=1)

        df_D3 = df_D[df_D.name == 'D3'].drop(['name'], axis=1)
        df_D3 = df_D3.resample('H').mean().mean(axis=1)

        df_D4 = df_D[df_D.name == 'D4'].drop(['name'], axis=1)
        df_D4 = df_D4.resample('H').mean().mean(axis=1)

        df_all = pd.concat([df_D1, df_D2, df_D3, df_D4], axis=1)
        df_all.columns = ['D1', 'D2', 'D3', 'D4']
        print(df_all.shape)
        df_all.to_csv('df_obraden.csv')
        try:
            self.canvas.get_tk_widget().pack_forget()
        except AttributeError:
            pass
        """
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)

        a = sns.heatmap(df_all, cmap="YlGnBu", vmin=0, vmax=100, annot=True)
        a.set_yticklabels(pd.to_datetime(df_all.index).strftime('%d-%m %H:%M'))

        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas.draw()
        """

