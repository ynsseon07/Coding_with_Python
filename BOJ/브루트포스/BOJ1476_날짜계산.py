o_E, o_S, o_M, cnt = 1, 1, 1, 1

E, S, M = map(int, input().split())

# o_E, o_S, o_M 이 E, S, M과 같아질 때까지 1씩 더하며 증가
# cnt가 우리가 알고 있는 연도
while True:
    if o_E == E and o_S == S and o_M == M:
        print(cnt)
        break
    else:
        o_E += 1
        if o_E > 15:
            o_E -= 15

        o_S += 1
        if o_S > 28:
            o_S -= 28

        o_M += 1
        if o_M > 19:
            o_M -= 19
            
        cnt += 1
