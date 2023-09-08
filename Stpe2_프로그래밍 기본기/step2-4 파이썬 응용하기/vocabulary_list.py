with open('vocabulary.txt', 'w') as f:
    while True:
        english_word = input('영어 단어를 입력하세요: ')    
        # 영단어를 입력받음과 동시에, q를 입력한경우 바로 종료되도록!
        if english_word == 'q':
            break
        
        korean_word = input('한국어 뜻을 입력하세요: ')
        # 영단어와 마찬가지로 .. 
        if korean_word == 'q':
            break
        
        # 입력받는 부분은 맞게 잘썼었다....!
        f.write('{}: {}\n'.format(english_word, korean_word))