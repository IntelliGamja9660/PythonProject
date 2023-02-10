'''
파일명 : Ex18-1-requests.py

모듈 설치 rerquests
pip install requests
'''

import requests

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn'
param = {'code': 161967}
response = requests.get(url, params=param)
print(response.text)