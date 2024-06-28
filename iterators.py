fruits = ['apple', 'orange', 'kola','mod']
iterator = iter(fruits)

for i in range(len(fruits)):
    try:
        print(next(iterator))
    except StopIteration:
        break       



def _sum(arr):
    sum=0
    for i in arr:
        sum+=i
    return(sum)
if __name__ == "__main__":
    arr= [12,3,4,15]
    n= len(arr)
    ans= _sum(arr)
    print('Sum of the array is ',ans)
    print('Size of that array was ',n)


arr1 = [1,2,3,4]
ans = sum(arr1)
print('Sum of the array will be',ans,'I hope.')

list1= [1,3,5,7]; s=0
for i, a in enumerate(list1):
    s+=a
print(s)

my_tuple = (1, 2, 3, 4, 5)
total = sum(my_tuple)
print(total)

my_dict = {'a': 10, 'b': 20, 'c': 30}
total = sum(my_dict.values())
print(total)

numbers = [1,2,3,4,5,1,4,5]
Sum = sum(numbers)
avg = Sum/len(numbers)
print(avg)