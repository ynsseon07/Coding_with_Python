def solution(bridge_length, weight, truck_weights):
    on_bridge = [0] * bridge_length     # 다리 길이만큼 0으로 채워놓음
    bridge_weight = 0                   # 다리 위에 있는 트럭 무게의 합
    time = 0    
    
    while on_bridge:
        time += 1
        bridge_weight -= on_bridge.pop(0)

        if truck_weights:               # truck_weights 배열 안에 값이 존재한다면
            if bridge_weight + truck_weights[0] > weight:
                on_bridge.append(0)
            else:
                truck = truck_weights.pop(0)
                on_bridge.append(truck)
                bridge_weight += truck

    return time