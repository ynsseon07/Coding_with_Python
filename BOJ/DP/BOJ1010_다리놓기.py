# 다이나믹 프로그래밍(동적 프로그래밍)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    # DP 테이블 만들기
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

    # N = 1일때, dp[N][M] = M
    for m in range(M+1):
        dp[1][m] = m

    # N >= 2일때, dp[N][M] = dp[N-1][M-1] + dp[N-1][M-2] + ... + dp[N-1][N-1]
    for i in range(2, N+1):
        for j in range(i, M+1):
            for k in range(1, j-i+2):
                dp[i][j] += dp[i-1][j-k]
    
    print(dp[N][M])