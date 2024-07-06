from itertools import batched

data: list[int] = [1,2,3,4,5,6,7,8,9]
batch: batched = batched(data, n=2)
print(list(batch))