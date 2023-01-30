id = None #id = ''
pwd = None #pwd = ''

# 아이디 입력
while True:
    id = input('아이디를 입력하세요 (3글자 이상) >>>')
    if len(id) >2:
        break
    print('>3글자 이상 입력해 주세요.')
# 패스워드 입력
while True:
    pwd = input('패스워드를 입력하세요(영문, 숫자 포함 8자 이상) >>>')
    isContainAlpha = False
    isContainNumeric = False

    if len(pwd) < 8:
        print('>영문, 숫자 포함 8자 이상 입력해 주세요.')
        continue

    for ch in pwd:
        if ch.isalpha():
            isContainAlpha = True
        elif ch.isnumeric():
            isContainNumeric = True

    # 영문 포함 유효성 검사
    if not isContainAlpha:
        print('>영문, 숫자 포함 8자 이상 입력해 주세요.')
        continue

    # 숫자 포함 유효성 검사
    if not isContainNumeric:
        print('>영문, 숫자 포함 8자 이상 입력해 주세요.')
        continue

    #패스워드 한번 더 확인 유효성 검사
    pwdChk = input('패스워드를 한 번 더 입력하세요. >>> ')
    if pwd != pwdChk:
        print('> 일치하지 않습니다. 다시 입력해 주세요. ')
        continue

    break

print('회원가입 완료!')

#로그인 아이디
while True:
    loginId = input('아이디를 입력하세요 >>> ')
    if id == loginId:
        break
    print('>아이디가 일치하지 않습니다.')

# 로그인 패스워드
while True:
    loginPwd = input('패스워드를 입력하세요 >>> ')
    if id == loginPwd:
        break
    print('>패스워드가 일치하지 않습니다.')

print('로그인 성공!')
print('{}님 환영합니다. :'.format(id))


'''id = input('아이디를 입력하세요(3글자 이상) >>>')
print(id)
while len(id) < 3:
    print('3 글자 이상 입력해 주세요!')
    id = input('아이디를 입력하세요(3글자 이상) >>>')
else:
    pw = input('패스워드를 입력하세요(영문 숫자 포함 8자 이상) >>>')
    print(pw)
    while len(pw) < 8 or pw.isalpha()==1 or pw.isnumeric()==1:
            pw = input('영문 숫자 포함 8자 이상 입력해 주세요!(8자 미만일 때)')
            print(pw)
    else:
            pw2 = input('패스워드 확인 한번 더 입력하세요 >>>')
            print(pw2)

    while   pw != pw2:
            pw2 = input('일치하지 않습니다! 다시 입력해 주세요! >>>')
            print(pw2)
    else:
            print('회원가입 완료!')

pw3 = input('비밀번호를 입력하세요. >>>')
if pw3 == pw:
    print('로그인 성공!\n {}님 환영합니다!'.format(id))

 '''





'''
주말 숙제!!

[회원가입]
hint - len() 함수 사용

아이디를 입력하세요(3글자 이상) >>>
> 3글자 이상 입력해 주세요!

아이디를 입력하세요(3글자 이상) >>>(다시 나와야 함)

패스워드를 입력하세요(영문 숫자 포함 8자 이상) >>>
> 영문 숫자 포함 8자 이상 입력해 주세요!(8자 미만일 때)

(제대로 입력 했을 때)
패스워드 확인 한번 더 입력하세요 >>>
>일치하지 않습니다! 다시 입력해 주세요!

(다시 돌아감)패스워드를 입력하세요(영문 숫자 포함 8자 이상) >>>

패스워드 확인 한번 더 입력하세요 >>>

회원가입 완료!!

[로그인]
아이디를 입력하세요 >>>
>아이디가 일치하지 않습니다.

아이디를 입력하세요 >>>

패스워드를 입력하세요>>>
패스워드가 일치하지 않습니다.

패스워드를 입력하세요 >>>

로그인 성공!
000님 환영합니다!
'''