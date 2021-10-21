import sys
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(i, j, visited, check):
    area = 0
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if (0 <= nx < M) and (0 <= ny < N) and not visited[nx][ny] and check[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                area += 1
    
    return area

M, N, K = map(int, sys.stdin.readline().split())
check = [[True] * N for _ in range(M)]

k_nums = []
for _ in range(K):
    k_nums.append(tuple(map(int, sys.stdin.readline().split())))

for kn in k_nums:
    x1, y1, x2, y2 = kn
    for row in range(M - y2, M - y1):
        for col in range(x1, x2):
            check[row][col] = False

visited = [[False] * N for _ in range(M)]
answer = []
cnt = 0
for i in range(M):
    for j in range(N):
        if not visited[i][j] and check[i][j]:
            res = bfs(i, j, visited, check)
            cnt += 1
            answer.append(res + 1)
answer.sort()

print(cnt)
for a in answer:
    print(a, end=' ')