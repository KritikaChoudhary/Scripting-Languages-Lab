import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('StudentsPerformance.csv')

'''
--Display header rows and description of the loaded dataset.
print(data.head())
print(list(data.columns))
print(data.describe())

--Remove unnecessary features (E.g. drop unwanted columns) from the dataset such as
‘lunch’ and ‘test preparation course’
print(list(data.drop(['lunch','test preparation course'],axis=1).columns))

--Manipulate data by replacing empty column values in ‘parental level of education’ with a
default value.
data['parental level of education'].fillna('nil',inplace=True);
print(data['parental level of education'])

---Convert the attribute ‘race/ethnicity’ to have ‘groupA’ to be ‘Asian Students’, ‘groupB’ to be ‘African Students’ , ‘groupC’ to be ‘Afro-Asian Students’, ‘groupD’ to be ‘American Students’ and ‘groupE’ to be ‘European Students’
data['race/ethnicity']=data['race/ethnicity'].map({'group A':'Asian Students','group B':'African Students','group C':'Afro-Asian Students','group D':'American Students','group E':'European Students'})
print(data['race/ethnicity'])

--Tally of the Number of Male &amp; Female students who took up the ‘test preparation
course’ and those who did not.
ax=sns.countplot(x='test preparation course',hue='gender', data=data)
plt.show()

--Total Number of Male &amp; Female Students belonging to each student group
ax=sns.countplot(x='race/ethnicity',hue='gender',data=data)
ax.set(title='Male/Female belonging to each student group')
plt.show()

---No of students who ‘failed’(less than 40), ‘second class’(between 40 &amp; 50).
‘first class’(between 60 &amp; 75) and ‘distinction’(above 75) in ‘Maths’,
‘Reading’ and ‘Writing’.

categories=['f','2nd','1st','d']
data['Math']=pd.cut(data['mathscore'],[0,40,50,60,75],labels=categories)
ax=sns.countplot(x='Math',data=data)
plt.show()

data['Reading']=pd.cut(data['reading score'],[0,40,50,60,75],labels=categories)
ax=sns.countplot(x='Reading',data=data)
plt.show()

data['Writing']=pd.cut(data['writing score'],[0,40,50,60,75],labels=categories)
ax=sns.countplot(x='Writing',data=data)
plt.show()

--Find the average Maths, Reading and Writing Score of each Group (Ethnicity)

gdf=data.groupby('race/ethnicity')
print(gdf['mathscore'].mean())
'''
