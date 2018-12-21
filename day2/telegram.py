import requests
from time import sleep
from bs4 import BeautifulSoup as bs
# url = f"https://api.telegram.org/bot{key}/"

# getMe 메소드로 확인

# getUpdates 메소드로 user id 확인

# 메세지 보내는 URL 작성
# https://api.telegram.org/bot{key}/sendMessage?chat_id={id}&text=message_from_chatbot

# 브라우저 과정으로 했던 위의 작업을 파이썬으로 자동화 시키기

## 단순 무식 방법

# url = "https://api.telegram.org/bot{key}/sendMessage?chat_id={id}&text=hey"
# requests.get(url)

# while True:
#     sleep(10) #10초 간격마다 코드 실행
#     requests.get(url)

## customizable 특정 변수값을 변경하여 만듬

html = requests.get('http://www.naver.com/').text
soup = bs(html, 'html.parser')
msg = []
for trend in soup.select('.PM_CL_realtimeKeyword_rolling .ah_item .ah_k'):
    msg.append(trend.text)

print("naver trend keyword 20")
for i in range(1,len(msg)):
    word = msg[i]
    url = f"https://api.telegram.org/bot{key}/sendMessage?chat_id={id}&text={word}"
    requests.get(url)
