str1= 'GeeksforGeeks'
upper= lambda string: string.upper()
print(upper(str1))

def cube(y):
  return y*y*y
lambda_cube = lambda y: y*y*y
print("Using function defined with 'def' keyword, cube: ", cube(5))
print("Using lambda function, cube: ", lambda_cube(5))

is_even_list = [lambda arg=x: arg*10 for x in range(1,5)]
for item in is_even_list:
    print(item())

max = lambda a,b: a if (a>b) else b
print(max(3,8))

points = [(2, 3), (1, 2), (4, 1)]
sorted_points = sorted(points, key=lambda x: x[1])
print(sorted_points)  # Output: [(4, 1), (1, 2), (2, 3)]


#lambda is used to create small, anonymous functions at runtime.
#can have any number of arguments but only a single expression.