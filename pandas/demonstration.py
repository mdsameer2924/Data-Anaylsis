import numpy as np
import pandas as pd

arr=np.arange(0,400)
arr=arr.reshape(100,4)

arr.to_csv("demonstrate.csv",index_label="serial no.")

read1=pd.read_csv("demonstrate.csv",index_col='serial no.',
                  usecols=['serial no.','0','1','2','3'],
                  nrows=2)      
print(arr)