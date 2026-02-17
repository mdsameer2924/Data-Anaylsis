
import numpy as np
array=np.array([[1,2,3,4,5],
                [6,7,8,9,0],
                [0,8,6,4,2]
                ]

               )
print(type(array))
print(f"dimension of an array {array.ndim}")
print("show the rows columns and depth of an array", array.shape)
print("minimum value of an array" ,array.min())
print("position of an min value of an array", array.argmin())
print("max value of an arary" ,array.max())
print("position of an max value of an array", array.argmax())
print("mean of an array is", array.mean())
print("Standard deviataion of array is ",array.std())
