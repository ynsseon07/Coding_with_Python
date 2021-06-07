from collections import deque

m, n, h = map(int, input().split())
graph = [ [] for _ in range(h) ]
for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, input().split())))

# 방문여부 표시위한 리스트
visit = [[[-1 for col in range(m)] for row in range(n)] for depth in range(h)]

# 좌표이동 리스트
dx = [1,0,-1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]

queue = deque()

# 익은 토마토(1)를 큐에 모두 넣음 + 익은 토마토의 방문여부 1로 표시
# 토마토가 들어있지 않은 칸(-1) 부분의 방문여부 0으로 표시
# 익지 않은 토마토(0) 부분의 방문여부는 -1
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                visit[i][j][k] = 1
                queue.append((i, j, k))

            if graph[i][j][k] == -1:
                visit[i][j][k] = 0

while queue:
    z, x, y = queue.popleft()

    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or ny<0 or nz<0 or nx>=n or ny>=m or nz>=h:
            continue
        if visit[nz][nx][ny] >= 0:      # 토마토가 들어있지 않은 칸 또는 이미 방문한 칸일 경우
            continue
        visit[nz][nx][ny] = visit[z][x][y] + 1
        queue.append((nz, nx, ny))

ans = 0
isTrue = False
for i in range(h):
    for j in range(n):
        for k in range(m):
            ans = max(ans, visit[i][j][k])

            # 토마토가 모두 익지 못한 상황
            if visit[i][j][k] == -1:
                isTrue = True
            
if isTrue:
    print(-1)
else:
    print(ans-1)
