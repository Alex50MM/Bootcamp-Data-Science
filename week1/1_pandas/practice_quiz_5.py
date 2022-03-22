# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:07:49 2022

@author: alexc
"""

import pandas as pd

sma = pd.read_csv('C:/Users/alexc/Documents/Bootcamp/data/Standard_Metropolitan_Areas_Data-data.csv')
print(sma)
print(sma.info())

# Question 1
sorted_data1 = sma.sort_values(by='crime_rate', ascending=False)
print(sorted_data1.head())

# Question 2


# Question 3

