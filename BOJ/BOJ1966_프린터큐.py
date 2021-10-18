from collections import deque
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    imp = list(map(int, sys.stdin.readline().split()))

    queue = deque()
    for i in range(len(imp)):
        queue.append((i, imp[i]))
    
    out = 0
    while True:
        flag = False
        frontVal = queue[0]
        
        # 나머지 문서들 중 현재 문서보다 중요도 높은 게 있을 경우
        for j in range(1, len(queue)):
            if frontVal[1] < queue[j][1]:
                front = queue.popleft()
                queue.append(front)
                flag = True
                break

        # flag == True 일 경우, while문 처음으로 되돌아감
        if flag:
            continue
        
        # 나머지 문서들 중 현재 문서보다 중요도 높은 게 없을 경우
        # 문서 인쇄
        out += 1
        front = queue.popleft()

        if front[0] == M:
            break
    
    print(out)
