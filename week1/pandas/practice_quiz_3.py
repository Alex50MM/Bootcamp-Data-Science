# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 02:51:45 2022

@author: alexc
"""

import pandas as pd

sma = pd.read_csv('C:/Users/alexc/Documents/Bootcamp/data/Standard_Metropolitan_Areas_Data-data.csv')
print(sma)
print(sma.info())

# Question 1
print(sma.iloc[9, 9])

# Question 2
print(sma.physicians)

# Question 3
'''
sample_data1 = sma
print(sample_data1)
'''
# Question 4
sample_data2 = sma[sma.region == 2]  # Get all the columns of the row that satisfies the condition
print(sample_data2)


