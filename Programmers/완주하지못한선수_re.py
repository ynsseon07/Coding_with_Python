def solution(participant, completion):
    answer = ''
    save_hash = dict()
    
    for p in participant:
        if p in save_hash:
            save_hash[p] += 1
        else:
            save_hash[p] = 1
            
    for c in completion:
        save_hash[c] -= 1
        
    for elem in save_hash:
        if save_hash[elem] != 0:
            answer += elem
            break
    
    return answer