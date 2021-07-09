N, K = map(int, input().split())

data = [i for i in range(N)]
ans = []
for _ in range(N):
    i = 0
    for _ in range(K):
        i += 1
        if i == len(data):
            i = 0
    ans.append(data.pop(i))

print(ans)


    
