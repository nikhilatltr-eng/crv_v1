import ccxt
import pandas as pd


exchange = ccxt.binance()


def download_data():

    bars = exchange.fetch_ohlcv(

        "CRV/USDT",

        timeframe="5m",

        limit=5000
    )

    df = pd.DataFrame(

        bars,

        columns=[

            "timestamp",

            "open",

            "high",

            "low",

            "close",

            "volume"
        ]
    )

    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        unit="ms"
    )

    df.to_csv(
        "data/crv_data.csv",
        index=False
    )

    print()

    print(
        "DATA DOWNLOADED"
    )


download_data()