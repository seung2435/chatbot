# open('파일명','뭘할지','[인코딩 등의 옵션]') 기본적으로 파일을 여는 함수
f = open('names.txt','a',encoding="utf-8")
f.write('\n무지')
f.close()

## 영구적(손실없이)으로 데이터를 저장할때

# .txt 파일 열기 
# 1. 읽기(Read)
# 2. 쓰기(Write)
# 3. 수정(Append)
# 파일 닫기

# .json 파일 열기 (import json) > dictionary
# 1. 읽기(Read)
# 2. 쓰기(Write)
# 3. 수정(Append)
# 파일 닫기

# .csv 파일 열기 (import csv) > 2d-list
# 1. 읽기(Read)
# 2. 쓰기(Write)
# 3. 수정(Append)
# 파일 닫기

# with 키워드 활용 > 코드를 간결

# DB 열기(connect) - CRUD operation
# 1. 읽기(CREATE)
# 2. 쓰기(READ / RETRIEVE)
# 3. 수정(UPDATE)
# 4. 삭제(DELETE / DESTROY)
# DB 닫기(disconnect)

# dictionary(key-value) + 강력한 메소드 추가 = object
# ORM 