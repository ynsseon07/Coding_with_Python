import sys
S = sys.stdin.readline().strip()

ans = ''
flag = False
stack = []
for i in range(len(S)):
    if S[i] == '<':
        while stack:
            ans += stack.pop()

        ans += S[i]
        flag = True

    elif S[i] == '>':
        ans += S[i]
        flag = False

    else:
        if flag:
            ans += S[i]
        else:
            if S[i] == ' ':
                while stack:
                    ans += stack.pop()
                ans += S[i]
            else:
                stack.append(S[i])

while stack:
    ans += stack.pop()
        
print(ans)