import copy
n = int(input())

arr = []    # 비교 대상의 원본
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr_copy = copy.deepcopy(arr)   # 새롭게 저장될 값

for i in range(n-1):
    for j in range(i+1):
        left = arr_copy[i][j] + arr[i+1][j]
        right = arr_copy[i][j] + arr[i+1][j+1]

        arr_copy[i+1][j] = max(left, arr_copy[i+1][j])
        arr_copy[i+1][j+1] = max(right, arr_copy[i+1][j+1])

ans = max(arr_copy[n-1])
print(ans)