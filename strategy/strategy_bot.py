from random import randint
import asyncio
import websockets
import json
async def web_main():
    url = 'wss://stream.binance.com:9443/stream?streams=btcusdt@kline_5m'
    async with websockets.connect(url) as client:
        while True:
            data = json.loads(await client.recv())['data']
            o = (data['k'])
            print (o)
            # print (type(o))
            # py_o = json.loads(o)
            # print(type(py_o))
            # print(py_o)
            await asyncio.sleep(305)

# o
# h
# l
# c
list_x_1 = []
list_x_2 =[]
async def data():
    while True:
        o = randint(4, 6)
        h = randint(7, 9)
        l = randint(1, 4)
        c = randint(1, 10)
        x_1 = o - l
        x_2 = h - o
        print (x_1)
        print (x_2)
        list_x_1.append(x_1)
        list_x_2.append(x_2)
        print (list_x_1)
        print (list_x_2)
        print ("Передано на проверку")
        await asyncio.sleep(2)

async def check():
    while True:
        if max(list_x_1)>max(list_x_2):
            print ("Покупать")
            list_x_1.clear()
            list_x_2.clear()
            await asyncio.sleep(2)
        else:
            print ("Ждем")
            list_x_1.clear()
            list_x_2.clear()
            await asyncio.sleep(2)

async def main():
    task_data = asyncio.create_task(data())
    task_check = asyncio.create_task(check())
    await task_data
    await task_check

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(web_main())

# o = randint(1,10)
# h = randint(1,10)
# l = randint(1,10)
# c = randint(1,10)
#
# x_1 = o-l
# x_2 = h - o
# print (o)
# print (h)
# print (l)
# print (c)
#
# print (x_1)
# print (x_2)