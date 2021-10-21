import sys
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs_normal(i, j, visited, N, grid):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    temp = grid[i][j]

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if (0 <= nx < N) and (0 <= ny < N) and not visited[nx][ny] and grid[nx][ny] == temp:
                visited[nx][ny] = True
                queue.append((nx, ny))

def bfs_rg(i, j, visited, N, grid):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    temp = grid[i][j]

    if temp == 'R' or temp == 'G':
        while queue:
            x, y = queue.popleft()

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if (0 <= nx < N) and (0 <= ny < N) and not visited[nx][ny] and grid[nx][ny] != 'B':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    else:
        while queue:
            x, y = queue.popleft()

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if (0 <= nx < N) and (0 <= ny < N) and not visited[nx][ny] and grid[nx][ny] == temp:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    


N = int(sys.stdin.readline())
grid = [list(sys.stdin.readline().strip()) for _ in range(N)]

cnt_normal = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs_normal(i, j, visited, N, grid)
            cnt_normal += 1

cnt_rg = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs_rg(i, j, visited, N, grid)
            cnt_rg += 1

print(cnt_normal, cnt_rg)