def detect_candle_pattern(df):

    latest = df.iloc[-1]

    previous = df.iloc[-2]

    latest_body = abs(
        latest["close"] - latest["open"]
    )

    previous_body = abs(
        previous["close"] - previous["open"]
    )

    bullish_engulfing = (

        latest["close"] > latest["open"]

        and

        previous["close"] < previous["open"]

        and

        latest_body > previous_body

    )

    bearish_engulfing = (

        latest["close"] < latest["open"]

        and

        previous["close"] > previous["open"]

        and

        latest_body > previous_body

    )

    hammer = (

        latest["close"] > latest["open"]

        and

        (
            latest["open"] - latest["low"]
        ) > latest_body * 2

    )

    shooting_star = (

        latest["close"] < latest["open"]

        and

        (
            latest["high"] - latest["open"]
        ) > latest_body * 2

    )

    if bullish_engulfing:

        return "BULLISH_ENGULFING"

    elif bearish_engulfing:

        return "BEARISH_ENGULFING"

    elif hammer:

        return "HAMMER"

    elif shooting_star:

        return "SHOOTING_STAR"

    return "NO_PATTERN"