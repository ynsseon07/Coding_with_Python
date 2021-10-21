import sys
# BFS 탐색시 import 필요
from collections import deque
# DFS 탐색시 제귀제한 필요
sys.setrecursionlimit(100000)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

# # BFS로 구현
# def find_ground(N, i, j, visited, sink):
#     queue = deque()
#     queue.append((i, j))
#     visited[i][j] = True

#     while queue:
#         x, y = queue.popleft()

#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]

#             if (0 <= nx < N) and (0 <= ny < N) and (not visited[nx][ny]) and (sink[nx][ny] == 0):
#                 visited[nx][ny] = True
#                 queue.append((nx, ny))

# DFS로 구현
def find_ground(N, i, j, visited, sink):
    visited[i][j] = True

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if (0 <= nx < N) and (0 <= ny < N) and (not visited[nx][ny]) and (sink[nx][ny] == 0):
            find_ground(N, nx, ny, visited, sink)

N = int(sys.stdin.readline())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sink = [[0] * N  for _ in range(N)]
visited = [[False] * N for _ in range(N)]

max_rain = max(max(ground))
max_val = 0

for rain in range(max_rain + 1):

    # 높이 <= rain인 부분 물에 잠김 표시 (1: 물에 잠김, 0: 물에 잠김X)
    for row in range(len(ground)):
        for col in range(len(ground[0])):
            if ground[row][col] <= rain:
                sink[row][col] = 1

    # 리스트 탐색 통해 물에 잠기지 않은 안전영역 갯수 확인
    cnt = 0
    for i in range(len(ground)):
        for j in range(len(ground[0])):
            if not visited[i][j] and sink[i][j] == 0:
                find_ground(N, i, j, visited, sink)
                cnt += 1

    max_val = max(max_val, cnt)
    sink = [[0] * N  for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

print(max_val)