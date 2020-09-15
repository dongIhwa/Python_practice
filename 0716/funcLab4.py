# [실습4]

def print_triangle(a):
    if a >= 1 and a <= 10:
        for i in range(1, a+1):
            for x in range(1, i+1):
                print("*", end='')
            print()

print_triangle(5)
print_triangle(11)