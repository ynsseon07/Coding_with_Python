import sys, math

T = int(sys.stdin.readline())

def isSosu(x):
    if x < 2:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for _ in range(T):
    n = int(sys.stdin.readline())

    for i in range(n // 2, 1, -1):
        if isSosu(i) and isSosu(n - i):
            print(i, n - i)
            break