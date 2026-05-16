import json

from datetime import datetime


MEMORY_FILE = (
    "logs/trade_memory.json"
)


def save_trade(signal_data):

    trade = {

        "timestamp":
            str(datetime.utcnow()),

        "signal":
            signal_data["signal"],

        "confidence":
            signal_data["confidence"],

        "entry":
            signal_data["entry"],

        "stop_loss":
            signal_data["stop_loss"],

        "take_profit":
            signal_data["take_profit"],

        "market_regime":
            signal_data["market_regime"],

        "reasons":
            signal_data["reasons"]
    }

    try:

        with open(
            MEMORY_FILE,
            "r"
        ) as f:

            data = json.load(f)

    except:

        data = []

    data.append(trade)

    with open(
        MEMORY_FILE,
        "w"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )

    print()

    print(
        "TRADE MEMORY SAVED"
    )