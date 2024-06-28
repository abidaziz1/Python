class Base:
    def __init__(self):
        self.__private_var = "I'm in Private"
    def __private_method(self):
        self.__private_method()
    def access_private_method(self):
        self.__private_method()
class Derived(Base):
    def __init__(self):
        super.__init__()
        self.__private_var = "I'm in Private in Derived"
    def __private_method(self):
        print("Private method in Derived")

obj1 = Base()
print(obj1._Base__private_var)
obj2 = Derived()
print(obj2._Derived__private_var)
