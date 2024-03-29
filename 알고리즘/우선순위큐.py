import heapq
# 파이썬은 최소힙으로 구현
# 최대힙을 위해서는 원소 push, pop시 마이너스 부호 붙이기

heap = []

# 우선순위큐에 삽입
heapq.heappush(heap, 5)     
heapq.heappush(heap, 2)
heapq.heappush(heap, 10)
heapq.heappush(heap, 7)
heapq.heappush(heap, 4)

print(heap[0])     # 최소값 삭제하지 않고 얻을 수 있음
                   # 단, data[1], data[2]가 차례로 두번째, 세번째로 작은 값일 보장은 없다
        
# 우선순위큐에서 삭제
heapq.heappop(heap)
heapq.heappop(heap)
print(heap[0])