from collections import deque

n, k = map(int, input().split())

visit = [ 0 for _ in range(100001)]

queue = deque()
queue.append(n)

while queue:
    x = queue.popleft()
    if x == k:
        break

    for next_step in (x-1, x+1, 2*x):
        if 0 <= next_step < 100001 and not visit[next_step]:
            visit[next_step] = visit[x] + 1
            queue.append(next_step)

print(visit[k])

# visit 리스트 0으로 초기화
# -> 방문 안했으면 그대로 0(=False)
# -> 방문했으면 0이 아닌 정수(=True)