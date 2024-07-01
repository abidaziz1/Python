# Using elvis, multiple condition checking in one line
def valid_length(user_input: str) -> bool:
    return 'Yes case' if len(user_input) > 10 else 'No case'
valid_length("I love")

# Password Generator
from secrets import choice
from typing import Callable
from string import ascii_letters, digits, punctuation

pass_gen: Callable[[int], str] = lambda x: ''.join(choice(ascii_letters + digits + punctuation) for _ in range(x))
password = pass_gen(12)  # Generate a 12-character password
print(password)

"""
choice(ascii_letters + digits + punctuation): This selects a random character from the combined string of all ASCII letters, digits, and punctuation characters.
for _ in range(x): This generates a sequence of x random characters using the choice function.
''.join(...): This concatenates the sequence of random characters into a single string, which is the generated password.
The Callable[[int], str] type hint indicates that pass_gen is a function that takes an integer as input and returns a string.
"""

# Email extractor
import re
from typing import List

Email = Callable[[str], List[str]]
get_emails: Email = lambda text: re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

text = "Hello, my email is john.doe@example.com and you can also reach me at jane.doe@example.co.uk."
emails = get_emails(text)
print(emails)  # Output: ['john.doe@example.com', 'jane.doe@example.co.uk']
"""
Email type alias represents a function that takes a single str argument (the input text) and returns a List[str] (a list of extracted email addresses).
\b: Word boundary (ensures we don't match part of a larger word)
[A-Za-z0-9._%+-]+: Matches one or more characters that are letters (both uppercase and lowercase), digits, or special characters (., _, %, +, -)
@: Matches the @ symbol
[A-Za-z0-9.-]+: Matches one or more characters that are letters (both uppercase and lowercase), digits, or special characters (., -)
\.: Matches a period (escaped with a backslash because . has a special meaning in regex)
[A-Z|a-z]{2,}: Matches the domain extension (it must be at least 2 characters long and consist only of letters)
"""

# Dictionary get Method with Default Value
info: dict[str, str] = {'name': 'Bob', 'job': 'Programmer'}
print(info.get('age', -1))  # Output: -1

# Reversing Lists and Strings
numbers: list[int] = [1, 2, 3, 4, 5]
greeting: str = 'Hello, Bob!'
print(numbers[::-1])  # Output: [5, 4, 3, 2, 1]
print(greeting[::-1])  # Output: '!boB ,olleH'

# String Multiplication
shout: str = 'AAAAAAAAAH!'
shout2: str = ('A' * 20) + 'H!'
print(shout2)  # Output: 'AAAAAAAAAAAAAAAAAAAAH!'

# Ternary Conditional Operator
number: int = 10
result: str = 'Even' if number % 2 == 0 else 'Odd'
print(result)  # Output: 'Even'

# Join List of Strings
emails: list[str] = ['bob@bobmail.com', 'notbob@bobmail.com', 'federico@bobmail.com']
print(f"Emails: {', '.join(emails)}")  # Output: 'Emails: bob@bobmail.com, notbob@bobmail.com, federico@bobmail.com'

# List Comprehension to Square Numbers
squares = [x ** 2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Dictionary Comprehension
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictio = {k: v for k, v in zip(keys, values)}
print(dictio)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Using map Function to Convert to Uppercase
words = ['hello', 'world']
upper_words = list(map(str.upper, words))
print(upper_words)  # Output: ['HELLO', 'WORLD']

# Filtering a List to Get Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6, 8, 10]

# Class with __call__ Method
class Multiplier:
    def __init__(self, value: int) -> None:
        self.value = value
    def __call__(self,other_value: int) -> int:
        return self.value * other_value
    
double: Multiplier = Multiplier(3)
print(double(10))

# Uses setdefault to set a default value for a key if it doesn't exist.
scores = {'Bob': 102, 'Mario': 55}
james_score: int = scores.setdefault('James', 0)
print(james_score)  # Output: 0
print(scores)  # Output: {'Bob': 102, 'Mario': 55, 'James': 0}

# Counts the occurrences of elements in a list and returns the most common elements.
from collections import Counter
letters: list[str] = ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'D']
counter: Counter = Counter(letters)
print(counter.most_common(n=3))  # Output: [('A', 3), ('B', 2), ('C', 2)]

# Merges two dictionaries using the |= operator.
a: dict[str, int] = {'a': 1, 'b': 2}
b: dict[str, int] = {'c': 3, 'd': 4}
a |= b
print(a)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Formats a large number with commas for better readability.
big_number: int = 1234567890
print(f'{big_number:,}')  # Output: 1,234,567,890

# Using zip to Iterate Over Multiple Sequences
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f'{name} is {age} years old')

# Using islice to Slice an Iterator
from itertools import islice
data = range(10)
sliced_data = list(islice(data, 2, 8))
print(sliced_data)  # Output: [2, 3, 4, 5, 6, 7]

# Using heapq to Get the Largest Elements
import heapq

numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
largest = heapq.nlargest(3, numbers)
print(largest)  # Output: [9, 8, 7]

# Finding the Name with the Most 'a's
names: list[str] = ['Timothy', 'Bob', 'James', 'Zebra', 'Amanda', 'Anna', 'Luigi']
for name in names:
    print(name, name.lower().count('a'), sep=': ')
# Output:
# Timothy: 0
# Bob: 0
# James: 1
# Zebra: 1
# Amanda: 2
# Anna: 2
# Luigi: 0
print('Max:', max(names, key=lambda x: x.lower().count('a')))
# Output: Max: Amanda

# Method Chaining in a Class
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    def modify_name(self, new_name: str) -> 'Person':
        self.name = new_name
        return self
    def modify_age(self, new_age: int) -> 'Person':
        self.age = new_age
        return self
bob: Person = Person('Bob', 29)
bob.modify_age(10).modify_name('James')
print(f'{bob.name}: {bob.age}')
# Output: James: 10

# Unpacking List with *
foods: list[str] = ['Apples', 'Bananas', 'Oranges']
print(*foods, sep=', ', end='.\n')
# Output: Apples, Bananas, Oranges.

# Unpacks the first and last elements from a list and collects the middle elements.
people: list[str] = ['Bob', 'James', 'George', 'Fred', 'Luigi', 'Sofia']
first, *_ , last = people
print(first, last)
print(_)

# Replacing Substrings in a String
sentence: str = 'The tired red fox on the red farm ate a bored red pig.'
print(sentence.replace('red', 'XXX'))
# Output: The tired XXX fox on the XXX farm ate a bored XXX pig.
print(sentence.replace(' red', ' blue'))
# Output: The tired blue fox on the blue farm ate a bored blue pig.


