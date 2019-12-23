'''
7a. Python for Data Science - Perform Data Visualization  on Iris Dataset
a) Load the Iris dataset into one of the data structures (NumPy or Pandas).
b) Display header rows and description of the loaded dataset.
c) Clean the data if applicable 
d) Find the average petal width of each category of IRIS Species 
e) Data Visualization for: How many flowers of each species exists for each value of sepal width 
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("iris.csv")

print(data.head())

print(data.describe())

data.drop(["Sepal_Length"," Petal_Length"],axis=1,inplace=True)
print(list(data.columns))

print(data[" Petal_Width"].mean())

axis=sns.countplot(data=data,x="Class",hue=" Sepal_Width")
plt.show()
