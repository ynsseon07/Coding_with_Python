import sys
s = sys.stdin.readline().strip()

stack = []
res = 0

for elem in s:
    temp = 0

    if elem == ')':
        if len(stack) == 0:
            print(0)
            exit()

        while stack:
            top = stack.pop()
            if top == '(':
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(temp*2)
                break
            elif top == '[':
                print(0)
                exit()
            else:
                temp += int(top)

    elif elem == ']':
        if len(stack) == 0:
            print(0)
            exit()

        while stack:
            top = stack.pop()
            if top == '[':
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(temp*3)
                break
            elif top == '(':
                print(0)
                exit()
            else:
                temp += int(top)

    else:
        stack.append(elem)

for s in stack:
    if s == '(' or s == '[':
        print(0)
        exit()
    else:
        res += s
print(res)