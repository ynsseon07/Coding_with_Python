n = int(input())
cities = []

for _ in range(n):
    cities.append(list(map(int,input())))

visit = [[False] * n for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

cnt = 0

def dfs(x, y, idx):
    global cnt
    visit[x][y] = True
    cities[x][y] = idx
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if cities[nx][ny] == 0 or cities[nx][ny] > 1:
            continue
        dfs(nx, ny, idx)

total = 0
idx = 2
result = []
for i in range(n):
    for j in range(n):
        if cities[i][j] == 1 and not visit[i][j]:
            cnt = 0
            dfs(i, j, idx)
            result.append(cnt)
            total += 1
            idx += 1

result.sort()
print(total)
for r in result:
    print(r)