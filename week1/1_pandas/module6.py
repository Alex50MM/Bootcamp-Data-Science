# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 01:28:23 2022

@author: alexc
"""

# SORTING AND RENAMING

import pandas as pd

exam_scores = pd.read_csv('C:/Users/alexc/Documents/Bootcamp/data/exam_scores.csv')
print(exam_scores.head())
print(exam_scores.info())

# Result in ascending method
print(exam_scores.sort_values(by = 'math score').head())

# Result in descending method
print(exam_scores.sort_values(by = 'math score', ascending = False).head())

# Sort a series using the sort_values() method
# Ascending method
print(exam_scores['math score'].sort_values)

# Descending method
print(exam_scores['math score'].sort_values(ascending = False) [:10])


# RENAMING
'''exam = exam_scores.rename(
    columns={
        'race/ethnicity': 'race',
        'parental level of education': 'parent_education_level',
        'test preparation course': 'test_prep_course',
        'math score': 'math_score',
        'reading score': 'reading_score',
        'writing score': 'writing_score'
        }, inplace=True
    )
print(exam.head())'''

exam = exam_scores.rename(
    columns={
        'race/ethnicity': 'race',
        'parental level of education': 'parent_education_level',
        'test preparation course': 'test_prep_course',
        'math score': 'math_score',
        'reading score': 'reading_score',
        'writing score': 'writing_score',
    }
)

print(exam.columns)
print(exam.info())
print(exam.head())

# Rename the indexes of the dataframe using the rename() 
print(exam.rename(index = {0: 'zero', 1: 'one', 3: 'three'}).head())
