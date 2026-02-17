## to acess only border of the matrix
import numpy as np

arr=np.arange(0,30)
arr=arr.reshape((6,5))
print(arr)

## crop matrices
print(arr[3:6,1:4])

# update of matrix
arr[3:6,1:4]=[1,2,4],[4,5,6],[7,8,9]
print(arr)