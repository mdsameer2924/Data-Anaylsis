## multiplication of matrix using functions
import numpy as np
## ARrray 1
arr1=np.arange(10,30)
arr1=arr1.reshape(4,5)
print(arr1[2,1]) # to access only one value from matrices
print(arr1[:,3]) # to access whole columns

## 2nd array
arr2=np.arange(40,60)
arr2=arr2.reshape(5,4) ## multiply only possible when one array is 5,4 second must be 4,5 then it's work

multi_of_matrices=np.dot(arr1,arr2)
print(multi_of_matrices)
np.savetxt("../testing_data.txt",multi_of_matrices,'%.2e')