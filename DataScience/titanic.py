import pandas as pd #importing pandas library
data=pd.read_csv("train.csv") #a)creating dataframe,data
import matplotlib.pyplot as plt
import seaborn as sns

#print(data.shape)  --(rows,columns)

print(list(data.columns)) #b)column headers as a list
print(data.head()) #column heads with first 5 rows
print(data.describe()) #b)description of each column:min,max,std,mean etc.
print(data.drop(['SibSp','Parch'],axis=1).head()) #c)Axis 1 will act on all the COLUMNS in each ROW! axis parameter compulsory here
#print(data.head())
data=data.fillna('null') #d)empty valuues are replaced by null
print(data)

#e1) Passenger status (Survived/Died) against Passenger Class
#data['Survived']=
data['Survived'].map({1:'Survived',0:'Died'})
print(data['Survived'])
ax=sns.countplot(hue='Survived',x='Pclass',data=data,)
plt.show()

#e2)Survival rate of male vs female
ax=sns.countplot(x='Sex',hue='Survived',data=data)
plt.show()

#e3)No of passengers in each age group
ax=sns.countplot(x='Age',data=data);
plt.show()

