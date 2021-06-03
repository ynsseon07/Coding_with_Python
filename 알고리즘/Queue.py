from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.popleft()
queue.append(1)
queue.popleft()
queue.append(4)

print(queue)