import pandas as pd

import joblib

from xgboost import XGBClassifier

from sklearn.model_selection import (
    train_test_split
)

from sklearn.metrics import (
    accuracy_score
)


df = pd.read_csv(
    "data/crv_features.csv"
)

features = [

    "ema20",

    "ema50",

    "rsi",

    "macd",

    "macd_signal",

    "atr",

    "returns",

    "volume_delta",

    "buy_pressure",

    "sell_pressure",

    "imbalance",

    "cvd",

    "volatility"
]

X = df[features]

y = df["target"]

X_train, X_test, y_train, y_test = (
    train_test_split(

        X,
        y,

        test_size=0.2,

        shuffle=False
    )
)

model = XGBClassifier(

    n_estimators=200,

    max_depth=6,

    learning_rate=0.05
)

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

accuracy = accuracy_score(
    y_test,
    predictions
)

joblib.dump(
    model,
    "models/xgb_model.pkl"
)

print()

print(
    f"MODEL ACCURACY: {accuracy}"
)

print()

print(
    "MODEL TRAINED"
)