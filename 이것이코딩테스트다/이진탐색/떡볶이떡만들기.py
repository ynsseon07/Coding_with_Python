n, m = map(int, input().split())
dduk = list(map(int, input().split()))

dduk.sort()

start = 0
end = len(dduk) - 1

while start <= end:
    get = 0
    mid = (start + end) // 2
    for i in dduk:
        