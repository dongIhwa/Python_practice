# [실습 3]

import random

count = 0
while True:
    num = random.randint(0, 30)
    if num>=27 and num <= 30:
        print("수행횟수는", count, "번입니다")
        break
    else:
        print(chr(num+64), "(", num, ")", sep='')