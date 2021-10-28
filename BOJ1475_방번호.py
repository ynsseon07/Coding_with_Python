import sys

N = sys.stdin.readline().strip()
nums = [0] * 9

for i in N:
    n = int(i)
    if n == 9:
        nums[6] += 1
    else:
        nums[n] += 1

if nums[6] % 2 != 0:
    nums[6] = nums[6] // 2 + 1
else:
    nums[6] = nums[6] // 2
    
print(max(nums))