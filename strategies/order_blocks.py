def detect_order_block(df):

    latest = df.iloc[-1]

    prev = df.iloc[-2]

    bullish_ob = (

        prev["close"] < prev["open"]

        and

        latest["close"] > prev["high"]

    )

    bearish_ob = (

        prev["close"] > prev["open"]

        and

        latest["close"] < prev["low"]

    )

    if bullish_ob:

        return "BULLISH_ORDER_BLOCK"

    elif bearish_ob:

        return "BEARISH_ORDER_BLOCK"

    return "NO_ORDER_BLOCK"