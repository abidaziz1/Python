def generate_numbers():
    for i in range(5):
        yield i

# Using the generator
gen = generate_numbers()
for number in gen:
    print(number)


'''
with open('example.txt','w') as file:
    file.write('Hello, world!')

# Output: This writes "Hello, world!" to the file example.txt
the with statement ensures that the file is properly closed after the block of code is executed, even if an exception is raised.
'''
#With is commonly used for resource management, such as opening and closing files, or acquiring and releasing locks.

def divide(x,y):
    if y==0:
        raise ValueError("Cannot divide by zero")
    return x/y
try:
    result = divide(10,2)
    print(result)
except ValueError as e:
    print(e)


def placeholder_function():
    pass

# Output: Nothing happens, as pass does nothing


def check_point(value):
    if value is None:
        return "No value"
    return value
print(check_value(None))
print(check_value(42))