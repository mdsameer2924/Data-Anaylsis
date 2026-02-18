## 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## load data form that csv file
data=pd.read_csv("Gathered.csv",usecols=['0','3'],nrows=2)
col1=data['0']
col2=data['3']
col2[1]=45

# x,y=np.arange(1,100),np.arange(1,100)**2
x=np.arange(1,7,0.5)
y=np.sin(x)
z=np.cos(x)
w=np.tan(x)

## different diagram here
plt.bar(x, height=x)
plt.show()
plt.pie(x)
plt.show()

## p
plt.subplot(1,3,1)
plt.plot(x,y,"r>--")
plt.xlabel('sin data')
plt.ylabel('sample data')
plt.title('sine waveform')

plt.subplot(1,3,2)
plt.plot(x,y,"g*--")
plt.xlabel('cos data')
plt.ylabel('sample data')
plt.title('cos waveform')

plt.subplot(1,3,3)
plt.plot(x,w,"b+--")
plt.xlabel('tan data')
plt.ylabel('sample data')
plt.title('tan waveform')
plt.show()
plt.hist([3,4,5,3,2,5,5,5,5,5])
plt.show()


## plot gathered.csv file
plt.plot(col1,col2,"kx")
plt.scatter(col1,col2)
plt.show()