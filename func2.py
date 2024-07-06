def myfunc():
    x=300
    def innerfunc():
        print(x)
    innerfunc()

myfunc()
# Nested function can access the variables of the outer function, even after the outer function has returned.

x1= 350
def myfuc():
   x2=200 #global x2=200 use korle baire theke x2 output deya zabe
   print(x2)
myfuc()

print(x1)


def func1():
    x= "Jane"
    def func2():
        nonlocal x #with nonlocal keyword, the variable will belong to the outer function
        x= "John"
    func2()
    return x
print(func1())


# Global variable
count = 0

def increment():
    global count  # Declare the variable as global
    count += 1    # Modify the global variable

def display_count():
    print(f"The current count is {count}")

# Before calling the function
print("Before incrementing:")
display_count() #0

# Call the increment function
increment()

# After calling the function
print("After incrementing:")
display_count() #1

'''
Inside the increment function, the global keyword is used to tell Python that we are referring to the global count variable, not a local one.The line count += 1 increments the global count variable by 1.
'''