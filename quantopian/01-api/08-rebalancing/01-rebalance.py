# Because sometimes you want to sell stock to get to a specific balance

def initialize(context):
    context.limit = 10  # Limits amount of stocks (Limit is 255)

    schedule_function(rebalance,
                      date_rule=date_rules.every_day(), # date_rules has methods
                      time_rule=time_rules.market_open(minutes=1))  # Also market_close

def rebalance(context, data):
     for stock in context.portfolio.positions:
            order_target_percent(stock, 0)



def before_trading_start(context):

    # get_fundamentals(query, filter_ordered_nulls)
    context.fundamentals  = get_fundamentals(
        query(
            fundamentals.balance_sheet.policy_loans
        )
        .filter(
            fundamentals.balance_sheet.policy_loans != 0
        )
        .order_by(
            fundamentals.balance_sheet.policy_loans.desc()
        )
        .limit(context.limit)
    )
    update_universe(context.fundamentals.columns.values)


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

        # Because a whole number for how much of each stock we can buy
        share_amount = int(plausible_investment / stock_price)

        try:
            # Because we need to have at least enough money to buy one share
            if stock_price < plausible_investment:

                # Because we only want to buy it if we don't have it yet
                if current_position == 0:
                    order(stock, share_amount)


        except Exception as e:
            print str(e)







