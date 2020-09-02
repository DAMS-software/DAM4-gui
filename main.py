"""
	Data Selection and visualization app based on Tkinter and Gui
	Created April 2019
	Copyright (C) Milan Petrovic
	
	This program is free software; you can redistribute it and/or
    modify it under the terms of the GNU General Public License
    as published by the Free Software Foundation; either version 3
    of the License, or (at your option) any later version.
	
	This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""

from DataApp import DataApp_
import tkinter
import pandas
import matplotlib
import sys
import openpyxl

def main():
    print('python: ' + str(sys.version))
    print('tkinter: ' + str(tkinter.TkVersion))
    print('pandas: ' + str(pandas.__version__))
    print('matplotlib: ' + str(matplotlib.__version__))
    print('openpyxl: ' + str(openpyxl.__version__))
    app = DataApp_()

    app.mainloop()
    	
    
if __name__ == '__main__':
	main()
	