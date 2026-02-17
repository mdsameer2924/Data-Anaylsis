##[3][4][3]
import numpy as np
array=np.arange(20,50)
array=array.reshape(6,5)
print("TO update all the value at an array: ",array.fill(0))
print("is any value is non-zero",array.any())
print("is here is this are all values are non-zero",array.all())
print((array))
print(f"dimension of an array {array.ndim}")
print("show the rows columns and depth of an array", array.shape)
print("minimum value of an array" ,array.min())
print("position of an min value of an array", array.argmin())
print("max value of an arary" ,array.max())
print("position of an max value of an array", array.argmax())
print("mean of an array is", array.mean())
print("Standard deviataion of array is ",array.std())

print("to transpose array means flip array dimenstion",array.transpose())
