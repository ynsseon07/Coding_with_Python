# 파이썬에서 Stack 자료구조는 List 자료구조로 구현 가능
# stack은 append와 pop 기억

stack = []
stack.append(4)     # push(4)
stack.append(5)     # push(5)
stack.append(3)
stack.append(9)

#top = stack.pop()   # top = 5

#top = stack.pop()   # top = 4

top = stack[-1]     # 원소를 pop하지 않고 값만 참조
print('top:', top)
print('stack[::1]:', stack[::-1])   # 최상단 원소부터 출력
print('stack:', stack)        # 최하단 원소부터 출력
