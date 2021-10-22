import sys

def make_team(cnt, idx, N, start_team, visited):
    global answer
    if cnt == N // 2:
        link_team = []
        for num in range(N):
            if not visited[num]:
                link_team.append(num+1)
        
        # 두 팀의 능력치 구하기
        start_sum = 0
        for i in range(len(start_team)):
            for j in range(len(start_team)):
                if i != j:
                    start_sum += S[start_team[i]-1][start_team[j]-1]
        
        link_sum = 0
        for i in range(len(link_team)):
            for j in range(len(link_team)):
                if i != j:
                    link_sum += S[link_team[i]-1][link_team[j]-1]

        answer = min(answer, abs(start_sum - link_sum))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            start_team.append(i+1)
            make_team(cnt+1, i+1, N, start_team, visited)
            visited[i] = False
            start_team.pop()

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

start_team = []
visited = [False] * N
answer = 10**9

make_team(0, 0, N, start_team, visited)
print(answer)