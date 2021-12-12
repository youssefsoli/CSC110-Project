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

if __name__ == '__main__':

    housing_data = load_data('House_Price_Index.csv')
    housing_data = pd.DataFrame(housing_data['c11'])


    # train_data, test_data = get_train_test_data(housing_data)['c11']
    #
    # train_data['transaction_date'] = train_data['transaction_date'].apply(calculate_days)
    # x_train = train_data[['sales_pair_count', 'transaction_date']].to_numpy()
    # y_train = train_data['index']
    #
    # test_data['transaction_date'] = test_data['transaction_date'].apply(calculate_days)
    # x_test = test_data[['sales_pair_count', 'transaction_date']].to_numpy()
    # y_test = test_data['index']
    #
    # knn_model.fit(x_train, y_train)
    # test_preds = knn_model.predict(x_test)
    #
    # test_data['pred_index'] = test_preds
    #
    # test_data = test_data.sort_values(by=['transaction_date'])

    fig = px.line(housing_data, x="transaction_date", y="index", title="test")
    fig.show()
