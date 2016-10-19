
def initialize(context):


    # Long Only:
    # Prevents us from holding negative shares of any security.
    set_long_only()

    # Maximum Order Count:
    # Algorithm will raise an exception if more than 50 orders are placed in a day
    set_max_order_count(50)

    # Maximum Order Size:
    # Algorithm will raise an exception if we attempt to order more than
    # 10 shares or 1000 dollars worth of AAPL in a single order.
    set_max_order_size(symbol('AAPL'), max_shares=10, max_notional=1000.0)

    # Maximum Position Size:
    # Algorithm will raise an exception if we attempt to hold more than
    # 30 shares or 2000 dollars worth of AAPL.
    set_max_position_size(symbol('AAPL'), max_shares=30, max_notional=2000.0)



def handle_data(context,data):
    order(symbol('AAPL'), 5)