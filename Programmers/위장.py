def solution(clothes):
    answer = 1
    
    hash_map = dict()
    for elem in clothes:
        if elem[1] in hash_map:
            hash_map[elem[1]] += 1
        else:
            hash_map[elem[1]] = 1        

    tmp = []
    for val in hash_map.values():
        tmp.append(val+1)
    
    for t in tmp:
        answer *= t
            
    return answer-1