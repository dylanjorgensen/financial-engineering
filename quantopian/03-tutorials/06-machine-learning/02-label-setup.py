from sklearn import linear_model
#from sklearn.linear_model import logisticRegression
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from collections import Counter
import numpy as np



def initialize(context):
    context.stocks = symbols('XLY',  # XLY Consumer Discrectionary SPDR Fund
                           'XLF',  # XLF Financial SPDR Fund
                           'XLK',  # XLK Technology SPDR Fund
                           'XLE',  # XLE Energy SPDR Fund
                           'XLV',  # XLV Health Care SPRD Fund
                           'XLI',  # XLI Industrial SPDR Fund
                           'XLP',  # XLP Consumer Staples SPDR Fund
                           'XLB',  # XLB Materials SPDR Fund
                           'XLU')  # XLU Utilities SPRD Fund

    context.historical_bars = 100
    context.feature_window = 10



def handle_data(context, data):

    prices = history(bar_count = context.historical_bars, frequency='1d', field='price')

    for stock in context.stocks:

        ma1 = data[stock].mavg(50)
        ma2 = data[stock].mavg(200)

        start_bar = context.feature_window
        price_list = prices[stock].tolist()

        X = []
        y = []

        bar = start_bar


        # Feature creation
        # Len will start with 1, but list sclicing is 0 so we -1
        while bar < len(price_list)-1:

            try:
                end_price = price_list[bar+1]
                start_price = price_list[bar]

                pricing_list  = []
                xx = 0
                for _ in range (context.feature_window):
                    price = price_list[bar-context.feature_window-xx]
                    pricing_list.append(price)
                    xx += 1


                features = np.around(np.diff(pricing_list) / pricing_list[:-1] * 100.0, 1)


                print features
                bar += 1









            except Exception as e:
                print(('feature creation', str(e)))




        price = data[stock].price

        if ma1 > ma2:
            order_target_percent(stock, 0.11)

        elif ma1 < ma2:
            order_target_percent(stock, -0.11)


    # Generates comparison benchmarks
    record('ma1', ma1)
    record('ma2', ma2)
    # Because it's so easy to over leverage your accounts
    record('Leverage', context.account.leverage)




