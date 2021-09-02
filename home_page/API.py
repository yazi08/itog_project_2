""" Бот по выводу определенной суммы"""
# from django.conf import settings
#
# settings.configure()
# 6gFDmF4ohM.T5SNvB&%9xj!h^1Hy:%Yc
# TXforrAh79JExWk8
import json
# import requests
import  asyncio
import websockets
# from home_page.views import *
# from bot import *
import time
# wss://stream.binance.com:9443/stream?streams=ethusdt@miniTicker
# wss://stream.binance.com:9443/stream?streams=btcusdt@kline_3m
import psycopg2

import os

pid = os.getpid()
print (pid)



con = psycopg2.connect(
  database="tredebot_db",
  user="tredebot",
  password="1234567890lP",
  host="127.0.0.1",
  port="5432"
)

print("Database opened successfully")


cur = con.cursor()
cur.execute("SELECT sum_client,who_client_id,date_client from home_page_summclientitog")
# cur.execute ("select username from  auth_user where id =(%i)"%a)
rows = cur.fetchall()
user = rows[0]


sum=(user[0])
id = user[1]

print (id)
# r = str(id)
# print (type(r))
cur.execute ("SELECT username FROM auth_user where id =%s" % id)
itog = cur.fetchall()
client =((itog[0])[0])

x = str(sum)
id_itog = str(id)

cur = con.cursor()
cur.execute(
"INSERT INTO home_page_historyclient (summ_history_client,who_id,date) VALUES (%s,%s,now()) RETURNING id" %(x,id_itog)

)
end = cur.fetchall()
end_itog = str((end[0])[0])

cur = con.cursor()
cur.execute("DELETE from home_page_summclientitog")
con.commit()
con.close()

btc_close = []
btc_min = []
# x = input("Введите сумму:")
print(x)
async def main():
    url = "wss://stream.binance.com:9443/stream?streams=btcusdt@kline_5m"
    async with websockets.connect(url) as client:
        data = json.loads(await client.recv())['data']
        btc_min.append(data['k']['h'])
        btc_close.append(data['k']['c'])
        print (btc_close)

        while x > max(btc_close) or x< min(btc_close):
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
            con = psycopg2.connect(
                database="tredebot_db",
                user="tredebot",
                password="1234567890lP",
                host="127.0.0.1",
                port="5432"
            )

            # bot.polling()
            from datetime import datetime
            cur = con.cursor()
            cur.execute(
                """UPDATE home_page_historyclient
                SET data_end = now()
                WHERE id =(%s)
                """ %(end_itog)

            )
            con.commit()
            con.close()
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

