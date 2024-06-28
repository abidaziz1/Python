"""
yield
Purpose: Turns a function into a generator, allowing it to return values one at a time, pausing and resuming state between each return.
Behavior: Pauses the function and returns a value; subsequent calls to the generator resume from where it left off.
Use Case: When you want to produce a sequence of values over time, rather than computing them all at once.
"""

def generate_numbers():
    for i in range(5):
        yield i

gen = generate_numbers()
for number in gen:
    print(number)


"""
return
Purpose: Used to exit a function and optionally pass back a value to the caller.
Behavior: Terminates the function entirely and returns a value immediately.
Use Case: When a function completes its task and needs to provide a result back to the caller.
"""
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8
