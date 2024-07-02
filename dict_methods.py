import json

# 1. clear()
fruits = {'apple': 1, 'banana': 2, 'cherry': 3}
fruits.clear()
print(fruits)  # Output: {}

# 2. copy()
fruits = {'apple': 1, 'banana': 2, 'cherry': 3}
new_fruits = fruits.copy()
print(new_fruits)  # Output: {'apple': 1, 'banana': 2, 'cherry': 3}

# 3. fromkeys()
keys = ['apple', 'banana', 'cherry']
fruits = dict.fromkeys(keys, 0)
print(fruits)  # Output: {'apple': 0, 'banana': 0, 'cherry': 0}

# 4. get()
fruits = {'apple': 1, 'banana': 2, 'cherry': 3}
print(fruits.get('banana'))  # Output: 2
print(fruits.get('date', 'Not Found'))  # Output: Not Found

# 5. items()
fruits = {'apple': 1, 'banana': 2, 'cherry': 3}
print(fruits.items())  # Output: dict_items([('apple', 1), ('banana', 2), ('cherry', 3)])

# 6. keys()
fruits = {'apple': 1, 'banana': 2, 'cherry': 3}
print(fruits.keys())  # Output: dict_keys(['apple', 'banana', 'cherry'])

# 7. pop()
fruits = {'apple': 1, 'banana': 2, 'cherry': 3}
print(fruits.pop('banana'))  # Output: 2
print(fruits)  # Output: {'apple': 1, 'cherry': 3}

# 8. popitem()
fruits = {'apple': 1, 'banana': 2, 'cherry': 3}
print(fruits.popitem())  # Output: ('cherry', 3) (the output may vary)
print(fruits)  # Output: {'apple': 1, 'banana': 2}

# 9. setdefault()
fruits = {'apple': 1, 'banana': 2}
print(fruits.setdefault('cherry', 3))  # Output: 3
print(fruits)  # Output: {'apple': 1, 'banana': 2, 'cherry': 3}

# 10. update()
fruits = {'apple': 1, 'banana': 2}
fruits.update({'cherry': 3, 'date': 4})
print(fruits)  # Output: {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4}

# 11. values()
fruits = {'apple': 1, 'banana': 2, 'cherry': 3}
print(fruits.values())  # Output: dict_values([1, 2, 3])

