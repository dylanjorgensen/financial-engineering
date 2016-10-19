# 17% US Stocks [SPY]
# 17% US Stocks [QQQ]
# 13% US Stocks (Large Cap) [SCHV]
# 10% Foreign Total Market [IXUS]
# 10% Foreign Emerging Market [VWO]
#  9% Foreign Developed Market [FNDF]
#  9% Inflation Protected Bonds [STIP]
#  7% Investment Grade Bonds [AGG]


def initialize(context):
    set_symbol_lookup_date('2014-01-01')


def handle_data(context, data):


    # Buy by order target percent
    order_target_percent(symbol('SPY'), 0.17)
    order_target_percent(symbol('QQQ'), 0.17)
    order_target_percent(symbol('SCHV'), 0.13)
    order_target_percent(symbol('IXUS'), 0.10)
    order_target_percent(symbol('VWO'), 0.10)
    order_target_percent(symbol('FNDF'), 0.09)
    order_target_percent(symbol('STIP'), 0.09)
    order_target_percent(symbol('AGG'), 0.07)


    log.info(context.account.total_positions_value)
    
    
    
