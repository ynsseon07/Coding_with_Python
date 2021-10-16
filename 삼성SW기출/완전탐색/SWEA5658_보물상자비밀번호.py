import copy

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    string = input()

    # 길이 N의 문자열 copy본 만들기
    string_cpy = string
    
    # 중복제거를 위한 set 자료형
    s = set()

    while True:
        idx = 0
        pair = N // 4
        while idx < len(string_cpy):
            # string_cpy를 4등분 -> 십진수로 변환 -> set에 저장
            s.add(int(string_cpy[idx:idx+pair], 16))
            idx += pair

        # string_cpy를 리스트로 변환 -> 인덱스 조정해서 1회전한 형태로 변경
        # 원본 리스트 & 변경될 리스트 2개 필요
        s_to_list = list(string_cpy)
        s_to_list_cpy = copy.deepcopy(s_to_list)
        
        for idx in range(len(s_to_list_cpy)):
            # 마지막 인덱스면 첫번째로
            if idx == len(s_to_list_cpy) - 1:
                s_to_list_cpy[0] = s_to_list[idx]
                continue

            s_to_list_cpy[idx+1] = s_to_list[idx]
        
        # 변경된 s_to_list_cpy를 string_cpy에 대입
        string_cpy = ''.join(s_to_list_cpy)

        # while문 종료
        if string_cpy == string:
            break

    data_list = list(s)
    data_list = sorted(data_list, reverse=True)

    # K번째로 큰 수 출력
    print('#{0} {1}'.format(test_case, data_list[K-1]))
