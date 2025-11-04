import pandas as pd
my_data= {
    "Name":["a",None,"c","d","e","f","g","h"],
    "Age":[1,None,32,45,23,56,21,46],
    "Salary":[45000,None,4600,45444,None,23456,23455,243633],
    "Performance_Score":[87,None,20,56,23,50,70,34]
}
df = pd.DataFrame(my_data)
print(df)

#dropna() axis 0 is row and axis 1 is columns
df.dropna(axis=0,inplace=True)
print(df)

