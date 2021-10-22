import sys
from collections import deque
# deque는 시간초과 => set으로 사용

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(i, j, board):
    global answer
    queue = set()
    queue.add((i, j, board[i][j]))

    while queue:
        x, y, visit = queue.pop()   # set에서 pop()은 맨 앞의 원소를 제거해줌

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if (0 <= nx < R) and (0 <= ny < C) and (board[nx][ny] not in visit):
                n_visit = visit + board[nx][ny]
                queue.add((nx, ny, n_visit))
                answer = max(answer, 1 + len(visit))


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
answer = 1
bfs(0, 0, board)
print(answer)