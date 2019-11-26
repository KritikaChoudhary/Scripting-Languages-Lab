import pandas as pd
with pd.ExcelFile('info.xlsx') as xls:
    s1=pd.read_excel(xls,'fruit')                     
    s2=pd.read_excel(xls,'animal')
print(s1[:3]['quantity'])
print(s2[1:3]['zoo'])
