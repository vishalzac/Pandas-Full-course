import pandas as pd

my_data= {
    "Name":["a","b","c","d","e","f","g","h"],
    "Age":[1,45,32,45,23,56,21,46],
    "Salary":[45000,2300,4600,45444,37833,23456,23455,243633],
    "Performance_Score":[87,98,20,56,23,50,70,34]
}
df = pd.DataFrame(my_data)
print(df)
#Adding new data to existing data 
# square bracket df["Column_Name"] = some_Data
df["Bonus"] = df['Salary'] *0.1

print(df)

#using insert()
# df.insert(loc,"Column_Name",some_data)
df.insert(1,"Employee ID",[10,20,30,40,50,60,70,80])
print(df)

# Practise
# df["Id"] = [1,2,3,4,5,67,8,9]
# print(df)


