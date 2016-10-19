# Sendex Tutorial
# https://www.youtube.com/watch?v=_nMoCsPI-IA&list=PLQVvvaa0QuDeN06s5ervxTfTcVvt-xpZN&index=2

# Quantopian Fundamentals List
# https://www.quantopian.com/help/fundamentals

# SQL Alchemy Syntax
# http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html#querying

# Morningstar Vairables
# https://www.quantopian.com/help/fundamentals#general-profile



def initialize(context):
    context.limit = 10  # Limits amount of stocks (Limit is 255)


# The before_trading_start method is called once per day prior to market open.
# It can be used to create a universe of securities using fundamental data
def before_trading_start(context):

    # get_fundamentals(query, filter_ordered_nulls)
    context.fundamental_df = get_fundamentals(
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

    # Updates universal data to use within handle_date() method
    update_universe(context.fundamental_df.columns.values)


def handle_data(context, data):

    # # Learn about returned DataFrame
    # print context.fundamental_df
    # print context.fundamental_df.info()
    
    
    for stock in data:
        print context.portfolio.positions[stock].amount
        print data[stock].price
        print context.fundamental_df[stock]['pe_ratio']
        print 'end'