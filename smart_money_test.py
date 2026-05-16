from exchange.market_data import get_ohlcv

from strategies.smart_money import (
    detect_market_structure,
    detect_liquidity_sweep
)

df = get_ohlcv()

structure = detect_market_structure(df)

sweep = detect_liquidity_sweep(df)

print("MARKET STRUCTURE:", structure)

print("LIQUIDITY:", sweep)