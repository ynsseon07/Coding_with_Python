import math
from itertools import permutations

def isSosu(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num_list = list(numbers)
    temp_set = set()
    for i in range(1, len(numbers) + 1):
        possible_num = list(permutations(num_list, i))
        print('possible_num =', possible_num)

        for pn in possible_num:
            print("pn:", pn)
            temp = ''.join(pn)
            temp_set.add(int(temp))
        
    temp_list = list(temp_set)
        
    for tm in temp_list:
        if isSosu(tm):
            answer += 1
    
    return answer

print(solution("17"))
print(solution("011"))