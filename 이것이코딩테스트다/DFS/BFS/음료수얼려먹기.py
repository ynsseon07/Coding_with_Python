def dfs(graph, x, y):
    if x<0 or x>=n or y<0 or y>=m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(graph, x-1, y)
        dfs(graph, x+1, y)
        dfs(graph, x, y-1)
        dfs(graph, x, y+1)
        return True
    return False

n, m = map(int, input().split())

graph = [ [] for _ in range(n) ]
for i in range(n):
    x = input()
    for j in x:
        graph[i].append(int(j))

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(graph, i, j):
            cnt += 1

print(cnt)
