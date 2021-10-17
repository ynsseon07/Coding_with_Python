import sys

L, C = map(int, sys.stdin.readline().split())
alphas = list(sys.stdin.readline().split())
visited = [False] * C
code_arr = []
answer = []

def make_code(cnt, start):
    if cnt == L:
        m_count = 0
        j_count = 0

        for ca in code_arr:
            if ca == 'a' or ca == 'e' or ca == 'i' or ca == 'o' or ca == 'u':
                m_count += 1
            else:
                j_count += 1
        
        if m_count >= 1 and j_count >= 2:
            code_arr_new = sorted(code_arr)
            answer.append(tuple(code_arr_new))

        return

    for i in range(start, C):
        if not visited[i]:
            visited[i] = True
            code_arr.append(alphas[i])
            make_code(cnt+1, i+1)
            visited[i] = False
            code_arr.pop()

make_code(0, 0)

answer = sorted(answer)

for elem in answer:
    print(''.join(elem))