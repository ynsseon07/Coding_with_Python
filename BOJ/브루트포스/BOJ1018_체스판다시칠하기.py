# 시작이 흰색인 체스판 형태 배열 --- 1
# 시작이 검은색인 체스판 형태 배열 --- 2

# 주어진 보드에서 (0,0)좌표부터 8*8크기로 차례로 탐색
# 시작좌표가 흰색이면 1과 비교해서 칠해야 될 부분 갯수 반환
# 시작좌표가 검은색이면 2와 비교해서 칠해야 될 부분 갯수 반환
# ==> 시작좌표로 white와 black 중 어느 것과 비교할지 고르는 것은 잘못된 방법
# ==> 8*8크기로 골라낸 board를 white, black 둘 다와 비교해야함

white = [ ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'] ]

black = [ ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'] ]

def compare_white(board, i, j):
    change = 0
    for a in range(8):
        for b in range(8):
            if white[a][b] != board[a + i][b + j]:
                change += 1

    return change

def compare_black(board, i, j):
    change = 0
    for a in range(8):
        for b in range(8):
            if black[a][b] != board[a + i][b + j]:
                change += 1

    return change

N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(str, input())))

min_change = 10**9
for i in range(N):
    for j in range(M):
        if i + 7 < N and j + 7 < M:
            tmp = min(compare_white(board, i, j), compare_black(board, i, j))
            min_change = min(tmp, min_change)

print(min_change)