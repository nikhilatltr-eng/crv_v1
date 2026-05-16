from binance.client import Client

from dotenv import load_dotenv

import os


load_dotenv()


API_KEY = os.getenv(
    "BINANCE_API_KEY"
)

API_SECRET = os.getenv(
    "BINANCE_API_SECRET"
)


client = Client(
    API_KEY,
    API_SECRET
)

client.FUTURES_URL = (
    "https://testnet.binancefuture.com/fapi"
)


def place_trade(signal_data):

    signal = signal_data["signal"]

    entry = signal_data["entry"]

    quantity = 20

    side = (
        "BUY"
        if signal == "LONG"
        else "SELL"
    )

    order = client.futures_create_order(

        symbol="CRVUSDT",

        side=side,

        type="MARKET",

        quantity=quantity
    )

    print()

    print("TRADE EXECUTED")

    print(order)

    return order