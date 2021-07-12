import math

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(math.lcm(A, B))

# math 라이브러리 안에 최대공약수 gcd / 최소공배수 lcm 존재
# 단, lcm은 파이썬 3.9 이상 버전에서만 작동