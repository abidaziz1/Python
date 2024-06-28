class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.__fuel_level = 0  # Private attribute

    def add_fuel(self, amount):
        self.__fuel_level += amount

    def start(self):
        if self.__fuel_level > 0:
            print("Car started")
        else:
            print("No fuel, please add fuel")

# Usage
my_car = Car("Toyota", "Camry")
my_car.add_fuel(10)
my_car.start()  # Output: Car started



class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload the + operator
    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)

    # Overload the str operator for printing
    def __str__(self):
        return f"({self.x}, {self.y})"

# Create two vectors
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Add the vectors using the overloaded + operator
v3 = v1 + v2

# Print the result using the overloaded _str_ method
print(v3)  # Output: (6, 8)




class Base: 
    def __init__(self): 
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"

# Creating a derived class 
class Derived(Base): 
    def __init__(self): 
        Base.__init__(self) 
        print("Calling private member of base class: ") 
        # Accessing the mangled private attribute
        print(self._Base__c) 

# Driver code 
obj1 = Base() 
print(obj1.a) 
# print(obj1.__c)  # This will raise an AttributeError

obj2 = Derived()  # This will now work correctly


class Bird:
  
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
  
    def flight(self):
        print("Sparrows can fly.")

class ostrich(Bird):

    def flight(self):
        print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()