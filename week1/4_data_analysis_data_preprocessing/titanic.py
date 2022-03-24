# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 01:17:00 2022

@author: alexc
"""

import numpy as np
import pandas as pd

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

# pd.set_option('display.max_rows', 500) # If change to 1000 show all data
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1000)

train_data = pd.read_csv('C:/Users/alexc/Documents/Bootcamp/data/titanic_data.csv')
train_data1 = pd.read_csv('C:/Users/alexc/Documents/Bootcamp/data/titanic_data.csv')

print(train_data.info())

print(train_data.head(3))


# Dropping Columns which no useful

cols = ['Name', 'Ticket', 'Cabin']  # Variable with columns that gonna drop
train_data = train_data.drop(cols, axis=1)  # dropping columns
train_data1 = train_data1.drop(cols, axis=1)  # dropping columns

print(train_data.info())


# Dropping rows having Missing Values
train_data = train_data.dropna()
print(train_data.info())



dummies = []

cols = ['Pclass', 'Sex', 'Embarked']
for col in cols:
    dummies.append(pd.get_dummies(train_data1[col]))
titanic_dummies = pd.concat(dummies, axis=1)


#
train_data1 = pd.concat((train_data1, titanic_dummies), axis=1)

# Convert Pclass, Sex and Embarked into columns and
# drop redundant same columns from the dataframe
train_data1 = train_data1.drop(cols, axis=1)
print(train_data1.info())

# Taking Care of Missing Data
# interpolate() will replace all missing data NaNs to interpolate values
# interpolate do the same median do
train_data1['Age'] = train_data1['Age'].interpolate()
print(train_data1.info())