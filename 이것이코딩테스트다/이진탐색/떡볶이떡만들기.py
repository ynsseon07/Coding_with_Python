n, m = map(int, input().split())
dduk = list(map(int, input().split()))

dduk.sort()

start = 0
end = max(dduk)

result = 0
while start <= end:
    get = 0
    mid = (start + end) // 2
    for x in dduk:
        if x > mid:
            get += (x - mid)
        
    if get < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)