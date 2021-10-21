import sys
N = int(sys.stdin.readline())
T = []
P = []
dp = []

for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)
    dp.append(p)

dp.append(0)
for i in range(N - 1, -1, -1):
    if i + T[i] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])

print(dp[0])