# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 22:25:50 2022

@author: alexc
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

housing = pd.read_csv('C:/Users/alexc/Documents/Bootcamp/data/house_ames.csv')

print(housing.info())

# print(ames.isnull().sum())  # list the count of missing data from all columns

# We not will work with 81 columns,
# so let's create some variables with the columns that we gonna work
numerical = ['SalePrice', 'LotArea','OverallQual', 'OverallCond', \
             '1stFlrSF', '2ndFlrSF', 'BedroomAbvGr']
categorical = ['MSZoning', 'LotShape', 'Neighborhood', \
               'CentralAir', 'SaleCondition', 'MoSold', 'YrSold']

housing = housing[numerical + categorical]  # Redefine the DataFrame with the variables
print(housing.shape)  # Show entries (1460) and columns (14)

# Creating a Histogram Plot
# The style of the Plot
sns.set(style='whitegrid', palette='deep', font_scale=1.1, rc={'figure.figsize': [8, 5]})
# The Histogram Plot
sns.distplot(housing['SalePrice'], norm_hist=False, kde=False, bins=20, hist_kws={'alpha': 1}).set(xlabel='Sale''Price', ylabel='Count');

# Create histograms for all numerical variables (PANDAS)
housing[numerical].hist(bins= 15, figsize= (15, 6), layout= (2, 4));

# Show the counts of observations in each categorical bin using bars (SEABORN)
sns.countplot(housing['SaleCondition']);

# create a figure with a grid of 2 rows and 4 columns
# The 2nd for loop gets each x-tick label and rotates it 90° to make the text fit on the plots better
fig, ax = plt.subplots(2, 4, figsize=(20, 10))
for variable, subplot in zip(categorical, ax.flatten()):
    sns.countplot(housing[variable], ax=subplot)
    for label in subplot.get_xticklabels():
        label.set_rotation(90)

# inspecting by month of register
housing[housing['YrSold'] == 2010].groupby('MoSold')['YrSold'].count()

# Analyzing Relationships Between Numerical Variables

# visualizing relationships between two numerical variables
sns.scatterplot(x=housing['1stFlrSF'], y=housing['SalePrice']);  # SEABORN

# jointplot give you a plot showing with histograms of each variable
sns.jointplot(x=housing['1stFlrSF'], y=housing['SalePrice']);

# Relationships Between Numerical and Categorical Variables
# plots for each of our categorical variables and relationships with SalePrice
fig, ax = plt.subplots(3, 3, figsize=(15, 10))
for var, subplot in zip(categorical, ax.flatten()):
    sns.boxplot(x=var, y='SalePrice', data=housing, ax=subplot)

# Sorted plot showing relationship between Neighborhood and SalePrice (SEABORN)
sorted_nb = housing.groupby(['Neighborhood'])['SalePrice'].median().sort_values()
sns.boxplot(x=housing['Neighborhood'], y=housing['SalePrice'], order=list(sorted_nb.index))
plt.xticks(rotation=45)  # apply rotation in X labels names

# For each individual neighborhood we can see the relationship between OverallQual and SalePrice
cond_plot = sns.FacetGrid(data=housing, col='Neighborhood', hue='CentralAir', col_wrap=4)
cond_plot.map(sns.scatterplot, 'OverallQual', 'SalePrice');
