N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)

cnt = 0
for coin in coins:
    if K >= coin:
        cnt += (K // coin)
        K = K % coin
    
    if K == 0:
        break

print(cnt)

###################################
# 덧셈, 뺄셈 사용했을 경우 시간초과
# 덧셈, 나누기가 더 효과적
###################################
