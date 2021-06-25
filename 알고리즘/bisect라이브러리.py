from bisect import bisect_left, bisect_right

a = [1,2,3,3,3,3,4,4,8,9]
x = 3

print(bisect_left(a, 3))    # 원소 3이 시작하는 인덱스
print(bisect_right(a, 3))   # 원소 3이 끝나는 인덱스(마지막 3의 다음 인덱스)
# 위의 두 값을 빼면 3의 갯수 알 수 있다

# 값이 특정 범위에 속하는 데이터 갯수 구하기

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 값이 4인 데이터 갯수 출력
print(count_by_range(a, 4, 4))

# 값이 3인 데이터 갯수 출력
print(count_by_range(a, 3, 3))
