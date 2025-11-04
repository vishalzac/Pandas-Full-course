import pandas as pd

my_data= {
    "Name":["a","b","c","d","e","f","g","h"],
    "Age":[1,45,32,45,23,56,21,46],
    "Salary":[45000,2300,4600,45444,37833,23456,23455,243633]
}


df = pd.DataFrame(my_data)
print("Sample data frame")
# print(df)

#1 filter simple row
hig_salry = df[df['Salary']>50000]
print("salary above 50k is")
print(hig_salry)

#2 filter grater and lower
in_between = df[(df['Age']>30) & (df['Salary'] >20000 )]
print("salary above 20k and age above 30")
print(in_between)

#3 filter and one condition
or_between = df[(df['Age']>30) | (df['Salary'] >20000 )]
print("salary above 20k or age above 30")
print(or_between)


# experiment
#multiple condition
print("last test")
condition1 = df[(df['Salary'] >20000) & (df['Age'] < 40) | (df['Name'] == 'h') ]
print(condition1)

print("next")

condition2 = df[(df["Age"]>2) & (df["Salary"]<100000)]
print(condition2)
