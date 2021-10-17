import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
calc = list(map(int, sys.stdin.readline().split()))

yeonsanja = [0] * (N-1)

max_val = -10**9
min_val = 10**9

def make_math(cnt):
    if cnt == N-1:
        res = nums[0]
        for i in range(len(yeonsanja)):
            if yeonsanja[i] == '+':
                res += nums[i+1]
            elif yeonsanja[i] == '-':
                res -= nums[i+1]
            elif yeonsanja[i] == '*':
                res *= nums[i+1]
            else:
                if res < 0:
                    res = -(abs(res) // nums[i+1])
                else:
                    res //= nums[i+1]

        global max_val, min_val
        max_val = max(max_val, res)
        min_val = min(min_val, res)
        return

    for i in range(len(calc)):
        if calc[i] > 0:
            calc[i] -= 1
            if i == 0:
                yeonsanja[cnt] = '+'
            elif i == 1:
                yeonsanja[cnt] = '-'
            elif i == 2:
                yeonsanja[cnt] = '*'
            else:
                yeonsanja[cnt] = '/'
            
            make_math(cnt+1)
            calc[i] += 1

make_math(0)
print(max_val)
print(min_val)