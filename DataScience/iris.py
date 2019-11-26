import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('iris.csv')

'''
print(list(data.columns))
print(data.head())

--Find the average petal width of each category of IRIS Species
gdf=data.groupby('Class')
print(gdf[' Petal_Width'].mean())

--How many flowers of each species exists for each value of sepal width
ax=sns.countplot(x=' Sepal_Width', hue='Class',data=data);
plt.show()

--How many flowers are there whose petal width is &lt;1, between 1 to 2 and &gt;2
data['Widths']=pd.cut(data[' Petal_Width'],[0,1,2,4],labels=['<1','1-2','>2'])
ax=sns.countplot(x='Widths',data=data)
plt.show()

--Tally the Iris-Versicolour and Iris-Virginica species according to the value of Sepal Width
ax=sns.countplot(data=data[data['Class']=='Iris-virginica'],x=' Sepal_Width',)
plt.show()

ax=sns.countplot(x=' Sepal_Width',data=data[data['Class']=='Iris-versicolor'])
plt.show()
                 
'''
