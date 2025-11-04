import pandas as pd

data = {
    "Name":['Arun','Varun','Karun','Narun','Tarun'],
    "Age":[20,5,30,5,90],
    "Salary":[10000,30000,5000,7000,1000],
}
df = pd.DataFrame(data)
print(df)

"""
dr.groupby("Age") ...so if 2 or more age are same ..it gonna be in 1 group
["Salary"].sum() ...we gotta add the salary of all ages which are same 

"""
grouped = df.groupby("Age")['Salary'].sum()
print(grouped)