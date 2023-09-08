# 상수 정의
INTEREST_RATE = 0.12  # 이자율 12% 고정
APARTMENT_PRICE_2016 = 1100000000  # 은마아파트 가격 11억원으로 고정 

# 변수 정의
  # 반복문을 돌기 위해 사용되는 변수들 ... 
year = 1988  # 연도를 나타내는 변수 필요 : 1988년부터 2016년까지 반복을 해야하므로
bank_balance = 50000000  # 은행 잔액을 나타내는 변수 필요 : 은행에 돈을 넣은 경우 매년 그 금액이 바뀔 것 (이자가 붙기 때문)

# 반복문 
# point !! 몇년을 반복할 것인가? 
# 2016년은 아직 오지 않았다 -> 포함되지 않는다!
while year < 2016:
    bank_balance = bank_balance * (1 + INTEREST_RATE) # 반복문의 핵심 코드..  1988년부터 2016년까지 돈이 얼마나 쌓이는지 계산 -> while 반복문의 수행 부분에 들어갈 때마다 'bank_balance'가 12%씩 늘어나도록!
    year += 1

# if, else 문
# 동일, 미란 비교 
if bank_balance > APARTMENT_PRICE_2016:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(bank_balance - APARTMENT_PRICE_2016)))
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(APARTMENT_PRICE_2016 - bank_balance)))