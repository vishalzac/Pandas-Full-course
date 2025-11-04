import pandas as pd
my_data= {
    "Time":[1,78,32,45,23],
    "Value":[1,78,None,45,23,]
}
df = pd.DataFrame(my_data)
print("Before interpolation")
print(df)

df['Value'] = df["Value"].interpolate(method="linear")
print('After interpolate')
print(df)

"""
linear value use in 
1)Time series (like consistant data like stock market)
2) numerical data with trends
3) avoid dropping rows

Disadvantage
1) cant work in chcarcter
2) It assume the value 
"""