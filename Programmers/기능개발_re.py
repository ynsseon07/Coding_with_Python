def solution(progresses, speeds):
    answer = []
    take_days = []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] != 0:
            take_days.append((100 - progresses[i]) // speeds[i] + 1)
        else:
            take_days.append((100 - progresses[i]) // speeds[i])
    
    out = 1
    tmp = take_days[0]
    for i in range(1, len(take_days)):
        if tmp >= take_days[i]:
            out += 1
        else:
            answer.append(out)
            tmp = take_days[i]
            out = 1
    answer.append(out)
    return answer