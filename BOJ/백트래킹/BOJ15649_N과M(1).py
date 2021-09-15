n, m = map(int, input().split())
visited = [False for _ in range(n)]
arr = []

def make_arr(k, n):
    if k == m:
        pass

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(i+1)
            make_arr(k+1, n)
            visited[i] = False
            print(arr.pop())

make_arr(0, n)