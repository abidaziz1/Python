# func to count number of given word
def print_even(test_string):
    for i in test_string:
        if i == "geeks":
            yield i

"""
The function iterates over each word i in the test_string using a for loop.
For each word, it checks if the word is equal to "geeks" using the if statement.
If the word is indeed "geeks", the function uses the yield keyword to produce a value. In this case, the value is the word "geeks" itself.
"""

# initializing string
test_string = " There are many geeks around you, \
              geeks are known for teaching other geeks"

# count numbers of geeks used in string
count = 0
print("The number of geeks in string is : ", end="")
#the end="" parameter is used to prevent a newline character from being printed.
test_string = test_string.split()
#splits the string into substrings separated by whitespace characters.
for j in print_even(test_string):
    count = count + 1

print(count)

'''
def infinite_sequence():
    num=0
    while True:
      yield num
      num+=1
for i in infinite_sequence():
print(i, end ="")
'''

#Fibonacci finder

def fib(n):
    a,b=0,1
    while a<n:
        yield a
        a,b=b,a+b
# Iterating over the generator object using next
x=fib(5) 
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# Iterating over the generator object using for 
for i in fib(5):
    print(i)


# generator expression 
generator_exp = (i * 5 for i in range(5) if i%2==0) 
for i in generator_exp: 
    print(i)
"""
i = 0, i * 5 = 0
i = 2, i * 5 = 10
i = 4, i * 5 = 20
"""
"""
Benefits of Iterators
Memory Efficiency: Iterators can be more memory-efficient than using lists, especially with large datasets, because they yield one item at a time.
Lazy Evaluation: Iterators compute their elements on the fly and only when required, which is known as lazy evaluation.
Infinite Sequences: You can use iterators to represent infinite sequences, like the Fibonacci sequence or an infinite stream of numbers.
"""
class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# Using the custom iterator
my_iter = MyIterator(5)

for num in my_iter:
    print(num)