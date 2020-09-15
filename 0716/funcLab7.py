# [실습7]

import random

def differtwovalue(a, b):
    if a > b:
        return(a - b)
    else:
        return(b - a)

num1 = random.randint(1, 30)
num2 = random.randint(1, 30)

result = differtwovalue(num1, num2)

for i in range(1, 6):
    print(num1, "와", num2, "의 차는", result, "입니다.")