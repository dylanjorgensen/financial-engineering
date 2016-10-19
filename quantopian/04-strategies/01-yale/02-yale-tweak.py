# 20% US Stocks [VTI, 0.05%]
# 10% International Stocks, Developed Market [VEA, 0.12%]
# 10% International Stocks from Emerging Markets [VWO, 0.18%]
# 10% Treasury Inflation Protected Securities (TIPS)  [TIP, 0.02%]
# 7% US Treasury Bonds [TLT, 0.15%]
# 9% US Real Estate [VNQ, 0.10%]
# 7% Foreign Real Estate [VNQI, 0.32%]
# 9% Commodities [DBC, 0.87%]

# 10% Global Stocks [VT, 0.19%]
# 4% US Total Bond Market [BND, 0.10%]
# 4% Gold [GLD, .40%]



def initialize(context):
    set_symbol_lookup_date('2014-01-01')


def handle_data(context, data):


    # Buy by order target percent
    order_target_percent(symbol('VTI'), 0.20)
    order_target_percent(symbol('VEA'), 0.10)
    order_target_percent(symbol('VWO'), 0.10)
    order_target_percent(symbol('TIP'), 0.10)
    order_target_percent(symbol('TLT'), 0.07)
    order_target_percent(symbol('VNQ'), 0.09)
    order_target_percent(symbol('VNQI'), 0.07)
    order_target_percent(symbol('DBC'), 0.09)

    order_target_percent(symbol('VT'), 0.10)
    order_target_percent(symbol('BND'), 0.04)
    order_target_percent(symbol('GLD'), 0.04)

    log.info(context.account.total_positions_value)
    
    
    
