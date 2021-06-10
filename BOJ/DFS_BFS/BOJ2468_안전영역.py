# 파이썬으로 풀기 위해서는 아래 코드가 꼭 필요
# 재귀를 제한하는 코드
import sys
sys.setrecursionlimit(100000)

n = int(input())

ground = []
for i in range(n):
    ground.append(list(map(int, input().split())))

sink = [ [False for _ in range(n)] for _ in range(n) ]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(x, y):
    sink[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if sink[nx][ny]:
            continue
        dfs(nx, ny)

max_h = 0
answer = 0

while max_h <= 100:
    for i in range(n):
        for j in range(n):
            if ground[i][j] <= max_h:
                sink[i][j] = True

    cnt = 0
    for i in range(n):
        for j in range(n):
            if not sink[i][j]:
                dfs(i, j)
                cnt += 1

    answer = max(answer, cnt)
    max_h += 1
    sink = [ [False for _ in range(n)] for _ in range(n) ]

print(answer)

