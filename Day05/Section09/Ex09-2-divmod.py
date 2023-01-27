'''
파일명 : Ex09-2-divmod.py

divmod() 함수
    두 숫자를 인자로 전달 바다
    첫 번째 인자를 두 번째 인자로
    나눈 몫과 나머지를 tuple 형식으로 반환한다.
'''
money = 10000
price = 3000
result = divmod(money, price)
print('빵을 {}개 사고 {}원이 남았습니다.' #몫과 나머지
      .format(result[0], result[1]))