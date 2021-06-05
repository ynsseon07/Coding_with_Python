# 가장 기본 sort -> 오름차순 정렬
x = [1,7,8,9,3,12,4]
x.sort()
print(x)

# 내림차순 정렬
x.sort(reverse=True)
print(x)

# sorted함수는 결과값을 받아줄 변수가 필요
y = sorted(x)
print(y)

# 중첩리스트에서 특정 인자를 기준으로 정렬하는 방법
# 안쪽 리스트의 두번째 인자 오름차순 정렬
tickets=[['a','b'],['b','a'],['c','d'],['d','c']]

tickets = sorted(tickets, key = lambda x: x[1])
print(tickets)