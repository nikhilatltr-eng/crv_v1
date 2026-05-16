def bullish_engulfing(df):

    prev = df.iloc[-2]

    curr = df.iloc[-1]

    return (

        prev["close"] < prev["open"]

        and

        curr["close"] > curr["open"]

        and

        curr["close"] > prev["open"]

        and

        curr["open"] < prev["close"]

    )


def bearish_engulfing(df):

    prev = df.iloc[-2]

    curr = df.iloc[-1]

    return (

        prev["close"] > prev["open"]

        and

        curr["close"] < curr["open"]

        and

        curr["open"] > prev["close"]

        and

        curr["close"] < prev["open"]

    )


def detect_doji(df):

    candle = df.iloc[-1]

    body = abs(
        candle["close"]
        -
        candle["open"]
    )

    wick = (
        candle["high"]
        -
        candle["low"]
    )

    return body < wick * 0.1


def detect_hammer(df):

    candle = df.iloc[-1]

    body = abs(
        candle["close"]
        -
        candle["open"]
    )

    lower_wick = min(
        candle["open"],
        candle["close"]
    ) - candle["low"]

    return lower_wick > body * 2