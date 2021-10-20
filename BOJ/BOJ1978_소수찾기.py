import math

def sosu(x):
    if x <= 1:
        return False
    
    if x == 2:
        return True
    
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

N = int(input())
nums = list(map(int, input().split()))

count = 0
for n in nums:
    if sosu(n):
        count += 1

print(count)