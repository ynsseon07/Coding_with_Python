import heapq, sys

heap = []

N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if not heap:
            print(0)
        else:
            print(heap[0])
            heapq.heappop(heap)

    else:
        heapq.heappush(heap, x)