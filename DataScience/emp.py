import pandas as pd
data=pd.read_csv("emp.csv")#create an excel fie emp and in save as choose csv as the file format
print(data)

print(data[0:2])#displays data of 2 people
print(data[2:4])#displays data that is indexed 2,3
print(data[0:3]['name'])#displays name of 2 people
print(data[:3])#same as print(data[0:3])
print(data[4:])#displays data of 4,5 employee

print(data.loc[:3,['name']])#.loc() extracts rows, here extracts rows of name
print(data.loc[[1,3,5],['name','age']])


