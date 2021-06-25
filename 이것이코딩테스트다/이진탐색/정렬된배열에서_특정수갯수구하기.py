from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
array = list(map(int, input().split()))

array.sort()

left_index = bisect_left(array, x)
right_index = bisect_right(array, x)

count = right_index - left_index

if count == 0:
    print(-1)
else:
    print(count)