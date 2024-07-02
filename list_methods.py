# 1. append()
fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# 2. extend()
fruits = ['apple', 'banana']
fruits.extend(['cherry', 'date'])
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# 3. insert()
fruits = ['apple', 'banana']
fruits.insert(1, 'cherry')
print(fruits)  # Output: ['apple', 'cherry', 'banana']

# 4. remove()
fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'cherry']

# 5. pop()
fruits = ['apple', 'banana', 'cherry']
last_item = fruits.pop()
print(last_item)  # Output: 'cherry'
print(fruits)    # Output: ['apple', 'banana']

# 6. clear()
fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits)  # Output: []

# 7. index()
fruits = ['apple', 'banana', 'cherry']
index = fruits.index('banana')
print(index)  # Output: 1

# 8. count()
fruits = ['apple', 'banana', 'cherry', 'banana']
count = fruits.count('banana')
print(count)  # Output: 2

# 9. sort()
fruits = ['banana', 'apple', 'cherry']
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# 10. reverse()
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)  # Output: ['cherry', 'banana', 'apple']

# 11. copy()
fruits = ['apple', 'banana', 'cherry']
new_fruits = fruits.copy()
print(new_fruits)  # Output: ['apple', 'banana', 'cherry']
