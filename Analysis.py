# ANALYSIS OF THE IRIS DATASET
#    1. EDA and Python Syntax
#    2. SQL queries

# Importing the necessary libraries

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

# Importing the dataset from the .csv type file with pandas to a dataframe
df = pd.read_csv("iris.csv")

## Starting to explore the dataframe
print ("Checking if the dataframe has been correctly imported:\n", df.head(5))

## First, checking for total null values
print ("The following statement will list the number of null values arranged by the rows:\n", df.isnull().sum())
print("It could also be checked indirectly with the .info() function, showing the following results:")
df.info()

## Given the lack of nulls in the df, it is time to start exploring more concisely
print ("The shape of the dataframe:", (df.shape), "\nThe 5 rows present the following nu,number of unique values\n", df.nunique(), "\nExploring -variety- to check the classes. \nThe different classes present in the dataframe are:",  pd.unique(df['variety']))

## The dataframe is divided in three different classes. Now we'll explore how does pertaining to a certain class affect the other variables
print ("The number of instancies within the classes to check the distribution:\n", df['variety'].value_counts())