def initialize(context):
    context.stocks = symbols('AA', 'AAPL', 'ALK')

def handle_data(context, data):
    # You can pass a string variable into record().
    # Here we record the price of all the stocks in our universe.
    for stock in data:
      price = data[stock].price
      record(stock, price)

    # You can also pass in a variable with a string value.
    # This records the high and low values for Apple.
    fields = ['high', 'low']
    for field in fields:
      record(field, data[symbol('AAPL')][field])
