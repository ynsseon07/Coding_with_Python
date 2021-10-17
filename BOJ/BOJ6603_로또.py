import sys
# 방법 1 -> 라이브러리 사용
# from itertools import combinations

# while True:
#     k, *rest = map(int, sys.stdin.readline().split())
#     if k == 0:
#         break
    
#     ans = list(combinations(rest, 6))

#     for a in ans:
#         print(' '.join(str(e) for e in a))
#     print()

# 방법 2 -> 백트래킹 직접 구현
def make_num(cnt, idx, k, arr, visited, rest):
    if cnt == 6:
        for i in range(6):
            print(arr[i], end=' ')
        print()
        return
    
    for i in range(idx, k):
        if not visited[i]:
            visited[i] = True
            arr.append(rest[i])
            make_num(cnt+1, i+1, k, arr, visited, rest)
            visited[i] = False
            arr.pop()

while True:
    k, *rest = map(int, sys.stdin.readline().split())
    if k == 0:
        break

    arr = []
    visited = [False] * k
    
    make_num(0, 0, k, arr, visited, rest)
    print()