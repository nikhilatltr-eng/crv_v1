def detect_sniper_entry(

    df,

    signal

):

    latest = df.iloc[-1]

    previous = df.iloc[-2]

    high = latest["high"]

    low = latest["low"]

    close = latest["close"]

    prev_high = previous["high"]

    prev_low = previous["low"]

    sniper = False

    reason = "NO SNIPER"

    if signal == "LONG":

        liquidity_grab = (
            low < prev_low
        )

        bullish_close = (
            close > previous["close"]
        )

        if (
            liquidity_grab
            and bullish_close
        ):

            sniper = True

            reason = (
                "LONG LIQUIDITY GRAB"
            )

    elif signal == "SHORT":

        liquidity_grab = (
            high > prev_high
        )

        bearish_close = (
            close < previous["close"]
        )

        if (
            liquidity_grab
            and bearish_close
        ):

            sniper = True

            reason = (
                "SHORT LIQUIDITY GRAB"
            )

    return {

        "sniper_entry": sniper,

        "sniper_reason": reason
    }