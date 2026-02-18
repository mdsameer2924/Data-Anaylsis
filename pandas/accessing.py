## ACcess the elemetns in pandas 
import pandas as pd

series=pd.Series([1,2,3,4,5.2],index=['a','b','c','d','e'],name="Col1")
print(series['a'])
print(type(series))
## trying to access in the form of number use= iloc
print(series.iloc[0])  # iloc used for access bydeafult indexing 


# To Print dimension of an Series
print("The dimension of an sereis: ", series.ndim)

#  TO print shape of an Series
print("The shape of a Series ",series.shape)

# conversion series to numpy or array
array=series.to_numpy()
print("Series Turned into array ",array)
print("NOW IT's TYPE: ",type(array))

# To apply Operatiuon whole value fucntoin(lamda parmeter:expression)
print(series.apply(lambda x:x**2 if x%2==0 else x**3))