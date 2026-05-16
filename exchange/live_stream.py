import asyncio
import json
import websockets


SOCKET = "wss://stream.binance.com:9443/ws/crvusdt@trade"

buy_volume = 0
sell_volume = 0


async def stream_trades():

    global buy_volume
    global sell_volume

    async with websockets.connect(SOCKET) as ws:

        print()
        print("LIVE ORDER FLOW STARTED")
        print()

        while True:

            data = await ws.recv()

            data = json.loads(data)

            price = float(data["p"])

            qty = float(data["q"])

            side = "SELL" if data["m"] else "BUY"

            usd_size = price * qty

            if side == "BUY":

                buy_volume += usd_size

            else:

                sell_volume += usd_size

            total = buy_volume + sell_volume

            buy_percent = (
                buy_volume / total
            ) * 100

            sell_percent = (
                sell_volume / total
            ) * 100

            print()

            print("LIVE TRADE")

            print("PRICE:", round(price, 6))

            print("SIZE:", round(usd_size, 2))

            print("SIDE:", side)

            print()

            print(
                "BUY PRESSURE:",
                round(buy_percent, 2),
                "%"
            )

            print(
                "SELL PRESSURE:",
                round(sell_percent, 2),
                "%"
            )

            if buy_percent > 60:

                print()

                print(
                    "BULLISH ORDER FLOW"
                )

            elif sell_percent > 60:

                print()

                print(
                    "BEARISH ORDER FLOW"
                )


asyncio.run(stream_trades())