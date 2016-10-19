


# --- Buy As Many Shares as Cash Can Afford --- #
cash = context.portfolio.cash
current_price = data[context.security].price
number_of_shares = int(cash/current_price)
order(context.security, number_of_shares)


# --- Sell All Shares --- #
order_target(context.security, 0)
log.info('Selling Shares')