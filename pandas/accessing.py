## ACcess the elemetns in pandas 
import pandas as pd

series=pd.Series([1,2,3,4,5.2],index=['a','b','c','d','e'])
print(series['a'])

## trying to access in the form of number use= iloc
print(series.iloc[0])