x = 9
print(x < 5 and x < 10)
print(x < 5 or x < 10)

x1 = ["apple", "banana"]
print("apple" not in x1)

thislist = ["apple", "banana", "cherry"]
tropical = ["apple", "banana", "pineapple"]
thislist.extend(tropical)
print(thislist)

for x in thislist:
    if 'a' in x:
        print(x)
print("apple")

mytuple = ("apple","banana","kola")
print(type(mytuple))