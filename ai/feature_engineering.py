import pandas as pd

import ta


def create_features():

    df = pd.read_csv(
        "data/crv_data.csv"
    )

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

    future_return = (
        (
            df["close"].shift(-6)
            -
            df["close"]
        )
        /
        df["close"]
    )

    df["target"] = 1

    df.loc[
        future_return > 0.01,
        "target"
    ] = 2

    df.loc[
        future_return < -0.01,
        "target"
    ] = 0

    df.dropna(inplace=True)

    df.to_csv(
        "data/crv_features.csv",
        index=False
    )

    print()

    print(
        "ADVANCED FEATURES CREATED"
    )


create_features()