def solution(participant, completion):
    answer = ''
    temp = {}
    for p in participant:
        if p in temp:
            temp[p] += 1
        else: temp[p] = 1
    
    for c in completion:
        temp[c] -= 1
        
    for elem in temp:
        if temp[elem] == 1:
            answer = elem
            break
            
    return answer

# dictionary 사용 (해시함수)
# 원소 in 컨테이너 => dictionary에서는 key가 원소에 해당
# => 해당 key값이 딕셔너리 안에 존재하는지 여부 확인
