import pandas as pd

from xgboost import XGBClassifier

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

import joblib

from ta.trend import EMAIndicator, MACD

from ta.momentum import RSIIndicator

from ta.volatility import AverageTrueRange

from exchange.market_data import get_ohlcv


print("DOWNLOADING DATA...")

df = get_ohlcv(limit=1500)

df["ema20"] = EMAIndicator(df["close"], window=20).ema_indicator()

df["ema50"] = EMAIndicator(df["close"], window=50).ema_indicator()

df["rsi"] = RSIIndicator(df["close"], window=14).rsi()

macd = MACD(df["close"])

df["macd"] = macd.macd()

df["macd_signal"] = macd.macd_signal()

df["atr"] = AverageTrueRange(
    df["high"],
    df["low"],
    df["close"]
).average_true_range()

df["returns"] = df["close"].pct_change()

df["future"] = df["close"].shift(-5)

df["target"] = (
    df["future"] > df["close"]
).astype(int)

df = df.dropna()

features = [

    "ema20",

    "ema50",

    "rsi",

    "macd",

    "macd_signal",

    "atr",

    "returns"

]

X = df[features]

y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    shuffle=False
)

model = XGBClassifier(

    n_estimators=400,

    max_depth=10,

    learning_rate=0.03,

    subsample=0.9,

    colsample_bytree=0.9,

    random_state=42
)

print("TRAINING AI MODEL...")

model.fit(X_train, y_train)

preds = model.predict(X_test)

accuracy = accuracy_score(y_test, preds)

print()

print("SUPER AI MODEL ACCURACY:", round(accuracy * 100, 2), "%")

joblib.dump(model, "models/xgb_model.pkl")

print()

print("SUPER MODEL SAVED")