i = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0  and V == 0:
        break

    n = V // P
    m = V % P
    ans = 0

    if m < L:
        ans = n * L + m
    else:
        ans = n * L + L

    print('Case ' + str(i) + ': ' + str(ans))

    i += 1