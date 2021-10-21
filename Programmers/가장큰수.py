from functools import cmp_to_key

def compare(a,b):
    if a+b > b+a:
        return 1
    elif a+b < b+a:
        return -1
    else:
        return 0

def solution(numbers):
    num_list = [str(x) for x in numbers]
    num_list = sorted(num_list, key=cmp_to_key(compare), reverse=True)
    answer = str(int(''.join(num_list)))
    return answer

solution([6,10,2])