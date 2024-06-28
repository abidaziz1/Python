import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])  #2,4

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])   #1,3,5,7

#Slicing 2-D Arrays

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])   #7,8,9

#From both elements, return index 2
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])   #3,8

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])