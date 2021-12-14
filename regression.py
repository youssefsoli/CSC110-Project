"""Regression: This file is used to derive the least squares regression lines.

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
import math
import pandas as pd


def least_squares_regression(df: pd.DataFrame) -> tuple[float, float]:
    """
    Return a tuple of the least squares regression slope
    and intercept for df.

    >>> baseline = datetime.date(1990, 7, 1)
    >>> transaction_date = [(baseline + datetime.timedelta(days = 0)).strftime('%m-%d-%Y'), \
                            (baseline + datetime.timedelta(days = 1)).strftime('%m-%d-%Y'), \
                            (baseline + datetime.timedelta(days = 2)).strftime('%m-%d-%Y'), \
                            (baseline + datetime.timedelta(days = 3)).strftime('%m-%d-%Y'), \
                            (baseline + datetime.timedelta(days = 4)).strftime('%m-%d-%Y')]
    >>> index = list(range(5))
    >>> dataframe = pd.DataFrame({'transaction_date': transaction_date, 'index': index})
    >>> least_squares_regression(dataframe)
    (1.0, 0.0)
    """
    days_data = df['transaction_date'].to_list()
    index_data = df['index'].to_list()

    sigma_xy = sum(calculate_days(days_data[i]) * index_data[i] for i in range(len(days_data)))
    sigma_x = sum(calculate_days(days) for days in days_data)
    sigma_x_squared = sum((calculate_days(days) ** 2) for days in days_data)
    sigma_y = sum(index_data)
    n = len(days_data)

    slope = ((n * sigma_xy) - (sigma_x * sigma_y)) / ((n * sigma_x_squared) - (sigma_x ** 2))
    intercept = (sigma_y - slope * sigma_x) / n
    return (slope, intercept)


def calculate_days(current_date: str) -> int:
    """Return the number of days passed from the baseline date, Jun 1990, to current_date

    Preconditions:
        - datetime.datetime.strptime(current_date, '%m-%d-%Y').date() >= datetime.date(1990, 7, 1)

    >>> calculate_days('7-1-1990')
    0
    >>> calculate_days('7-1-1991')
    365
    """
    current_date = datetime.datetime.strptime(current_date, '%m-%d-%Y').date()
    baseline = datetime.date(1990, 7, 1)
    days_passed = current_date - baseline
    return days_passed.days


def natural_logarithm(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return a dataframe with the natural logarithm applied to all index values in df.

    >>> index = list(range(1, 5))
    >>> dataframe = pd.DataFrame({'index': index})
    >>> log_df = natural_logarithm(dataframe)
    >>> lst = log_df['index'].to_list()
    >>> lst == [math.log(i) for i in range(1, 5)]
    True
    """
    index_data = df['index'].to_list()
    df['index'] = [math.log(entry) for entry in index_data]
    return df
