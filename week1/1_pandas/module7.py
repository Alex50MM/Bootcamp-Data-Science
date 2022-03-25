# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:43:57 2022

@author: alexc
"""

# MISSING DATA
# Missing data (or missing values) is defined as the data value that are not
# stored in a column or row

import pandas as pd

exam_scores = pd.read_csv('C:/Users/alexc/Documents/Bootcamp/data/exam_scores.csv')
print(exam_scores.head())
print(exam_scores.info())

# isna() and isnull(), both return the DataFrame with boolean values 
print(exam_scores.isna())
print(exam_scores.isnull())
print(exam_scores.isnull().sum()) # Retorn the number of null rows by column

# fillna() fill (preenche) the cell ,NaN, with data you put inside ()
# dataframe still contains missing values in the column.
# The changes are not made inplace. Temporary change
print(exam_scores.lunch.fillna('unknown')) 
print(exam_scores)

# inplace make changes in the original DataFrame
print(exam_scores.lunch.fillna('unknown', inplace = True))

# There is still a missing value in 'Marks%' column. Let's say we want to fill the missing value in this column with the mean of the marks scored by other people.
# Finding the mean() from a column
print(exam_scores['math score'].mean())

# fill the missing value with mean number
print(exam_scores['math score'].fillna(exam_scores['math scores'].mean().inplace = True)
print(exam_scores)
