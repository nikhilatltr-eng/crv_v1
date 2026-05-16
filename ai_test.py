from exchange.market_data import (
    get_ohlcv
)

from ai.feature_engineering import (
    create_features
)

df = get_ohlcv()

df = create_features(df)

print(df.tail())

print()

print(df.columns)