def solution(citations):
    answer = 0
    for h in range(max(citations) + 1):
        cnt = 0
        for c in citations:
            if c >= h:
                cnt += 1
        if cnt < h:
            break
    
    if h == 0:
        answer = h
    else:
        answer = h - 1     
    return answer