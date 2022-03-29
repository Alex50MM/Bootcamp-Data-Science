# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 19:03:41 2022

@author: alexc
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

height = pd.read_csv('C:/Users/alexc/Documents/Bootcamp/data/heights.csv')

print(height)

# Distribution
sns.histplot(height['Height(Inches)'], x=height['Height(Inches)'], kde=True)
sns.displot(height['Height(Inches)'], x=height['Height(Inches)'], kind='kde')

