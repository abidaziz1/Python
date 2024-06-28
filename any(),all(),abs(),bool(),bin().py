# all() returns True if all elements of an iterable are true
numbers = [1, 2, 3, 4, 5]
if all(x > 0 for x in numbers):
    print("All numbers are positive")
# another example
strings = ["hello", "world", "python"]
if all(s.isalpha() for s in strings):
    print("All strings are alphabetic")

# any() returns True if any element of an iterable is true
numbers = [0, 0, 1, 0, 0]
if any(x > 0 for x in numbers):
    print("At least one number is positive")
# another example
strings = ["hello", "world", "", "python"]
if any(not s for s in strings):
    print("At least one string is empty")
def my_any(list_x):
    for i in list_x:
        if i:
            return True
    return False # If it iterates over the entire list and doesn't find any truthy elements, it returns False.
x= [4,5,8,9,10,17]
print(my_any(x))

# bin() returns a binary representation of an integer
x = 10
print(bin(x))  # output: 0b1010
# another example
y = 20
print(bin(y))  # output: 0b10100

# abs() returns the absolute value of a number
x = -5
print(abs(x))  # output: 5
# another example
y = 3.5
print(abs(y))  # output: 3.5

# bool() returns a Boolean value (True or False) for a given expression
x = 5
print(bool(x))  # output: True
# another example
y = 0
print(bool(y))  # output: False
# another example
s = "hello"
print(bool(s))  # output: True
# another example
s = ""
print(bool(s))  # output: False

"""
In Python, the following values are considered "falsy":
False
None
Zero of any numeric type (e.g., 0, 0.0, 0j)
Any empty sequence (e.g., '', [], ())
Any empty mapping (e.g., {})
Any other value that is considered "empty" or "null"
If it finds an element that is truthy, it immediately returns True.
If it iterates over the entire list and doesn't find any truthy elements, it returns False.
"""