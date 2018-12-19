# 네이버 실시간 검색어
# 1. requests 에게 naver.com 요청을 보내기
# 2. 응답 받은 문서를 저장
# 3. BeautifulSoup 패키지 사용 : 정보를 찾기 좋게 만듬
# 4. 우리가 원하는 정보 추출 //day1
# 5. web browser 통해 트랜드1위 단어를 검색한 페이지 열어줌

import requests
import bs4
import webbrowser

url = "https://www.naver.com/"

response = requests.get(url)
doc = bs4.BeautifulSoup(response.text,'html.parser')
# print(doc) #양이 많아서 제대로 출력하지 못해 에러 발생
# result = doc.select_one('ul.ah_l:nth-child(5) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)')
result = doc.select_one('.ah_k') #첫번째 항목 선택
# print(result.text) #첫번째 항목의 단어만 출력

# webbrowser 통해 result.text에 있는 단어로 검색한 페이지를 연다
search_url = "https://search.naver.com/search.naver?query="
# webbrowser.open(search_url + result.text)

# 트랜드검색어 1~5위 추출
trend = doc.select(".ah_k")
trend_5 = trend[0:5]
print(trend_5)
for i in trend_5 :
    webbrowser.open(search_url + i.text)