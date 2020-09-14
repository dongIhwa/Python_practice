#[실습 5]
word = input("문자 한 개를 입력하세요 :")
word_code = hex(ord(word))
print("'",word, "'", " 문자의 코드값은 ", word_code, "입니다.", sep='')