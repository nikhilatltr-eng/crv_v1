from exchange.order_flow import (
    get_order_book
)

data = get_order_book()

print()

print(
    "ORDER FLOW ANALYSIS"
)

print()

print(
    "IMBALANCE:",
    data["imbalance"]
)

print()

print(
    "TOTAL BID VOLUME:",
    data["bid_volume"]
)

print(
    "TOTAL ASK VOLUME:",
    data["ask_volume"]
)

print()

print(
    "TOP BIDS:"
)

for bid in data["top_bids"]:

    print(bid)

print()

print(
    "TOP ASKS:"
)

for ask in data["top_asks"]:

    print(ask)