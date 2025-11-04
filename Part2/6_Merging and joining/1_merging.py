import pandas as pd

df_customer = {
    "CustomerId":[1,5,30,5,90],
    "Name":['Arun','Varun','Arun','Varun','Tarun'],
    "Salary":[10000,30000,5000,7000,1000],
}

df_orders = {
    "CustomerId":[1,8,900,5,9],
    "OrderAmount":[10000,30000,5000,7000,1000],
}
df_custom = pd.DataFrame(df_customer)
df_order = pd.DataFrame(df_orders)

df_merged = pd.merge(df_custom, df_order, on="CustomerId", how="inner")
print('INNER JOIN')
print(df_merged)

#we have left and right join too..where how = "right" or how = "left"
# We also have cross join
