from exchange.market_data import get_ohlcv

from indicators.trend import (
    apply_indicators
)

df = get_ohlcv()

df = apply_indicators(df)

print(
    df[
        [
            "close",
            "ema20",
            "ema50",
            "rsi",
            "macd"
        ]
    ].tail()
)