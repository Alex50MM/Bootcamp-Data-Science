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
print(sma.mean())

# Question 2
print(sma.region.unique())

# Question 3
print(sma.describe())
print(sma.income.describe())
print(sma.land_area.describe())

# Question 4
sample_data1 = sma[sma.region == 3]
print(sample_data1)
print(sample_data1.crime_rate.describe())
print(sample_data1.info())


# Question 5
print(sma.region.value_counts())