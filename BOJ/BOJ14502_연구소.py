import sys, copy, time
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(N, M, i, j, check_bfs, lab_cpy):
    queue = deque()
    queue.append((i, j))
    check_bfs[i][j] = True

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if (0 <= nx < N) and (0 <= ny < M) and (not check_bfs[nx][ny]) and (lab_cpy[nx][ny] == 0):
                check_bfs[nx][ny] = True
                lab_cpy[nx][ny] = 2
                queue.append((nx, ny))

# 벽 세우기 가능한 모든 경우의 수에 대해 BFS 수행
def backtracking(N, M, cnt, check_backtracking, lab):
    global max_val

    # 벽 3개 세우기 완료하면, 바이러스 전파 시작
    if cnt == 3:
        lab_cpy = copy.deepcopy(lab)
        check_bfs = [[False] * M for _ in range(N)]

        for i in range(N):
            for j in range(M):
                if not check_bfs[i][j] and lab_cpy[i][j] == 2:
                    bfs(N, M ,i, j, check_bfs, lab_cpy)

        # BFS 수행 후, 안전영역 카운트
        safety = 0
        for i in range(N):
            for j in range(M):
                if lab_cpy[i][j] == 0:
                    safety += 1

        max_val = max(max_val, safety)
        return

    for row in range(N):
        for col in range(M):
            if not check_backtracking[row][col] and lab[row][col] == 0:
                check_backtracking[row][col] = True
                lab[row][col] = 1
                backtracking(N, M, cnt + 1, check_backtracking, lab)
                check_backtracking[row][col] = False
                lab[row][col] = 0


N, M = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
check_backtracking = [[False] * M for _ in range(N)]
max_val = 0

backtracking(N, M, 0, check_backtracking, lab)
print(max_val)