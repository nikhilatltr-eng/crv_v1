import asyncio

from exchange.market_data import (
    get_ohlcv
)

from strategies.signal_engine import (
    generate_signal
)

from telegram_bot import (
    send_message
)

from ai.trade_memory import (
    save_trade
)

from ai.trade_journal import (
    log_trade
)


async def run_bot():

    print()
    print("crv_v1 LIVE BOT STARTED")
    print()

    while True:

        try:

            df = get_ohlcv()

            signal = generate_signal(df)

            message = f"""
CRV AI SIGNAL

SIGNAL: {signal['signal']}

CONFIDENCE: {signal['confidence']}%

ENTRY: {signal['entry']}

STOP LOSS: {signal['stop_loss']}

TAKE PROFIT: {signal['take_profit']}

RISK REWARD: {signal['risk_reward']}

1M BIAS: {signal['bias_1m']}
5M BIAS: {signal['bias_5m']}
15M BIAS: {signal['bias_15m']}

MARKET STRUCTURE:
{signal['market_structure']}

ORDER FLOW:
{signal['order_flow']}

WHALE ACTIVITY:
{signal['whale_activity']}

LIQUIDITY:
{signal['liquidity_sweep']}

FVG:
{signal['fvg_signal']}

ORDER BLOCK:
{signal['order_block']}

STRUCTURE:
{signal['structure_signal']}

CVD:
{signal['cvd_bias']}

MARKET REGIME:
{signal['market_regime']}

SNIPER ENTRY:
{signal['sniper_entry']}

REASONS:
{signal['reasons']}
"""

            print(message)

            log_trade(signal)

            if signal["signal"] != "NO TRADE":

                save_trade(signal)

                await send_message(message)

            await asyncio.sleep(60)

        except Exception as e:

            print()
            print("ERROR:")
            print(e)

            await asyncio.sleep(10)


asyncio.run(run_bot())