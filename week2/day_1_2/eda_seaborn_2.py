# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 22:37:27 2022

@author: alexc
"""
# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading example Dataset installed with Seaborn
tips = sns.load_dataset('tips')

print(tips.head())
# print(tips.shape)  # Show numbers of rows and columns in DataFrame
# print(tips.isnull().sum())  # Show the count of NULL entries in DataFrame
# print(tips.info())  # Show the type of data (dtypes) from each columns
print(tips.describe())  # Show the statistics of numerical data

# UNIVARIATE PLOTS
# plot single variable and show the frequency of uniques values
sns.distplot(tips['tip'], kde=False, bins=10)  # KDE false will show Histogram
sns.distplot(tips['tip'], kde=False, bins=30)  # KDE false will show Histogram
sns.distplot(tips['tip'], hist=False, bins=10)  # Histogram false will show KDE


# BIVARIATE PLOTS
# used when you need to find a relation between two variables and to find how
# the value of one variable changes the value of another variable
# Different types of plots are used based on the data type of the variable

# Statistical Data Types
# scatterplot - if you need to find the correlation between two variables scatterplot can be used
sns.relplot(x='total_bill', y='tip', data=tips)  # Default plot type of relplot is scatterplot
sns.relplot(x='total_bill', y='tip', hue='day', data=tips)
sns.relplot(x='total_bill', y='tip', hue='smoker', data=tips)

# Lineplot
#  the line joining all the dots by arranging the variable value on the x-axis
sns.relplot(x='total_bill', y='tip', kind='line', data=tips)
sns.relplot(x='total_bill', y='tip', sort=False, kind='line', data=tips)


# Categorical Data Types
# Scatterplot
sns.catplot(x='sex', y='tip', data=tips)
sns.catplot(x='day', y='total_bill', hue='sex', kind='swarm', data=tips)
sns.catplot(x='smoker', y='tip', order=['No', 'Yes'], data=tips)

# Boxplot
sns.catplot(x='day', y='total_bill', kind='box', data=tips)
sns.catplot(x='day', y='total_bill', hue='sex', kind='box', data=tips)

# Violin plot
sns.catplot(x='day', y='total_bill', hue='sex', kind='violin', data=tips)

# Point plots
sns.catplot(x='day', y='total_bill', hue='sex', kind='point', data=tips)
