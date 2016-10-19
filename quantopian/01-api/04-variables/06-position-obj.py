

def initialize(context):

    context.us_stock = symbol('VTI')




def handle_data(context, data):

    print context.portfolio.positions[symbol('AAPL')].amount
    print context.portfolio.positions[symbol('AAPL')].cost_basis
    print context.portfolio.positions[symbol('AAPL')].last_sale_price
    print context.portfolio.positions[symbol('AAPL')].sid
    print 'end'

    order(symbol('AAPL'),5)
