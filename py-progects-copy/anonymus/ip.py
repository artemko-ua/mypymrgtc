###############################################################
#       __ _ _ __   ___  _ __  _   _ _ __ ___  _   _ ___      #
#      / _` | '_ \ / _ \| '_ \| | | | '_ ` _ \| | | / __|     #
#     | (_| | | | | (_) | | | | |_| | | | | | | |_| \__ \     #
#      \__,_|_| |_|\___/|_| |_|\__, |_| |_| |_|\__,_|___/     #
#                              |___/                          #
#                                                             #
#   author: @artemko-ua                                       #
#   github: https://github.com/artemko-ua                     #
#   ip and mac chenger for linux for free                     #
#   support: bc1qdrqemhgw5zphg2unnk6h9663hj96lp83nhq6jm (btc) #
#   version: 1.0                                              #
###############################################################

import os 
import requests
from time import sleep

def Main():
    change = int(input("Через скільки секунд змінити IP? "))
    os.system('service tor start')
    url = 'https://httpbin.org/ip'
    proxy = {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'}

    while True:
        response = requests.get(url, proxies=proxy)
        if response.status_code == 200:
            print("yor curent ip :: {}". format(response.json()['origin']))
        else:
            print("failed to get current ip")
        sleep(change)
        os.system('service tor reload')

if __name__ == '__main__':
    Main() 