import sys
N = sys.stdin.readline().strip()

len_N = len(N)

res = 0
for i in range(len_N - 1):
    res += 9 * 10 ** i * (i+1)

res += (int(N) - 10 ** (len_N - 1) + 1) * len_N

print(res)