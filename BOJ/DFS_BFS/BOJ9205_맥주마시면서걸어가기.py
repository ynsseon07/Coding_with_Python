# dfs 사용

t = int(input())

def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def dfs(x):
    visit[x] = True

    for idx, p in enumerate(pos):
        if not visit[idx] and distance(pos[x], p) <= 1000:
            dfs(idx)

for _ in range(t):
    n = int(input())

    pos = []
    for _ in range(n+2):
        pos.append(list(map(int, input().split())))

    visit = [False for _ in range(n+2)]

    dfs(0)

    if visit[n+1]:
        print("happy")
    else:
        print("sad") 
