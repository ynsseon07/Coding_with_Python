import sys

N, M = map(int, sys.stdin.readline().split())
visited = [False for _ in range(N)]
arr = []

def make_arr(x, idx):
    if x == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()
    else:
        for i in range(idx, N):
            arr.append(i+1)
            make_arr(x+1, i)
            arr.pop()

make_arr(0, 0)
