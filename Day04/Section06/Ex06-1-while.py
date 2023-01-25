'''
파일명 : Ex06-1-while.py

반복문
    어떤 수행 작업을 한 번이 아니라 계속해서 수행해야 할 때 사용한다.

반복문 종류
    while, for문

while문
    특정 조건을 만족하는 동안 반복해서 수행하는 코드

while 조건식:
    반복 실행코드
'''
n = 10
while n >= 1:
    print(n)
    n -= 1 # n = n - 1
print("while문 끝나고 n 값 : {}".format(n))



#별찍기
n = 1
while n <= 10:
    print("*"*n)
    n += 1 # n = n - 1
print("while문 끝나고 n 값 : {}".format(n))

# 언어 go lang 비주류 언어 / 러스트 (C나 C++ 대체할 언어)

# 구구단 2단
n = 1
while n <= 9:
    print(2*n)
    n += 1
print("구구단 2단을 출력")

# 구구단 x단
x = int(input("몇 단을 출력할까요? >>> "))
print(x)
print("구구단 {}단을 출력!".format(x))
n = 1
while n <= 9:
    print(x * n)
    n += 1


