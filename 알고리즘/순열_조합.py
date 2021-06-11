data = [6,10,24,13]

###### 순열 ######
from itertools import permutations

result = list(permutations(data, 2))
# print(result)


###### 조합 ######
from itertools import combinations

result = list(combinations(data, 2))
# print(result)


###### 순열(중복허용) ######
from itertools import product

result = list(product(data, repeat=2))
# print(result)


###### 조합(중복허용) ######
from itertools import combinations_with_replacement

result = list(combinations_with_replacement(data, 2))
print(result)