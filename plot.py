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
import numpy as np
from plotly.subplots import make_subplots
from sklearn.svm import SVR
import plotly.graph_objs as go
import pandas as pd
import math
import parse
import regression
import datetime
from evaluate_error import evaluate_rmse


class Plot:
    """
    A wrapper for a plotly graph object
    """

    def __init__(self, layout: dict, locations: list[str]) -> None:
        self._fig = go.Figure()
        self._fig.update_layout(layout)
        self._rmse = {}
        for location in locations:
            self._rmse[location] = {}
        self._rmse_fig = make_subplots(
            rows=len(locations)//3, cols=3,
            subplot_titles=locations,
            shared_xaxes=True,
            vertical_spacing=0.03,
            specs=[[{"type": "table"}] * 3] * (len(locations) // 3))

    def add_raw_data_line(self, df: pd.DataFrame, location: str) -> None:
        """Plots the raw data of a housing dataframe"""
        self._fig.add_trace(go.Scatter(x=df["transaction_date"], y=df["index"],
                                       name=location, legendgroup=location,
                                       line=dict(color="blue")))

    def add_linear_regression_line(self, train_data: pd.DataFrame, test_data: pd.DataFrame,
                                   location: str, size: int) -> None:
        """Adds the linear regression of the given dataframe with its RMSE"""
        slope, intercept = regression.linear_least_squares_regression(train_data)

        start_day = train_data['calculated_days'].iloc[0]

        transaction_dates = [parse.days_to_date(day) for day in range(start_day, size + 1)]
        indexes = [slope * day + intercept for day in range(start_day, size + 1)]

        predicted_train = [slope * day + intercept for day in train_data['calculated_days']]
        predicted_test = [slope * day + intercept for day in test_data['calculated_days']]

        train_rmse = evaluate_rmse(train_data['index'].to_list(), predicted_train)
        test_rmse = evaluate_rmse(test_data['index'].to_list(), predicted_test)
        rmse_ratio = test_rmse / train_rmse

        self._rmse[location]['linear'] = (train_rmse, test_rmse, rmse_ratio)

        self._fig.add_scatter(x=transaction_dates, y=indexes,
                              name='Linear: ' + location + '<br>RMSE ratio: ' + str(rmse_ratio),
                              legendgrouptitle_text=location,
                              legendgroup=location, line=dict(color="green"))

    def add_exponential_regression_line(self, train_data: pd.DataFrame, test_data: pd.DataFrame,
                                        location: str, size: int) -> None:
        """Adds the exponential regression of the given dataframe with its RMSE"""
        slope, intercept = regression.exponential_least_squares_regression(train_data)

        start_day = train_data['calculated_days'].iloc[0]

        transaction_dates = [parse.days_to_date(day) for day in range(start_day, size + 1)]
        indexes = [math.exp((slope * day) + intercept) for day in range(start_day, size + 1)]

        predicted_train = [math.exp((slope * day) + intercept) for day in train_data['calculated_days']]
        predicted_test = [math.exp((slope * day) + intercept) for day in test_data['calculated_days']]

        train_rmse = evaluate_rmse(train_data['index'].to_list(), predicted_train)
        test_rmse = evaluate_rmse(test_data['index'].to_list(), predicted_test)
        rmse_ratio = test_rmse / train_rmse

        self._rmse[location]['exponential'] = (train_rmse, test_rmse, rmse_ratio)

        self._fig.add_scatter(x=transaction_dates, y=indexes,
                              name='Exponential: ' + location + '<br>RMSE ratio: ' + str(rmse_ratio),
                              legendgrouptitle_text=location,
                              legendgroup=location, line=dict(color="yellow"))

    def add_svr_line(self, train_data: pd.DataFrame, test_data: pd.DataFrame,
                     location: str) -> None:
        """Adds the SV regression of the given test data with its RMSE"""
        poly_svr = SVR(kernel='poly', C=1000, degree=2)

        x_train = train_data[['sales_pair_count', 'calculated_days']].to_numpy()
        y_train = train_data['index']

        x_test = test_data[['sales_pair_count', 'calculated_days']].to_numpy()

        poly_svr.fit(x_train, y_train)
        predicted_train = poly_svr.predict(x_train)
        predicted_test = poly_svr.predict(x_test)

        transaction_dates = pd.concat([train_data['transaction_date'], test_data['transaction_date']])
        indexes = np.concatenate([predicted_train, predicted_test])

        train_rmse = evaluate_rmse(train_data['index'].to_list(), predicted_train)
        test_rmse = evaluate_rmse(test_data['index'].to_list(), predicted_test)
        rmse_ratio = test_rmse / train_rmse

        self._rmse[location]['svr'] = (train_rmse, test_rmse, rmse_ratio)

        self._fig.add_scatter(x=transaction_dates, y=indexes,
                              name='SVR: ' + location + '<br>RMSE ratio: ' + str(rmse_ratio),
                              legendgrouptitle_text=location,
                              legendgroup=location, line=dict(color="red"))

    def add_vline(self, date: datetime.date) -> None:
        """Adds a vertical line at the specified date"""
        self._fig.add_vline(x=date)

    def add_rmse_table(self) -> None:
        """Adds a table with RMSE values"""
        row = 0
        col = 0
        for location in self._rmse:
            table = []
            row = (row % (len(self._rmse) // 3)) + 1
            col = (col % 3) + 1
            for reg_type in self._rmse[location]:
                train_rmse, test_rmse, rmse_ratio = self._rmse[location][reg_type]
                table.append([reg_type, train_rmse, test_rmse, rmse_ratio])

            # Transpose the 2D array for table order
            table = np.transpose(table)

            self._rmse_fig.add_trace(
                go.Table(
                    header=dict(
                        values=["Regression Type", "Train RMSE", "Test RMSE", "RMSE Ratio"],
                        font=dict(size=10),
                        align="center"
                    ),
                    cells=dict(
                        values=table,
                        align="left")
                ),
                row=row, col=col
            )

    def show(self) -> None:
        """Displays the plot to a new browser window"""
        self._fig.show()
        self._rmse_fig.show()
