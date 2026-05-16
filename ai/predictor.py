import joblib

import pandas as pd


model = joblib.load(
    "models/xgb_model.pkl"
)


def predict_signal(df):

    latest = df.iloc[-1]

    features = pd.DataFrame([{

        "ema20":
        latest["ema20"],

        "ema50":
        latest["ema50"],

        "rsi":
        latest["rsi"],

        "macd":
        latest["macd"],

        "macd_signal":
        latest["macd_signal"],

        "atr":
        latest["atr"],

        "returns":
        latest["returns"],

        "volume_delta":
        latest["volume_delta"],

        "buy_pressure":
        latest["buy_pressure"],

        "sell_pressure":
        latest["sell_pressure"],

        "imbalance":
        latest["imbalance"],

        "cvd":
        latest["cvd"],

        "volatility":
        latest["volatility"]
    }])

    prediction = model.predict(
        features
    )[0]

    probabilities = model.predict_proba(
        features
    )[0]

    confidence = max(
        probabilities
    ) * 100

    if prediction == 2:

        side = "LONG"

    elif prediction == 0:

        side = "SHORT"

    else:

        side = "NO TRADE"

    return {

        "side": side,

        "confidence": round(
            confidence,
            2
        )
    }