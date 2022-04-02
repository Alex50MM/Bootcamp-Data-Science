# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 21:23:08 2022

@author: alexc

https://dphi.tech/notebooks/857/manish_kc_06/day-1-notebooks-intro-to-model-building?


"""
# IMPORT LIBRARY
import pandas as pd

# LOAD DATASET
melborne_file_path = 'C:/Users/alexc/Documents/Bootcamp/data/melbourne_data.csv'
melborne_data = pd.read_csv(melborne_file_path)
melborne_data.columns
melborne_data.info()



# TO SHOW ALL COLUMNS AND ROWS DATA ON PRINT DATAFRAME
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

# pd.set_option('display.max_rows', 500) # If change to 1000 show all data
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1000)