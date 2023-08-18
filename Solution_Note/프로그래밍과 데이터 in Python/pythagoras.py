for a in range(1,400):
    for b in range(a+1, 400-a):
        c = 400 - a - b
        if(a**2 + b**2 == c**2):
            print(a*b*c)


            