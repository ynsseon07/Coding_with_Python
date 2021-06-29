alphabet = input()
result = 0
check = [False] * len(alphabet)

for i in range(len(alphabet)):
    if alphabet[i] == '=' and not check[i]:
        if (i != 0) and (alphabet[i-1] == 'c' or alphabet[i-1] == 's' or alphabet[i-1] == 'z') and not check[i-1]:
            if alphabet[i-1] == 'z':        # 'dz==' 또는 'z=='인 경우
                if (i-1) != 0 and alphabet[i-2] == 'd' and not check[i-2]:  # 'dz=' 일 경우
                    check[i-2] = True
                    check[i-1] = True
                    check[i] = True
                    result += 1
                else:                                                       # 'z=' 일 경우
                    check[i-1] = True
                    check[i] = True
                    result += 1
            else:                           # 'c=' 또는 's='인 경우
                check[i-1] = True
                check[i] = True
                result += 1

    if alphabet[i] == 'j' and not check[i]:
        if (i != 0) and (alphabet[i-1] == 'l' or alphabet[i-1] == 'n') and not check[i-1]:
            check[i-1] = True
            check[i] = True
            result += 1

    if alphabet[i] == '-' and not check[i]:
        if (i != 0) and (alphabet[i-1] == 'c' or alphabet[i-1] == 'd') and not check[i-1]:
            check[i-1] = True
            check[i] = True
            result += 1

for i in range(len(check)):
    if check[i] == False:
        result += 1

print(result)