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


N = int(input())
M = int(input())
parent = [0] * (N + 1)

for i in range(N + 1):
    parent[i] = i

edges= []
result = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost

print(result)