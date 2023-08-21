def mask_security_number(security_number):
    # 여기에 코드를 작성하세요
    public_number = [] 
    for i in security_number[0:-4]:
        public_number.append(i)
    for i in security_number[-4:]:
        public_number.append('*')
    #print(public_number)
    str_number = ''.join(str(s) for s in public_number)
    return str_number
    
    
# 테스트 코드
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))