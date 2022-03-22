# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 03:45:04 2022

@author: alexc
"""
#Summary Functions

import pandas as pd

exam_scores = pd.read_csv('C:/Users/alexc/Documents/Bootcamp/data/exam_scores.csv')
print(exam_scores)

print(exam_scores.info())
print(exam_scores.describe())  # Return a summary about numerical columns only
print(exam_scores.describe(include='object'))  # Returned summary all categorical columns
print(exam_scores.describe(include='all'))  #  Summary about numerical and categorical column together

# count - the count of non - null entries in the particular column
# unique - the count of unique values in a column. Only for categorical column
# top - this is also for only categorical column. This tells which category is occurring maximum number of times
# freq - this is again for categorical column only. This tells you the number of occurence of the category that is occurring maximum number of times in the column
# mean - the mean value of the numerical column
# std - This is standard deviation of the numerical column. This tells you about the variation of data
# min - the minimum value in the numerical column
# 25% - the 25th percentile (or 1st quartile) value in the numerical column
# 50% - the 50th percentile (or 2nd quartile or the median) value in the numerical column
# 75% - the 75th percentile (or 3rd quartile) value in the numerical column
# max - the maximum value in the numerical column
# NaN values means for a particular column a particular summary value is not available

# To get summary, use [brackets] for name of columns with space, 
# For columns with simple word can use the name using dot(.)
print(exam_scores['math score'].describe())  # Summary of a particular column
print(exam_scores.gender.describe())  # Summary of a particular column


# Aggregation
print(exam_scores.mean())  # Returns only from numerical columns
print(exam_scores.gender.unique())  # Returns all unique values in column
print(exam_scores.gender.value_counts())  # Returns unique values and how many times they are occuring in the dataset
