class A:
    def show(self):
        print("Welcome")
    def show(self,f_name=''):
        print("Welcome ",f_name)
    def show(self,f_name='',l_name=''):
        print("Welcome ", f_name, l_name)

obj = A()
obj.show()
obj.show("Abid!")
obj.show("Abid", "Aziz!")


class B:
    def disp(self):
        print("Parent Class")
class C(B):
    def disp(self):
        print("Child Class")
        super().disp()  
obj1 = C()
obj1.disp()

