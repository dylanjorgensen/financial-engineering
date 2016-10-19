def initialize(context):
    pass


def handle_data(context, data):

    # Buy by share quantity
    order(symbol('goog'), 1)  # Positive means buy
    order(symbol('goog'), -1)  # Negative means sell

    # Buy by dollars willing to spend
    order_value(symbol('AAPL'), 1000)  #  If price of AAPL is $105 a share, this would buy 9 shares

    # Buy by portfiolio percent
    order_percent(symbol('AAPL'), .15)  # Will spend .15% of total portfolio

    # Buys or sells to adjust to targe
    order_target(security, amount, style=OrderType)

    # Buy by order target percent
    order_target_percent(symbol('AAPL'), 0.1)

    
    
    
    
    
    