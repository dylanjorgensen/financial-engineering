# Sendex Tutorial
# https://www.youtube.com/watch?list=PLQVvvaa0QuDeN06s5ervxTfTcVvt-xpZN&t=428&v=vkD4iKpXYbk


def preview(df):
    log.info(df.head())
    return df


def initialize(context):
    # This is keep our invenstments down to 10% of the total
    context.investment_size = (context.portfolio.cash / 10.0)
    # This sets a number we can use to as a percent for stop loss
    context.stop_loss_pct = 0.995

    context.shorting = True

    # This acounts for how different companies had the same symbol
    set_symbol_lookup_date('2012-10-01')
    # pre_func lets youspecify the log function
    fetch_csv('http://sentdex.com/api/finance/sentiment-signals/sample/', pre_func = preview)
    # Choose specfic 255 stocks to track
    context.stocks = symbols('AAPL', 'MCD', 'FB', 'GME', 'INTC', 'SBUX', 'T', 'MGM', 'SHLD', 'NKE', 'NFLX', 'PFE', 'GS', 'TGT', 'NOK', 'SNE', 'TXN', 'JNJ', 'KO', 'VZ', 'XOM', 'WMT', 'MCO', 'TWTR', 'URBN', 'MCP', 'MSFT', 'HD', 'KSS', 'AMZN', 'S', 'BA', 'F', 'JPM', 'QCOM', 'TSLA', 'YHOO', 'BBRY', 'GM', 'IBM', 'C', 'ZNGA', 'BAC', 'DIS', 'SCHW', 'UA', 'CSCO', 'ORCL', 'SYMC', 'WFC', 'TM', 'EBAY', 'SCHL', 'MS', 'NDAQ', 'TIF', 'AIG', 'DAL', 'JCP', 'MRK', 'CA', 'SIRI', 'AMD', 'CVX', 'FSLR', 'LMT', 'P', 'CBS', 'TWX', 'PEP', 'LNKD', 'CMG', 'NVDA', 'BBY', 'TWC', 'M', 'RHT', 'ACN', 'CRM', 'PETS', 'CELG', 'BLK', 'GD', 'DOW', 'YUM', 'GE', 'MA', 'DTV', 'DDD', 'CAT', 'FDX', 'GRPN', 'ACE', 'BK', 'GILD', 'V', 'DUK', 'FFIV', 'WFM', 'CVS', 'UNH', 'LUV', 'CBG', 'AFL', 'CHK', 'BRCM', 'HPQ', 'LULU', 'ATVI', 'RTN', 'EMC', 'NOC', 'MAR', 'X', 'BMY', 'LOW', 'COST', 'HON', 'SPLS', 'BKS', 'AA', 'AXP', 'AMGN', 'GPS', 'MDT', 'LLY', 'CME', 'MON', 'WWWW', 'MU', 'DG', 'TRIP', 'HAL', 'COH', 'WYNN', 'PCLN', 'HTZ', 'CLF', 'DD', 'ACI', 'FCX', 'AON', 'GMCR', 'CSX', 'ADBE', 'PRU', 'PG', 'MYL', 'STT', 'PPG', 'EXPE', 'KORS', 'JNPR', 'UTX', 'HOT', 'SNDK', 'CCL', 'DRI', 'BIIB', 'MHFI', 'BBT', 'APA', 'A', 'TDC', 'ANF', 'MTB', 'PPL', 'ABT', 'GNW', 'KMI', 'MET', 'FE', 'DVA', 'ETFC', 'GLW', 'NRG', 'INTU', 'KR', 'ARNA', 'VALE', 'MSI', 'EOG', 'AET', 'MAT', 'HST', 'COP', 'MO', 'IVZ', 'HUM', 'NUE', 'CI')

# Will be called on every trade event for the securities you specify.
def handle_data(context, data):
    cash = context.portfolio.cash

    try:
        for s in data:
            # Because we want to know if we have a value fetched
            if 'sentament_signal' in data[s]:

                # Sets the sentament
                sentament = data[s]['sentament_signal']

                # Because we need to know if we have a position in this company yet
                current_position = context.portfolio.positions.amount
                current_price = data[s].price


                # --- Begin Long Logic --- #
                # Because we only want to invest is high sentament companies
                if (sentament > 5) and (current_position == 0):
                    # Because we to check if we have enough cash
                    if cash > context.investment_size:

                        # Because we to check if we have enough cash
                        order_value(s, context.investment_size, style=StopOrder(context.stop_loss_pct*current_price))
                        cash -= context.investment_size

                elif (sentament <= 1) and (current_position > 0):
                    order_target(s, 0)



                # --- Begin shorting Logic --- #
                # We want to use shorting to lower beta
                # Reminder: We are inside a for loop so this is per stock
                if context.shorting == True:

                    ma1 = data[s].mavg(100)
                    ma2 = data[s].mavg(300)

                    # Because we want to sell -3 stocks that we have
                    if (sentament <= -3) and (current_position) == 0:
                        # Compare the short moving average to see if it's below the long one.
                        if ma2 > ma1:

                            #
                            if cash > context.investment_size:
                                order_value(s, -context.investment_size)
                                context.shorts.append(s)

                    elif (sentament >= -1) and (current_position > 0) and s in context.shorts:
                        order_target(s,0)
                        context.shorts.remove(s)

















    except Exception as e:
        print(str(e))














