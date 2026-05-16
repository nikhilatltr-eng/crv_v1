from exchange.market_data import get_ohlcv

from indicators.volatility import (
    apply_volatility
)

df = get_ohlcv()

df = apply_volatility(df)

print(
    df[
        [
            "close",
            "atr",
            "bb_upper",
            "bb_lower",
            "supertrend"
        ]
    ].tail()
)