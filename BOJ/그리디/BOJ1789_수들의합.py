S = int(input())

num = 0
cnt = 0
for i in range(1, S):
    num += i
    cnt += 1
    if S - num <= i:
        num -= i
        break

print(cnt)