# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 12:45:40 2022

@author: Robbier20
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to load json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
 
 
#transform to dataframe
loandata = pd.DataFrame(data)   
 
#Finding unique values for the purpose column
loandata['purpose'].unique()

#describe the data
loandata.describe()    

#describe the data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using the EXP() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

#FICO score
fico = 718
# fico >= 300 and < 400:'Very Poor'
# fico >= 400 and ficoscore < 600:'Poor'
# fico >= 601 and ficoscore < 660:'Fair'
# fico >= 660 and ficoscore < 780:'Good'
# fico >=780:'Excellent'

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 700:
    ficocat = 'Good'
elif fico >= 700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)

#applying for loops to loan data

#using first 10

length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    if category >= 300 and category < 400:
        cat = 'very poor'
    elif category >= 400 and category < 600: 
        cat = 'Poor'
    elif category >= 601 and category < 660: 
        cat = 'Fair'  
    elif category >= 660 and category < 700: 
        cat = 'Good'     
    elif category >= 700: 
        cat = 'Excellent'
    else:
       cat = 'unknown'
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat

#df.loc as conditional statements
# df.loc[df[columnname] condition, newcolumnname] = 'value if the condition is met'

#for interest rates, a new column is wanted. rate >0.12 then high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'low'

#number of loans/rows by fico.category

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'red')
plt.show()


purposeplot = loandata.groupby(['purpose']).size()
purposeplot.plot.bar(color = 'red')
plt.show()

#scatter plots
ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint)
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv', index=True)
















