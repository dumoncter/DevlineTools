import requests
from docker import telegram_settings


def send_msg(text):
    token = telegram_settings.token
    chat_id = telegram_settings.chat_id
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print('Send message successful')
