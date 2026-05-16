def detect_fvg(df):

    latest = df.iloc[-1]

    prev = df.iloc[-2]

    prev2 = df.iloc[-3]

    bullish_fvg = (
        prev2["high"]
        <
        latest["low"]
    )

    bearish_fvg = (
        prev2["low"]
        >
        latest["high"]
    )

    if bullish_fvg:

        return "BULLISH_FVG"

    elif bearish_fvg:

        return "BEARISH_FVG"

    return "NO_FVG"