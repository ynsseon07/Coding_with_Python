def solution(n, lost, reserve):
    answer = 0

    # 모든 학생이 체육복 하나씩 갖고 있는 상태의 리스트
    clothes = [1 for i in range(n)]
    for i in lost:
        clothes[i-1] -= 1

    for i in reserve:
        clothes[i-1] += 1

    # 첫번째 학생이 체육복이 0개라면
    if clothes[0] == 0:
        if clothes[1] == 2:
            clothes[0] += 1
            clothes[1] -= 1

    for i in range(1, n-1):
        if clothes[i] == 0:
            if clothes[i-1] == 2:
                clothes[i] += 1
                clothes[i-1] -= 1
            elif clothes[i+1] == 2:
                clothes[i] += 1
                clothes[i+1] -= 1

    # 마지막 학생이 체육복이 0개라면
    if clothes[n-1] == 0:
        if clothes[n-2] == 2:
            clothes[n-1] += 1
            clothes[n-2] -= 1

    for i in clothes:
        if i >= 1:
            answer += 1

    return answer
