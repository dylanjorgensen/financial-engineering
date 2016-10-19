
def initialize(context):
    pass


def handle_data(context, data):


    # Buy by order target percent
    order_target_percent(symbol('SPY'), 1.0)

    log.info(context.account.total_positions_value)



