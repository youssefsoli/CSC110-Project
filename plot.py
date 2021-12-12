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

import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import math
from parse import load_data
import regression


if __name__ == '__main__':
    housing_data = load_data('House_Price_Index.csv')
    df = pd.DataFrame(housing_data['bc_victoria'])
    df['transaction_date'] = df['transaction_date'].apply(regression.calculate_days)

    # create line_regression_dataframe
    x_values = [i for i in range(0, 11386)]
    slope = regression.calculate_regression_slope(housing_data['bc_victoria'])
    intercept = regression.calculate_regression_intercept(housing_data['bc_victoria'], slope)
    y_values = [slope * x + intercept for x in x_values]
    df2 = pd.DataFrame()
    df2['x'] = x_values
    df2['y'] = y_values
    # fig2 = px.line(df2, x='x', y='y', title='test')

    # exponential regression
    log_data_list = regression.natural_logarithm(housing_data['bc_victoria'])
    slope2 = regression.calculate_regression_slope(log_data_list)
    intercept2 = regression.calculate_regression_intercept(log_data_list, slope2)
    y_values2 = [math.exp((x * slope2) + intercept2) for x in x_values]
    df3 = pd.DataFrame()
    df3['x'] = x_values
    df3['y'] = y_values2

    # plot both figs on same axis
    fig = px.line(df, x="transaction_date", y="index", title="Unsorted Input")
    fig.add_scatter(x=df2['x'], y=df2['y'])
    fig.add_scatter(x=df3['x'], y=df3['y'])
    fig.show()
