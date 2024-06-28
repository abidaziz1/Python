import re
import camelcase
txt= "The rain in Spain stays mainly in the plain"
x= re.findall("\AThe", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
    
x1= re.findall(r"\bain",txt)
print(x1)
x2= re.findall(r"\d",txt)
print(x2)
if x1:
    print("Yes, there is at least one match!")
else:
    print("No match")
    
x3= re.split("\s",txt,3)
print(x3)

x4= re.sub("\s","9",txt)
print(x4)

x5= re.search("\s",txt)
print(x5.span())

c= camelcase.CamelCase()
txt1= "hello world"
print(c.hump(txt1))