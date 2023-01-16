'''
파일명 : Ex02-1-circle.py
개요 : 반지름을 전달하면 원의 넓이를 반환하는 get_area() 함수
'''

#math 모듈 포함
import math

#get_area() 함수 정의
def get_area(radius):
    """반지름을 입력 받아서 원의 넓이를 반환하는 get_area() 함수""" #공식 문서식으로 쓸 때 독스트링으로 쓰면 된다
    area = math.pi * math.pow(radius, 2)
    return area

#함수는 코드 묶음, 반복되는 것을 줄이기 위해 쓴다.
#def 함수명(함수값=매개변수/인자)
#값을 담는 그릇을 선언, 뒤에 있는 값을 앞에다가 대입하겠다는 뜻.
#math 모듈에서 pi를 불러오겠다,  math 모듈에 있는 pow 함수에 radius^2, 원의 넓이를 구하는 공식이 area라는 메모리에 저장이 돼요
#호출한 함수에서 area값을 돌려줘요 선언이 돼요 실행은 아래에서

radius = 1.5 #반지름 1.5
print(radius)

# get_area() 함수 호출 결과를 area 변수에 저장
area = get_area(radius) #함수 실행
print(area) #출력
print(get_area.__doc__) # Docstring 확인
