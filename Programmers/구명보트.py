def solution(people, limit):
    answer = 0
    people = sorted(people)
    heavyIdx = len(people) - 1
    lightIdx = 0
    
    while lightIdx <= heavyIdx:
        answer += 1
        
        if lightIdx == heavyIdx:
            break
        
        if people[lightIdx] + people[heavyIdx] > limit:
            heavyIdx -= 1
        else:
            heavyIdx -= 1
            lightIdx += 1
            
    return answer