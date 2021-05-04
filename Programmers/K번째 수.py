# 정렬

def solution(array, commands):
    answer = []
    for command in commands:
        n_array = array[command[0]-1: command[1]]
        n_array.sort()
        answer.append(n_array[command[2]-1])
    return answer

# 리스트 슬라이싱
