def detect_liquidity_sweep(df):

    latest = df.iloc[-1]

    prev = df.iloc[-2]

    high_break = latest["high"] > prev["high"]

    low_break = latest["low"] < prev["low"]

    close_back_down = latest["close"] < prev["high"]

    close_back_up = latest["close"] > prev["low"]

    if high_break and close_back_down:

        return "BUY SIDE LIQUIDITY TAKEN"

    if low_break and close_back_up:

        return "SELL SIDE LIQUIDITY TAKEN"

    return "NO SWEEP"