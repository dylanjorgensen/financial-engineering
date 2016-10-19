# What I learned
# - All vars must be converted to strings then concatenated
# - If logs do not showing it might be because throttling
# - - The basic limit is two log messages per call of initialize and handle_data



def initialize(context):
    pass


def handle_data(context, data):

    order(symbol('goog'), 5)

    # Log Info
    log.info('hello' + str(data[symbol('GOOG')].price))

    # Log Error
    log.error('hello' + str(data[symbol('GOOG')].price))

    # Log Debug
    log.debug('hello' + str(data[symbol('GOOG')].price))

    # Log War
    log.warn('hello' + str(data[symbol('GOOG')].price))






