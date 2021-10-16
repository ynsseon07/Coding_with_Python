import sys

def make_arr(cnt, idx):
    if cnt == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()
    
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            arr.append(i+1)
            make_arr(cnt+1, i+1)
            visited[i] = False
            arr.pop()

N, M = map(int, sys.stdin.readline().split())
visited = [False for _ in range(N)]
arr = []

make_arr(0, 0)