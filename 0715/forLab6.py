# [실습6]
result_sum = 0
for i in range(1, 51):
    if i % 3 == 0:
        if i % 5 == 0:
            continue
        else:
            result_sum += i

print("결과 =", result_sum)