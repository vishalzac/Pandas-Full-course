"""
1) select specific column
2) filters row
3) combine multiple conditions

a) square brackets
b) boolean conditions

selecting columns
1) a series
2) dataframe multiple column of data


filtering rows
boolean indexing

"""


import pandas as pd

my_data= {
    "Name":["a","b","c","d","e","f","g","h"],
    "Age":[1,45,32,45,23,56,21,46],
    "Salary":[45000,2300,4600,45444,37833,23456,23455,243633]
}

df = pd.DataFrame(my_data)
print("Sample data frame")
# print(df)

#2
print("Name (Single column return series)")
name = df['Name']
print(name)

#3 selecting multiple column
subset = df[["Name" ,"Age"]]
print("Both name and age")
print(subset)



#test

print("below is the salary")
print(df["Salary"])

#multiple items require more bracket 
print("below is 2 items")
print(df[["Salary" , "Age"]])



