from ai.predictor import predict_signal

from strategies.smart_money import (
    analyze_market_structure
)

from strategies.liquidity_sweep import (
    detect_liquidity_sweep
)

from strategies.candles import (
    detect_candle_pattern
)

from strategies.sniper_entry import (
    detect_sniper_entry
)

from strategies.fvg import (
    detect_fvg
)

from strategies.order_blocks import (
    detect_order_block
)

from strategies.bos_choch import (
    detect_bos_choch
)

from strategies.cvd import (
    calculate_cvd
)

from strategies.regime_filter import (
    detect_market_regime
)

from exchange.order_flow import (
    analyze_order_flow,
    detect_whale_activity
)

from exchange.market_data import (
    get_ohlcv
)


def timeframe_bias(timeframe):

    df = get_ohlcv(
        timeframe=timeframe
    )

    signal = predict_signal(df)

    return signal["side"]


def generate_signal(df):

    prediction = predict_signal(df)

    market_structure = (
        analyze_market_structure(df)
    )

    liquidity_sweep = (
        detect_liquidity_sweep(df)
    )

    candle_pattern = (
        detect_candle_pattern(df)
    )

    sniper_data = (
        detect_sniper_entry(
            df,
            prediction["side"]
        )
    )

    fvg_signal = (
        detect_fvg(df)
    )

    order_block = (
        detect_order_block(df)
    )

    structure_signal = (
        detect_bos_choch(df)
    )

    order_flow = (
        analyze_order_flow()
    )

    cvd_data = calculate_cvd(
        order_flow["recent_trades"]
    )

    market_regime = (
        detect_market_regime(df)
    )

    whale_activity = detect_whale_activity(
        order_flow["recent_trades"]
    )

    bias_1m = timeframe_bias("1m")

    bias_5m = timeframe_bias("5m")

    bias_15m = timeframe_bias("15m")

    latest = df.iloc[-1]

    current_price = round(
        latest["close"],
        6
    )

    atr = latest["atr"]

    volatility = latest["volatility"]

    signal = prediction["side"]

    confidence = float(
        prediction["confidence"]
    )

    reasons = []

    alignment_score = 0

    if bias_1m == signal:
        alignment_score += 1

    if bias_5m == signal:
        alignment_score += 1

    if bias_15m == signal:
        alignment_score += 1

    confidence += alignment_score * 4

    if sniper_data["sniper_entry"]:

        confidence += 15

        reasons.append(
            sniper_data["sniper_reason"]
        )

    if (
        signal == "LONG"
        and fvg_signal ==
        "BULLISH_FVG"
    ):

        confidence += 10

        reasons.append(
            "Bullish FVG"
        )

    elif (
        signal == "SHORT"
        and fvg_signal ==
        "BEARISH_FVG"
    ):

        confidence += 10

        reasons.append(
            "Bearish FVG"
        )

    if (
        signal == "LONG"
        and order_block ==
        "BULLISH_ORDER_BLOCK"
    ):

        confidence += 12

        reasons.append(
            "Bullish Order Block"
        )

    elif (
        signal == "SHORT"
        and order_block ==
        "BEARISH_ORDER_BLOCK"
    ):

        confidence += 12

        reasons.append(
            "Bearish Order Block"
        )

    if (
        signal == "LONG"
        and structure_signal in [
            "BULLISH_BOS",
            "BULLISH_CHOCH"
        ]
    ):

        confidence += 12

        reasons.append(
            structure_signal
        )

    elif (
        signal == "SHORT"
        and structure_signal in [
            "BEARISH_BOS",
            "BEARISH_CHOCH"
        ]
    ):

        confidence += 12

        reasons.append(
            structure_signal
        )

    if (
        signal == "LONG"
        and cvd_data["cvd_bias"]
        == "BULLISH"
    ):

        confidence += 10

        reasons.append(
            "Bullish CVD"
        )

    elif (
        signal == "SHORT"
        and cvd_data["cvd_bias"]
        == "BEARISH"
    ):

        confidence += 10

        reasons.append(
            "Bearish CVD"
        )

    if market_regime == "TRENDING":

        confidence += 10

        reasons.append(
            "Trending market"
        )

    elif market_regime == "SIDEWAYS":

        confidence -= 4

        reasons.append(
            "Sideways market"
        )

    if volatility < atr * 0.3:

        confidence -= 2

        reasons.append(
            "Low volatility"
        )

    if (
        signal == "LONG"
        and order_flow["imbalance"]
        == "BULLISH"
    ):

        confidence += 8

    elif (
        signal == "SHORT"
        and order_flow["imbalance"]
        == "BEARISH"
    ):

        confidence += 8

    if whale_activity in [

        "WHALE_ACCUMULATION",
        "WHALE_DISTRIBUTION"

    ]:

        confidence += 5

    if (
        bias_1m != prediction["side"]
        and bias_5m != prediction["side"]
    ):

        confidence -= 5

        reasons.append(
            "Timeframe conflict"
        )

    confidence = max(
        0,
        min(confidence, 100)
    )

    minimum_confidence = 42

    if confidence < minimum_confidence:

        signal = "NO TRADE"

        reasons.append(
            "Confidence below threshold"
        )

    if (
        market_regime == "SIDEWAYS"
        and confidence < 35
    ):

        signal = "NO TRADE"

        reasons.append(
            "Weak sideways market"
        )

    if signal == "LONG":

        entry = current_price

        stop_loss = round(
            entry - atr * 1.5,
            6
        )

        take_profit = round(
            entry + atr * 3,
            6
        )

    elif signal == "SHORT":

        entry = current_price

        stop_loss = round(
            entry + atr * 1.5,
            6
        )

        take_profit = round(
            entry - atr * 3,
            6
        )

    else:

        entry = None

        stop_loss = None

        take_profit = None

    rr = 2.0

    return {

        "signal": signal,

        "confidence": round(
            confidence,
            2
        ),

        "market_structure":
            market_structure,

        "liquidity_sweep":
            liquidity_sweep,

        "candle_pattern":
            candle_pattern,

        "sniper_entry":
            sniper_data["sniper_entry"],

        "sniper_reason":
            sniper_data["sniper_reason"],

        "fvg_signal":
            fvg_signal,

        "order_block":
            order_block,

        "structure_signal":
            structure_signal,

        "cvd_bias":
            cvd_data["cvd_bias"],

        "cvd_value":
            cvd_data["cvd_value"],

        "market_regime":
            market_regime,

        "order_flow":
            order_flow["imbalance"],

        "whale_activity":
            whale_activity,

        "entry": entry,

        "stop_loss": stop_loss,

        "take_profit": take_profit,

        "risk_reward": rr,

        "bias_1m": bias_1m,

        "bias_5m": bias_5m,

        "bias_15m": bias_15m,

        "reasons": reasons
    }