def mask_security_number(security_number):
    num_list = list(security_number)

    # 마지막 네 값을 *로 대체
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = '*'

    # 리스트를 문자열로 복구하여 반환
    return ''.join(num_list) #간단하게!
    
    
# 테스트 코드
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))