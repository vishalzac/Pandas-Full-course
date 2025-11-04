import pandas as pd


my_data= {
    "Name":["a","b","c","d","e","f","g","h"],
    "Age":[1,45,32,45,23,56,21,46],
    "Salary":[45000,2300,4600,45444,37833,23456,23455,243633],
    "Performance_Score":[87,98,20,56,23,50,70,34]
}

df = pd.DataFrame(my_data)
print(df)

# df.drop(Columns = ["ColumnName"], inplace = True)
#inplace is for modifying the original data
# By default pandas give you copy of modified data

print('Modified Data')
df.drop(columns=["Performance_Score"],inplace=True)
print(df)