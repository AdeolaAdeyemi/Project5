print ("Financial data ABD Company")
Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
Revenue = [145, 760, 861, 917, 805, 810, 114, 976, 103, 143, 107, 154]
Expenses = [120, 569, 123, 120, 865, 840, 328, 582, 697, 166, 100, 380]
print (Months)
print (Revenue)
print (Expenses)
import numpy as np
np.Profit = np.array(Revenue) - np.array(Expenses)
Profit = (np.Profit)
print (Profit)
#Create a dictionary
Fin_status = {}
y = 0
for x in Months:
    Fin_status[x] = Profit[y]
    y=y+1
print (Fin_status)
import pandas as pd
#Create Panda Series
Dframe= pd.Series(Fin_status)
print (Dframe)
#Create New graph
print (Dframe.plot.line(x='Months', y='Profit'))
