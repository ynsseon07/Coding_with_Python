# 이분탐색(이진탐색)
import sys

K, N = map(int, sys.stdin.readline().split())
lanseon = [int(sys.stdin.readline()) for _ in range(K)]

def binary(arr, target, start, end):
    while start <= end:
        cnt = 0
        mid = (start + end) // 2

        # 이미 갖고 있는 K개의 랜선으로부터 몇개의 랜선 얻어낼 수 있는지 구함
        for i in range(len(arr)):
            cnt += arr[i] // mid

        # 랜선 길이 줄여야함
        if cnt < target:
            end = mid - 1
        # 랜선 길이 늘려야함
        else:
            start = mid + 1
    return end

# 랜선 길이 1부터 가장 긴 랜선길이까지 사이의 값을 탐색
ans = binary(lanseon, N, 1, max(lanseon))
print(ans)