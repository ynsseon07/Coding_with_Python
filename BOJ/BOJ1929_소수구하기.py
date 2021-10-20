import math, sys

def isSosu(x):
    if x < 2:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

M, N = map(int, sys.stdin.readline().split())

for elem in range(M, N + 1):
    if isSosu(elem):
        print(elem)