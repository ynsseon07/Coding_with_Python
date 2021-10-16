import sys
N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums = sorted(nums)

visited = [False for _ in range(N)]
arr = []

def make_arr(x):
    if x == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()

    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                arr.append(nums[i])
                make_arr(x+1)
                visited[i] = False
                arr.pop()

make_arr(0)
