#Searching Arrays
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)
"""
The example above will return a tuple: (array([3, 5, 6],)
Which means that the value 4 is present at index 3, 5, and 6.
"""

#Find the indexes where the values are even
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)

#Search Sorted, Find the indexes where the value 7 should be inserted
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)

#Find the indexes where the values 2, 4, and 6 should be inserted
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)

#Sorting Arrays
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
#This method returns a copy of the array, leaving the original array unchanged.

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))

#Sorting a 2-D Array
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

