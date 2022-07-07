# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 01:46:25 2022

@author: Robbier20
"""

import pandas as pd
# file_name = pd.read_csv('file.csv')<---- of read_csv

data = file_name = pd.read_csv('transaction.csv')

data = file_name = pd.read_csv('transaction.csv', sep=';')

# Summary of the data
data.info()

# Playing around with variables
var = True

# Working with calculations

#Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

# Mathematical Operatoins on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased*ProfitPerItem
CostPerTransactoin = CostPerItem*NumberofItemsPurchased
SellingPricePerTransaction = NumberofItemsPurchased*SellingPricePerItem

# Cost Per Transaction Column Calculation
# CostPerTransaction = CostPerIten * NumberofItemsPurchases
# variable = dataframe['column_name']
CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransactoin = CostPerItem * NumberOfItemsPurchased

# Adding a new column to a dataframe

data['CostPerTransaction'] = CostPerTransactoin

# Sales per Transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit Calculation = sales - Cost

data['ProfitperTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# Markup = (Sales - Cost) / Cost

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/ data['CostPerTransaction']


# Rounding Marking

roundmarkup = round(data['Markup'], 2)
data['Markup'] = round(data['Markup'], 2)


# Combining data fields

#Checking column data type

print(data['Day'].dtype)

#Changing column type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year

data['Date'] = my_date

#Using split to split the client keywords fields
#new_var = column.str.split('sep' , expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand = True)

#creating new columns for the split columns in client keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']' , '')

#using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files

#bring in a new dataset

seasons = file_name = pd.read_csv('value_inc_seasons.csv' , sep = ';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key)

data = pd.merge(data, seasons, on = 'Month')

#dropping columns

# df = df.drop('columnname' , axis = 1)

data = data.drop('ClientKeywords' , axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Year', 'Month'], axis = 1)

#Export into as csv

data.to_csv('ValueInc_Cleaned.csv', index = False)
