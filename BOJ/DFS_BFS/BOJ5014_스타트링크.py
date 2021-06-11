from collections import deque

F, S, G, U, D = map(int, input().split())

visit = [False for _ in range(F+1)]
move = [0 for _ in range(F+1)]

def bfs(x):
    queue = deque()
    queue.append(x)
    visit[x] = True

    while queue:
        x = queue.popleft()
        if x == G:
            break

        for next_step in (x+U, x-D):
            if 1 <= next_step <= F and not visit[next_step]:
                move[next_step] = move[x] + 1
                visit[next_step] = True
                queue.append(next_step)

bfs(S)

if visit[G]:
    print(move[G])
else:
    print("use the stairs")
