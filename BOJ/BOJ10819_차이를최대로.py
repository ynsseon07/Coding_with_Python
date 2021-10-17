from itertools import permutations
import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
visited = [False] * N
arr = [0] * N

max_val = -10**3

possible_num = list(permutations(nums, N))

for pn in possible_num:
    res = 0
    for i in range(len(pn) - 1):
        res += abs(pn[i] - pn[i+1])

    max_val = max(max_val, res)

print(max_val)

# N = int(sys.stdin.readline())
# nums = list(map(int, sys.stdin.readline().split()))
# visited = [False] * N
# arr = []
# max_val = -10**3

# def calc_num(cnt):
#     global max_val
#     if cnt == N:
#         res = 0
#         for i in range(N-1):
#             res += abs(arr[i] - arr[i+1])
        
#         max_val = max(max_val, res)
#         return
    
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             arr.append(nums[i])
#             calc_num(cnt+1)
#             visited[i] = False
#             arr.pop()

# calc_num(0)
# print(max_val)