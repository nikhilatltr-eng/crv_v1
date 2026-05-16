import ccxt

from dotenv import load_dotenv

import os


load_dotenv()


API_KEY = os.getenv(
    "BINANCE_API_KEY"
)

API_SECRET = os.getenv(
    "BINANCE_API_SECRET"
)


exchange = ccxt.binance({

    "apiKey": API_KEY,

    "secret": API_SECRET,

    "enableRateLimit": True,

    "options": {
        "defaultType": "future"
    }
})


def place_trade(signal_data):

    signal = signal_data["signal"]

    quantity = 20

    side = (
        "buy"
        if signal == "LONG"
        else "sell"
    )

    try:

        order = exchange.create_market_order(

            symbol="CRV/USDT",

            side=side,

            amount=quantity
        )

        print()

        print("TRADE EXECUTED")

        print(order)

        return order

    except Exception as e:

        print()

        print("TRADE ERROR")

        print(e)

        return None