# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 23:06:53 2022

@author: alexc
"""

import numpy as np  # for array related operations
import pandas as pd  # for working with CSV files
import matplotlib.pyplot as plt  # for data visualization

sma = pd.read_csv('C:/Users/alexc/Documents/Bootcamp/data/Standard_Metropolitan_Areas_Data-data.csv')
print(sma.info())

# The problem objective is to find the crime rate of each area

# Creating Scatter Plot
plt.scatter(sma.crime_rate, sma.percent_senior)  # Plotting the scatter plot
plt.show()  # Showing the figure


# Line Plot
plt.plot(sma.work_force, sma.income) # 2 arguments: X an Y points
plt.show()

# Creating a Line Plot with single argument
plt.plot([1, 2, 3, 4])  # 1 argument
plt.show()

# Histogram Plot
plt.hist(sma.percent_senior)
plt.show()


# Bar Plot

# Vertical Bar Plot
plt.bar(sma.region, sma.crime_rate)
plt.show()

# Horizontal Bar Plot
plt.barh(sma.region, sma.crime_rate)
plt.show()

# Pie Chart Plot

firms = ['Firm A', 'Firm B', 'Firm C', 'Firm D', 'Firm E']
market_share = [20, 25, 15, 10, 20]
Explode = [0.05, 0.15, 0.05, 0.05, 0.05]

plt.pie(market_share, explode=Explode, labels=firms, autopct='%1.1f%%')
plt.show()
