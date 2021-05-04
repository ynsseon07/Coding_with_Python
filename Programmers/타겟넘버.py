answer = 0

def func(i, numbers, target, result):
    if i == len(numbers):
        if result == target:
            global answer
            answer += 1
        return

    func(i+1, numbers, target, result+numbers[i])
    func(i+1, numbers, target, result-numbers[i])

def solution(numbers, target):
    global answer
    func(0, numbers, target, 0)
    return answer
