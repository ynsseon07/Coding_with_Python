n = int(input())

ans = 0
for num in range(1, n):
    ans = num
    hap = num
    for i in str(num):
        hap += int(i)
    
    if hap == n:
        break

if ans == n-1:
    print(0)
else:
    print(ans)
