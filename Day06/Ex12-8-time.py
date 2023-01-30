'''
파일명 : Ex12-8-time.py

time 모듈
    시간 처리에 관련된 time 모듈
'''
import time
# 1970년 1월 1일 0시 0분 0초부터 현재까지 경과 시간을 반환
# 마이크로 초
print(time.time()) #타임 모듈에 타임 함수가 있음

# ctime() 함수 - 인수로 전달된 time 시간 형식을 갖춰 반환
print(time.ctime(time.time()))

# 인수로 전달된 날짜와 지시자를 이용하여 형식을 갖춘
# 날짜 데이터를 문자열로 반환
print(time.strftime('%Y-%m-%d %H:%M:%S')) #스트링 포맷 타임
print(time.strftime('%Y년 %m월 %d일 %H:%M:%S')) #스트링 포맷 타임

#만약 인코딩 에러가 난다면 아래와 같이 사용하시면 됩니다.
print(
    time.strftime(
        '%Y년 %m월 %d일'
        .encode('unicode-escape')
        .decode()
    ).encode().decode('unicode-escape')
)

# 인자 초만큼 시스템 일시중지
time.sleep(1)

sec = 1
while True:
    print(sec)
    if sec == 10:
        break
    time.sleep(1)
    sec += 1
