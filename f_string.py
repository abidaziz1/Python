for n in range(1,11):
    sentence = f'The value is {n:02}'
    print(sentence)

from datetime import datetime
birthday = datetime(1990,1,1)
sentence = f'Jenn has a birthday on {birthday:%B %d, %Y}'
print(sentence)

#They are more readable and concise compared to str.format() and % formatting.
#f-strings are generally faster than other string formatting methods.
#You can include expressions directly within the curly braces, not just variable names.
x = 10
y = 20
print(f"The sum of {x} and {y} is {x + y}.")

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

# bin() returns a binary representation of an integer
x = 10
print(bin(x))  # output: 0b1010

# another example
y = 20
print(bin(y))  # output: 0b10100