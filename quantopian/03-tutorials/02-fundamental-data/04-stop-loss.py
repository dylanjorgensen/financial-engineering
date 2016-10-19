def initialize(context):
    context.limit = 10  # Limits amount of stocks (Limit is 255)

    schedule_function(rebalance,
                      date_rule=date_rules.every_day(), # date_rules has methods
                      time_rule=time_rules.market_open())  # Also market_close

def rebalance(context, data):
     for stock in context.portfolio.positions:
            order_target_percent(stock, 0)



def before_trading_start(context):
    context.fundamentals = get_fundamentals(
        query(
            fundamentals.valuation_ratios.pb_ratio,  # Did not find with autocomplete
            fundamentals.valuation_ratios.pe_ratio,  # Information is in documentation
        )
        .filter(
            fundamentals.valuation_ratios.pe_ratio < 14,
        )
        .filter(
            fundamentals.valuation_ratios.pb_ratio < 2,
        )
        .order_by(
            fundamentals.valuation.market_cap.desc()  # Orders by large market cap
        )
        .limit(context.limit)
    )
    update_universe(context.fundamentals.columns.values)  # Update our universe with query


def handle_data(context, data):
    cash = context.portfolio.cash
    current_position = context.portfolio.positions

    for stock in data:
        current_position = context.portfolio.positions[stock].amount
        stock_price = data[stock].price
        plausible_investment = cash / context.limit
        stop_price = stock_price - (stock_price*0.005)

        share_amount = int(plausible_investment / stock_price)

        try:
            if stock_price < plausible_investment:
                if current_position == 0:
                    if context.fundamentals[stock]['pe_ratio'] < 11:
                        order(stock, share_amount, style=StopOrder(stop_price))

        except Exception as e:
            print (str(e))





