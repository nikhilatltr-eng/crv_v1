import ccxt


exchange = ccxt.binance()


def analyze_order_flow():

    trades = exchange.fetch_trades(
        "CRV/USDT",
        limit=100
    )

    order_book = exchange.fetch_order_book(
        "CRV/USDT",
        limit=20
    )

    buy_volume = 0

    sell_volume = 0

    recent_trades = []

    for trade in trades:

        amount = float(
            trade["amount"]
        )

        side = trade["side"]

        recent_trades.append({

            "amount": amount,

            "side": side
        })

        if side == "buy":

            buy_volume += amount

        else:

            sell_volume += amount

    total = buy_volume + sell_volume

    buy_pressure = round(
        (buy_volume / total) * 100,
        2
    )

    sell_pressure = round(
        (sell_volume / total) * 100,
        2
    )

    bid_volume = sum([
        bid[1]
        for bid in order_book["bids"]
    ])

    ask_volume = sum([
        ask[1]
        for ask in order_book["asks"]
    ])

    imbalance_ratio = round(
        bid_volume / (
            ask_volume + 0.0001
        ),
        2
    )

    imbalance = "NEUTRAL"

    if imbalance_ratio > 1.2:

        imbalance = "BULLISH"

    elif imbalance_ratio < 0.8:

        imbalance = "BEARISH"

    return {

        "buy_pressure":
            buy_pressure,

        "sell_pressure":
            sell_pressure,

        "bid_volume":
            round(bid_volume, 2),

        "ask_volume":
            round(ask_volume, 2),

        "imbalance_ratio":
            imbalance_ratio,

        "imbalance":
            imbalance,

        "recent_trades":
            recent_trades
    }


def detect_whale_activity(trades):

    whale_count = 0

    for trade in trades:

        if float(
            trade["amount"]
        ) > 500:

            whale_count += 1

    if whale_count >= 3:

        return "WHALE_ACCUMULATION"

    elif whale_count >= 1:

        return "LARGE_PLAYERS_ACTIVE"

    return "NORMAL_FLOW"