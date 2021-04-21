import pandas as pd
import numpy as np
import login
import sys 
from tkinter import * 

root = Tk()
root.geometry('580x250')

dframe = pd.read_csv("./data/shopper.csv")
df1 = dframe[['nama_shopper', 'no_telp_shopper']]

txt = Text(root) 
txt.pack() 

class PrintToTXT(object): 
 def write(self, s): 
     txt.insert(END, s)

#sys.stdout = PrintToTXT() 
print (df1.values.tolist())

mainloop()