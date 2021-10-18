N = int(input())
N_nums = list(map(int, input().split()))
N_nums = sorted(N_nums)

M = int(input())
M_nums = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid
    return -1

for i in range(len(M_nums)):
    res = binary_search(N_nums, M_nums[i], 0, N-1)
    if res != -1:
        print(1)
    else:
        print(0)