import math

M = int(input())
N = int(input())

def isSosu(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

sosuList = []
for k in range(M, N + 1):
    if isSosu(k):
        sosuList.append(k)

if sosuList:
    print(sum(sosuList))
    print(min(sosuList))
else:
    print(-1)