'''
파일명 : Ex02-9-mutable-immutable.py
mutable - 메모리 값을 변경 가능 객체
    리스트(list), 세트(set), 딕셔너리(dict)
'''
me = [1,2,3]
print(id(me)) #2986748083968
me.append(4)
print(id(me)) #2986748083968 주소값이 같다

'''
immutable - 메모리 값 변경 불가
    정수(int), 실수(float), 문자열(str), 튜플(tuple)
'''
me = 10
print(id(me)) #1878060722768
me += 1 # me = me + 1
print(id(me)) #1878060722800 주소값이 다르다



# 튜플 테스트

thistuple = ("피카츄", "라이츄", "파이리")
print(id(thistuple))
thiscast = list(thistuple) #casting 또는 형변환
thiscast[1] = "잠만보"
thistuple = tuple(thiscast) #다시 튜플로 바꾸기
print(id(thistuple))
