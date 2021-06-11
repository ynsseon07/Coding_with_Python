def solution(priorities, location):
    answer = 0
    
    # 인덱스와 중요도를 저장한 리스트 각각 선언
    idx = [i for i in range(len(priorities))]
    val = priorities.copy()
    
    i = 0
    while True:
        if val[i] < max(val[i+1:]):     # i에 위치한 중요도가 리스트 내의 중요도보다 작은 상황이 존재한다면
            val.append(val.pop(i))      # 해당 값을 대기 목록 맨뒤로 보냄
            idx.append(idx.pop(i))      # 인덱스도 마찬가지로 맨뒤로 보냄
        else:
            i += 1                      # pop하지 않는다는 점이 중요
            
        if val == sorted(priorities, reverse=True):     # 중요도가 정렬된 상태가 기존 priorities 리스트의 내림차순과 같다면
            break
    
    answer = idx.index(location) + 1                    # 현재 인덱스 리스트 상태에서 location에 해당하는 위치를 찾아내기
                                                        # 인덱스 리스트는 초기 상태를 기준으로 순서가 바뀜
    return answer