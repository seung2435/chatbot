import os # 운영체제 관련 
import requests
from pprint import pprint as pp

token = os.getenv('TELEGRAM_TOKEN')

msg = input()

def getId(token):
    # url (baseurl + token + methods)
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    res = requests.get(url)
    doc = res.json()
    
    # json.loads(json) > python dictionary
    chat_id = doc['result'][0]['message']['chat']['id']
    return chat_id


def sendMessage(chat_id, token, msg):
    base_url = "https://api.telegram.org"
    url = f"{base_url}/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)
    return f"{msg}를(을) {chat_id}님에게 보냈습니다."

print(sendMessage(getId(token), token, msg))
