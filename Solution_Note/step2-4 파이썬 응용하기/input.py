import random

# 정답 변수 : correct
correct = random.randint(1,20)
# 기회 변수 : cnt
cnt = 4

while cnt > 0: 
    # 사용자 입력값 변수 : number
    # 한번 입력 받을 때마다 출력해야할 내용
    number = int(input(f'기회가 {cnt}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요.'))
    
    if number == correct:
        print(f'축하합니다. {5-cnt}번 만에 숫자를 맞히셨습니다.')
        break

    # 1과 20 사이의 정수가 아닌 수를 입력할 경우에 출력할 코멘트도 작성
    elif number < correct and 1 <= number <= 20:
        print('Up')
        cnt -= 1
    elif number > correct and 1 <= number <= 20:
        print('Down')
        cnt -= 1
    else:
        print('올바르지 않은 값입니다.1-20 사이의 정수를 입력하세요.')

    # 기회를 모두 썼을 때 
    if cnt == 0:
        print(f'아쉽군요. 정답은 {correct}입니다. 다시 도전하세요.')