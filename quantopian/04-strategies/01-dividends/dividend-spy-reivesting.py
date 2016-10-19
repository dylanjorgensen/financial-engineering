
def initialize(context):
    set_symbol_lookup_date('2014-01-01')


def handle_data(context, data):

    record(Dividends = context.portfolio.cash)

    record(Positions_Value = context.portfolio.positions_value)

    # # Remember to set backtesting totals to $100,0000
    # if context.portfolio.cash > 95000.0:

        # 2014, 1 year test
        # Dividends = $1,649
        # Positions_Value = $112,213

        # 2010, 5 year test
        # Dividens = $11,196
        # Position_Value = $182,826

        #order_target_percent(symbol('SPY'), 1.0)


        # --- Reivesting --- #


        # 2014, 1 year test
        # Dividends = $174
        # Positions_Value = $113,858

        # 2010, 5 year reinvesting test
        # Dividens = $115
        # Position_Value = $198,739

    order_target_percent(symbol('SPY'), 1.0)

