# When backtesting, you can create time series charts by using the record method
# and passing series names and corresponding values using keyword arguments.
# Up to five series can be recorded and charted. Recording is done at day-level granularity.



def initialize(context):
    pass

def handle_data(context, data):

    # Plot the 20-day moving average for MSFT and AAPL
    record(msft_mavg=data[symbol('MSFT')].mavg(20), aapl_mavg=data[symbol('AAPL')].mavg(20))


    # Plot two moving averages
    MA1 = data[context.security].mavg(50)
    MA2 = data[context.security].mavg(200)
    record(Moving_Average_1 = MA1, Moving_Average_2 = MA2)