import sys

N = int(sys.stdin.readline())
answer = 0

col = [False] * 40
diag1 = [False] * 40
diag2 = [False] * 40

def set_Queen(x):
    global answer
    if x == N:
        answer += 1
        return
    
    for i in range(N):
        if not col[i] and not diag1[x+i] and not diag2[x-i+N-1]:
            col[i] = True
            diag1[x+i] = True
            diag2[x-i+N-1] = True

            set_Queen(x+1)

            col[i] = False
            diag1[x+i] = False
            diag2[x-i+N-1] = False

set_Queen(0)
print(answer)
