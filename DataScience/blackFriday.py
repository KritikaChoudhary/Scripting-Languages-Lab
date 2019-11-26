import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv('blackfri.csv')

'''
print(data.head())
print(list(data.columns))
print(data.describe())

--Remove unnecessary features (E.g. drop unwanted columns) from the dataset such as
‘User_ID’, ‘Product_ID ‘ ‘Stay_In_Current_City_Years’ .
data.drop(['User_ID','Product_ID','Stay_In_Current_City_Years'],axis=1,inplace=True)
print(list(data.columns))


--Rename the attribute ‘City_Category’ to have ‘A’ to be ‘Metro Cities’, ‘B’ to be ‘Small Towns’ ,
‘C’ to be ‘Villages’
data['City_Category']=data['City_Category'].map({'A':'MetroCity','B':'SmallTown','C':'Village'})
print(data['City_Category'])

--Manipulate data by replacing empty column values in ‘City_Category’ with a default value for
the city.
data['City_Category']=data['City_Category'].fillna('nil')
print(data['City_Category'])

--Rename the attribute ‘Product_Category_1’ to have ‘Baseball Caps’, ‘Product_Category_2’ to
have ‘Wine Tumblers’ and ‘Product_Category_3’ to have ‘Pet Raincoats’
data.rename(columns={'Baseball_Caps':'Product_Category_1','Wine_Tumblers':'Product_Category_2','Pet_Raincoats':'Product_Category_3'},inplace=True)
#print(list(data.columns))

--Convert the attribute ‘Marital_Status’ to have ‘1:Married’ and ‘0:Un-Married’
data['Marital_Status']=data['Marital_Status'].map({1:'Married',0:'Unmarried'})
print(data['Marital_Status'])

--Tally of the Number of Male &amp; Female persons who bought ‘Product_Category_1’ and
‘Product_Category_2’.
ax=sns.countplot(x="Product_Category_1", hue="Gender",data=data)
plt.show()
ax=sns.countplot(x="Product_Category_2", hue="Gender",data=data)
plt.show()

--Total Number of Male &amp; Female persons belonging to each city category
ax=sns.countplot(x='City_Category',hue='Gender',data=data)
plt.show()
'''
