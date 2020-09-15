# [실습1]
import random

num = random.randint(5, 10)
i = 1

while i <= num:
    print(i, "->", i ** 2)
    i += 1