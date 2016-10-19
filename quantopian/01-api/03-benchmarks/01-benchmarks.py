def initialize(context):
    
    # set_benchmark accepts sid() or symbol()
    # Benchmark will be plotted and used in risk metrics.
    # Set Apple as the custom benchmark
    set_benchmark(symbol('AAPL'))
    #set_benchmark(sid(24))


def handle_data(context, data):
    
    order_target_percent(symbol('GOOG'), 1.0)