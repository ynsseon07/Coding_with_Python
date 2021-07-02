data = input().split('-')

temp = []

for elem in data:
    data2 = elem.split('+')
    cnt = 0
    for d in data2:
        cnt += int(d)
    temp.append(cnt)

result = temp[0]
for i in range(1, len(temp)):
    result -= temp[i]

print(result)

#######################################
# 가장 먼저 -를 구분자로 문자열을 입력받고
# 이후 +를 구분자로 문자열을 나눠 더해준다
# data 리스트 안의 첫번째 원소만 더한 후
# 나머지는 빼준다
# eval로 문자열을 계산할 경우 
# 0으로 시작하는 수는 계산 불가하므로
# 런타임 에러 남
#######################################