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


plt.plot(sma.work_force, sma.income, '--ro')  # --: dashline, r: red color, o: circular marker
plt.xlabel('Work Force')
plt.ylabel('Income')
plt.show()

plt.plot(sma.work_force, sma.income, 'ro')  # r: red color, o: circular marker
plt.show()

plt.plot(sma.work_force, sma.income, 'gx')  # g: green color, x: x marker
plt.show()

'''
Other Options:

plt.plot(sma.work_force, sma.income, 'go')  # g: green color, o: circular marker
plt.plot(sma.work_force, sma.income, 'g^')  # g: green color, ^: triangles marker
plt.plot(sma.work_force, sma.income, 'ro')  # r: red color, o: circular marker
plt.plot(sma.work_force, sma.income, 'rx')  # r: red color, x: x marker
plt.plot(sma.work_force, sma.income, 'b^')  # b: blue color, o: Triangle marker
plt.plot(sma.work_force, sma.income, 'go--', linewidth=3)  # r: red color, o: circular marker


'''

# Changing Plot Size

# Arguments
# plt.figure(figsize=(new_width_pixels, new_height_pixels))

plt.figure(figsize=(12, 5))  # 12x5 plot
plt.plot(sma.work_force, sma.income)
plt.xlabel('Work Force')
plt.ylabel('Income')
plt.show()


# Multiple Plots

# Multiple Plots in 1 Figure

# Empty Plot
fig, ax = plt.subplots()
print(fig, ax)

# 1 row and 2 columns - Method 1
plt.subplot(1, 2, 1)  # row, column, index
plt.plot(sma.work_force, sma.income, 'go')  # green + circles
plt.title('Income vs Work Force')

plt.subplot(1, 2, 2)  # row, column, index

plt.plot(sma.hospital_beds, sma.income, 'r^')  # ed + triangles
plt.title('Income vs Hospital Beds')

plt.suptitle('Sub Plots')  # Add a centered title to the figure
plt.show()


# 1 row and 2 columns - Method 2
fig, (ax1, ax2) = plt.subplots(1, 2)  # row, column

fig.suptitle('Horizontally staked subplots')
ax1.plot(sma.work_force, sma.income, 'go')
ax1.set_title('Income vs Work Force')

ax2.plot(sma.hospital_beds, sma.income, 'r^')
ax2.set_title('Income vs WHospital Beds')

plt.show()

# sharey=True make the two subplots will share the y axis values then
# no more numbers between plots
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)  # row, column

fig.suptitle('Horizontally staked subplots')
ax1.plot(sma.work_force, sma.income, 'go')
ax1.set_title('Income vs Work Force')

ax2.plot(sma.hospital_beds, sma.income, 'r^')
ax2.set_title('Income vs WHospital Beds')


# 2 rows and 1 column
plt.subplot(2, 1, 1)  # row, column, index
plt.plot(sma.work_force, sma.income, 'go')

plt.subplot(2, 1, 2)  # row, column, index
plt.plot(sma.hospital_beds, sma.income, 'r^')

plt.suptitle('Sub Plots')
plt.show


# 2 rows ad 2 columns
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(6, 6), sharey=True)  #creating a grid of 2 rows, 2 columns and 6x6 figure size

ax[0, 0].plot(sma.work_force, sma.income, 'go')
ax[0, 1].plot(sma.work_force, sma.income, 'bo')
ax[1, 0].plot(sma.work_force, sma.income, 'yo')
ax[1, 1].plot(sma.work_force, sma.income, 'ro')

plt.show()