'''
파일명 : Ex13-9-readHello6.py
'''

import sys #OS(Operating System)

with open('hello2.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines()
    sys.stdout.writelines(line_list) #시스템 스탠다드 아웃, 줄 단위로 프린트 한 거랑 동일
#print(line_list)
