N, M = map(int, input().split())

card = list(map(int, input().split()))

max_result = 0
for i in range(len(card)):
    for j in range(i + 1, len(card)):
        for k in range(j + 1, len(card)):
            hap = card[i] + card[j] + card[k]
            if hap <= M:
                max_result = max(hap, max_result)

print(max_result)