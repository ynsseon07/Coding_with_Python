# 가장 기본 sort -> 오름차순 정렬
x = [1,7,8,9,3,12,4]
x.sort()
print('1', x)

# 내림차순 정렬
x.sort(reverse=True)
print('2', x)

# sorted함수는 결과값을 받아줄 변수가 필요
y = sorted(x)
print('3', y)

# sorted 함수 이용한 내림차순 정렬
z = sorted(x, reverse=True)
print('4', z)

# 중첩리스트에서 특정 인자를 기준으로 정렬하는 방법
# 안쪽 리스트의 두번째 인자 오름차순 정렬
tickets=[['a','b'],['b','a'],['c','d'],['d','c']]

tickets = sorted(tickets, key = lambda x: x[1])
print(tickets)

# 정렬 기준으로 다중 조건 넘겨줄 수 있음
# 두번째 인자 기준으로 오름차순 정렬 먼저 한다
# 그 결과를 가지고 첫번째 인자 기준으로 내림차순 정렬
# -를 붙이면 내림차순 정렬 된다
data = [[1,5], [2,3], [3,-1], [2,1], [1,3], [4,5]]
data = sorted(data, key=lambda x: (x[1], -x[0]))
print(data)

# .sort()       vs      sorted()
data = [1,5,6,7,4,3,7,9,2,3]
print('data.sort(reverse=True) = ', data.sort(reverse=True))
print('sorted(data, reverse=True) = ', sorted(data, reverse=True))