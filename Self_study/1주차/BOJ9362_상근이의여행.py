# 최소신장트리 문제 (MST: Minimum Spanning Tree)
# n개의 노드를 가진 그래프를 n-1 개의 간선으로 연결한 형태

import sys
t = int(input())

while t > 0:
    n, m = map(int, sys.stdin.readline().split())
    area = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        area[x].append(y)
        area[y].append(x)

    print(n-1)
    t -= 1