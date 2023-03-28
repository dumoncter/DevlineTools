import requests
import datetime
import time
import json
import telegram_bot
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

count_ip = 0
ip_error = {}

def sync_devline(ip, name):
    try:
        date_server = datetime.datetime.today().strftime("%Y-%m-%dT%H:%M:%S")
        base_url = 'https://admin:PurgeXenos2012@' + ip + ':9796/datetime'
        requests.post(f"{base_url}", date_server, verify=False, timeout=10)
        print(f'{name}. Синхронизация ВР {ip} прошла успешно!')
    except:
        global ip_error
        ip_error[ip] = name
        print(f'Синхронизация не выполнена. Регистратор {name} не отвечает')


def main():
    try:
        with open("ip_devline.json", 'r', encoding='utf-8') as json_file:
            global count_ip
            data = json.load(json_file)
            for key, value in data.items():
                count_ip += 1
                sync_devline(value, key)
                time.sleep(2)
    except Exception as e:
        print(datetime.datetime.now(), "\nError : {}".format(e))


def send_telegram():
    try:
        if len(ip_error) >= 1:
            new_line = '\n'
            without_error = count_ip - len(ip_error)
            telegram_bot.send_msg(f'🎞 Время установлено на {without_error} ВР. 🎞\n'
                                  f'❌ Всего: {len(ip_error)} ВР с ошибками ❌\n'
                                  f'{new_line.join(map(str, ip_error.items() ))}')
        else:
            telegram_bot.send_msg(f'✅ Время на {count_ip} ВР установлено без ошибок ✅')
    except Exception as e:
        print('Telegram:', datetime.datetime.now(), "\nError : {}".format(e))


if __name__ == "__main__":
    main()
    send_telegram()
