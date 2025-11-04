# head() tail()
# head() 5
# tail(n) 5 

import pandas as pd

df = pd.read_json("sample_Data.json")
print('Display 20 rows of first')
# head display top rows
print(df.head(20))

print('Display 10 rows of last')
print(df.tail(10))  # tail display top last rows

#if you dont put number than by default it will display top 5 rows
