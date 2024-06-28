class A:
    _a=10 #protected
    __b=20 #private
    def show(self):
        print("a = ",self._a)
        print("b = ",self.__b)
obj = A()
obj.show()
print("Outside class", obj._a)
#print("Outside class", obj.__b) #error

class Student:
    __name = "Abid Aziz"
    def __init__(self):
        print(self.__name)
        self.__displayInfo()
    def __displayInfo(self):
        print("Welcome!")
obj = Student()

class Employee:
    def setId(self,id):
        self.id = id
    def getId(self):
        return self.id
E1 = Employee()
E1.setId(100)
print(E1.getId())