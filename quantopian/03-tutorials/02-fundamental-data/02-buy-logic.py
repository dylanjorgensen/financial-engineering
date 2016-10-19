


def initialize(context):
    context.limit = 10  # Limits amount of stocks (Limit is 255)


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
        plausible_investment = cash / 10.0

        share_amount = int(plausible_investment / stock_price)

        try:
            if stock_price < plausible_investment:
                if current_position == 0:
                    if context.fundamentals[stock]['pe_ratio'] < 11:
                        order(stock, share_amount)

        except Exception as e:
            print (str(e))


