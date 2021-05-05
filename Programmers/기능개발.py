def solution(progresses, speeds):
    answer = []
    time = 0
    cnt = 0
    while len(progresses) > 0:
        if progresses[0] + time * speeds[0] >= 100:  # 기능의 진도가 100% 이상일때
            progresses.pop(0)                        # 해당 기능 & 속도 pop
            speeds.pop(0)
            cnt += 1
        else:                                        # 기능의 진도가 100%가 안될때
            if cnt > 0:                              # cnt가 0보다 크면, 이미 배포된 기능이 존재함을 의미
                answer.append(cnt)                   # 한 번에 몇개의 기능이 배포됐는지(cnt) answer에 추가
                cnt = 0
            time += 1                                # 기능의 진도가 100% 이상이 아니라면 time은 1씩 계속 증가
    
    answer.append(cnt)                               # 마지막 기능까지 센 cnt도 answer에 추가
    
    return answer