import datetime
import math
import mymodule as mm
a= mm.person1["age"]
print(a)

from mymodule import person1
print(person1["country"])

x= datetime.datetime.now()
print(x)

x1= datetime.datetime(2024, 4, 30)
print(x1.strftime("%B"))

x=math.ceil(1.4) 
y=math.floor(1.4)
print(x)
print(y)

