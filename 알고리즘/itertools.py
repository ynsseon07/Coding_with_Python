from itertools import permutations, combinations

data = [1,2,3,4,5]

result1 = list(permutations(data, 3))
result2 = list(combinations(data, 3))

print(result1)
print('-------------------')
print(result2)