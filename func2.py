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
