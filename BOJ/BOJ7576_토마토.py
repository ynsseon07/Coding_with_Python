import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
tomatoes = []
for i in range(N):
    tomatoes.append(list(map(int, sys.stdin.readline().split())))

visited = [[-1]*M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque()

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = 0

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M) and (tomatoes[nx][ny] != -1) and (visited[nx][ny] < 0):
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))

max_val = 0
for i in range(N):
    for j in range(M):
        max_val = max(max_val, visited[i][j])

        # 토마토가 모두 익지 못하는 상황
        if (visited[i][j] == -1) and (tomatoes[i][j] == 0):
            print(-1)
            exit()

print(max_val)