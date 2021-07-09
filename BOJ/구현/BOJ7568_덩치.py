N = int(input())

pp = []
for _ in range(N):
    pp.append(list(map(int, input().split())))

rank = [0] * len(pp)
for i in range(len(pp)):
    for j in range(len(pp)):
        if i == j:
            continue
        if pp[i][0] < pp[j][0] and pp[i][1] < pp[j][1]:
            rank[i] += 1

for r in rank:
    print(r+1, end=' ')