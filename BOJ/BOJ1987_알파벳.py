import sys

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

answer = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# BFS 활용
def move():
    global answer

    queue = set([(0, 0, board[0][0])])

    while queue:
        x, y, visited = queue.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < R) and (0 <= ny < C) and (board[nx][ny] not in visited):
                n_visited = visited + board[nx][ny]
                queue.add((nx, ny, n_visited))
                answer = max(answer, len(n_visited))

move()
print(answer)