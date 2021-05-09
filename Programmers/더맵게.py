# 우선순위 큐 (heapq) 사용
import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    
    for elem in scoville:
        heapq.heappush(heap, elem)
        
    while heap[0] < K :
        if len(heap) == 1: return -1
        smallest = heapq.heappop(heap)
        next_smallest = heapq.heappop(heap)
        heapq.heappush(heap, smallest + next_smallest * 2)
        answer += 1
        
    return answer