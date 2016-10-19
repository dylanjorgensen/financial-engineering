

def initialize(context):
    pass




def handle_data(context, data):

    print context.portfolio.capital_used
    print context.portfolio.cash
    print context.portfolio.pnl
    print context.portfolio.portfolio_value
    print context.portfolio.positions
    print context.portfolio.positions_value
    print context.portfolio.returns
    print context.portfolio.starting_cash
    print context.portfolio.start_date
    print 'end'

    order(symbol('AAPL'),5)

