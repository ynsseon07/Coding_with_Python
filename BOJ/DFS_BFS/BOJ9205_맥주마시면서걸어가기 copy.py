# bfs 사용

from collections import deque

t = int(input())

def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

for _ in range(t):
    n = int(input())

    pos = []
    for _ in range(n+2):
        pos.append(list(map(int, input().split())))

    visit = [False for _ in range(n+2)]

    queue = deque()
    queue.append(0)
    visit[0] = True

    while queue:
        x = queue.popleft()

        for idx, p in enumerate(pos):
            if not visit[idx] and distance(pos[x], p) <= 1000:
                visit[idx] = True
                queue.append(idx)


    if visit[n+1]:
        print("happy")
    else:
        print("sad") 