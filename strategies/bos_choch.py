def detect_bos_choch(df):

    latest = df.iloc[-1]

    prev = df.iloc[-2]

    prev2 = df.iloc[-3]

    bullish_bos = (

        latest["high"]
        >
        prev["high"]

        and

        prev["high"]
        >
        prev2["high"]
    )

    bearish_bos = (

        latest["low"]
        <
        prev["low"]

        and

        prev["low"]
        <
        prev2["low"]
    )

    bullish_choch = (

        latest["close"]
        >
        prev["high"]

        and

        prev["close"]
        <
        prev2["close"]
    )

    bearish_choch = (

        latest["close"]
        <
        prev["low"]

        and

        prev["close"]
        >
        prev2["close"]
    )

    if bullish_bos:

        return "BULLISH_BOS"

    elif bearish_bos:

        return "BEARISH_BOS"

    elif bullish_choch:

        return "BULLISH_CHOCH"

    elif bearish_choch:

        return "BEARISH_CHOCH"

    return "NO_STRUCTURE_SHIFT"