'''
파일명 : Ex03-2-print.py
print() 함수 사용법
    sep : 출력할  value의 구분 문자
    end : value 출력 후 출력할 문자 (기본값) '\n')
    file : 출력 방향 지정
'''
print('재미있는','파이썬') #자동 띄어쓰기, 문자 연결
print('Python', 'Java', 'C', sep=',') #sep라는 파라미터

print("안녕", end='') #디폴트는 end='\n'
print("하세요")

fos = open('sample.py', mode='wt') #open 함수 sample이라는 file을 생성시킴, mode write text
print('print("Hello World")', file=fos) #엔드 포인트를 파일에다가 쓰겠다
fos.close()