# Global variable
x = 10

def outer():
    # Local variable in outer function
    x = 20

    def inner():
        # Nonlocal variable in inner function
        nonlocal x
        x = 30

        def innermost():
            # Local variable in innermost function
            x = 40
            print("Innermost:", x)

        innermost()
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
print("Global:", x)

'''
When the innermost function returns, its local variables are discarded, and the inner function's x variable remains unchanged.
nonlocal keyword in the inner function allows it to modify the x variable in the outer function's scope. When the inner function assigns x = 30, it modifies the x variable in the outer function's scope, so when the outer function prints its x variable, it prints 30
'''

"""
Innermost: 40: This is printed by the innermost function, which has its own local x set to 40.
Inner: 30: This is printed by the inner function, where x is the nonlocal variable referring to the x in outer, which was set to 30.
Outer: 30: This is printed by the outer function, where x was set to 30 by the inner function.
Global: 10: This is printed outside of any function, showing the global x, which remains unchanged at 10.
"""


def outer_function():
    x = "outer"
    def inner_function():
        nonlocal x  # This refers to the x in outer_function
        x = "inner"
        print("Inner:", x)  # Output: Inner: inner
    inner_function()
    print("Outer:", x)  # Output: Outer: inner
outer_function()


x = "global"
def modify_global():
    global x  # This refers to the global x
    x = "modified"
    print("Inside function:", x)  # Output: Inside function: modified
modify_global()
print("Outside function:", x)  # Output: Outside function: modified
