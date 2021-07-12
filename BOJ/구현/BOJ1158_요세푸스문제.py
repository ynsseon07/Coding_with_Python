N, K = map(int, input().split())

data = [i for i in range(N)]    # 사람 리스트 (초기)

ans = []    # 제거될 사람 담을 배열
idx = 0     # 제거될 사람 인덱스

for _ in range(N):
    idx += K - 1
    if idx >= len(data):     # idx >= N 안되는 이유 : data에서 원소를 pop 시켜서 idx의 최댓값은 계속 변하기 때문 (pop index out of range 에러 발생)
        idx = idx % len(data)
    
    ans.append(str(data.pop(idx) + 1))

print('<%s>' % (', '.join(ans)))

# 리스트를 계속 돌아야할 경우는 나머지 연산 사용하기★★★