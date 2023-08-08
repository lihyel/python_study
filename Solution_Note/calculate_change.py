def calculate_change(payment, cost):
    # 여기에 코드를 작성하세요
    change = payment - cost #거스름돈 총액
    
    fifty_thousand = change // 50000   # 50,000원 지폐
    ten_thousand = (change % 50000) // 10000   # 10,000원지폐
    five_thousand = (change % 10000) // 5000   # 5,000원 지폐
    one_thousand = (change % 5000) // 1000   # 1,000원 지폐 

    print("50000원 지폐: {}장".format(fifty_thousand))
    print("10000원 지폐: {}장".format(ten_thousand))
    print("5000원 지폐: {}장".format(five_thousand))
    print("1000원 지폐: {}장".format(one_thousand))
    
# 테스트 코드
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)