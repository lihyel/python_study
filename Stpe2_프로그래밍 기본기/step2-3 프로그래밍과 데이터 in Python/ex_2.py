# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
# 코드를 입력하세요
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)

# numbers에서 홀수 제거
# 코드를 입력하세요
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        del(numbers[i]) 
				# 여기서 i += 1 을 하면 (X) 
				# if 조건문을 만족시킨 경우(홀수인 요소를 제거)에 i + 1을하면, 요소 하나를 검토하지 않고 건너뛰게 되는 것! 
    else: i += 1
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
# 코드를 입력하세요
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
# 코드를 입력하세요
numbers.sort()
print(numbers)