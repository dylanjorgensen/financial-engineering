




def initialize(context):

  # You can prevent the algorithm from trading specific securities by using set_do_not_order_list
  # create the trading guard to avoid over-leveraged ETFs
  set_do_not_order_list(security_lists.leveraged_etf_list)

def handle_data(context,data):
  # the point in time lists allow for in/not in checks and iteration
  # the list is point-in-time and allows for checks and iterations
  if symbol('AAPL') not in security_lists.leveraged_etf_list:
    order_target(symbol('AAPL'), 100)

  # view the contents of the list
  for etf in security_lists.leveraged_etf_list:
    print '{s} is a leveraged etf'.format(s=etf)