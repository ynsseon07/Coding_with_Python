# def solution(phone_book):
    
#     # 전화번호 담긴 리스트 차례로 탐색
#     for i in range(len(phone_book)):
#         for j in range(len(phone_book)):
#             flag = True
#             if i != j: 
#                 min_len = min(len(phone_book[i]), len(phone_book[j]))
#                 for k in range(min_len):
#                     if phone_book[i][k] != phone_book[j][k]:
#                         flag = False
#                         break
#                 if flag:
#                     return False
    
#     return True


# 해시 사용

def solution(phone_book):
    
    # phone_book 리스트의 원소를 해시에 저장
    phone_number = dict()
    for elem in phone_book:
        phone_number[elem] = 1
        
    # 해시에 저장된 원소 탐색
    for number in phone_number:
        tmp = ""
        
        # 각 전화번호의 앞부분부터 탐색
        for n in number:
            tmp += n
            
            if (tmp in phone_number) and (tmp != number):
                return False
    
    return True

solution(["119", "97674223", "1195524421"])