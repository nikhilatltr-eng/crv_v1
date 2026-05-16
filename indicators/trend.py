import pandas_ta as ta

def apply_indicators(df):

    # EMA

    df["ema20"] = ta.ema(
        df["close"],
        length=20
    )

    df["ema50"] = ta.ema(
        df["close"],
        length=50
    )

    # RSI

    df["rsi"] = ta.rsi(
        df["close"],
        length=14
    )

    # MACD

    macd = ta.macd(df["close"])

    df["macd"] = macd["MACD_12_26_9"]

    df["macd_signal"] = macd[
        "MACDs_12_26_9"
    ]

    return df