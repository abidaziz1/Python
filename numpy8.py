from numpy import random
import numpy as np

x=random.randint(100, size=(5))
print(x)  #5 random numbers in an 1-D array

x = random.rand()
print(x)   #random float from 0 and 1

x = random.randint(100)
print(x)   #random integer from 0 and 100

x = random.randint(100, size=(3, 5))
print(x)    #Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100

x = random.rand(5)
print(x)    #1-D array containing 5 random floats

#2-D array with 3 rows, each row containing 5 random float numbers
x = random.rand(3, 5)
print(x)

#Return one of the values in an array
x = random.choice([3, 5, 7, 9])
print(x)

x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)

x = random.choice([3,5,7,9], p = [0.1,0.3,0.6,0.0], size=(100))
print(x)  #The sum of all probability numbers should be 1

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)

arr = np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)   #Randomly shuffle elements of following array
#The shuffle() method makes changes to the original array.

arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr)) 
#The permutation() method returns a re-arranged array (and leaves the original array un-changed).

