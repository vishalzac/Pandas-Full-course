import pandas as pd
my_data= {
    "Name":["a","b","c",None,"e","f","g","h"],
    "Age":[1,78,32,45,23,None,21,46],
    "Salary":[45000,None,4600,45444,89000,23456,23455,243633],
    "Performance_Score":[87,98,20,56,23,50,70,34]
}
df = pd.DataFrame(my_data)
print(df)

#linear , polynomial , time series 
#Interploate value fill the missing value automatically as per trend 

df.interpolate(method="linear",axis=0,inplace=True)
print(df)