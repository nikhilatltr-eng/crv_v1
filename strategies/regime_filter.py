def detect_market_regime(df):

    latest = df.iloc[-1]

    atr = latest["atr"]

    close = latest["close"]

    volatility_ratio = atr / close

    if volatility_ratio > 0.015:

        return "HIGH_VOLATILITY"

    elif volatility_ratio > 0.008:

        return "TRENDING"

    return "SIDEWAYS"