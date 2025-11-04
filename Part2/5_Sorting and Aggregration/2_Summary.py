import pandas as pd

data = {
    "Name":['Arun','Varun','Karun'],
    "Age":[20,40,30],
    "Salary":[10000,30000,5000],
}
df = pd.DataFrame(data)
print(df)

"""
Summary of data 
df["Column Name].mean()
df["Column Name].sum()
df["Column Name].min()
df["Column Name].max()
"""

avg_salary = df['Salary'].mean()
print(avg_salary)