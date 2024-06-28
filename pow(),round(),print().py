import math

# pow(x, y, z) returns x to the power of y, modulo z
print(pow(3, 4, 1))  # 3^4 = 81, modulo 1 is 0, so output is 0
print(pow(-4, -3))  # (-4)^(-3) = -0.015625
print(pow(4, -3))  # 4^(-3) = 0.015625
print(pow(-4, 3))  # (-4)^3 = -64

# math functions
num = 3.6
print(math.floor(num))  # returns the largest integer less than or equal to num, so output is 3
print(math.ceil(num))  # returns the smallest integer greater than or equal to num, so output is 4
print(round(51.6))  # rounds to the nearest integer, so output is 52
print(round(-4.7))  # rounds to the nearest integer, so output is -5
print(round(-2.5))  # rounds to the nearest integer, so output is -2
print(round(-1234, 2))  # rounds to 2 decimal places, so output is -1234.0

# converting a range to a set
r = range(5)  # creates a range object from 0 to 4
r = set(r)  # converts the range object to a set
print(str(r))  # output is '{0, 1, 2, 3, 4}'

# string formatting
a, b = 10, 1000
print('The value of a is {} and b is {}'.format(a, b))  # output is 'The value of a is 10 and b is 1000'

# printing multiple values with a separator
c = 12
d = 12
e = 2024
print(c, d, e, sep="-")  # output is '12-12-2024'