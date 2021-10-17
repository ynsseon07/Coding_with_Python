import sys
N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
visited = [False] * N
arr = [0] * N
ans = 0

def partial_number(cnt, start, n):
    global ans
    if cnt == n:
        if sum(arr) == S:
            ans += 1
        return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            arr[i] = nums[i]
            partial_number(cnt+1, i+1, n)
            visited[i] = False
            arr[i] = 0


# 뽑을 숫자의 갯수 정하기 (1개 ~ N개)
for i in range(1, N + 1):
    partial_number(0, 0, i)

print(ans)