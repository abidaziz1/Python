#The Difference Between Copy and View
#the copy is a new array, and the view is just a view of the original array.
'''
The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
'''

import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0]=42
print(arr)
print("Copy Method",x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print("View Method", x)

"""
The copy returns None.
The view returns the original array.
"""
arr = np.array([1,2,3,4,5])
x= arr.copy()
y=arr.view()
print(x.base)   #None
print(y.base)   #1 2 3 4 5


#Get the Shape of an Array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)  #returns (2,4) , 2 rows each with 4 elements

arr = np.array([1,2,3,4],ndmin=5)
print(arr)
print("Shape of array:",arr.shape)
