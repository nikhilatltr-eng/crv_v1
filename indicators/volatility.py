import pandas_ta as ta

def apply_volatility(df):

    # ATR

    df["atr"] = ta.atr(
        df["high"],
        df["low"],
        df["close"],
        length=14
    )

    # Bollinger Bands

    bb = ta.bbands(df["close"])

    print(bb.columns)

    df["bb_lower"] = bb.iloc[:, 0]

    df["bb_middle"] = bb.iloc[:, 1]

    df["bb_upper"] = bb.iloc[:, 2]

    # Supertrend

    st = ta.supertrend(
        df["high"],
        df["low"],
        df["close"],
        length=10,
        multiplier=3
    )

    df["supertrend"] = st.iloc[:, 0]

    return df