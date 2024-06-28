def add(a, b):
    return a + b
def greet(name):
    return f"Hello, {name}!"
def no_return():
    return
# Using the functions
result = add(3, 5)
print(result)  # Output: 8
message = greet("Alice")
print(message)  # Output: Hello, Alice!
none_value = no_return()
print(none_value)  # Output: None


a = True
b = False
result = a or b
print(result)  # Output: True
result = b or False
print(result)  # Output: False
def check_conditions(x, y):
    return x > 0 or y > 0
print(check_conditions(1, -1))  # Output: True
print(check_conditions(-1, -1))  # Output: False


a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # Output: True (b is assigned to a)
print(a is c)  # Output: False (c is a different object with the same content)
d = 5
e = 5
print(d is e)  # Output: True (small integers are cached and reused)
f = 1000
g = 1000
print(f is g)  # Output: False (larger integers may not be cached)
