# [실습3]

import random

num1 = random.randint(1, 10)
num2 = random.randint(30, 40)
print(num1, num2)
result_sum = 0

for i in range(num1, num2+1):
    if i % 2 == 0:
        result_sum += i

print(num1, "부터", num2, "까지의 짝수의 합 :", result_sum)