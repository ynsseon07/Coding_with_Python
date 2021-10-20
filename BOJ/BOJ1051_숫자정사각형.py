import sys
N, M = map(int, sys.stdin.readline().split())
rect = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

val = min(N, M)
max_size = 0

# 1 * 1 배열이 입력으로 주어질 경우 0이 아닌 1로 출력돼야함
for k in range(0, val):
    for i in range(N - k):
        for j in range(M - k):
            japyo = [[i, j], [i+k, j], [i, j+k], [i+k, j+k]]
            
            point_val = rect[japyo[0][0]][japyo[0][1]]

            if point_val == rect[japyo[1][0]][japyo[1][1]] and point_val == rect[japyo[2][0]][japyo[2][1]] and point_val == rect[japyo[3][0]][japyo[3][1]]:
                max_size = max(max_size, (k+1)**2)

print(max_size)