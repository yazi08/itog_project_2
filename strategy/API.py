
""" Бот по выводу определенной суммы"""

# 6gFDmF4ohM.T5SNvB&%9xj!h^1Hy:%Yc
# TXforrAh79JExWk8
import json
import requests
import  asyncio
import websockets

from bot import *
import time
# wss://stream.binance.com:9443/stream?streams=ethusdt@miniTicker
# wss://stream.binance.com:9443/stream?streams=btcusdt@kline_3m
# from home_page.models import *
# a = Blog.objects.all()
# x = a.values().last()['id']

# print(x)
btc_close = []
btc_min = []
x = input("Введите сумму:")
async def main():
    url = "wss://stream.binance.com:9443/stream?streams=btcusdt@kline_5m"
    async with websockets.connect(url) as client:
        data = json.loads(await client.recv())['data']
        btc_min.append(data['k']['h'])
        btc_close.append(data['k']['c'])
        print (btc_close)
        while x > max(btc_close):
            data = json.loads(await client.recv())['data']
            event_time = time.localtime(data['E']//1000)
            print (f"{event_time.tm_hour}:{event_time.tm_min}:{event_time.tm_sec} -> Открытие - {data['k']['o']}, Максимум - {data['k']['h']}, Минимум - {data['k']['l']}, Закрытие - {data['k']['c']} ")
            # print (type(data['k']['h']))
            btc_close.append(data['k']['c'])
            btc_min.append(data['k']['c'])
            print ("Цена не достигла заданного значения ")
            await asyncio.sleep(2)
        else:
            print ("Сумма есть!")
            bot.polling()
            await asyncio.sleep(2)
            btc_close.clear()
            btc_min.clear()

            # print(btc)
async def test():
    while x not in btc_close:
        await asyncio.sleep(3)
    #x = "32817.77000000"
        print ("NO")

async def loops():
    task_main = asyncio.create_task(main())
    # task_test = asyncio.create_task(test())
    await task_main
    # await task_test
if __name__ =='__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(loops())

