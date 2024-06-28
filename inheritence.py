class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    
    def __str__(self):
        return f"{self.firstname} ({self.lastname})"
        
p1= Person("John","Doe")
print(p1)

class Person1:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(abc):
        print("Hello my name is "+abc.name+ ". My age is "+str(abc.age))
p1 = Person1("John",36)

p1.myfunc()
p1.age=40
p1.myfunc()

class Student[Person]:
    def __init__(self,fname,lname):
        Person.__init__(      self,fname,lname)
x= Student("Mike", "Olsen")
print(x)
