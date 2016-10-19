

# !!! When trading live initialize will run every day !!!

# Required: Called once at the very beginning of a backtest,
# use this method to set up any bookkeeping
def initialize(context):

    # context is a dict that contains your working variables
    print context


# Optional: Called daily prior to the open of market. Orders cannot be placed inside this method.
def before_trading_start(context):
    print context


# Required: Runs on every time stop (day or minute)
def handle_data(context, data):

    # data is a dict containing your universe of stock info
    # Market information about each security and transforms are all available in this object.
    print data

    # An order is required to run backtest
    order(symbol('goog'), 1)

