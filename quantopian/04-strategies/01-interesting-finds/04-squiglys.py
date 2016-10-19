
# Strategy
# The more the market moves up and down the more you make, the more it stays smooth the less you make.
# Another note about this is that I believe we will have many exponential growth industries and there should traid well against them.



def initialize(context):
    context.stocks = symbols('XLY',  # XLY Consumer Discrectionary SPDR Fund
                           'XLF',  # XLF Financial SPDR Fund
                           'XLK',  # XLK Technology SPDR Fund
                           'XLE',  # XLE Energy SPDR Fund
                           'XLV',  # XLV Health Care SPRD Fund
                           'XLI',  # XLI Industrial SPDR Fund
                           'XLP',  # XLP Consumer Staples SPDR Fund
                           'XLB',  # XLB Materials SPDR Fund
                           'XLU')  # XLU Utilities SPRD Fund





def handle_data(context, data):

    for stock in context.stocks:
        ma1 = data[stock].mavg(50)
        ma2 = data[stock].mavg(200)

        price = data[stock].price

        if ma1 > ma2:
            order_target_percent(stock, 0.11)
        elif ma1 < ma2:
            order_target_percent(stock, -0.11)














    