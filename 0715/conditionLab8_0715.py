# [실습 8]

import random

operNum = random.randint(1, 5)

if operNum == 1:
    result = 300 + 50
elif operNum == 2:
    result = 300 - 50
elif operNum == 3:
    result = 300 * 50
elif operNum == 4:
    result = 300 / 50
else:
    result = 300 % 50

print("결과값 :", result)