'''
파일명 : Ex02-7-set.py

Set

    순서가 없다.
    인덱싱 되지 않는 컬렉션
    중복값 없다.
'''
thisset = {"피카츄", "라이츄", "파이리"}
#실행할 때마다 순서가 변경. 내부적으로는 순서를 구분하지 않음.
print(thisset)

#항목 가져오기
for x in thisset: #thisset 길이만큼 반복
    print(x)


# 값이 있는지 확인
thisset = {"피카츄", "라이츄", "파이리"}
print("피카츄" in thisset)
print("꼬부기" in thisset)

#항목 추가하기
thisset.add("꼬부기")
print(thisset)

#다른 Set 항목 추가
thisset1 = {"피카츄", "라이츄", "파이리"}
thisset2 = {"꼬부기", "잠만보", "뮤츠"}
thisset1.update(thisset2) #update라는 메소드
print(thisset1)

#항목 제거
thisset = {"피카츄", "라이츄", "파이리"}
thisset.remove("피카츄")
print(thisset)
#thisset.remove("피카츄")
#print(thisset)

#항목제거. 없는 항목을 제거해도 오류가 안난다.
thisset.discard("피카츄")
print(thisset)
thisset.discard("피카츄")
print(thisset)

#항목제거
thisset.pop()
print(thisset)

#비우기
thisset.clear()
print(thisset)