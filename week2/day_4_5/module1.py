# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 00:38:06 2022

@author: alexc

https://dphi.tech/notebooks/855/manish_kc_06/day-4-notebooks-data-pre-processing?
"""

# IMPORT LIBRARIES
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno

import random
import sklearn
import graphviz

from sklearn import tree
from sklearn import preprocessing
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from collections import Counter
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline

# LOAD THE DATASET
fraud = pd.read_csv('C:/Users/alexc/Documents/Bootcamp/data/fraud_data.csv')

print(fraud.info())

# VERIFI MISSING DATA
pct_missing = fraud.isna().mean()
print(pct_missing[:10])

# VERIFI MISSING DATA IN GRAPHIC WITH MISSINGNO
# PLOT
msno.bar(fraud.iloc[:, :30])
msno.matrix(fraud.iloc[:, :30])
msno.heatmap(fraud.iloc[:, :30])
msno.dendrogram(fraud.iloc[:, :30])

# VERIFI MISSING DATA IN GRAPHIC WITH MATPLOTLIB AND SEABORN
# PLOT
plt.figure(figsize=(130, 50))

colsplot = fraud.columns
colours = ['#000099', '#ffff00']
sns.heatmap(fraud[colsplot].isna(), cmap=sns.color_palette(colours))

#
print(fraud.isFraud.value_counts())

# Train Test Data Split
# Set X and Y variables
y = fraud['isFraud']
x = fraud.loc[:, fraud.columns != 'isFraud']


# Split ramdomly into 70% train data and 30% test data
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size= 0.3, random_state=123)
print(xTrain.info())

# Step 1. Check for missingness in variables
print(xTrain.isnull().sum())

print(pct_missing[pct_missing > .2])  # show columns with over 20% missing data

# Eliminate automatically variables with more than 20% of missingness
xTrain_before_filling = xTrain
xTrain = xTrain[xTrain.columns[xTrain.isnull().mean() < 0.2]]
missing_cols = xTrain.columns[xTrain.isnull().mean() > 0]
print(missing_cols)

print(xTrain['card5'].isnull().mean())


# Step 1a. Single Imputation Technique
# Impute Numeric Variables with mean of the variable
xTrain_single = xTrain
cols = xTrain_single.columns
num_cols = xTrain_single.select_dtypes(include=np.number).columns
xTrain_single.loc[:, num_cols] = xTrain_single.loc[:, num_cols].fillna(xTrain_single.loc[:, num_cols].mean())
print(num_cols)
print(xTrain_single.loc[:, num_cols].mean())

# Impute Categorical Variables with mode of the variable
cat_cols = list(set(cols) - set(num_cols))
xTrain_single.loc[:, cat_cols] = xTrain_single.loc[:, cat_cols].fillna(xTrain.loc[:, cat_cols].mode().iloc[0])
train_cols = xTrain_single.columns
print(xTrain_single.loc[:, cat_cols].mode().iloc[0])

# Check if missingness is now 0 for all variables remaining
print(xTrain_single.columns[xTrain_single.isnull().mean() > 0])

# Comparing variable before and after filling: (variable 'Card5' earlier)
# PLOT
xTrain_single['card5'].plot.hist(figsize=(16, 8));  # variable before filling
xTrain_before_filling['card5'].plot.hist(figsize=(16, 8));  # variable after filling
print(xTrain_before_filling['card5'].describe())
print(xTrain_single['card5'].describe())

# let us single imputed data as further data for preprocessing in the next step
xTrain = xTrain_single

print(xTrain.info())
xTrain_dummy = pd.get_dummies(xTrain, prefix_sep= '_', drop_first=True)
print(xTrain_dummy)

# Finalizing the data before training a model
final_tr = pd.DataFrame(data= xTrain_dummy)
print(final_tr.head())
print(final_tr.shape)

# Decision Tree using grid search CV
parameters = {'max_depth': range(3, 20)}
clf = GridSearchCV(tree.DecisionTreeClassifier(), parameters, n_jobs= 4, cv= 5, scoring= 'roc_auc')
clf.fit(X= final_tr, y= yTrain)
dt = clf.best_estimator_  #
print(clf.best_score_, clf.best_params_)

# Visualizing the decision tree initially- load visualization libraries
# PLOT
dot_data = tree.export_graphviz(dt, out_file=None,
feature_names=final_tr.columns,
class_names=['No_Fraud','Fraud'],
filled=True, rounded=True,
special_characters=True)
graph = graphviz.Source(dot_data)
graph


#
over = SMOTE(sampling_strategy= 0.2, random_state= 2)
steps = [('o', over)]
pipeline = Pipeline(steps= steps)
X_res, y_res = pipeline.fit_resample(xTrain_dummy, yTrain)

print('Original dataset shape %s ' % Counter(yTrain))
print('Resampled dataset shape %s ' % Counter(y_res))

# 
final_tr_res = pd.DataFrame(data= X_res)
final_tr_res.columns = xTrain_dummy.columns
final_tr_res
print(final_tr_res.head())

# Decision Tree using grid search CV
parameters = {'max_depth': range(3, 20)}
clf = GridSearchCV(tree.DecisionTreeClassifier(), parameters, n_jobs= 4, cv= 5, scoring= 'roc_auc')
clf.fit(X= final_tr_res, y=y_res)
dt_smote= clf.best_estimator_  # final decision tree
print(clf.best_score_, clf.best_params_)


## Visualizing the decision tree initially- load visualization libraries
dot_data = tree.export_graphviz(dt, out_file=None,
feature_names=final_tr.columns,
class_names=['No_Fraud','Fraud'],
filled=True, rounded=True,
special_characters=True)
graph = graphviz.Source(dot_data)
graph

# Apply on Test Data : apply steps 1-4 namely and then do prediction
# Apply single imputation,
# Select only variables which are used for training
# One Hot encode variables 4: make sure test data again has exact same number of variables as training !
# Step 1: Account for missing values with single imputation like we did earlier
cols= xTest.columns
num_cols = xTest.select_dtypes(include=np.number).columns
xTest.loc[:,num_cols] = xTest.loc[:,num_cols].fillna(xTest.loc[:,num_cols].mean())

cat_cols= list(set(cols) - set(num_cols))
xTest.loc[:,cat_cols] = xTest.loc[:,cat_cols].fillna(xTest.loc[:,cat_cols].mode().iloc[0])
test_cols = xTest.columns

# Step 2: Select only those features which are there in training
#train_cols = xTrain.columns
xTest = xTest[train_cols]

# Step 3. One Hot encode variables
xTest.info()
xTest_dummy = pd.get_dummies(xTest, prefix_sep='_', drop_first=True)
# Dummify categorical vars
xTest_dummy = pd.get_dummies(xTest, prefix_sep='__', drop_first=True)

##missing columns levels train and test
missing_levels_cols= list(set(xTrain_dummy.columns) - set(xTest_dummy.columns))


for c in missing_levels_cols:
    xTest_dummy[c]=0

# Select only those columns which are there in training data
xTest_dummy=xTest_dummy[xTrain_dummy.columns]

# Step 4: make sure test data again has exact same number of variables as training
final_ts = pd.DataFrame(data=xTest_dummy)
final_ts.columns= xTest_dummy.columns
final_ts
print(final_ts.head())
print(final_ts.shape)

# Prediction on test data: Without SMOTE vs With SMOTE
# Without SMOTE
ytest_dt = dt.predict_proba(final_ts)
print('The ROC AUC score for 1st model without SMOTE is {}'.format(roc_auc_score(yTest,ytest_dt[:,1])))

# With SMOTE
ytest_dt_smote = dt_smote.predict_proba(final_ts)
print('The ROC AUC score for 1st model after SMOTE is {}'.format(roc_auc_score(yTest,ytest_dt_smote[:,1])))
