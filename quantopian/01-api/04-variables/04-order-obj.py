

def initialize(context):

    context.us_stock = symbol('VTI')



def handle_data(context, data):

    o_object = order(symbol('AAPL'), 5)

    print get_order(o_object).status
    print get_order(o_object).created
    print get_order(o_object).stop
    print get_order(o_object).limit
    print get_order(o_object).amount
    print get_order(o_object).sid
    print get_order(o_object).filled
    print get_order(o_object).stop_reached
    print get_order(o_object).limit_reached
    print get_order(o_object).commission
    print 'end'


