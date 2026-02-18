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
print(pd.merge(df,df1))
print(df1)