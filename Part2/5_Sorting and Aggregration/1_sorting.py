import pandas as pd

# Sorting Data 1_ Column sort_value
# df.sort(_values(by="Column Name"),True/False , Implace = true)

data = {
    "Name":['Arun','Varun','Karun'],
    "Age":[20,40,30],
    "Salary":[10000,30000,5000],
}

df = pd.DataFrame(data)
print(df)

#by default sorting is True ..which means it is in ascending orders
# df.sort_values(by="Age",ascending=False, inplace=True)
# print('Sorted Age by Descending')
# print(df)

# Multiple sort
df.sort_values(by= ["Age","Salary"],ascending=[False,True], inplace=True)
print('Sorted Age by Descending')
print(df)