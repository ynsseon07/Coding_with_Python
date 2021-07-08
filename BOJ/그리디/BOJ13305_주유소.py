N = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

ans = costs[0] * roads[0]  # 첫 도시에서는 처음 가야될 길만큼만 주유
temp = 0  # 현재까지 주유한 기름 양
min_val = costs[0]  # 현재까지 가장 낮은 주유 비용

# 현재 도시의 주유비용보다 더 낮은 주유비용이 등장하면,
# `지금까지 왔던 거리 * 가장 낮은 주유비용` 값을 결과에 더해줌
for i in range(1, N-1):
    if costs[i] < min_val:
        ans += temp * min_val
        temp = roads[i]
        min_val = costs[i]
    else:
        temp += roads[i]

    # 마지막 도로를 넘어가기 전에 `지금까지 왔던 거리 * 주유 비용` 계산 결과를 더해줌
    if i == N-2:
        ans += temp * min_val

print(ans)