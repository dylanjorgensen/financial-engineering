
# Put any initialization logic here.  The context object will be passed to
# the other methods in your algorithm.


def preview(df):
    log.info(df.head())
    return df


def initialize(context):
    # This is keep our invenstments down to 10% of the total
    context.investment_size = (context.portfolio.cash / 10.0)
    # This sets a number we can use to as a percent for stop loss
    context.stop_loss_pct = 0.995
    # This acounts for how different companies had the same symbol
    set_symbol_lookup_date('2012-10-01')
    # pre_func lets youspecify the log function
    fetch_csv('http://sentdex.com/api/finance/sentiment-signals/sample/', pre_func = preview)


# Will be called on every trade event for the securities you specify.
def handle_data(context, data):
    pass