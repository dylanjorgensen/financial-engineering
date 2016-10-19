# https://www.youtube.com/playlist?list=PLQVvvaa0QuDeN06s5ervxTfTcVvt-xpZN

# Strategy: Simple Moving Average Crossover
# Moving averages are a range of averages plotted for each day. Ex. 20 days
# The crossover refers to when you take two averages. Ex. 20 day and 50 day and they cross over.


# Runs on initiation
def initialize(context):  # context is a dict with useful data
    context.security = symbol('SPY')
    # print context

# Runs on every timestep
def handle_data(context, data):  # data is a pandas DataFrame
    # print data
    MA1 = data[context.security].mavg(50)  # Applys moving average method
    MA2 = data[context.security].mavg(200)
    
    # Make some variables
    current_price = data[context.security].price
    current_positions = context.portfolio.positions[symbol('SPY')].amount
    cash = context.portfolio.cash
    
    if (MA1 > MA2) and current_positions == 0:
        number_of_shares = int(cash/current_price)
        order(context.security, number_of_shares)
        log.info('Buying Shares')
        
    elif (MA1 < MA2) and current_positions != 0:
        order_target(context.security, 0)
        log.info('Selling Shares')
        
    record(MA1 = MA1, MA2 = MA2, Price = current_price)
        
    