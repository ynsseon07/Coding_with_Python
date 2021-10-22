import sys

# def binary_search(arr, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] < target:
#             start = mid + 1
#         elif arr[mid] > target:
#             end = mid - 1
#         else:
#             return mid
#     return -1

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

V, E = map(int, input().split())
parent = [i for i in range(V+1)]

edges = []
result = 0

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    cost, x, y = edge

    if find_parent(parent, x) != find_parent(parent, y):
        union(parent, x, y)
        result += cost

print(result)