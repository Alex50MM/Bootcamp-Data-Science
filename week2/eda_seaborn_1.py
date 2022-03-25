# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 22:25:50 2022

@author: alexc
"""

import pandas as pd
import matplotlib as plt

housing = pd.read_csv('C:/Users/alexc/Documents/Bootcamp/data/house_ames.csv')

print(housing.info())

# print(ames.isnull().sum())  # list the count of missing data from all columns

numerical = ['SalePrice', 'LotArea','OverallQual', 'OverallCond', \
             '1stFlrSF', '2ndFlrSF', 'BedroomAbvGr']
categorical = ['MSZoning', 'LotShape', 'Neighborhood', \
               'CentralAir', 'SaleCondition', 'MoSold', 'YrSold']

housing = housing[numerical + categorical]
print(housing.shape)
