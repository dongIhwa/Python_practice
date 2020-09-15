# [실습6]

def print_gugudan(a):
    if type(a) is int:
        if a>= 1 and a <= 9:
            for i in range(1, 10):
                print(a, "*", i, "=", a*i)
        else:
            return None
    else:
        return None

print_gugudan(1)
print_gugudan("a")
print_gugudan(10)