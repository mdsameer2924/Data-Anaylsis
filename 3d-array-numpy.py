##[3][4][3]
import numpy as np
array=np.array([[[6,7,88],[3,8,0],[5,34,2],[88,98,78]],[[5,51,67],[3,4,2],[7,8,9],[2,5,7]],[[11,12,23],[5,2,1],[8,9,9],[3,7,8]]])
print(type(array))
print(f"dimension of an array {array.ndim}")
print("show the rows columns and depth of an array", array.shape)
print("minimum value of an array" ,array.min())
print("position of an min value of an array", array.argmin())
print("max value of an arary" ,array.max())
print("position of an max value of an array", array.argmax())
print("mean of an array is", array.mean())
print("Standard deviataion of array is ",array.std())
