import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
button_error = list(map(int, sys.stdin.readline().split()))

# 채널 번호에 고장난 버튼 포함되는지 확인
# check의 결과가 False이면 이동할 수 없는 채널
# check의 결과가 True이면 이동할 수 있는 채널
def check(x):
    num = list(str(x))
    button_check = [str(e) for e in button_error]
    for n in num:
        if n in button_check:
            return False
    return True

result = abs(N - 100)
# 채널 1부터 100만까지 돌리면서 리모컨 이동 최소 횟수 구하기
for i in range(1000001):
    if check(i):
        result = min(result, len(str(i)) + abs(N - i))

print(result)