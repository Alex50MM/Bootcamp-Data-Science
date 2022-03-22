# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 01:24:04 2022

@author: alexc
"""

import numpy as np  # for array related operations
import pandas as pd  # for working with CSV files
import matplotlib.pyplot as plt  # for data visualization

sma = pd.read_csv('C:/Users/alexc/Documents/Bootcamp/data/Standard_Metropolitan_Areas_Data-data.csv')
print(sma.info())

# Plotting Consecutive Plots
plt.plot(sma.work_force, sma.income, color='r')
plt.show()
plt.plot(sma.physicians, sma.income)
plt.show()

# Combining the 2 plots into 1
plt.plot(sma.work_force, sma.income, color='r')
plt.plot(sma.physicians, sma.income)
plt.show()

# Making The Plots Descriptive

# Adding Title
plt.scatter(sma.percent_senior, sma.crime_rate)
plt.title('Plot of Crime Rate vc Percent Senior')  # Adding a title to the plot
plt.show()

# Adding Labels
plt.scatter(sma.percent_senior, sma.crime_rate)
plt.title('Plot of Crime Rate vc Percent Senior')  # Adding a title to the plot
plt.xlabel('Percent Senior')  # Adding label for the Horizontal axies
plt.ylabel('Crime Rate')  # Adding label for the Vertical axies
plt.show()

# Adding a Legend
plt.plot(sma.work_force, sma.income, color='r', label='work_force')
plt.plot(sma.physicians, sma.income, label='physicians')
plt.legend()
plt.show()


# Formatting The Plots

# Changing Colours
plt.plot(sma.physicians, sma.income, color='blue')
plt.plot(sma.work_force, sma.income, color='c')
plt.plot(sma.hospital_beds, sma.income, color='0.75')
plt.show()

'''
Matplotlib recognizes the following formats to specify a color.
ALWAYS USE: color=
Hexadecimal - '#0f0f0f80'
RGB tuple of float values in a closed interval [0, 1 - (0.1, 0.2, 0.5)
HTML Color Names - 'aquamarine', 'mediumseagreen'

'''

# Changing LineStyles
plt.plot(sma.work_force, sma.income, linestyle='dashed')  # Default style
#plt.plot(sma.work_force, sma.income, linestyle='--')  # Shortcut for dashed line

'''
Other Styles

plt.plot(sma.work_force, sma.income, linestyle='solid')  # Default style
plt.plot(sma.work_force, sma.income, linestyle='-')  # Shortcut for dashed line
plt.plot(sma.work_force, sma.income, linestyle='dashdot')  # Default style
plt.plot(sma.work_force, sma.income, linestyle='-.')  # Shortcut for dashed line
plt.plot(sma.work_force, sma.income, linestyle='dotted')  # Default style
plt.plot(sma.work_force, sma.income, linestyle=':')  # Shortcut for dashed line

'''
plt.xlabel('Work Force')
plt.ylabel('Income')
plt.show()

# Adding Markers
plt.plot(sma.work_force, sma.income, marker='o')  # circular marker
#plt.plot(sma.work_force, sma.income, marker='x')  # crosses marker
#plt.plot(sma.work_force, sma.income, marker='^')  # triangles marker
plt.xlabel('Work Force')
plt.ylabel('Income')
plt.show()


# Combining the 3 Formatting Option
plt.plot(sma.work_force, sma.income, color='r', linestyle='solid', marker='^')
plt.xlabel('Work Force')
plt.ylabel('Income')
plt.show()