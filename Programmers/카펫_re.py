# 1
def solution(brown, yellow):
    answer = []
    
    y_garo = yellow
    while True:
        if yellow % y_garo == 0:
            y_sero = yellow // y_garo
            
            if y_garo * 2 + y_sero * 2 + 4 == brown:
                answer.append(y_garo + 2)
                answer.append(y_sero + 2)
                break
            else:
                y_garo -= 1
        else:
            y_garo -= 1
    
    return answer


# 2
def solution(brown, yellow):
    answer = []
    for i in range(yellow, 0, -1):
        if yellow % i == 0:
            garo = i
            sero = yellow // i

            if garo * 2 + sero * 2 + 4 == brown:
                answer.append(garo + 2)
                answer.append(sero + 2)
                break

    return answer