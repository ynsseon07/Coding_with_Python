def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer.append(cnt)
        
    return answer

# enumerate 사용해서 인덱스 알아내는 것보다
# range(len(리스트)) 통해 인덱스 사용하는 게 시간 더 빠름
# enumerate(prices) 사용했을 때 시간 초과 발생했었음