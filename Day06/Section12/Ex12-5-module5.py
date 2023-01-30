'''
파일명 : Ex12-5-module5.py
별명 사용하기 2
'''
from converter import kilometer_to_miles as k_to_m #as 사용

miles = k_to_m(150)
print('150km={}miles'.format(miles))
