''' THis is practice set to make a different type of array
🔹 1-D Array ✔️
🔹 2-D Array ✔️
🔹 3-D Array
'''
import numpy as np
onedarray=np.array([1,2,3,4,5]) # how to create an array in numpy ? stuck
print(onedarray)

twodarray=np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9] 
                   ])
print(twodarray)

## 3D array # shape would be (4,2,3)
''' Where 4 = layer/depth
2 = rows
3 = columns
'''
threedarray=np.array([
                      [[1,3,4],[2,5,6]],
                      [[3,4,9],[23,53,12]],
                      [[9,7,8],[2,12,2]],
                      [[2,6,9],[4,5,6]]
                      ]) 
print(threedarray.shape)