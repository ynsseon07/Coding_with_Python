from collections import deque

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

graph = [ [] for _ in range(n+1) ]
visit = [0] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(p1, p2):
    queue = deque()
    queue.append(p1)

    while queue:
        x = queue.popleft()
        if x == p2:
            return visit[x]
        
        for i in graph[x]:
            if visit[i] == 0:
                visit[i] = visit[x] + 1
                queue.append(i)

if bfs(p1, p2):
    print(visit[p2])
else:
    print(-1)
