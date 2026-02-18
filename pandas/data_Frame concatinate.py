## Concatinate in data frame
import pandas as pd
df=pd.DataFrame({'a':[1,2,4],
                 'b':[4,5,6],
                 'c':[8,9,20],
                },index=['e','f','g'])
df1=pd.DataFrame({'a':[21,22,46],
                 'b':[44,53,6],
                 'c':[8,9,20],
                 },index=['e','f','g'])
print(pd.concat((df,df1),axis=1))
df2=df.merge(df1,how='outer') # or 'inner'
df2.dropna(inplace=True,axis=1)

## to delete particular columns
df2.drop(['a'],inplace=True,axis=1)  # what inplace do it's udate value after drop the value

print("update value\n",df2)