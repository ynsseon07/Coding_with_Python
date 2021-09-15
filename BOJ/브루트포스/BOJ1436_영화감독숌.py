# 666부터 시작하여 1씩 더해주고
# 해당 수에 '666'이 포함되어 있다면 카운트 1씩 증가
N = int(input())

num = 666
cnt = 0
while True:
    if '666' in str(num):
        cnt += 1
    if cnt == N:
        print(num)
        break
    num += 1