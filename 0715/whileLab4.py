# [실습4]

while True:
    num = int(input("1부터 12까지 숫자 하나를 입력해주세요."))
    if num == 1 or num == 2 or num == 12:
        print(num, "월은 겨울", sep='')
    elif num == 3 or num == 4 or num == 5:
        print(num, "월은 봄", sep='')
    elif num == 6 or num == 7 or num == 8:
        print(num, "월은 여름", sep='')
    elif num == 9 or num == 10 or num == 11:
        print(num, "월은 가을", sep='')
    else:
        print("1~12 사이의 값을 입력하세요!")
        break