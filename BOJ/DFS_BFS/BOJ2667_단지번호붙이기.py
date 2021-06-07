n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 각 단지내의 인원 파악하기 위한 변수
living = 0

def dfs(x, y, dangee):
    global living
    graph[x][y] = dangee
    living += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if graph[nx][ny] == 0 or graph[nx][ny] > 1:
            continue
        dfs(nx, ny, dangee)


dangee = 2
cnt = 0     # 전체 단지 수 파악하기 위한 변수
house = []  # 각 단지내의 인원 수를 담을 리스트
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            living = 0  # 각 단지내의 인원 파악 위해 초기화
            dfs(i, j, dangee)      # dfs 수행
            house.append(living)   # dfs 실행 후의 living을 house 리스트에 추가
            cnt += 1        # 전체 단지 수 증가
            dangee += 1     # 단지 번호는 2, 3, 4, ...

print(cnt)
house.sort()
for i in house:
    print(i)

