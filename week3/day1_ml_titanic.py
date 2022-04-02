# -*- coding: utf-8 -*-
'''
Created on Fri Apr  1 01:14:16 2022

@author: alexc

https://dphi.tech/notebooks/858/manish_kc_06/day-1-notebooks-ml-with-titanic-dataset?




This tutorial is aimed at beginners, especially those who are both new to
machine learning/data science as well as python.

In this tutorial I would walk you through the process of building a predictive
model, namely a decision tree.

The pipeline consists of several steps:

1. Exploratory Data Analysis (EDA) - understanding the data and the underlying
    interactions between the different variables
2. Data Pre-processing - preparing the data for modelling
3. Building the model
4. Evaluating the performance of the model, and possibly fine-tune and tweak
    it if necessary
The goal of the model is to predict whether a passenger survived the Titanic
disaster, given their age, class and a few other features.

Almost every line of code would be explained, so those who are more familiar
with python (and especially with the numpy and pandas libraries) are welcome
to skip the first parts

'''

# IMPORT LIBRARY
import numpy as np  # whenever calculations are required
import pandas as pd  # or data processing and data frames
import missingno as msno
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz
import graphviz


# LOAD DATASET
titanic = pd.read_csv('C:/Users/alexc/Documents/Bootcamp/data/titanic.csv')
print(titanic.info())
print(titanic.head())

# TO SHOW ALL COLUMNS AND ROWS DATA ON PRINT DATAFRAME
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

# pd.set_option('display.max_rows', 500) # If change to 1000 show all data
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1000)



# 1. Exploratory Data Analysis (EDA)
print()
print('Total number of passengers in the training data.......... ', len(titanic))
print('Number of passengers in the training data who survived... ', len(titanic[titanic['Survived'] == 1 ]))
print()
print('% of men who survived   ', 100* np.mean(titanic['Survived'] [titanic['Sex'] == 'male' ]))
print('% of women who survived ', 100* np.mean(titanic['Survived'] [titanic['Sex'] == 'female' ]))
print()
print('% of passengers who survived in first class  ',100* np.mean(titanic['Survived'] [titanic['Pclass'] == 1]))
print('% of passengers who survived in second class ',100* np.mean(titanic['Survived'] [titanic['Pclass'] == 2]))
print('% of passengers who survived in third class  ',100* np.mean(titanic['Survived'] [titanic['Pclass'] == 3]))
print()
print('% of children who survived ',  100* np.mean(titanic['Survived'] [titanic['Age'] <  18 ]))
print('% of adults who survived   ',  100* np.mean(titanic['Survived'] [titanic['Age'] >= 18 ]))


# 2. Data Pre-processing
# Non numeric features to numeric (convert words male and female in numbers 1 and 0)
titanic['Sex'] = titanic['Sex'].apply(lambda x: 1 if x == 'male' else 0)

# Missing Values
print(titanic.isnull().sum())

# missingno is a small library focused on missing data viz and utilities
msno.bar(titanic)  # Bar  is a simple viz of nullity by column
msno.matrix(titanic)  # Missing data heatmap VERTICAL
msno.dendrogram(titanic)  # Dendrogram revealing trends deeper

# Fill the NaN in column Age with mean from all column
titanic['Age'] = titanic['Age'].fillna(np.mean(titanic['Age']))

# Looking at frequency of each values in Embarked
titanic.Embarked.value_counts()
titanic.Embarked.fillna(value= 'S', axis= 0, inplace= True)
print(titanic.isnull().sum())

# Omit irrelevant columns
titanic = titanic[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]

# Separating input variables (X) and target variable (y)
x = titanic.drop('Survived', axis= 1)
y = titanic['Survived']

# Train and Test Split
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size= 0.33, random_state= 42)

# Building ML Model
model = DecisionTreeClassifier()
model.fit(X_train,Y_train)

# Evaluete the model
print('Training accuracy ...', accuracy_score(Y_train, model.predict(X_train)))
print('Test accuracy ', accuracy_score(Y_test, model.predict(X_test)))

dot_data = export_graphviz(model, out_file=None,
feature_names = X_test.columns,
class_names = ['0','1'],
filled=True, rounded=True,
special_characters = True)

graph1 = graphviz.Source(dot_data)

# Create the graphic in CONSOLE I/A ==>
graph1

# Create and save the graphic in FOLDER
graph1.render('C:/Users/alexc/Documents/Bootcamp/images/round-table.gv').replace('\\', '/')
'C:/Users\alexc/Documents/Bootcamp/images/round-table.gv.pdf'

# Create, save and open the graphic in BROWSER
graph1.render('C:/Users/alexc/Documents/Bootcamp/images/round-table.gv', view=True)  
'C:/Users/alexc/Documents/Bootcamp/images/round-table.gv.pdf'


# improve the model
model_improved = DecisionTreeClassifier(max_depth= 3)
model_improved.fit(X_train, Y_train)

print('Train score ... ', accuracy_score(Y_train, model_improved.predict(X_train)))
print('Train score... ', accuracy_score(Y_test, model_improved.predict(X_test)))

dot_data= export_graphviz(model_improved, out_file=None,impurity=False,
feature_names=X_test.columns,
class_names=['0', '1'],
filled=True, rounded=True)

graph2=graphviz.Source(dot_data)

graph2.render('C:/Users/alexc/Documents/Bootcamp/images/round-table2.gv', view=True)  
'C:/Users/alexc/Documents/Bootcamp/images/round-table.gv2.pdf'