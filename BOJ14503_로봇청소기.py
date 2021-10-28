import sys
sys.setrecursionlimit(1000000)

# 북, 동, 남, 서 이동 방향
headingX = [-1, 0, 1, 0]
headingY = [0, 1, 0, -1]

# 후진 방향
backX = [1, 0, -1, 0]
backY = [0, -1, 0, 1]

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = 0

def cleaning(i, j, d):
    global cnt
    
    # 청소할 수 없는 곳일 경우
    if board[i][j] == 1:
        return
    
    # 청소가능한 곳일 경우
    if board[i][j] == 0:
        board[i][j] = 2
        cnt += 1

    # 현재 방향 기준으로 왼쪽부터 인접한 칸 탐색
    for _ in range(4):
        if d - 1 < 0:
            hIdx = 3
        else:
            hIdx = d-1
        
        x = i + headingX[hIdx]
        y = j + headingY[hIdx]

        if (0 <= x < N) and (0 <= y < M) and board[x][y] == 0:
            cleaning(x, y, hIdx)
            return
        else:
            d = hIdx

    # 네 방향 모두 청소 되어있는 상태 or 벽인 경우 한 칸 뒤로 후진
    x = i + backX[d]
    y = j + backY[d]
    cleaning(x, y, d)

cleaning(r, c, d)
print(cnt)