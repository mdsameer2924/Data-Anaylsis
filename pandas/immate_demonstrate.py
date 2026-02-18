## Data frame using dictnaries method
## Data frame is the combination of Series
import pandas as pd
import numpy as np
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
df['sum of all']=df['a']+df['b']+df['c']
print(df)

# turn data frame into an array
arr_turn=df.to_numpy()
print("now series turn into array\n", arr_turn)

# concatination of an array
## axis attribute to decided row wise or columns wise operatoins
## axis 1= row wise
## axis 0= coln wise (by default)
print("\n\nconcatenate array is:\n\n",np.concatenate((df.to_numpy(),df.to_numpy()),axis=1))

## gathered data 
gathtered=np.concatenate((df.to_numpy(),df.to_numpy()),axis=1)

gathtered=pd.DataFrame(gathtered,index=['d','e','f'])
print(gathtered)
# gathtered.to_csv("Gathered.csv")
# gathtered.to_csv("Gathered.csv",index=False)

gathtered.to_csv("Gathered.csv",index_label="serial no.")

read1=pd.read_csv("Gathered.csv",index_col='serial no.',
                  usecols=['serial no.','0','1','2','3'],
                  nrows=2)                                        #nrows is  to set limit of data you want
                                                                    #to resize
print(read1)

## to show only columns
print(df.columns)
 
## to show information about data frame
print("\n\n\n")
print(df.info())