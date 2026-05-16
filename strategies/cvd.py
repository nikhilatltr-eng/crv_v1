def calculate_cvd(trades):

    cvd = 0

    for trade in trades:

        amount = float(
            trade["amount"]
        )

        side = trade["side"]

        if side == "buy":

            cvd += amount

        else:

            cvd -= amount

    if cvd > 0:

        return {

            "cvd_bias":
                "BULLISH",

            "cvd_value":
                round(cvd, 2)
        }

    elif cvd < 0:

        return {

            "cvd_bias":
                "BEARISH",

            "cvd_value":
                round(cvd, 2)
        }

    return {

        "cvd_bias":
            "NEUTRAL",

        "cvd_value":
            0
    }