
def initialize(context):
    pass

def before_trading_start(context):
    context.fundamentals = get_fundamentals(
        query(
            fundamentals.asset_classification.value_score
        )
        .filter(
            # none
        )
        .order_by(
            fundamentals.valuation.market_cap.desc()
        )
        .limit(10)  # Limits results to 10
    )
    print type(context.fundamentals) # Returns Pandas DataFrame
    print type(context.fundamentals.columns)  # Returns Pandas index
    print type(context.fundamentals.columns.values)  # Returns Numpy arry
    
    update_universe(context.fundamentals.columns.values)  # Update our universe with query


def handle_data(context, data):
    for stock in data:
        order(stock, 10)
        # Performed amazing