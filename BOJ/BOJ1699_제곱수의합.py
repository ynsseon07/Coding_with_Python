import sys

N = int(sys.stdin.readline())

d = [i for i in range(N + 1)]

for i in range(N + 1):
    for j in range(2, i):
        if j * j > i:
            break
        d[i] = min(d[i],  d[i - (j * j)] + 1)

print(d[N])


# https://it-and-life.tistory.com/76 참조