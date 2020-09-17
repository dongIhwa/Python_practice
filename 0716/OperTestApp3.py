print("*입력한 숫자만큼 데코문자를 출력하는 프로그램입니다.*")
deco = input("데코문자를 입력하세요 : ")
number = int(input("출력횟수를 입력하세요 : "))
for i in range(number) :
    print(deco, end="")
print()

while True:
    x = input("계속 수행할까요(y/n)? ")
    if x == "Y" or x =="y":
        deco = input("데코문자를 입력하세요 : ")
        number = int(input("출력횟수를 입력하세요 : "))
        for i in range(number):
            print(deco, end="")
        print()
        continue
    elif x =="n" or x =="N":
        print("*수행 종료됩니다.*")
        break
    else:
        print("y나 n이 입력되지 않았습니다.")
        continue