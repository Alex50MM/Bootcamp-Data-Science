# -*- coding: utf-8 -*-

# Series and DataFrames
import pandas as pd

# Explicação sobre Series
series = [1, 1, 2, 3, 5, 8, 13]
print(pd.Series(series))

another_series = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7}
print(pd.Series(another_series))


# Explicação sobre DataFrame
data = [[1000, 'Steve', 86.29], [1001, 'Mathew', 91.63], [1002, 'Jose', 72.90], [1003, 'Patty', 69.23], [1004, 'Vin', 88.30]]
print(pd.DataFrame(data))
print(pd.DataFrame(data,columns = ['Regd. No', 'Name', 'Marks%'], index = [1, 2, 3, 4, 5] ))
