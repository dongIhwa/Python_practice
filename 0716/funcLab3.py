# [실습3]

def expr(a, b, c):
    if c == '+':
        return(a+b)
    elif c == '-':
        return(a-b)
    elif c == '*':
        return(a*b)
    elif c == '/':
        return(a/b)
    else:
        return(None)

result = expr(1, 2, "*")
if result == None:
    print("수행 불가")
else:
    print("연산결과 :", result)

result = expr(1, 2, "a")
if result == None:
    print("수행 불가")
else:
    print("연산결과 :", result)