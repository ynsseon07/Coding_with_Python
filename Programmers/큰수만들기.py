def solution(number, k):
    answer = ''
    st = []
    for i in range(len(number)):
        # st의 맨 끝에 들어있는 원소보다 더 큰 값이 들어온다면
        while st and k > 0 and st[-1] < number[i]:
            st.pop()
            # 전체 numbers에서 k개의 수를 제거하는 것이기 때문에 k를 1씩 감소
            k -= 1
        st.append(number[i])
        
    answer = ''.join(st[:len(st)-k])
    return answer

solution("1924", 2)

# st = []           -> while문 들어가지 못함 / number[i] 리스트에 추가 / k = 2
# st = ['1']        -> while문 들어감 / 9가 1보다 더 크므로 pop함 / k = 1
# st = ['9']        -> while문 들어가지 못함 / number[i] 리스트에 추가
# st = ['9', '2']   -> while문 들어감 / 4가 2보다 더 크므로 pop함 / k = 0
# st = ['9', '4']

solution("4177252841", 4)

# st = []
# st = ['4']
# st = ['4', '1']   -> while문 들어감 / 7이 1, 4보다 더 크므로 pop함 / k = 2
# st = ['7']
# st = ['7', '7', '2']  -> while문 들어감 / 5가 2보다 더 크므로 pop함 / k = 1
# st = ['7', '7', '5']
# st = ['7', '7', '5', '2'] -> while문 들어감 / 8이 2보다 더 크므로 pop함 / k = 0
#                           -> k == 0이기 때문에 while문 빠져나옴 / 8 리스트에 추가
# 이후에는 계속 while문 들어가지 못하고 원소만 리스트에 추가
# st = ['7', '7', '5', '8', '4', '1']


# def solution(number, k):
#     answer = ''
#     l = len(number) - k
#     start = 0
#     for i in range(l):
#         maxNum = number[start]
#         maxIdx = start
#         for j in range(start, k + i + 1):
#             if number[j] > maxNum:
#                 maxNum = number[j]
#                 maxIdx = j
#         answer += maxNum
#         start = maxIdx + 1

#     return answer

# solution("1231234", 3)
