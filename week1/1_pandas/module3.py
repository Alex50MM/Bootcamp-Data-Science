# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 19:56:16 2022

@author: alexc
"""
# Read Files
# Import the library that we gonna use
import pandas as pd

# Create a variable associated with our dataset
exam_scores = pd.read_csv('data/exam_scores.csv')
print(exam_scores)  # Show our DataFrame

print(exam_scores.shape)  # Show the number of rows and columns from our DataFrame

print(exam_scores.head())  # head() show the first 5 rows from our DataFrame
print(exam_scores.tail())  # tail() show the last 5 rows from our DataFrame

print(exam_scores.dtypes)  # Show atributes of columns (object [strings], int, float)
print(exam_scores.info())  # Show a summary about the DataFrame
