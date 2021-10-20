# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())

# 부모 테이블 초기화하기 (노드 갯수만큼)
parent = [0] * (v + 1)  

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생하지 않았다면 합집합(Union) 연산 수행
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
