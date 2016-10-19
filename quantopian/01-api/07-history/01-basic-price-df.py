def initialize(context):

    # Adds stocks to the current usable universe (Automaticly found by history)
    context.stocks = symbols('XLY',  # XLY Consumer Discrectionary SPDR Fund
                           'XLF',  # XLF Financial SPDR Fund
                           'XLU')  # XLU Utilities SPRD Fund



def handle_data(context, data):

    # History returns pandas DataFrame
    # Parmiters
    # - bar_count = days (or minutes) of past data to return
    # - frequency = '1d' or '1m'
    # - field = 'price', 'open_price', 'high', 'low', 'close_price', 'price,volume'
    prices = history(bar_count = 100, frequency = '1d', field = 'price')
    print prices.head()


