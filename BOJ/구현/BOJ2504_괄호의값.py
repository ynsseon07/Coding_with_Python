data = input()
stack = []
temp = 0
flag = True

for i in data:
    if i == '(' or i == '[':
        stack.append(i)
    
    if i == ')':
        while stack:
            if stack[-1] == '(':
                stack.pop()
                temp = (1 if temp == 0 else temp)
                stack.append(2 * temp)
                temp = 0
                break
            elif stack[-1] == '[':
                flag = False
                break
            else:
                temp += stack.pop()

    if i == ']':
        while stack:
            if stack[-1] == '[':
                stack.pop()
                temp = (1 if temp == 0 else temp)
                stack.append(3 * temp)
                temp = 0
                break
            elif stack[-1] == '(':
                flag = False
                break
            else:
                temp += stack.pop()

if flag:
    for st in stack:
        if type(st) == str:
            print(0)
            exit()
    print(sum(stack))
else:
    print(0)


##########################################################################
#
#   for문으로 주어진 문자열 한개씩 탐색
#   if '(' or '['이면 스택에 push
#   if ')'이면 스택의 top 확인
#       1. top이 숫자이면 pop해서 temp에 더하기
#       2. top이 '(' 이면 pop해서 `2 * 현재까지 temp에 저장 된 값` 을 push
#                   ( 이때 top = 0일 경우 1로 변경해서 곱셈해준다 )
#       3. top이 '[' 이면 올바르지 않은 괄호열 (flag = False 설정)
#   if ']'이면 위와 마찬가지로 스택의 top 확인
#   
#   flag = False일 경우는 올바르지 않은 괄호열이므로 0 출력
#   flag = True일 경우는 올바른 괄호열
#   이때 스택에 '(' 나 '['가 남아있는 경우가 존재할 수도 있음 (EX: (()()[] )
#   해당 경우도 올바르지 않은 괄호열이므로 0 출력해야함
#
##########################################################################