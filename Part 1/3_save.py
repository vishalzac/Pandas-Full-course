import pandas as pd
data = {
    "Name":['RAM','Shyam','Ghanshyam'],
    "Age":[4,6,9],
    "City":['delhi','shimla','kangra']
}
# this data frame command is to read data 
df = pd.DataFrame(data)
print(df)

# to save a file in csv foramt
df.to_csv("output.csv")

# to save a file in csv foramt and remove indexing
df.to_csv("output.csv",index=False)

# to save a file in exel foramt
df.to_excel("output.xlsx",index=False)

# to save a file in json foramt
df.to_json("output.json",index=False)




df2 = {
    "Name":["zac","vishal","singh"],
    "Age":[23,25,20],
    "salary":[20,40,50]
}

data_read = pd.DataFrame(df2)
print(data_read)

data_read.to_json("newfile.json")
