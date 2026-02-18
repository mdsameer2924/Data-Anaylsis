## Data frame using dictnaries method
## Data frame is the combination of Series
import pandas as pd
df=pd.DataFrame({
    'a':[1,4,7],
    'b':[2,5,8],
    'c':[3,6,9]
},index=['d','e','f'])
print("Print data frame into array: ")
print(df)


## fucntion/ method and attributes
print(df[['a']])
print(type(df))
print(df.shape)
print(df.ndim)

## add new columsn in data frame with a's square in new columns
# df['a**2']=df['a'].apply(lambda x:x**2)
# print(df)
df['sum']=df.apply(lambda x,y:x+y)
print(df)