# visit 리스트 하나로 풀이
# 리스트 전체를 -1로 초기화
# 시작점은 0으로 설정
# visit[x] == -1인 경우는 방문 안한 좌표
# 따라서 결과가 -1이라면 use the stairs

from collections import deque

F, S, G, U, D = map(int, input().split())

visit = [-1 for _ in range(F+1)]

def bfs(x):
    queue = deque()
    queue.append(x)
    visit[x] = 0

    while queue:
        x = queue.popleft()
        if x == G:
            break

        for next_step in (x+U, x-D):
            if 1 <= next_step <= F and visit[next_step] == -1:
                visit[next_step] = visit[x] + 1
                queue.append(next_step)

bfs(S)

if visit[G] != -1:
    print(visit[G])
else:
    print("use the stairs")