'''
파일명 : Ex02-5-List.py
List
    단일 변수에 여러 항목을 저장하는 데 사용된다.
    List 항목은 순서가 지정되고 변경 가능하며 중복값 허용
    List 에는 다양한 데이터 유형이 포함될 수 있다.
'''
thislist = ["피카츄", "라이츄", "꼬부기"]
print(thislist)
print(thislist[0]) #0번 째 값 피카츄 가지고 옴
print(thislist[0][0]) #피카츄의 0번째 값 피
# List 길이
print(len(thislist))

#List 데이터 유형
List1 = ["피카츄", "라이츄", "꼬부기"]
List2 = [1, 2, 3, 4, 5]
List3 = [True, False, False]
#다양한 유형 포함 가능
List4 = ["abc", 34, False, 40]

#thislist = ["피카츄", "라이츄", "꼬부기"]
print(thislist[1])
thislist[1] = "잠만보" #라이츄를 잠만보로 바꾸겠다.

#항목 변경 2개
thislist = ["피카츄", "라이츄", "꼬부기", "파이리", "버터플", "야도란"]
thislist[1:3] = ["울먹이", "메타몽"]
print(thislist)

#두번째 세번째 값을 하나의 값으로 변경
thislist = ["피카츄", "라이츄", "꼬부기", "파이리", "버터플", "야도란"]
thislist[1:3] = ["울먹이"]
print(thislist)

# 항목 추가
thislist = ["피카츄", "라이츄", "파이리"]
thislist.append("꼬부기")
print(thislist)

# 항목 추가 - 인덱스 번호로 추가
thislist = ["피카츄", "라이츄", "파이리"]
thislist.insert(1, "잠만보")
print(thislist)

#항목 값으로 제거
thislist = ["피카츄", "라이츄", "파이리"]
thislist.remove("라이츄")
print(thislist)

# 항목을 지정된 인덱스로 제거
thislist = ["피카츄", "라이츄", "파이리"]
thislist.pop(2)
print(thislist)

# 마지막 값 제거
thislist = ["피카츄", "라이츄", "파이리", "잠만보"]
thislist.pop()
print(thislist)

#목록 삭제
thislist = ["피카츄", "라이츄", "파이리"]
thislist.clear()
print(thislist)

# 확장
thislist = ["피카츄", "라이츄", "파이리"]
thislist.extend(["버터플","야도란"])
print(thislist)

#객체 삭제
#del thislist
#print(thislist)

#list는 중요하다.