# 방법1
# 인접행렬을 인접리스트 graph로 변환 후 dfs 수행
def dfs(graph, visited, v):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False] * n
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                if i != j:
                    graph[i].append(j)
    
    for i in range(n):
        if not visited[i]:
            dfs(graph, visited, i)
            answer += 1
    
    return answer


# 방법 2
# 인접행렬을 사용 -> dfs 함수 안의 내용만 바뀜
def dfs(computers, visited, v):
    visited[v] = True
    
    for i in range(len(computers[v])):
        if not visited[i] and computers[v][i] == 1:
            dfs(computers, visited, i)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            answer += 1
    
    return answer