from exchange.market_data import get_ohlcv

df = get_ohlcv()

print(df.tail())