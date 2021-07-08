# 왼쪽 상단부터 행렬 두개를 비교
# 두 원소가 다를 경우
# 3*3 크기의 부분 행렬에 있는 모든 원소를 뒤집음

N, M = map(int, input().split())
graphA = []
graphB = []
for _ in range(N):
    graphA.append(list(map(int, input())))
for _ in range(N):
    graphB.append(list(map(int, input())))

cnt = 0
for i in range(N):
    for j in range(M):
        if i + 2 >= N or j + 2 >= M:
            continue
        if graphA[i][j] != graphB[i][j]:
            for a in range(i, i+3):
                for b in range(j, j+3):
                    if graphA[a][b] == 1:
                        graphA[a][b] = 0
                    else:
                        graphA[a][b] = 1
            cnt += 1

if graphA == graphB:
    print(cnt)
else:
    print(-1)
            
# 파이썬 2차원 리스트 Slicing / 일부만 선택, 추출
# temp = [row[j:j+3] for row in graphA[i:i+3]]
