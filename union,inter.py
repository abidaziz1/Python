set1 = {"apple", "banana", "Kola"}
set2 = {"apple", "banana"}

set3 = {"apple", "banana", "Kola", "orange"}

print(set1.intersection(set2))
myset = set1.union(set2, set3)
print(myset)

print(set1.difference(set2))

print(set1.symmetric_difference(set2))

print(set1.issubset(set2))