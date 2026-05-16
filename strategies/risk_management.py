def calculate_position_size(

    account_balance,

    risk_percent,

    entry_price,

    stop_loss

):

    risk_amount = (
        account_balance
        * risk_percent
    )

    stop_distance = abs(
        entry_price - stop_loss
    )

    if stop_distance == 0:

        return 0

    quantity = (
        risk_amount / stop_distance
    )

    return round(quantity, 2)


def generate_trade_levels(
    signal,
    entry,
    atr
):

    if signal == "LONG":

        stop_loss = (
            entry
            -
            atr * 1.5
        )

        take_profit = (
            entry
            +
            atr * 3
        )

        breakeven = (
            entry
            +
            atr
        )

        trailing_stop = (
            atr * 0.8
        )

    elif signal == "SHORT":

        stop_loss = (
            entry
            +
            atr * 1.5
        )

        take_profit = (
            entry
            -
            atr * 3
        )

        breakeven = (
            entry
            -
            atr
        )

        trailing_stop = (
            atr * 0.8
        )

    else:

        return None

    rr = abs(
        (
            take_profit - entry
        )
        /
        (
            entry - stop_loss
        )
    )

    return {

        "entry": round(
            entry,
            6
        ),

        "stop_loss": round(
            stop_loss,
            6
        ),

        "take_profit": round(
            take_profit,
            6
        ),

        "breakeven": round(
            breakeven,
            6
        ),

        "trailing_stop": round(
            trailing_stop,
            6
        ),

        "risk_reward": round(
            rr,
            2
        )
    }