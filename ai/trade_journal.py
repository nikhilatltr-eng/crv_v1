import pandas as pd

from datetime import datetime

import os


def log_trade(signal_data):

    trade = {

        "time":
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

        "market_structure":
        signal_data["market_structure"],

        "order_flow":
        signal_data["order_flow"],

        "whale_activity":
        signal_data["whale_activity"],

        "liquidity":
        signal_data["liquidity_sweep"],

        "sniper_entry":
        signal_data["sniper_entry"],

        "fvg":
        signal_data["fvg_signal"],

        "order_block":
        signal_data["order_block"],

        "structure_signal":
        signal_data["structure_signal"]
    }

    file_path = (
        "data/trade_memory.csv"
    )

    if os.path.exists(file_path):

        old_df = pd.read_csv(
            file_path
        )

        new_df = pd.concat(
            [
                old_df,
                pd.DataFrame([trade])
            ],
            ignore_index=True
        )

    else:

        new_df = pd.DataFrame(
            [trade]
        )

    new_df.to_csv(
        file_path,
        index=False
    )

    print()

    print("TRADE STORED")