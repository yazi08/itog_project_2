import json
import requests
import  asyncio
import websockets
async def main():
    url = "wss://stream.binance.com:9443/stream?streams=btcusdt@kline_5m"
    while True:
        async with websockets.connect(url) as client:


            data = json.loads(await client.recv())['data']
            open = data['k']['o']
            print (open)
            await asyncio.sleep(65)



if __name__ =='__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())