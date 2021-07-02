testcase = int(input())

while testcase > 0:
    N, x = map(int, input().split())
    priorities = list(map(int, input().split()))
    items = priorities.copy()
    idx = [i for i in range(N)]

    if N != 1:
        i = 0
        while True:
            if items[i] < max(items[i+1:]):
                items.append(items.pop(i))
                idx.append(idx.pop(i))
            else:
                i += 1

            # priorities.sort()가 아닌 sorted(priorities)이어야함
            # 리턴값이 있어야하므로
            if items == sorted(priorities, reverse=True):
                break
        
        print(idx.index(x) + 1)
    else:
        print(1)
    testcase -= 1