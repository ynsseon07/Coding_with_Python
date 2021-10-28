import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
queue = deque([i for i in range(N)])

print('<', end='')
while queue:
    for _ in range(K-1):
        x = queue.popleft()
        queue.append(x)

    if len(queue) == 1:
        print(queue.popleft() + 1, end='')
        print('>')
    else:
        print(queue.popleft() + 1, end='')
        print(',', end=' ')



# visit = [False] * N

# ans = []
# idx = 0
# cnt = 0
# while len(ans) < N:
#     while cnt < K:
#         if idx == N:
#             idx = 0
        
#         if not visit[idx]:
#             cnt += 1
#             if cnt == K:
#                 break
#         idx += 1
    
#     visit[idx] = True
#     ans.append(idx + 1)
#     idx += 1
#     cnt = 0

# print("<", end='')
# for i in range(len(ans)-1):
#     print(ans[i], end=', ')
# print(ans[-1], end='')
# print(">")