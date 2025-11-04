"""
how big is your data?
what is the name of your columns 

can be done with the help of shape and column
"""

import pandas as pd

my_data= {
    "Name":["a","b","c","d","e","f","g","h"],
    "Age":[1,45,32,45,23,56,21,46],
    "Salary":[45000,2300,4600,45444,37833,23456,23455,243633]
}

df = pd.DataFrame(my_data)
print(df)
print(f"shape : {df.shape}")
print(f"column name : {df.columns}")
