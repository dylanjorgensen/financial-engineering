
def initialize(context):
    pass

def handle_data(context, data):

    # Gets our cash on hand and current positions
    cash = context.portfolio.cash
    current_position = context.portfolio.positions

    for stock in data:

        # Checks to see if we are currently invested in each stock
        current_position = context.portfolio.positions[stock].amount

        # Because we want a simple var for the current stock price
        stock_price = data[stock].price

        # Because we want our cash distibuted equally
        plausible_investment = cash / context.limit

        # Because we want to cut our losses if it's going down.
        stop_price = stock_price - (stock_price*0.005)

        # Because a whole number for how much of each stock we can buy
        share_amount = int(plausible_investment / stock_price)

        try:
            # Because we need to have at least enough money to buy one share
            if stock_price < plausible_investment:

                # Because we only want to buy it if we don't have it yet
                if current_position == 0:
                    order(stock, share_amount, style=StopOrder(stop_price))


        except Exception as e:
            print str(e)
