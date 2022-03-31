# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:49:52 2022

@author: alexc
"""

import numpy as np
import pandas as pd

# LOAD THE DATASET
titanic_data = pd.read_csv('C:/Users/alexc/Documents/Bootcamp/data/titanic.csv', index_col= 'PassengerId')


# QUESTION 1
print(titanic_data.info())
print(titanic_data.Fare.shape)
print(titanic_data['Sex'].value_counts())


# QUESTION 2
# Most of the passengers have _______ siblings/spouses
print(titanic_data['SibSp'].value_counts())
print(titanic_data.SibSp.value_counts())

# QUESTION 3
# Survived: This feature have value 0 and 1.
# 0 for not survived and 1 for survived
print(titanic_data['Survived'].value_counts())
print(titanic_data['Survived'].mean())

# QUESTION 4
# THE ANSWER IS THE 50% VALUE, NOT MEAN VALUE
print(titanic_data.Fare.describe())

# QUESTION 5
# 0 for not survived and 1 for survived
print(titanic_data[['Survived', 'Sex']].value_counts())
print(titanic_data[['Survived', 'Sex']].groupby('Sex').mean())
print(titanic_data.groupby(['Pclass', 'Survived'])['Survived'].sum())

# QUESTION 6
survived_passengers = titanic_data[(titanic_data['Survived'] == 1) | (titanic_data['Embarked'] == 'S')]
survived_passengers = titanic_data.loc[titanic_data['Survived'] == 1, 'Survived']
print(survived_passengers.head())

print(titanic_data.groupby(['Embarked', 'Survived'])['Survived'].sum())


# QUESTION 7


# QUESTION 8

data = titanic_data.sort_values('Fare', ascending=False)
print(data.Fare.head())


# QUESTION 9
# THE ANSWER IS THE 50% VALUE, NOT MEAN VALUE
print(titanic_data.Age.describe())


# QUESTION 10
print(titanic_data.Name.describe())
