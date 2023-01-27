'''
파일명 : Ex08-2-continue.py

continue
    while문이나 for문과 같은
    반복문을 강제로 건너뛰기
    (아래 코드 실행하지 않는다)
'''
total = 0
for a in range(1 , 101): # 1부터 100까지의 값을 a에 넣어줌
    if a % 3 == 0: # 3의 배수면
        continue #빼기
    print('a: {}, total {}'.format(a, total))
    total += a #3의 배수 빼고 더하기

print(total)
