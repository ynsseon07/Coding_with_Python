def solution(brown, yellow):
    answer = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            sero = i
            garo = yellow // i
            
            temp = garo * 2 + sero * 2 + 4
            if temp == brown:
                answer.append(garo + 2)
                answer.append(sero + 2)
                break
                
    return answer

# 약수관계를 이용해서 구현