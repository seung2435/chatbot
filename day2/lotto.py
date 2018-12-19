import random, requests

import json
# json : 중괄호와 콜론으로 구성 > 파이썬의 딕셔너리와 비슷
# json_phonenumber = "{\"john\":\"010123456789\",\"ashley\":\"010986541\"}"
# # json_phonenumber["john"] #json은 문자열 그 자체이기 때문에 이렇게 사용x
# dict_phonenumber = json.loads(json_phonenumber)
# print(type(dict_phonenumber))

# # String 3가지 조작방법
# ## 1. Concatenation : "+" 글자 합체
# name = "john"
# loca = "seoul"
# print("hello " + name + ", this is " + loca + "SSAFY class")
# ## 2. Interpolation : 글자 삽입(수술)
# print(f"hello {name}, this is {loca} SSAFY class")
# # >>> hello john, this is seoul SSAFY class
# ## 3. Slicing : 글자 자르기
# greeting = "hello john, this is ashley"
# greeting[0:5]

# 0. 랜덤으로 로또 번호 생성
# picked = sorted(random.sample(range(1,46),6))
# print(picked)

# 1. 나눔로또정보 API 통해 우승번호 가져오기
# API 사용해서 긁어오기 : firefox json lite 확장 프로그램 설치하여 json 파일 읽기
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837'
res = requests.get(url)
print(type(res.text)) #str 구조

lotto = json.loads(res.text)
print(type(lotto)) #dir 구조

winner = []

for i in range(1,7):
    winner.append(lotto[f"drwtNo{i}"]) #lotto["drwtNo"]+str(i)
print(winner)

# 2. 랜덤으로 생성된 번호와 우승번호를 비교해서 나의 등수를 확인
# - 1등 : 6개
# - 2등 : 5개 + 보너스 번호
# - 3등 : 5개
# - 4등 : 4개
# - 5등 : 3개


# 집합만이 가능한 operation 사용가능
def pickLotto():
    picked = sorted(random.sample(range(1,46),6))
    
    matched = len(set(winner) & set(picked)) #교집합 원소(요소)의 개수(길이)

    if matched == 6:
        print("1등")
    elif matched == 5:
        print("3등")
    elif matched == 4:
        print("4등")
    # elif matched == 5:
    #     print("5등")


for i in range(10000000):
    pickLotto()
