from abc import ABC, abstractmethod
class Car(ABC):
    def show(self):
        print("Every class has 4 wheels.")
    @abstractmethod
    def speed(self):
        pass
class BMW(Car):
    def speed(self):
        print("Speed is: 100 Km/H")
class Suzuki(Car):
    def speed(self):
        print("Speed is: 70 Km/H")

obj = BMW()
obj.show()
obj.speed()

obj2 = Suzuki()
obj2.show()
obj2.speed()