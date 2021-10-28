import sys

def calc_dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def backtracking(cnt, start, chicken, chicken_spot):
    global ans
    if cnt == M:
        house_chicken = []
        for i in range(N):
            for j in range(N):
                if city[i][j] == 1:
                    x1 = i + 1
                    y1 = j + 1
                    min_val = 10**9
                    for spot in chicken:
                        x2 = spot[0] + 1
                        y2 = spot[1] + 1
                        min_val = min(min_val, calc_dist(x1, y1, x2, y2))
                    # 각 집마다의 치킨거리 구하기
                    house_chicken.append(min_val)      
        city_chicken = sum(house_chicken)
        ans = min(ans, city_chicken)
        return

    for i in range(start, len(chicken_spot)):
        if not visit[i]:
            visit[i] = True
            chicken.append(chicken_spot[i])
            backtracking(cnt+1, i+1, chicken, chicken_spot)
            visit[i] = False
            chicken.pop()


N, M = map(int, sys.stdin.readline().split())
city = []
for _ in range(N):
    city.append(list(map(int, sys.stdin.readline().split())))

# 치킨집들 좌표 저장
chicken_spot = []
for row in range(N):
    for col in range(N):
        if city[row][col] == 2:
            chicken_spot.append([row, col])
visit = [False] * len(chicken_spot)

ans = 10**9
backtracking(0, 0, [], chicken_spot)
print(ans)