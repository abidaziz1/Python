def fun(variable):
    letters= ['a','e','i','o','u']
    if(variable in letters):
        return True
    else:
        return False
sequence = ['g','e','i','k','a']
filtered = filter(fun, sequence) #Syntax is filter(function,iterable)
print("Filtered elements are: ")
for s in filtered:
    print(s)
    
#with lambda
seq= [0,1,2,3,5,8,13]
result= list(filter(lambda x: x%2!=0, seq))
print(result)

def is_multiple_of_3(num):
    return num%3==0
nums = [1,2,3,4,5,6,7,8,9,10]
result= list(filter(lambda x:is_multiple_of_3(x) , nums))
print(result)