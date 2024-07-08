class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, MyNumber):
            return MyNumber(self.value + other.value)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, MyNumber):
            self.value += other.value
            return self
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, MyNumber):
            return MyNumber(self.value - other.value)
        return NotImplemented

    def __rsub__(self, other):
        return MyNumber(other.value - self.value)

    def __isub__(self, other):
        if isinstance(other, MyNumber):
            self.value -= other.value
            return self
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, MyNumber):
            return MyNumber(self.value * other.value)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        if isinstance(other, MyNumber):
            self.value *= other.value
            return self
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, MyNumber):
            return MyNumber(self.value / other.value)
        return NotImplemented

    def __rtruediv__(self, other):
        return MyNumber(other.value / self.value)

    def __itruediv__(self, other):
        if isinstance(other, MyNumber):
            self.value /= other.value
            return self
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, MyNumber):
            return MyNumber(self.value // other.value)
        return NotImplemented

    def __rfloordiv__(self, other):
        return MyNumber(other.value // self.value)

    def __ifloordiv__(self, other):
        if isinstance(other, MyNumber):
            self.value //= other.value
            return self
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, MyNumber):
            return MyNumber(self.value % other.value)
        return NotImplemented

    def __rmod__(self, other):
        return MyNumber(other.value % self.value)

    def __imod__(self, other):
        if isinstance(other, MyNumber):
            self.value %= other.value
            return self
        return NotImplemented

    def __pow__(self, other):
        if isinstance(other, MyNumber):
            return MyNumber(self.value ** other.value)
        return NotImplemented

    def __rpow__(self, other):
        return MyNumber(other.value ** self.value)

    def __ipow__(self, other):
        if isinstance(other, MyNumber):
            self.value **= other.value
            return self
        return NotImplemented

    def __repr__(self):
        return f'MyNumber({self.value})'

# Creating instances of MyNumber
num1 = MyNumber(5)
num2 = MyNumber(10)

# Using arithmetic methods
print(f'Addition: {num1 + num2}')  # Calls __add__
print(f'In-place Addition: {num1 += num2}')  # Calls __iadd__
print(f'Subtraction: {num1 - num2}')  # Calls __sub__
print(f'In-place Subtraction: {num1 -= num2}')  # Calls __isub__
print(f'Multiplication: {num1 * num2}')  # Calls __mul__
print(f'In-place Multiplication: {num1 *= num2}')  # Calls __imul__
print(f'True Division: {num1 / num2}')  # Calls __truediv__
print(f'In-place True Division: {num1 /= num2}')  # Calls __itruediv__
print(f'Floor Division: {num1 // num2}')  # Calls __floordiv__
print(f'In-place Floor Division: {num1 //= num2}')  # Calls __ifloordiv__
print(f'Modulo: {num1 % num2}')  # Calls __mod__
print(f'In-place Modulo: {num1 %= num2}')  # Calls __imod__
print(f'Exponentiation: {num1 ** num2}')  # Calls __pow__
print(f'In-place Exponentiation: {num1 **= num2}')  # Calls __ipow__
