# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 20:27:46 2022

@author: alexc

https://www.justintodata.com/data-cleaning-techniques-python-guide/
"""

# Import the Dataset

import pandas as pd

house = pd.read_csv('C:/Users/alexc/Documents/Bootcamp/data/sberbank.csv')

print(house.info(verbose=True))

print(house.head())


# Separated Numerical and Non Numerical columns
numeric_cols = house.select_dtypes(include=['number']).columns
print(numeric_cols)
non_numeric_cols = house.select_dtypes(exclude=['number']).columns
print(non_numeric_cols)


# MISSING DATA
# Method #1: missing data (by columns) count & percentage
print(house[non_numeric_cols].info())

# create a variable with the total of missing data per columns
num_missing = house.isna().sum()
print(num_missing[:10])

# calculate the percentages of missing values by columns
pct_missing = house.isna().mean()
print(pct_missing[:10])

# Method #2: missing data (by columns) heatmap
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))

cols = house.columns[:30]
colours = ['#000099', '#ffff00']
sns.heatmap(house[cols].isna(), cmap=sns.color_palette(colours))

# missingno is a small library focused on missing data viz and utilities
# conda install -c conda-forge missingno
# pip install missingno

import missingno as msno
msno.matrix(house.iloc[:, :30])  # Missing data heatmap VERTICAL
msno.heatmap(house.iloc[:, :30])  # Heatmap SQUARE
msno.bar(house.iloc[:, :30])  # Bar  is a simple viz of nullity by column
msno.dendrogram(house.iloc[:, :30])  # Dendrogram revealing trends deeper


# Method #3: missing data (by rows) histogram
missing_by_row = house.isna().sum(axis='columns')
print(missing_by_row.hist(bins=50))



# CLEANING THE MISSING DATA
# Technique #1: drop columns / features

# We drop the entire column or feature with missing data, which will
# certainly cause a loss of information
print(pct_missing[pct_missing > .3])  # show columns with over 30% missing data

# drop the columns with more then 30% of missing data
house_less_missing_cols = house.loc[:, pct_missing <= .3].copy()
print(house_less_missing_cols.shape)   # show number of rows and columns
print(house.shape)


# Technique #2: drop rows / observations
house_less_missing_rows = house[missing_by_row < 35].copy()
print(house_less_missing_rows.shape)


# Technique #3: impute the missing with constant values
house_copy = house.copy()
house_copy[numeric_cols] = house_copy[numeric_cols].fillna(-999)
house_copy[non_numeric_cols] = house_copy[non_numeric_cols].fillna('_MISSING_')


# Technique #4: impute the missing with statistics

# we can impute the numeric columns with their respective medians
house_copy2 = house.copy()
med = house_copy2[numeric_cols].median()
house_copy2[numeric_cols] = house_copy2[numeric_cols].fillna(med)


# We can also impute the non-numeric columns with their most frequent values
most_freq = house_copy2[non_numeric_cols].describe().loc['top']
print(most_freq)
# Then we can use it to fill in the missing
house_copy2[non_numeric_cols] = house_copy2[non_numeric_cols].fillna(most_freq)


'''
Continuar amanhã
https://www.justintodata.com/data-cleaning-techniques-python-guide/
Irregular data (outliers)
'''

# Irregular data (outliers)
# outliers is broadly defined for numeric data only

# Method #1: descriptive statistics
print(house.kurt(numeric_only=True)[:10])  # single statistic to detect potential outlier

print(house['life_sq'].describe())


# Method #2: histogram & box plot
print(house['life_sq'].hist(bins=100))  # Histogram
print(house.boxplot(column=['life_sq']))  # Boxplot


# Method #3: bar chart
print(house['ecology'].value_counts().plot(kind='bar'))


# Unnecessary data
# Unnecessary type #1: repetitive & uninformative

num_rows = len(house)

for col in house.columns:
    cnts = house[col].value_counts(dropna=False)
    top_pct = (cnts / num_rows).iloc[0]
    
    if top_pct > 0.999:
        print('{0}: {1:, .2f}%'.format(col, top_pct*100))
        print(cnts)
        print()

# Unnecessary type #2: irrelevant
# When the features are not serving the project’s goal, we can remove them.
# You could use the drop method in pandas


# Unnecessary type #3: duplicates
# Duplicates type #1: all columns based
print(house[house.duplicated()])
print(house.drop_duplicates())


# Duplicates type #2: key columns based
print(house[house.drop(columns=['id']).duplicated()])

# We could remove them and save the new dataset as df_dedupped.
# We can also compare the shapes of the two datasets (df and df_dedupped)
house_dedupped = house.drop(columns=['id']).drop_duplicates()

print(house.shape)
print(house_dedupped.shape)