import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
friendship = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    queue = deque()
    queue.append(start)
    friendship[start] = 1

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if friendship[i] == 0:
                friendship[i] = friendship[x] + 1
                queue.append(i)

bfs(1)

count = 0
for f in friendship:
    if 0 < f <= 3:
        count += 1
print(count-1)