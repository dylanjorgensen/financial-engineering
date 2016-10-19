# I learned
# - data is an object full of dataframes, When you pass data the stock parameter you target one
# - The dataframe has the below options as columns and time steps as rows



def initialize(context):

    context.us_stock = symbol('VTI')
    
    

def handle_data(context, data):  
    
    print data[context.us_stock].close_price
    print data[context.us_stock].datetime
    print data[context.us_stock].high
    print data[context.us_stock].low
    print data[context.us_stock].mavg(2)
    print data[context.us_stock].open_price
    print data[context.us_stock].price
    print data[context.us_stock].returns()
    print data[context.us_stock].stddev(1)
    print data[context.us_stock].volume
    print data[context.us_stock].vwap(1)
    print 'end'
    