import ccxt
import pandas as pd
import ta


exchange = ccxt.binance({
    "enableRateLimit": True
})


def get_ohlcv(
    symbol="CRV/USDT",
    interval="1m",
    limit=200,
    timeframe=None
):

    if timeframe:

        interval = timeframe

    ohlcv = exchange.fetch_ohlcv(
        symbol,
        timeframe=interval,
        limit=limit
    )

    df = pd.DataFrame(

        ohlcv,

        columns=[
            "time",
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]
    )

    df["open"] = df["open"].astype(float)

    df["high"] = df["high"].astype(float)

    df["low"] = df["low"].astype(float)

    df["close"] = df["close"].astype(float)

    df["volume"] = df["volume"].astype(float)

    df["ema20"] = ta.trend.ema_indicator(
        df["close"],
        window=20
    )

    df["ema50"] = ta.trend.ema_indicator(
        df["close"],
        window=50
    )

    df["rsi"] = ta.momentum.rsi(
        df["close"],
        window=14
    )

    macd = ta.trend.MACD(
        df["close"]
    )

    df["macd"] = macd.macd()

    df["macd_signal"] = (
        macd.macd_signal()
    )

    df["atr"] = ta.volatility.average_true_range(
        df["high"],
        df["low"],
        df["close"]
    )

    df["returns"] = (
        df["close"].pct_change()
    )

    df["volume_delta"] = (
        df["volume"].diff()
    )

    df["buy_pressure"] = (
        (
            df["close"] - df["low"]
        )
        /
        (
            df["high"] - df["low"]
            + 0.0001
        )
    )

    df["sell_pressure"] = (
        (
            df["high"] - df["close"]
        )
        /
        (
            df["high"] - df["low"]
            + 0.0001
        )
    )

    df["imbalance"] = (
        df["buy_pressure"]
        -
        df["sell_pressure"]
    )

    df["cvd"] = (
        (
            df["close"] - df["open"]
        )
        * df["volume"]
    ).cumsum()

    df["volatility"] = (
        df["high"] - df["low"]
    )

    df.dropna(inplace=True)

    return df