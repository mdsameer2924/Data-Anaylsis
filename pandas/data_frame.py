## 
import pandas as pd
# ser=np.Series([1,2,3,4,5.7],index=['a','b','c','d','e'],name='col1')

## Data Frame using Array method
df=pd.DataFrame([[1,2,3],
                 [4,5,6],
                 [7,8,9]
                 ],index=['d','e','f'],columns=['a','b','c'])
print(df)

