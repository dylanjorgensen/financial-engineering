

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

    print context.fundamentals












