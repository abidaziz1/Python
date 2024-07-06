class MyNumber:
    def __init__(self, value):
        self.value = value

    def __neg__(self):
        return MyNumber(-self.value)

    def __pos__(self):
        return MyNumber(+self.value)

    def __abs__(self):
        return MyNumber(abs(self.value))

    def __invert__(self):
        return MyNumber(~self.value)

    def __repr__(self):
        return f'MyNumber({self.value})'

# Creating an instance of MyNumber
num = MyNumber(5)

# Using unary methods
print(f'Negative: {-num}')  # Calls __neg__
print(f'Positive: {+num}')  # Calls __pos__
print(f'Absolute: {abs(num)}')  # Calls __abs__
print(f'Bitwise NOT: {~num}')  # Calls __invert__
