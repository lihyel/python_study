import random

# 1. 사전 만들기
## !!사전(딕셔너리)을 새롭게 만든다.
vocab = {}
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        vocab[english_word] = korean_word

# 목록 가져오기
# !! 영어 단어 목록을 받아오려면 파이썬 사전의 'keys'를 사용하면 된다. 
keys = list(vocab.keys())


# 2. 문제 내기
while True:
    # 랜덤한 문제 받아 오기
    # random 모듈의 randint() 함수를 이용해서 랜덤한 인덱스를 받는다.
    ## !! randint로 인덱스값을 랜덤하게 받아오는것! _ 내 아이디어와 동일
        ## 다만, 새롭게 사전을 만들어서 가져온다는 것이 다른점
        ## 한글 뜻은 우선 생각하지 않고, 영단어만 가져온다는 것에 유의
    index = random.randint(0, len(keys) - 1)
    english_word = keys[index]
    korean_word = vocab[english_word]
    
    ## 나머지 부분은 앞의 실습과 동일
    
    # 유저 입력값 받기
    guess = input("{}: ".format(korean_word))
    
    # 프로그램 끝내기
    if guess == 'q':
        break
    
    # 정답 확인하기
    if guess == english_word:
        print("정답입니다!\n")
    else:
        print("틀렸습니다. 정답은 {}입니다.\n".format(english_word))
이번 레슨은 어땠나요?