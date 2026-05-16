from exchange.market_data import (
    get_ohlcv
)

from indicators.trend import (
    apply_indicators
)

from indicators.volatility import (
    apply_volatility
)

from ai.feature_engineering import (
    prepare_features
)

from strategies.signal_engine import (
    generate_signal
)

df = get_ohlcv()

df = apply_indicators(df)

df = apply_volatility(df)

df = prepare_features(df)

signal = generate_signal(df)

print()

print(
    "LIVE AI SIGNAL"
)

print()

print(signal)