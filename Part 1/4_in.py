import pandas as pd

df = pd.read_json("sample_Data.json")
print("Displaying the info data set")
print(df.info())


data = {
    "Name":['RAM','Shyam','Ghanshyam'],
    "Age":[4,6,9],
    "City":['delhi','shimla','kangra']
}
# this data frame command is to read data 
df1 = pd.DataFrame(data)
# print(df1.info())