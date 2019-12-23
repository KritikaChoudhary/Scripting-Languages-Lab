'''
11b.  Python and DataScience 
     a) Load the ‘Student Performance’ dataset into one of the data structures (NumPy or Pandas).
	b)Display header rows and description of the loaded dataset.
	c) Remove unnecessary features (E.g. drop unwanted columns) from the dataset such as ‘lunch’ and ‘test preparation course’ .
	d) Manipulate data by replacing empty column values in ‘parental level of education’ with a default value.
	e) Perform the following visualization on the loaded dataset: Tally of the Number of Male & Female students who took up the ‘test preparation  course’ and those who did not. 
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_excel("StudentsPerformance.xlsx")

print(data.head())
print(data.describe())
print(data.info(verbose=True))
axis=sns.countplot(x='gender',hue="test preparation course",data=data)
plt.show()
data.drop(["lunch","test preparation course"],inplace=True,axis=1)
print(list(data.columns))
data["parental level of education"]=data["parental level of education"].fillna('NONE')
print(data["parental level of education"])




