# 25% US Stocks [VTI, 0.05%]
# 14% International Stocks, Developed Market [VEA, 0.12%]
# 14% International Stocks from Emerging Markets [VWO, 0.18%]
# 15% Treasury Inflation Protected Securities (TIPS)  [TIP, 0.02%]
# 7% US Treasury Bonds [TLT, 0.15%]
# 9% US Real Estate [VNQ, 0.10%]
# 7% Foreign Real Estate [VNQI, 0.32%]
# 9% Commodities [DBC, 0.87%]

def initialize(context):
    pass


def handle_data(context, data):


    # Buy by order target percent
    order_target_percent(symbol('VTI'), 0.25)
    order_target_percent(symbol('VEA'), 0.14)
    order_target_percent(symbol('VWO'), 0.14)
    order_target_percent(symbol('TIP'), 0.15)
    order_target_percent(symbol('TLT'), 0.07)
    order_target_percent(symbol('VNQ'), 0.09)
    order_target_percent(symbol('VNQI'), 0.07)
    order_target_percent(symbol('DBC'), 0.09)
    
    log.info(context.account.total_positions_value)
    
    
    
