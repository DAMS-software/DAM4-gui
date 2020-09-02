import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import pandas as pd

from DataEdit import DataEdit_
from GraphPage import GraphPage_
from IndividualReport import IndividualReport_
from CompareExperiments import CompareExperiments_
from HourAve import HourAve_

#import GraphPage
LARGE_FONT = ('Verdana', 12)
MID_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)

class DataPage_(tk.Frame):
    """
    """
    #učitavanje pandas podataka u tablicu
    def on_show_frame(self, event):
        T = tk.Text(self, height=40, width=210, wrap=None)
        T.grid(row=2, column=4, columnspan=14, rowspan=14, padx=10, pady=10)
        T.config(state='normal')
        T.delete('1.0', tk.END)
        T.insert(tk.END, self.controller.df.to_string())

        # create a Scrollbar and associate it with txt
        scrollb = ttk.Scrollbar(self, command=T.yview)
        scrollb.grid(row=2, column=19, rowspan=14, sticky='nsew')
        T['yscrollcommand'] = scrollb.set

        scrollbx = ttk.Scrollbar(self, command=T.xview, orient='horizontal')
        scrollbx.grid(row=16, column=3, columnspan=14, sticky='nsew')
        T['xscrollcommand'] = scrollbx.set


    def filter_data(self,start_col,end_col,start_row,end_row):
        DataEdit_.select_cols_rows(self,start_col,end_col, start_row, end_row)
        T = tk.Text(self, height=40, width=200, wrap=None)
        T.grid(row=2, column=4, columnspan=14, rowspan=14, padx=10, pady=10)
        T.config(state='normal')
        T.delete('1.0','end')
        T.insert(tk.END, self.controller.df.to_string())

    def browse(self):
        filepath = filedialog.askopenfilename(
            initialdir = r"C:\\Users\\Desktop\\gui-master",
            title = "Select file",
            filetypes = (('txt','*.txt'),
            ("all files","*.*")))
        #controller je tk koji je pozvao ovaj prozor, odnosno DataApp, znači ovo sprema pandas dataframe u globalnu varijablu u DataApp
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None, 'display.max_columns', None)

        self.controller.df = pd.read_csv(filepath, sep='\t', header=None)
        DataEdit_.clear_data(self)
        #self.controller.df = DataEdit_.get_stats(self)
        self.on_show_frame(self)

    #def split_table(self, start_bsl_morning, start_1st_expo, start_bsl_noon, start_2nd_expo):
    #    DataEdit_.split_for_graph(self, start_bsl_morning, start_1st_expo, start_bsl_noon, start_2nd_expo)
        
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        tk.Label(self, text='Data edit').grid(pady=10,padx=10)
        
        ttk.Button(self, text='Browse files',
                   command=self.browse).grid(row=1)

        ttk.Button(self, text='Stats (mean/std/sum)',
                   command=lambda: DataEdit_.get_stats(self)).grid(row=1, column=4)

        ttk.Button(self, text='Consumption pop activity',
                   command=lambda: DataEdit_.d_stats(self)).grid(row=1, column=5)

        ttk.Button(self, text='F00 3',
                   command=lambda: controller.show_frame(HourAve_)).grid(row=1, column=6)


        self.controller = controller

        self.bind("<<ShowFrame>>", self.on_show_frame)

        #########ROWS AND COLUMNS SELECTION COL0####################################
        ttk.Label(self, text='Select flies:', font=MID_FONT).grid(row=2, column=1)           
        ttk.Label(self, text="Start column:" , font=SMALL_FONT).grid(row=3)
        ttk.Label(self, text="End column:", font=SMALL_FONT).grid(row=4)       
        
        start_col = '1' #tk.StringVar()
        end_col = '15' #tk.StringVar()
        self.start_col = ttk.Entry(self, textvariable=start_col).grid(row=3, column=1)     
        self.end_col = ttk.Entry(self, textvariable=end_col).grid(row=4, column=1)                    


        """           s1 selection COL1            """
        ttk.Label(self, text='Time selection:', font=MID_FONT).grid(row=6, column=1)    
        ttk.Label(self, text="Start time:" , font=SMALL_FONT).grid(row=8)
        ttk.Label(self, text="End time:", font=SMALL_FONT).grid(row=9)       
               
        start_row = '2020-04-06 00:00' #tk.StringVar()
        end_row = '2020-04-06 23:59' #tk.StringVar()
        self.start_row = ttk.Entry(self, textvariable=start_row).grid(row=8, column=1)     
        self.end_row = ttk.Entry(self, textvariable=end_row).grid(row=9, column=1)                    
        """
        ttk.Button(self, text='Select main table', command=lambda: DataPage_.filter_data(self, start_col.get(),
                                                                                         end_col.get(),
                                                                                         start_row.get(),
                                                                                         end_row.get())).grid(row=10, column=1, padx=10, pady=10)
        """
        ttk.Button(self, text='Select main table', command=lambda: DataPage_.filter_data(self, start_col,
                                                                                         end_col,
                                                                                         start_row,
                                                                                         end_row)).grid(row=10, column=1, padx=10, pady=10)


        
        
        
        ttk.Button(self, text='Save XLSX',
                   command=lambda: DataEdit_.save_to_xlsx(self.controller.df)).grid(row=20, column=4) 
        ttk.Button(self, text='Save TXT',
                   command=lambda: DataEdit_.save_to_txt(self.controller.df)).grid(row=20, column=5) 
        
               