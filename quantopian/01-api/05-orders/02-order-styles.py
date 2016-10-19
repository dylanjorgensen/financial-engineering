# https://www.youtube.com/watch?v=R7MQsTuBWQ8



def initialize(context):
    context.stock = symbol('GOOG')


def handle_data(context, data):

    # Market Order: order(security, amount)
    # Guarntees execution but not price (slipage)
    order(context.stock, 1)

    # Limit Order: order(security, amount, style=LimitOrder(price))
    # Guarntees price but order execution
    order(context.stock, 1, style=LimitOrder(499.99))

    # Stop "Market" Order (or stop-loss): order(security, amount, style=StopOrder(price))
    # Triggers a market order when the specified price is hit
    order(context.stock, 1, style=StopOrder(499.00))


    # Stop-Limit Order: order(security, amount, style=StopLimitOrder(limit_price, stop_price))
    # The order converts into a limit order at the first price and will only sell at the second price
    order(context.stock, 1, style=StopLimitOrder(520.00, 499.99))
    
    
    log.info("Google Price: " + str(data[context.stock].price))
    log.info("Total Shares: " + str(context.portfolio.positions[context.stock].amount))
    
    