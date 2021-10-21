# 풀이는 단순한데 아이디어가 이해가 가질 않음
# 추후 확인 다시 필요


# import sys, time
# from collections import deque

# dx = [1,0,-1,0]
# dy = [0,1,0,-1]

# def bfs(i, j, visited, board_map):
#     queue = deque()
#     queue.append((i, j))
#     visited[i][j] = 1

#     while queue:
#         x, y = queue.popleft()

#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]

#             if (0 <= nx < N) and (0 <= ny < M) and (visited[nx][ny] < 0) and (board_map[nx][ny] == 0):
#                 visited[nx][ny] = visited[x][y] + 1
#                 queue.append((nx, ny))


# N, M = map(int, sys.stdin.readline().split())
# board_map = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
# visited = [[-1] * M for _ in range(N)]

# min_dist = 10**9
# bfs(0, 0, visited, board_map)
# if visited[N-1][M-1] != -1:
#     min_dist = visited[N-1][M-1]

# for row in range(len(board_map)):
#     for col in range(len(board_map[0])):
#         if board_map[row][col] == 1:
#             board_map[row][col] = 0
            
#             visited = [[-1] * M for _ in range(N)]
#             bfs(0, 0, visited, board_map)
#             if visited[N-1][M-1] != -1:
#                 min_dist = min(min_dist, visited[N-1][M-1])

#             board_map[row][col] = 1

# if min_dist == 10**9:
#     print(-1)
# else:
#     print(min_dist)