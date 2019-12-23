'''
9b. Python and DataScience
a)Load the ‘Black Friday’ dataset into one of the data structures (NumPy or Pandas).
b)Display header rows and description of the loaded dataset.
c) Manipulate data by replacing empty column values in ‘City_Category’ with a default value for the city. 
d) Rename the attribute ‘City_Category’ to have ‘A’ to be ‘Metro Cities’, ‘B’ to be ‘Small Towns’ ,  ‘C’ to be ‘Villages’.
e) Perform the following visualization on the loaded dataset: Total Number of Male & Female persons belonging to each city category
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("BlackFriday.csv")

print(data.head())

print(data.describe())

data["City_Category"].fillna("NIL",inplace=True)
print(data["City_Category"])

data["City_Category"]=data["City_Category"].map({"A":"Metro Cities","B":"Small Towns","C":"Villages"})
print(data["City_Category"])

axis=sns.countplot(x="Gender",hue="City_Category",data=data)
plt.show()
