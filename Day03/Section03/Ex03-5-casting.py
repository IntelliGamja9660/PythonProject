'''
파일명 : Ex03-5-casting.py

Casting
    변수에 유형을 지정하려는 경우 캐스팅으로 가능.
'''
# 정수형
x = int(1)
print(x)
y = int(2.8) #실수를 정수로 캐스팅-> 그냥 없어짐
print(y)
z = int("3")
print(z)
print(type(z)) #class int
print(x+z)

# 실수형
x = float(1)
print(x)
z = float("3")
print(z)

# 문자형
x = str(1)
y = str(2)
print(x)
print(x+y) #문자열 연결

# 아스키코드 변환
a = ord('A')
print(a) #65
b = chr(65)
print(b) #A