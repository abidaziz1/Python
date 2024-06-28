import functools
tuple1 = tuple()
print("Empty tuple: ", tuple1)
mystring = "nihal"
tuple2 = tuple(mystring)
print("Str to tuple: ", tuple2)

my_string = "Abid Aziz"
slice_obj = slice(1,5,2)
result = my_string[slice_obj]
print(result)

x=[2,8,1,4,6,3,7]
print("Reverse sort: ", sorted(x,reverse=True))
test1= "abidaziz"
res = functools.reduce(lambda x,y: x+y, sorted(test1, reverse =  True))
print("String after reverse sorting: ", str(res))

'''
sorted(test1, reverse=True) returns the list ['z', 'z', 'i', 'd', 'b', 'a', 'a'].
The reduce function applies the lambda function to the first two elements z and z, resulting in the string zz.
The reduce function applies the lambda function to the result zz and the next element i, resulting in the string zzi.
The reduce function continues this process, concatenating the remaining elements in the sorted list, resulting in the final string zzidbaa.
The print statement outputs the final string: String after reverse sorting: zzidbaa.
'''

def func(x):
    return x%7
L = [15,3,11,7]
print("Sorted with key: ",sorted(L,key=func))

Students = [
    {'name':'John', 'age':20},
    {'name':'Alice','age':18},
    {'name':'Bob','age':22}
]
sorted_stu = sorted(Students, key = lambda x: x['age'])
print(sorted_stu)