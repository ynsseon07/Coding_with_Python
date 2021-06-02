answer = 0
n, m = map(int, input().split())

for i in range(n):
    nums = list(map(int, input().split()))
    min_value = min(nums)
    answer = max(answer, min_value)

print(answer)
