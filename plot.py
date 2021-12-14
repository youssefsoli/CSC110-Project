"""Plotting: This file is used to plot the regression model lines on a scatterplot.

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
import plotly.graph_objs
import plotly.graph_objs as go
import pandas as pd
import math
import parse
import regression
import datetime


class Plot:
    """
    A wrapper for a plotly graph object
    """
    def __init__(self, layout: dict) -> None:
        self._fig = go.Figure(layout=layout)

    def add_raw_data_line(self, df: pd.DataFrame, location: str) -> None:
        """Plots the raw data of a housing dataframe"""
        self._fig.add_trace(go.Scatter(x=df["transaction_date"], y=df["index"],
                                       name=location, legendgroup="Raw Data"))

    def add_linear_regression_line(self, df: pd.DataFrame, location: str, size: int) -> None:
        """Adds the linear regression of the given dataframe"""
        slope, intercept = regression.linear_least_squares_regression(df)

        transaction_dates = [parse.days_to_date(day) for day in range(size + 1)]
        indexes = [slope * day + intercept for day in range(size + 1)]

        self._fig.add_scatter(x=transaction_dates, y=indexes,
                              name=location, legendgroup="Linear Regression")

    def add_exponential_regression_line(self, df: pd.DataFrame, location: str, size: int) -> None:
        """Adds the exponential regression of the given dataframe"""
        slope, intercept = regression.exponential_least_squares_regression(df)

        transaction_dates = [parse.days_to_date(day) for day in range(size + 1)]
        indexes = [math.exp((slope * day) + intercept) for day in range(size + 1)]

        self._fig.add_scatter(x=transaction_dates, y=indexes,
                              name=location, legendgroup="Exponential Regression")

    def add_vline(self, date: datetime.date) -> None:
        """Adds a vertical line at the specified date"""
        self._fig.add_vline(x=date)

    def show(self) -> None:
        """Displays the plot to a new browser window"""
        self._fig.show()
