import pandas as pd

my_data= {
    "Name":["a","b","c","d","e","f","g","h"],
    "Age":[1,45,32,45,23,56,21,46],
    "Salary":[45000,2300,4600,45444,37833,23456,23455,243633]
}

df = pd.DataFrame(my_data)
print("Simple Data frame")
print(df)

print("descriptive statistics")
print(df.describe())