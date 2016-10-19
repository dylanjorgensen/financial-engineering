# I learned
# - Its important to notice if the symbol method has an 's' or not
# - If it does have an 's' you need to pass a list of symbols


def initialize(context):

    # Adding a symbol to context makes a data frame of stock information
    context.us_stock = symbol('VTI')
    #context.int_stocks = symbols('VEA', 'SPY')  # Notice the 's'

def handle_data(context, data):

    print data[context.us_stock].price

    # Required
    order(symbol('GOOG'), 1)


