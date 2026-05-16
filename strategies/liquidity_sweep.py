def detect_liquidity_sweep(df):

    latest = df.iloc[-1]

    previous = df.iloc[-2]

    high_sweep = (
        latest["high"] > previous["high"]
        and latest["close"] < previous["high"]
    )

    low_sweep = (
        latest["low"] < previous["low"]
        and latest["close"] > previous["low"]
    )

    if high_sweep:

        return "BEARISH_LIQUIDITY_SWEEP"

    elif low_sweep:

        return "BULLISH_LIQUIDITY_SWEEP"

    return "NO_SWEEP"