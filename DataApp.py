import tkinter as tk
import pandas as pd 

from StartPage import StartPage_
from DataPage import DataPage_
from GraphPage import GraphPage_
from IndividualReport import IndividualReport_
from CompareExperiments import CompareExperiments_
from HourAve import HourAve_

LARGE_FONT = ('Verdana', 12)
MID_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)

class DataApp_(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)     
        tk.Tk.wm_title(self, "flyGUI v0.2.0")
        
        container = tk.Frame(self)

        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.df = pd.DataFrame()
        self.dfEdited = pd.DataFrame()

        self.frames = {}      
        for F in (StartPage_, DataPage_, GraphPage_, IndividualReport_, CompareExperiments_, HourAve_):
            frame = F(container, self)        
            self.frames[F] = frame       
            frame.grid(row=0, column=0, sticky='nsew')       
        self.show_frame(DataPage_)

    def show_frame(self, cont):   
        frame = self.frames[cont]       
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")
        if(type(frame).__name__ == 'GraphPage_'):
            frame.event_generate("<<ShowGraph>>")

        if(type(frame).__name__ == 'HourAve_'):
            frame.event_generate("<<ShowHourGraph>>")