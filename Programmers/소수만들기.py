from itertools import combinations
import math

def isSosu(num):                        # 소수판별 함수
    if num < 2: return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        
    return True

def solution(nums):
    answer = 0

    pick = list(combinations(nums, 3))  # nums 리스트에서 서로 다른 3개의 조합 구하기
    for elem in pick:                   # 3개씩 뽑힌 수의 합이 소수인지 판별
        if isSosu(sum(elem)):
            answer += 1

    return answer