import sys
sys.setrecursionlimit(100000)
# 재귀 문제를 풀때는 위 코드 필수
import copy

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(x, y):
    visit[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if bingsan_copy[nx][ny] > 0 and not visit[nx][ny]:
            dfs(nx, ny)

# 빙산 주변 0의 갯수(바닷물과 맞닿는 면 갯수) 세기
def melt(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if bingsan[nx][ny] == 0:
            cnt += 1

    return cnt


n, m = map(int, input().split())
bingsan = []
for i in range(n):
    bingsan.append(list(map(int, input().split())))

visit = [[False for _ in range(m)] for _ in range(n)]

# bingsan_copy 값이 변하는게 bingsan에 영향을 주면X
# deepcopy는 값만 그대로 복사, 메모리주소는 공유X
bingsan_copy = copy.deepcopy(bingsan)
year = 0

while year >= 0:
    year += 1
    for i in range(n):
        for j in range(m):
            if bingsan_copy[i][j] != 0:
                melting = melt(i, j)
                bingsan_copy[i][j] = 0 if bingsan_copy[i][j] - melting < 0 else bingsan_copy[i][j] - melting

    ans = 0
    for i in range(n):
        for j in range(m):
            if bingsan_copy[i][j] != 0 and not visit[i][j]:
                dfs(i, j)
                ans += 1

    if ans > 1:
        print(year)
        exit()

    # 빙산이 모두 녹으면 ans는 0이다. (dfs 수행안되므로)
    if ans == 0:
        print(0)
        exit()

    # 변경된 빙산 상태를 다시 bingsan에 deepcopy
    # visit 리스트도 초기화 필요
    bingsan = copy.deepcopy(bingsan_copy)
    visit = [[False for _ in range(m)] for _ in range(n)]
