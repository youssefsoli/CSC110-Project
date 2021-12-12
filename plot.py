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
from parse import load_data
import regression


if __name__ == '__main__':
    housing_data = load_data('House_Price_Index.csv')
    df = pd.DataFrame(housing_data['bc_victoria'])
    df['transaction_date'] = df['transaction_date'].apply(regression.calculate_days)

    # create line_regression_dataframe
    x_values = range(0, 11386)
    slope = regression.calculate_regression_slope(housing_data['bc_victoria'])
    intercept = regression.calculate_regression_intercept(housing_data['bc_victoria'], slope)
    y_values = [slope * x + intercept for x in x_values]
    df2 = pd.DataFrame()
    df2['x'] = x_values
    df2['y'] = y_values

    # plot both figs on same axis
    fig = px.line(df, x="transaction_date", y="index", title="Unsorted Input")
    fig.add_scatter(x=df2['x'], y=df2['y'])
    fig.show()
