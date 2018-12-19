# naver webtoon 화요일 웹툰 긁어오기

import requests 
from bs4 import BeautifulSoup as bs

url = "https://m.comic.naver.com/webtoon/weekday.nhn?week=tue"

res = requests.get(url).text #text 요소만 추출하여 res에 저장
doc = bs(res, 'html.parser') #html을 파싱하여 doc에 저장
toon_name = doc.select('.toon_name')

names =[]
imgs = []

for e in toon_name:
    names.append(e.text) #리스트에 저장
    print(e.text)

# 요소보기 > 복사 > css 선택자 : 이렇게 하면 너무 많이 추출하여 확인하기 어려움
# toon = doc.select("li.smart_toon:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(2) > h4:nth-child(1) > span:nth-child(1) > strong:nth-child(1)")

# for i in toon_name:
#     toon_img = doc.find("img")
#     img_src = toon_img.get("src")
# print(img_src)

for e in doc.select('.im_br'):
    imgs.append(e.select_one('img')["src"])
    print(e.select_one('img')["src"]) #dic를 key베이스로 추출하듯

# for name in names:
#     f = open('./a.text', 'a+')
#     f.write(name + ' ' + imgs + '\n')

print(len(names))
print(len(imgs))