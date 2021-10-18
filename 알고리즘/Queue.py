from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
# 큐는 append와 popleft 기억
# 첫번째 원소는 popleft로 알 수 있음
# 마지막 원소는 pop으로 알 수 있음

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.popleft()
queue.append(1)
queue.popleft()
queue.append(4)
queue.append(7)
queue.append(6)

print('큐에서 인덱스 사용가능: queue[3] =', queue[3])

print('순서대로:', queue)        # 먼저 들어온 순서대로 출력
print('첫번째 원소 출력 및 pop:', queue.popleft())
print('마지막 원소 출력 및 pop:', queue.pop())
print('변경된 큐:', queue)

print('==========================')

queue.reverse()                 # 역순으로 바꾸기
print('역순서:', queue)        # 나중에 들어온 원소부터 출력
print('첫번째 원소 출력 및 pop:', queue.popleft())
print('마지막 원소 출력 및 pop:', queue.pop())
print('변경된 큐:', queue)