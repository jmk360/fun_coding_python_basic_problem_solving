# -*- coding: utf-8 -*-

# [1. 파이썬 입력과 출력]

# Exercise 1. 문자열 출력하기
# 화면에 "Hello World"를 출력하라.

# sol)
print("Hello World")

# Exercise 2. 문자열 출력하기
# 화면에 "Mary's cosmetics"를 출력하라. (중간에 '가 있음에 주의.)

# sol)
print("Mary's cosmetics")
print("\"Mary\'s cosmetics\"")

# Exercise 3. 포맷 연산자
# print 함수를 사용하여 3.141592의 값을 출력하라. 단, 출력된 값이 소수점 아래로 두 자리 숫자까지만 표시되도록 하라.
# 실행 예: 3.14

# sol)
print("{:.2f}".format(3.141592)) # format 함수 사용
print("%.2f" %(3.141592)) # 형식지정자 사용
print(f"{3.141592:.2f}") # f-string 사용

# Exercise 4. 사용자 입력
# 사용자로부터 두 개의 숫자를 입력받은 후 두 개의 숫자를 더한 값을 출력하는 프로그램을 작성하라.
# 실행 예: first: 3 second: 4 합: 7

# sol)
# a = int(input())
# b = int(input())
# isum = a + b
# print('{} + {} = {}'.format(a, b, a + b))

# Exercise 5. 사용자 입력 (반복문을 배우는 이유)
# 사용자로부터 출력하고자 하는 문자열과 반복 횟수를 4로 입력받았다고 가정하기, 문자열을 반복 횟수(4번)만큼 출력하는 프로그램을 작성하라.
# 실행 예: 문자열: hello 반복횟수: 4 "hellohellohellohello"

# sol1)
# s = input("문자열: ")
# count = int(input("반복횟수: "))
# print("{}".format(s) * count)

# sol2)
# s = input("문자열: ")
# count = int(input("반복횟수: "))
# for i in range(count):
#     print(s, end='')
# print()

# Exercise 6. 형 변환
# 문자열 '720'를 정수형으로 변환하라. 정수 100을 문자열 '100'으로 변환하라.

# sol)
s1 = '720'
i1 = 100
print(int(s1))
print(str(i1))

# Exercise 7. 사칙 연산
# 사용자로부터 두 개의 숫자를 입력 받은 후 두 숫자의 덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/) 결괏값을 출력하라.

# sol)
# a = int(input())
# b = int(input())
# print('{} + {} = {}'.format(a, b, a + b))
# print('{} - {} = {}'.format(a, b, a - b))
# print('{} * {} = {}'.format(a, b, a * b))
# print('{} / {} = {}'.format(a, b, a / b))

# Exercise 8. 거듭제곱
# 사용자로부터 밑과 지수를 입력 받은 후 거듭제곱 값을 출력하라.
# 실행 예: 밑: 3 지수: 2 3^2 = 9

# sol)
# i1 = int(input("밑: "))
# i2 = int(input("지수: "))
# print("밑: {} 지수: {} {}^{} = {}".format(i1, i2, i1, i2, i1**i2))
# print("밑: {} 지수: {} {}^{} = {}".format(i1, i2, i1, i2, pow(i1, i2)))

# Exercise 9, 10 입력과 출력
# 사용자로부터 두 개의 숫자를 입력받은 후 두 개의 숫자를 더한 값, 곱한 값, 나눈 값, 나눈 몫, 나머지 값을 각각 출력하는 프로그램을 작성하세요.

# sol)
# a = int(input())
# b = int(input())
# print('{} + {} = {}'.format(a, b, a + b))
# print('{} * {} = {}'.format(a, b, a * b))
# print('{} / {} = {}'.format(a, b, a / b))
# print('{} // {} = {}'.format(a, b, a // b)) # 몫
# print('{} % {} = {}'.format(a, b, a % b)) # 나머지

# Exercise 10. 입력과 출력
# 사용자로부터 두 개의 숫자를 입력받은 후 두 개의 숫자를 더한 값, 곱한 값, 나눈 값, 나눈 몫, 나머지 값을 각각 다음과 같이 출력하는 프로그램을 작성하세요.

# sol)

# Exercise 11. 입력과 출력
# 사용자로부터 두 개의 숫자를 입력받은 후 두 개의 숫자를 나눈 값을 다음 조건에 맞추어 출력하는 프로그램을 작성하세요.
# format() 함수를 사용해서 출력하세요
# 단, 나눈 값은 소숫점 첫번째 자리까지만 출력하세요.

# sol)
# a = int(input())
# b = int(input())
# print('나눈값 = {:.1f}'.format(a / b))