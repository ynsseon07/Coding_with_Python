n = int(input())
m = int(input())

graph = [ [] for _ in range(n+1) ]
visit = [False] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0
def dfs(x):
    global cnt
    visit[x] = True
    cnt += 1

    for i in graph[x]:
        if not visit[i]:
            dfs(i)    

dfs(1)
print(cnt-1)

# graph를 인접리스트로 표현해서 풀이
# 방문여부 표시하는 visit 리스트 (노드 갯수만큼 = n+1)