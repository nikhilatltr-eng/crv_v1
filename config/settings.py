import os
from dotenv import load_dotenv

load_dotenv()

SYMBOL = os.getenv(
    "SYMBOL",
    "CRVUSDT"
)

LEVERAGE = int(
    os.getenv(
        "LEVERAGE",
        3
    )
)

RISK_PER_TRADE = float(
    os.getenv(
        "RISK_PER_TRADE",
        0.01
    )
)

MAX_TRADES_PER_DAY = int(
    os.getenv(
        "MAX_TRADES_PER_DAY",
        10
    )
)

DAILY_MAX_LOSS = float(
    os.getenv(
        "DAILY_MAX_LOSS",
        5
    )
)

TIMEFRAMES = [
    "1m",
    "5m",
    "15m",
    "1h"
]