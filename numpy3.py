'''
Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''
import numpy as np

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)
#Create an array with data type string

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)
#Create an array with data type 4 bytes integer


#Converting Data Type on Existing Arrays
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i') #you can use int inside the bracket
print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

