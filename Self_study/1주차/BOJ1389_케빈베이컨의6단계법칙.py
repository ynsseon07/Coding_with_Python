from collections import deque

def bfs(p1, p2, graph, visited):
    queue = deque()
    queue.append(p1)

    while queue:
        x = queue.popleft()
        if x == p2:
            return visited[p2]

        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = visited[x] + 1
                queue.append(i)


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

data = []   # 각 사람의 단계수 저장할 리스트
for i in range(1, n + 1):
    hap = 0
    for j in range(1, n + 1):
        if i == j:
            continue
        else:
            visited = [0] * (n + 1)
            val = bfs(i, j, graph, visited)
            hap += val
    data.append(hap)

kebin_bacon = min(data)
ans = data.index(kebin_bacon) + 1
print(ans)