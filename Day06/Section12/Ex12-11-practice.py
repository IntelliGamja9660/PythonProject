'''
파일명 : Ex12-11-practice.py
'''
import random
import time

# [1,2,3,4,5, ... 45]
pot = [n for n in range(1, 46)] # 뒤에 n을 앞에 n list에 하나씩 추가해줌

jackpot = []

for n in range(1, 7): #1~6까지 n이 반복
    random.shuffle(pot) #섞었어요
    pick = pot.pop() #pop이면 맨 뒤에서부터 가져오죠
    print('{}번째 당첨번호는 {}입니다.'.format(n, pick)) #섞은 거의 젤 마지막 값
    jackpot.append(pick)
    time.sleep(2) #2초 동안 멈췄다가 다시 반복

jackpot.sort() #크기 순서대로 정렬
print('이번 당첨번호는 {}입니다.'.format(jackpot))