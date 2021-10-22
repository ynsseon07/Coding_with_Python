def solution(n, lost, reserve):
    answer = 0

    # 각 학생이 가지고 있는 체육복 갯수 저장
    student = [1] * n
    for l in lost:
        student[l-1] -= 1
    for r in reserve:
        student[r-1] += 1
        
    for i in range(n):
        if student[i] == 0:
            if i == 0:
                if student[i+1] == 2:
                    student[i+1] -= 1
                    student[i] += 1
            elif i == n-1:
                if student[i-1] == 2:
                    student[i-1] -= 1
                    student[i] += 1
            else:
                if student[i-1] == 2:
                    student[i-1] -= 1
                    student[i] += 1
                elif student[i+1] == 2:
                    student[i+1] -= 1
                    student[i] += 1
    
    for s in student:
        if s > 0:
            answer += 1
    
    return answer