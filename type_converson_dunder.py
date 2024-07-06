class MyNumber:
    def __init__(self, num):
        self.num = num
    def __int__(self):
        return int(self.num)
    def __float__(self):
        return float(self.num)
    def __str__(self):
        return str(self.num)
    def __complex__(self):
        return complex(self.num)
    def __bool__(self):
        return bool(self.num)
    def __index__(self):
        return int(self.num)
    def __repr__(self):
        return repr(self.num)

num = MyNumber(5)

# Type conversions
print(f'Integer: {int(num)}')       # Calls __int__
print(f'Float: {float(num)}')       # Calls __float__
print(f'Complex: {complex(num)}')   # Calls __complex__
print(f'Boolean: {bool(num)}')      # Calls __bool__

# Using __index__ for indexing
arr = [10, 20, 30, 40, 50,60]
print(f'Indexing: {arr[num]}')      # Calls __index__

# String representations
print(f'Repr: {repr(num)}')         # Calls __repr__
print(f'Str: {str(num)}')           # Calls __str__