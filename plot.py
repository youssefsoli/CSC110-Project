"""
Plotting
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
