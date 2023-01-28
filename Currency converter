import requests

currency_I_have = input().lower()
cache = {}

if currency_I_have == "usd":
    r = requests.get('http://www.floatrates.com/daily/usd.json').json()
    cache["eur"] = r['eur']['rate']
elif currency_I_have == "eur":
    r = requests.get('http://www.floatrates.com/daily/eur.json').json()
    cache["usd"] = r['usd']['rate']
else:
    r = requests.get(f'http://www.floatrates.com/daily/{currency_I_have}.json').json()
    cache["eur"] = r['eur']['rate']
    cache["usd"] = r['usd']['rate']
while True:
    currency_I_need = input().lower()
    if len(currency_I_need) == 0:
        break
    amount = int(input())
    print("Checking the cache...")
    if currency_I_need in cache.keys():
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        cache[currency_I_need] = requests.get(f'http://www.floatrates.com/daily/{currency_I_have}.json').json()[currency_I_need]['rate']

    total = cache[currency_I_need] * amount
    print(f"You received {total} {currency_I_need.upper()}.")

