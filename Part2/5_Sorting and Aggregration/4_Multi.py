import pandas as pd

data = {
    "Name":['Arun','Varun','Arun','Varun','Tarun'],
    "Age":[20,5,30,5,90],
    "Salary":[10000,30000,5000,7000,1000],
}
df = pd.DataFrame(data)
print(df)

"""
for multiple group ..put it inside [("Value1")]
"""
grouped = df.groupby(["Age","Name"])['Salary'].sum()
print(grouped)