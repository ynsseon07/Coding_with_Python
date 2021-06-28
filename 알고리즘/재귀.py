def recursive_function(i):
    if i == 100:
        return
    
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다')


recursive_function(1)

# 파이썬으로 재귀문제 풀기 위해서는 아래 코드가 꼭 필요
# 재귀를 제한하는 코드
import sys
sys.setrecursionlimit(100000)