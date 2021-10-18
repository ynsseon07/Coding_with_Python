# 브루트 포스(완전탐색)
# 시간 초과 발생...
# 제한 시간은 3초
# 1. 현재 코드 상태로 할 경우 4.95초
# 2. arr을 미리 지정하는 대신 빈 리스트로 선언 후, append와 pop 사용시에는 6.82초

import sys, time

start = time.time()

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
visited = [False] * N
arr = [0] * N
answer = 0

def calc(cnt, start):
    global answer

    if cnt == 3:
        temp = []
        for i in range(N):
            if arr[i] != 0:
                temp.append(arr[i])
        
        ai, aj, ak = temp[0], temp[1], temp[2]
        if aj - ai == ak - aj:
            answer += 1

        return
    
    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            arr[i] = A[i]
            calc(cnt+1, i+1)
            visited[i] = False
            arr[i] = 0

calc(0, 0)
print(answer)

print('time:', time.time() - start)