# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:22:37 2022

@author: alexc
"""

import numpy as np  # for array related operations
import pandas as pd  # for working with CSV files
import matplotlib.pyplot as plt  # for data visualization

sma = pd.read_csv('C:/Users/alexc/Documents/Bootcamp/data/Standard_Metropolitan_Areas_Data-data.csv')
print(sma)
print(sma.info())

# Question 1


# Question 2


# Question 3
print(sma.describe())
print(sma.income.describe())
print(sma.region.count())
print(sma.region.value_counts())

print(sma.sort_values(by = 'land_area'))


sample_data1 = sma[sma.region == 1]
print(sample_data1)


plt.plot(sma.land_area, sma.crime_rate) # 2 arguments: X an Y points
plt.show()


plt.scatter(sma.physicians, sma.hospital_beds)  # Plotting the scatter plot
plt.show()  # Showing the figure

