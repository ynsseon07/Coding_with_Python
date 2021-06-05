from collections import deque

def compare(w1, w2):
    cnt = 0
    for i, j in zip(w1, w2):
        if i != j:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False
    
    
def bfs(begin, target, words, check):
    # words 안에 target이 없는 경우
    if target not in words:
        return 0
    
    # words 안에 target이 있는 경우 bfs 수행
    queue = deque()
    queue.append(begin)
    
    while queue:
        val = queue.popleft()
        if val == target:
            return check[words.index(val)][1]
        
        for i,v in enumerate(words):
            if compare(val, v) and not check[i][0]:
                if val == begin:
                    check[i][0] = True
                    check[i][1] += 1
                else:
                    check[i][0] = True
                    check[i][1] = check[words.index(val)][1] + 1
                queue.append(v)

                
def solution(begin, target, words):
    answer = 0
    check = []
    for i in range(len(words)):
        check.append([False, 0])
    answer = bfs(begin, target, words, check)
    return answer


# words 리스트 길이만큼 check 리스트 생성
# 이중 리스트로 선언 -> [방문여부(True, False), 길이] 저장
