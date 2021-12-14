"""Plotting

Copyright and Usage Information
===============================

This file is provided solely for marking purposes for the CSC110 instruction
and marking team at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for this CSC110
project, please consult one of the team members.

This file is Copyright (c) 2021 Aidan Li, Youssef Soliman, Min Gi Kwon, and Tej Jaspal Capildeo.
"""
import datetime

import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from parse import load_data
from train_test_data import get_train_test_data
from regression import calculate_days
from sklearn.svm import SVR

# if __name__ == '__main__':
#
#     housing_data = load_data('House_Price_Index.csv')
#     #housing_data = pd.DataFrame(housing_data['c11'])
#
#     poly_svr = SVR(kernel='poly', C=1000, degree=2)
#
#     train_data, test_data = get_train_test_data(housing_data)['c11']
#
#     # print(train_data, test_data)
#
#     train_data['transaction_date'] = train_data['transaction_date'].apply(calculate_days)
#     x_train = train_data[['sales_pair_count', 'transaction_date']].to_numpy()
#     y_train = train_data['index']
#
#     test_data['transaction_date'] = test_data['transaction_date'].apply(calculate_days)
#     x_test = test_data[['sales_pair_count', 'transaction_date']].to_numpy()
#     y_test = test_data['index']
#
#     poly_svr.fit(x_train, y_train)
#     test_preds = poly_svr.predict(x_test)
#
#     test_data['index'] = test_preds
#
#     train_data['color'] = 'blue'
#     test_data['color'] = 'red'
#
#     housing_data = pd.concat([train_data, test_data])
#
#     fig = px.line(housing_data, x="transaction_date", y="index", title="test", color="color")
#     fig.show()

if __name__ == '__main__':
    housing_data = load_data('House_Price_Index.csv')
    # housing_data = pd.DataFrame(housing_data['c11'])

    poly_svr = SVR(kernel='poly', C=1000, degree=2)

    train_data, test_data = get_train_test_data(housing_data)['c11']

    train_data['transaction_date'] = train_data['transaction_date'].apply(calculate_days)
    x_train = train_data[['sales_pair_count', 'transaction_date']].to_numpy()
    y_train = train_data['index']

    test_data['transaction_date'] = test_data['transaction_date'].apply(calculate_days)
    x_test = test_data[['sales_pair_count', 'transaction_date']].to_numpy()
    y_test = test_data['index']

    poly_svr.fit(x_train, y_train)
    train_preds = poly_svr.predict(x_train)
    test_preds = poly_svr.predict(x_test)

    train_data['pred_index'] = train_preds
    test_data['pred_index'] = test_preds

    train_data['color'] = 'blue'
    test_data['color'] = 'red'

    housing_data = pd.concat([train_data, test_data])

    fig = px.line(housing_data, x="transaction_date", y=["index", "pred_index"], title="test", color="index")
    fig.show()
