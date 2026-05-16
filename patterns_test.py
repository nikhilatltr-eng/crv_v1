from exchange.market_data import get_ohlcv

from indicators.patterns import (
    bullish_engulfing,
    bearish_engulfing,
    detect_doji,
    detect_hammer
)

df = get_ohlcv()

print(
    "BULLISH ENGULFING:",
    bullish_engulfing(df)
)

print(
    "BEARISH ENGULFING:",
    bearish_engulfing(df)
)

print(
    "DOJI:",
    detect_doji(df)
)

print(
    "HAMMER:",
    detect_hammer(df)
)