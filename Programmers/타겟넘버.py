answer = 0

def func(numbers, target, cnt, result):
    if cnt == len(numbers):
        if result == target:
            global answer
            answer += 1
        return
    
    func(numbers, target, cnt+1, result + numbers[cnt])
    func(numbers, target, cnt+1, result - numbers[cnt])

    
def solution(numbers, target):
    func(numbers, target, 0, 0)
    global answer
    return answer