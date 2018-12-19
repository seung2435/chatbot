# Bithumb의 
import requests
from bs4 import BeautifulSoup as bs
url = "http://www.bithumb.com"

res = requests.get(url).text
doc = bs(res, 'html.parser')
# coinlist = doc.select('.coin_list')

# css선택자로 링크를 긁어오면 제대로 긁어올 수 없음 
# result = doc.select_one('tr.one:nth-child(1) > td:nth-child(1) > p:nth-child(2) > a:nth-child(1) > span:nth-child(2)')
# print(result)

# for coin in coinlist:
#     print(coin.select_one('strong'))

coinlist = doc.select('tr.one:nth-child(1) > td:nth-child(1) > p:nth-child(2) > a:nth-child(1) > strong:nth-child(1)')
for coin in coinlist:
    print(coin.text)
