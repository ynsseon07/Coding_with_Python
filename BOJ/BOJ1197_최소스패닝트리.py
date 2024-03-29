# 그래프 최단경로 / 최소 신장 트리
# 크루스칼 알고리즘 사용 (Union-Find)

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#  두 원소가 속한 집합 합치기
def union(parent, a, b):
    rootA = find_parent(parent, a)
    rootB = find_parent(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

V, E = map(int, input().split())
parent = [0] * (V + 1)

edges = []
result = 0

for i in range(1, V + 1):
    parent[i] = i

for _ in range(E):
    a, b, c = map(int, input().split())
    # 비용 순으로 오름차순 정렬하기 위해 첫 번째 원소를 비용으로 설정
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge

    # 사이클이 발생하지 않는 경우에만 집합에 포함시킴
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost

print(result)