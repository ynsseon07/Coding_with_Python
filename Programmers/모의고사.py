def solution(answers):
    answer = []
    st1 = [1, 2, 3, 4, 5]
    st2 = [2, 1, 2, 3, 2, 4, 2, 5]
    st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # answers 길이만큼 각 학생의 답안 리스트 늘리기
    while (len(st1) < len(answers)):
        st1 *= 2
    while (len(st2) < len(answers)):
        st2 *= 2
    while (len(st3) < len(answers)):
        st3 *= 2

    right1 = 0
    right2 = 0
    right3 = 0
    for i in range(len(answers)):
        if (answers[i] == st1[i]):
            right1 += 1
        if (answers[i] == st2[i]):
            right2 += 1
        if (answers[i] == st3[i]):
            right3 += 1

    if (right1 >= right2 and right1 >= right3):
        answer.append(1)
    if (right2 >= right3 and right2 >= right1):
        answer.append(2)
    if (right3 >= right1 and right3 >= right2):
        answer.append(3)

    return answer
