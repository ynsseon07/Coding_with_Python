import sys

n = int(input())

data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

data = sorted(data, key=lambda x: (x[0],x[1]))

for elem in data:
    for e in elem:
        print(e, end=' ')
    print()