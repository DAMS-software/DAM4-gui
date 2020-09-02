# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:24:37 2019

@author: mile
"""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd

import DataPage
from DataEdit import DataEdit_

LARGE_FONT = ('Verdana', 12)
MID_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)

class CompareExperiments_(tk.Frame):
    def on_show_frame(self, event: object) -> object:
        T = tk.Text(self, height=25, width=130, wrap=None)
        T.grid(row=4, columnspan=4, rowspan=20, padx=10, pady=10)
        
        T.insert(tk.END, self.controller.exp_comp_results.to_string())

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label= tk.Label(self, text='Experiment comparing', font=MID_FONT)
        label.grid(pady=10,padx=10)     
        ttk.Button(self, text='Back to Data page ',
                   command=lambda: controller.show_frame(DataPage.DataPage_)).grid(column=1)

        ttk.Button(self, text='Browse experiment 1',
                   command=self.browse_exp_1).grid(row=1, padx=10, pady=10)
        ttk.Button(self, text='Browse experiment 2',
                   command=self.browse_exp_2).grid(row=2, padx=10, pady=10)
        ttk.Button(self, text='Browse experiment 3',
                   command=self.browse_exp_3).grid(row=3, padx=10, pady=10)
        ttk.Button(self, text='Compare experiments',
                   command=lambda: DataEdit_.compare_experiments(
                       self,
                       self.controller.df_exp_1,
                       self.controller.df_exp_2,
                       self.controller.df_exp_3)).grid(row=3, column=1, padx=10, pady=10)

        self.bind("<<ShowFrame>>", self.on_show_frame)

    def browse_exp_1(self):
        filepath = filedialog.askopenfilename(
            initialdir = r"C:\\Users\\Desktop\\gui-master",
            title = "Select file",
            filetypes = (('xlsx','*.xlsx'),
            ("all files","*.*")))
        #controller je tk koji je pozvao ovaj prozor, odnosno DataApp, znači ovo sprema pandas dataframe u globalnu varijablu u DataApp
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_rows', None, 'display.max_columns', None)

        self.controller.df_exp_1 = pd.read_excel(filepath, index_col=0 )

    def browse_exp_2(self):
        filepath = filedialog.askopenfilename(
            initialdir = r"C:\\Users\\Desktop\\gui-master",
            title = "Select file",
            filetypes = (('xlsx','*.xlsx'),
            ("all files","*.*")))
        #controller je tk koji je pozvao ovaj prozor, odnosno DataApp, znači ovo sprema pandas dataframe u globalnu varijablu u DataApp
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_rows', None, 'display.max_columns', None)

        self.controller.df_exp_2 = pd.read_excel(filepath, index_col=0 )

    def browse_exp_3(self):
        filepath = filedialog.askopenfilename(
            initialdir = r"C:\\Users\\Desktop\\gui-master",
            title = "Select file",
            filetypes = (('xlsx','*.xlsx'),
            ("all files","*.*")))
        #controller je tk koji je pozvao ovaj prozor, odnosno DataApp, znači ovo sprema pandas dataframe u globalnu varijablu u DataApp
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_rows', None, 'display.max_columns', None)

        self.controller.df_exp_3 = pd.read_excel(filepath, index_col=0 )

