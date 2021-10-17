import sys

N = int(sys.stdin.readline())
number = N // 2

S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [False for _ in range(N)]
total = set(range(0, N))
start = [0] * number

global min_value
min_value = 10**9

def make_team(cnt, idx):
    if cnt == number:   # 스타트팀 정해짐
        # 링크팀 정하기
        link = list((total - set(start)))

        # 각 팀의 능력치 구하기
        start_hap = 0
        link_hap = 0

        for i in range(number):
            for j in range(i+1, number):
                start_hap += S[start[i]-1][start[j]-1] + S[start[j]-1][start[i]-1]
                link_hap += S[link[i]-1][link[j]-1] + S[link[j]-1][link[i]-1]

        global min_value
        min_value = min(min_value, abs(start_hap - link_hap))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            start[cnt] = i
            make_team(cnt+1, i+1)
            visited[i] = False

make_team(0, 0)
print(min_value)