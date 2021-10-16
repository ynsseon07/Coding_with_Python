def make_arr(k, n):
    if k == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(i+1)
            make_arr(k+1, n)
            visited[i] = False
            arr.pop()

n, m = map(int, input().split())
visited = [False for _ in range(n)]
arr = []

make_arr(0, n)