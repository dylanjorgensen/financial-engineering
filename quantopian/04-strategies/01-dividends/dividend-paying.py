# 10% - Equities of all types (CVY)
# 5% - Treasuries ETF: (BWX)
# 5% - Corporate Bonds: (VCIT)
# 5% - Muni Bonds: (MUB)
# 5% - TIPS: (TIP)
# 20% - US Dividend Paying Stocks
# - 5% - All US companies that keep raising dividends (PFM)
# - 5% - 50 companies paying the highest dividends now (PEY)
# - 5% - Dow Jones Best US Dividends Stocks (DVY)
# - 5% - Tracks dividends with highest yield (DHS)
# 10% - International Paying Stocks
# - 5% History of raising dividends (PID)
# - 5% Tracks companies paying highest dividend  (DTH)
# 10% - Utilities
# - 5% - US Utilities: (VPU)
# - 5% - Foreign Utilities: (IPU)
# 10% - REIT’s
# - 7% - US REIT: (VNQ)
# - 3% - Foreign REIT
# - - 1% - (RWX)
# - - 1% - (WPS)
# - - 1% - (DRW)
# 5% - Canadian Foreign Trust: (ENY)
# 5% - MLPs: (TYG)
# 5% - Preferred Stock
# - 2.5% (PFF)
# - 2.5% (PGF)
# 5% - BDC (PSP)




def initialize(context):
    set_symbol_lookup_date('2014-01-01')


def handle_data(context, data):

    record(Dividends = context.portfolio.cash)

    record(Positions_Value = context.portfolio.positions_value)

    # Remember to set backtesting totals to $100,0000
    if context.portfolio.cash > 95000.0:


        # 2014, 1 year test
        # Dividends = $1,649
        # Positions_Value = $112,213

        # 2010, 5 year test
        # Dividens = $11,196
        # Position_Value = $182,826

        #order_target_percent(symbol('SPY'), 1.0)


        # --- Break --- #

        # 2014, 1 year test
        # Dividends = $3,581
        # Positions_Value = $104,868

        # 2010, 5 year test
        # Dividens = 18,482
        # Position_Value = $134,192
        order_target_percent(symbol('BWX'), 0.05)
        order_target_percent(symbol('VCIT'), 0.05)
        order_target_percent(symbol('MUB'), 0.05)
        order_target_percent(symbol('TIP'), 0.05)

        order_target_percent(symbol('PFM'), 0.10)
        order_target_percent(symbol('PEY'), 0.10)
        order_target_percent(symbol('DVY'), 0.05)
        order_target_percent(symbol('DHS'), 0.05)

        order_target_percent(symbol('PID'), 0.05)
        order_target_percent(symbol('DTH'), 0.05)

        order_target_percent(symbol('VPU'), 0.05)
        order_target_percent(symbol('IPU'), 0.05)

        order_target_percent(symbol('VNQ'), 0.07)
        order_target_percent(symbol('RWX'), 0.01)
        order_target_percent(symbol('WPS'), 0.01)
        order_target_percent(symbol('DRW'), 0.01)

        order_target_percent(symbol('ENY'), 0.05)
        order_target_percent(symbol('TYG'), 0.05)

        order_target_percent(symbol('PFF'), 0.025)
        order_target_percent(symbol('PGF'), 0.025)

        order_target_percent(symbol('PSP'), 0.05)








