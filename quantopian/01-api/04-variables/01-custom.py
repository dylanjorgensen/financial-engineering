"""
param(context)
    'account': Account({see below}),
    'portfolio': Portfolio({see below}),
    'my_dict': {'foe': 'Jill', 'friend': 'dylan'}, 'my_list': ['dylan', 'Jill'], 'my_var': 'dylan'})
"""








def initialize(context):

    # Add global vars for book keeping
    context.my_var = 'dylan'
    context.my_list = ['dylan', 'Jill']
    context.my_dict = {'friend' : 'dylan', 'foe' : 'Jill'}


def before_trading_start(context):

    print context.my_var  # Retrieve value


def handle_data(context, data):

    print context.my_list  # Retrieve list value

    # Required
    order(symbol('GOOG'), 1)