# 설정된 n에 따라 소수 갯수를 구해주면 시간초과 발생
# => 문제에서 주어진 제한 범위 내의 소수들을 모두 구한 후, 
# n값에 따라 해당 범위 안의 소수 갯수를 카운팅하는 방법 사용

import math, sys

def isSosu(x):
    if x < 2:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

prime_list = [e for e in range(1, 123456 * 2) if isSosu(e)]

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break
    
    count = 0
    for pl in prime_list:
        if n < pl <= 2* n:
            count += 1

    print(count)