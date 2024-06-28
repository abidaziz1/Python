from itertools import chain
print("Concatenating the result: ")
res =  chain(range(5), range(10,20,2))
for i in res:
    print(i, end=" ")

fruits = ["apple","banana","Cherry"]
for i in range(len(fruits)):
    print(fruits[i])

ele = range(10)[-1]
print("\Last element: ", ele)

for i in range(0,10,2):
    print(i,end=" ")

str =  "Reversed in Python"
for char in reversed(str):
    print(char,end=" ")

lst = [1,2,3]
rev_lst =  reversed(lst)
print(next(rev_lst))

class Test:
    def __init__(self):
        self._internal_var = 42
    def _internal_method(self):
        return self._internal_var
obj = Test()
print(obj._internal_method)
