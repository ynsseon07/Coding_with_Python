import sys

str_list = sys.stdin.readline().strip().split('-')

res = []

# str_list 원소 하나씩 계산 => 최종적으로 계산된 결과를 빼줘야함
for str in str_list:
    temp = 0
    temp_list = str.split('+')

    temp = sum([int(e) for e in temp_list])
    res.append(temp)

answer = res[0]
for i in range(1, len(res)):
    answer -= res[i]

print(answer)