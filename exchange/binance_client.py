from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv(
    "BINANCE_API_KEY"
)

SECRET_KEY = os.getenv(
    "BINANCE_SECRET_KEY"
)

client = Client(
    API_KEY,
    SECRET_KEY,
    requests_params={
        "timeout": 30
    }
)

def get_price():

    ticker = client.futures_symbol_ticker(
        symbol="CRVUSDT"
    )

    return ticker["price"]