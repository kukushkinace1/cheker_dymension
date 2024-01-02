import time
import requests
from tqdm import tqdm

# Список адресов из файла
with open('addresses.txt', 'r') as f:
    addresses = [line.strip() for line in f]

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru,en;q=0.9,ru-RU;q=0.8,zh-TW;q=0.7,zh;q=0.6',
    'Connection': 'keep-alive',
    'Origin': 'https://genesis.dymension.xyz',
    'Referer': 'https://genesis.dymension.xyz/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

total_point = 0

for address in tqdm(addresses, ncols=70):
    params = {
        'address': address.lower(),
    }
    try:
        attempt = 0
        point = 0
        while attempt < 3 and point == 0:
            response = requests.get('https://geteligibleuserrequest-xqbg2swtrq-uc.a.run.app/', params=params, headers=headers)
            if response.json()['amount']:
                point = int(response.json()['amount'])
                total_point += point
            else:
                time.sleep(3)
                attempt += 1
        with open('stats.txt', 'a') as output:
            print(f"{address}: {point}", file=output)
    except:
        pass
    time.sleep(2)

print(f'{total_point} всего поинтов')
