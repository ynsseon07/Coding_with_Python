answer = 0
n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort(reverse=True)
first_larg = num[0]
second_larg = num[1]

m_cnt = 0
while m_cnt <= m:
    for i in range(k):
        if m_cnt == m:
            break
        answer += first_larg
        m_cnt += 1
        
    if m_cnt == m:
        break
    answer += second_larg
    m_cnt += 1

print(answer)