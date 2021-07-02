# 시간초과 방지를 위한 sys
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    volunteers = []
    cnt = 0
    for _ in range(n):
        volunteers.append(list(map(int, input().split())))

    volunteers.sort(key=lambda x: x[0])

    cnt += 1
    min = volunteers[0][1]
    for i in range(1, len(volunteers)):
        if min > volunteers[i][1]:
            cnt += 1
            min = volunteers[i][1]

    print(cnt)

###########################################
# 서류순위 기준으로 오름차순 정렬
# 인덱스 0(=0번째 지원자)부터 면접순위 비교
# min으로 설정 후 값을 계속 갱신해나간다
############################################