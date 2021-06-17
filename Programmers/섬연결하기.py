def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x: x[2])   # 비용 오름차순 정렬
    conn = set()                                # 통행가능한 섬 번호를 담을 set
    conn.add(0)
    
    while len(conn) != n:       # conn에 담긴 원소 갯수가 섬 갯수와 같으면 while문 종료
        for start, end, cost in costs:
            # 출발하는 섬 번호 또는 도착하는 섬 번호가 conn에 담겨있을 경우
            if start in conn or end in conn:
                # 출발하는 섬 번호, 도착하는 섬 번호가 모두 conn에 담겨있는 경우는 이미 통행했다는 의미
                if start in conn and end in conn:
                    continue
                    # start, end 둘 중 하나만 conn에 속한 경우는 섬끼리 연결 가능함을 의미
                conn.add(start)
                conn.add(end)
                answer += cost
                break
    
    return answer