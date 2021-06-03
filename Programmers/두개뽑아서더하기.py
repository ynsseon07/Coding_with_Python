def solution(numbers):
    answer = []
    temp = set()
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            temp.add(numbers[i] + numbers[j])
    
    for data in temp:
        answer.append(data)
    
    answer.sort()
        
    return answer