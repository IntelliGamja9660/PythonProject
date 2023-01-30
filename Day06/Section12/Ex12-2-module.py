'''
파일명 : Ex12-2-module.py
모듈 사용법2
from 모듈명 import 함수
form 모듈명 import 함수1, 함수2
from 모듈명 import * #컨버터에 있는 모든 함수 쓰겠다
'''
from converter import kilometer_to_miles

miles = kilometer_to_miles(160)
print('150km={}miles'.format(miles))