import sys
N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums = sorted(nums)

arr = []
ans = []

def make_arr(x, idx):
    if x == M:
        ans.append(tuple(arr))

    else:
        for i in range(idx, N):
            arr.append(nums[i])
            make_arr(x+1, i)
            arr.remove(nums[i])

make_arr(0, 0)

ans_new = list(set(ans))
ans_new = sorted(ans_new)

for an in ans_new:
    print(' '.join(str(e) for e in an))