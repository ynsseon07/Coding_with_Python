numbers = [False] * 10001

for i in range(1, 10001):
    temp_i = str(i)
    temp_list = list(temp_i)
    result = i
    for t in temp_list:
        result += int(t)
    if result <= 10000:
        numbers[result] = True

for i in range(1, 10001):
    if not numbers[i]:
        print(i)