
def initialize(context):
    pass


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
        .limit(3)
    )
    update_universe(context.fundamentals.columns.values)


def handle_data(context, data):
    for stock in data:
        print stock
        
        order(stock, 10)
        # Performed amazing