from websocket import WebSocketApp

import json

SOCKET = (
    "wss://fstream.binance.com/ws/"
    "crvusdt@trade"
)

def on_message(
    ws,
    message
):

    data = json.loads(message)

    price = data["p"]

    quantity = data["q"]

    side = data["m"]

    if side:

        trade_side = "SELL"

    else:

        trade_side = "BUY"

    print()

    print(
        "LIVE TRADE"
    )

    print(
        "PRICE:",
        price
    )

    print(
        "QTY:",
        quantity
    )

    print(
        "SIDE:",
        trade_side
    )

def on_open(ws):

    print()

    print(
        "WEBSOCKET CONNECTED"
    )

def start_websocket():

    ws = WebSocketApp(

        SOCKET,

        on_message=on_message,

        on_open=on_open

    )

    ws.run_forever()