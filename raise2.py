from collections.abc import Iterable
def sum(values):
    if not isinstance(values, Iterable):
        raise TypeError('Parameter must be an iterable')
    total = 0
    for value in values:
        if not isinstance(value,(int,float)):
            raise TypeError('Iterable must contain numbers')
        total += value
    return total

numbers = [1, 2, 3, 4, 5,6]
print(sum(numbers))