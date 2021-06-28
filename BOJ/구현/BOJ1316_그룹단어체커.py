n = int(input())
result = 0
while n > 0:
    flag = False
    string = input()
    for idx in range(len(string)):
        temp_idx = string.find(string[idx], idx + 1)
        if temp_idx != -1:
            if temp_idx - idx == 1:
                continue
            flag = True
            break
        #try:
        #    temp_idx = string.index(string[idx], idx + 1)
        #    if temp_idx - idx == 1:
        #        continue
        #    flag = True
        #    break
        #except ValueError:      # 해당 단어가 문자열 안에 존재하지 않음을 의미
        #    pass

    if not flag:
        result += 1
    n -= 1

print(result)