from abc import ABC, abstractmethod
import math
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    def move(self):
        return "Runs"

class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

    def move(self):
        return "Flies"

# Trying to instantiate an abstract class will raise an error
# animal = Animal()  # This will raise TypeError: Can't instantiate abstract class Animal with abstract methods make_sound, move

dog = Dog()
print(dog.make_sound())  # Output: Woof!
print(dog.move())        # Output: Runs

bird = Bird()
print(bird.make_sound())  # Output: Chirp!
print(bird.move())        # Output: Flies




math.sin(x)    # Sine of x radians
math.cos(x)    # Cosine of x radians
math.tan(x)    # Tangent of x radians
math.asin(x)   # Inverse sine of x, in radians
math.acos(x)   # Inverse cosine of x, in radians
math.atan(x)   # Inverse tangent of x, in radians
math.atan2(y, x)  # Arctangent of y/x, in radians
math.degrees(x)   # Convert angle x from radians to degrees
math.radians(x)   # Convert angle x from degrees to radians

math.sinh(x)   # Hyperbolic sine of x
math.cosh(x)   # Hyperbolic cosine of x
math.tanh(x)   # Hyperbolic tangent of x
math.asinh(x)  # Inverse hyperbolic sine of x
math.acosh(x)  # Inverse hyperbolic cosine of x
math.atanh(x)  # Inverse hyperbolic tangent of x

math.exp(x)    # e raised to the power of x
math.expm1(x)  # e raised to the power of x, minus 1
math.log(x, base=math.e)  # Natural logarithm of x to base e (default)
math.log1p(x)  # Natural logarithm of 1 + x
math.log10(x)  # Base-10 logarithm of x
math.log2(x)   # Base-2 logarithm of x

math.pow(x, y)  # x raised to the power y
math.sqrt(x)    # Square root of x
math.isqrt(x)   # Integer square root of x

math.ceil(x)   # Ceiling of x (smallest integer >= x)
math.floor(x)  # Floor of x (largest integer <= x)
math.trunc(x)  # Truncate x to the nearest integer towards zero
math.copysign(x, y)  # Return a float with the magnitude of x and the sign of y
math.fabs(x)   # Absolute value of x

math.factorial(x)  # Factorial of x
math.gcd(a, b)     # Greatest common divisor of a and b
math.lcm(a, b)     # Least common multiple of a and b (Python 3.9+)
math.isfinite(x)   # Check if x is neither an infinity nor a NaN
math.isinf(x)      # Check if x is positive or negative infinity
math.isnan(x)      # Check if x is NaN
