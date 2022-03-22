# -*- coding: utf-8 -*-
# Indexing, Selecting and Assigning

import pandas as pd

exam_scores = pd.read_csv('C:/Users/alexc/Documents/Bootcamp/data/exam_scores.csv')
print(exam_scores.head())
print(exam_scores.info())

#  df.iloc[row , columns] Index - based selection is to select data based
#  on its numerical position in dataframe
print(exam_scores.iloc[0, 0])
print(exam_scores.iloc[0:5, 4])
print(exam_scores.iloc[[0, 1, 2, 3], 2])
print(exam_scores.iloc[-5:, 0:2])

#  df.loc[ , ] Label based selection selects data based on
# the column or row names/index, loc is used for selecting data based on
# the data index value/name, not the numerical positions
print(exam_scores.loc[0, 'race/ethnicity'])
print(exam_scores.loc[0:5, ['gender', 'lunch', 'math score']])


print(exam_scores.gender)  # Attribute (Dot) Based Selection
print(exam_scores['gender'])  # Dictionary [Bracket] Based Selection
print(exam_scores[['gender', 'lunch']])  # Multiple Columns use double brackets
print(exam_scores.lunch == 'standard')  # Conditional Selection return True/False
print(exam_scores[exam_scores.lunch == 'standard'])  # Get all the columns of the row that satisfies the condition
exam_scores.gender = 'unisex'  # Replace all rows in a especific columns with a value or name
print(exam_scores)
