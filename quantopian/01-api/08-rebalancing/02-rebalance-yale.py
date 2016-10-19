def initialize(context):

    context.stocks = symbols('VTI',  # 25% US Stocks [VTI, 0.05%]
                             'VEA',  # 14% International Stocks, Developed Market [VEA, 0.12%]
                             'VEA',  # 14% International Stocks from Emerging Markets [VWO, 0.18%]
                             'VEA',  # 15% Treasury Inflation Protected Securities (TIPS)  [TIP, 0.02%]
                             'TLT',  # 7% US Treasury Bonds [TLT, 0.15%]
                             'VNQ',  # 9% US Real Estate [VNQ, 0.10%]
                             'VNQI',  # 7% Foreign Real Estate [VNQI, 0.32%]
                             'DBC')  # 9% Commodities [DBC, 0.87%]


    schedule_function(rebalance,
                      date_rule=date_rules.week_start(), # date_rules has methods
                      time_rule=time_rules.market_open(minutes=1))  # Also market_close

def rebalance(context, data):
     for stock in context.portfolio.positions:
            order_target_percent(stock, 10)

