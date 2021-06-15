from itertools import permutations
import math

def isSosu(x):
    if x < 2: return False
    if x == 2: return True
    for i in range(2, math.floor(math.sqrt(x)+1)):      # range 안에는 int 형태만 존재할 수 있음 (주의)
        if x % i == 0: return False
    return True

def solution(numbers):
    answer = 0
    numList = []        # 문자열 numbers를 numList로 변환
    for n in numbers:
        numList.append(n)
        
    getNum = set()
    i = 1
    while i <= len(numbers):
        # permutations 통해 얻어낸 결과값은 tuple 형태 -> join함수 통해 tuple 원소들을 string 형태로 바꿔줌
        temp = list(map(''.join, permutations(numList, i)))
        
        # temp 리스트 안의 string 원소들을 int 형태로 변환하여 getNum에 저장
        # getNum은 set 컨테이너이므로, 중복값은 제외하고 저장
        for t in temp:
            getNum.add(int(t))

        i += 1
    
    for elem in getNum:
        if isSosu(elem): answer += 1
            
    return answer