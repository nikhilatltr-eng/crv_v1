def analyze_market_structure(df):

    latest = df.iloc[-1]

    ema20 = latest["ema20"]

    ema50 = latest["ema50"]

    if ema20 > ema50:

        return "BULLISH"

    elif ema20 < ema50:

        return "BEARISH"

    return "RANGING"