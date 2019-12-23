#Titanic Dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("train.csv")
print(data.head())
print(data.describe())

data.drop(["PassengerId","Name","Ticket"],axis=1,inplace=True)
print(list(data.columns))

data["Cabin"]=data["Cabin"].fillna("Nil")
print(data["Cabin"])

axis=sns.barplot(data=data,y="Survived",x="Pclass")
plt.show()
