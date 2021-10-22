# 큐 사용(deque)

from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리에 올라갈 수 있는 트럭 수 만큼 0으로 채운 배열 생성
    queue = deque([0] * bridge_length)
    # 시간 체크 변수
    count = 0
    # 현재 다리 위 트럭들의 무게
    bridge_weight = 0
    
    while queue:
        count += 1
        bridge_weight -= queue.popleft()
            
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                queue.append(truck_weights[0])
                bridge_weight += truck_weights[0]
                truck_weights.pop(0)
            else:
                queue.append(0)
                           
    return count