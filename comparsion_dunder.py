class MyNumber:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, MyNumber):
            return self.value == other.value
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, MyNumber):
            return self.value != other.value
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, MyNumber):
            return self.value < other.value
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, MyNumber):
            return self.value <= other.value
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, MyNumber):
            return self.value > other.value
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, MyNumber):
            return self.value >= other.value
        return NotImplemented

    def __repr__(self):
        return f'MyNumber({self.value})'

# Creating instances of MyNumber
num1 = MyNumber(5)
num2 = MyNumber(10)

# Using comparison methods
print(f'num1 == num2: {num1 == num2}')  # Calls __eq__
print(f'num1 != num2: {num1 != num2}')  # Calls __ne__
print(f'num1 < num2: {num1 < num2}')    # Calls __lt__
print(f'num1 <= num2: {num1 <= num2}')  # Calls __le__
print(f'num1 > num2: {num1 > num2}')    # Calls __gt__
print(f'num1 >= num2: {num1 >= num2}')  # Calls __ge__


"""
__init__ Method: This is the initializer method that sets up an instance of the MyNumber class with a given value. When you create an instance of MyNumber, you pass a value to it, and this value is stored in the value attribute of the instance.
__eq__ Method: Checks if the other object is an instance of MyNumber. If it is, it compares their value attributes for equality. If other is not an instance of MyNumber, it returns NotImplemented.

"""