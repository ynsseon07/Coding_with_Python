N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)

visited = [False] * N
arr = []
answer = []

def make_arr(cnt, start):
    if cnt == M:
        answer.append(tuple(arr))
        return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            arr.append(nums[i])
            make_arr(cnt+1, i+1)
            visited[i] = False
            arr.pop()

make_arr(0, 0)
answer = list(set(answer))
answer = sorted(answer)

for a in answer:
    print(' '.join(str(e) for e in a))
