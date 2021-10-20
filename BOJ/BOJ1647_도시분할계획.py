import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find_parent(parent, a)
    rootB = find_parent(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

N, M = map(int, sys.stdin.readline().split())
parent = [0] * (N + 1)

for i in range(N + 1):
    parent[i] = i

edges = []
result = 0
temp = []

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost
        temp.append(cost)

max_len = max(temp)
result -= max_len
print(result)