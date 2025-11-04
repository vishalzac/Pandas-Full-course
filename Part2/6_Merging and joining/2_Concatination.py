"""
vertically (row+wise)
horizontally ()
"""

import pandas as pd

df_customer = {
    "CustomerId":[1,2],
    "Name":['Arun','Varun'],
}
df_customer2 = {
    "CustomerId":[3,4],
    "Name":['shyam','nyam'],
}
dfc = pd.DataFrame(df_customer)
dfc2 = pd.DataFrame(df_customer2)

# df_concat = pd.concat([dfc,dfc2],ignore_index=True)
# print(df_concat)

df_concat = pd.concat([dfc,dfc2],axis=1,ignore_index=True)
print(df_concat)