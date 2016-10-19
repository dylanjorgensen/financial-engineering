

def initialize(context):
    pass




def handle_data(context, data):

    print context.account.accrued_interest
    print context.account.available_funds
    print context.account.buying_power
    print context.account.cushion
    print context.account.day_trades_remaining
    print context.account.equity_with_loan
    print context.account.excess_liquidity
    print context.account.initial_margin_requirement
    print context.account.leverage
    print context.account.maintenance_margin_requirement
    print context.account.net_leverage
    print context.account.net_liquidation
    print context.account.regt_equity
    print context.account.regt_margin
    print context.account.settled_cash
    print context.account.total_positions_value
    print 'end'

    order(symbol('AAPL'),5)
