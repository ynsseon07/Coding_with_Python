N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

# 기본 sort(), sorted() 정렬은 첫 번째 요소가 같으면 두번째 요소로 비교함
# key인자에 lambda 함수를 넘겨주면 반환값 가지고 비교해서 정렬
# 이때, key로 전달되지 않은 요소에 대해선 정렬하지 않음

# 정렬 기준으로 다중 조건 넘겨줄 수 있음
# 두번째 인자 기준으로 오름차순 정렬 먼저 한다
# 그 결과를 가지고 첫번째 인자 기준으로 오름차순 정렬
# -를 붙이면 내림차순 정렬 된다
data = sorted(data, key=lambda x: (x[1], x[0]))

for elem in data:
    for e in elem:
        print(e, end=' ')
    print()