import sys

K = int(sys.stdin.readline())
num = []
for _ in range(K):
    x = int(sys.stdin.readline())
    if x == 0:
        num.pop()
    else:
        num.append(x)
    
print(sum(num))