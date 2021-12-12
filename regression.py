"""
DOCSTRING
"""
import datetime

import pandas as pd


def least_squares_regression(data: pd.DataFrame) -> tuple:
    """
    Return a tuple of the least squares regression equation for data, a list of Index Data.
    :param data: list
    """
    days_data = data['transaction_date'].to_list()
    index_data = data['index'].to_list()
    slope = calculate_regression_slope(days_data, index_data)
    intercept = calculate_regression_intercept(days_data, index_data, slope)
    return (slope, intercept)


def calculate_days(current_date: datetime.date) -> int:
    """return days passed since baseline date Jun 1990 to current_date"""
    baseline = datetime.date(1990, 7, 1)
    days_passed = current_date - baseline
    return days_passed.days


def calculate_regression_slope(days_data: list, index_data: list) -> float:
    """DOCSTRING"""
    sigma_xy = sum(calculate_days(days_data[i]) * index_data[i] for i in range(0, len(days_data)))
    sigma_x = sum(calculate_days(days) for days in days_data)
    sigma_x_squared = sum((calculate_days(days) ** 2) for days in days_data)
    sigma_y = sum(index for index in index_data)
    n = len(days_data)

    slope = ((n * sigma_xy) - (sigma_x * sigma_y))/((n * sigma_x_squared) - (sigma_x ** 2))
    return slope


def calculate_regression_intercept(days_data: list, index_data: list, slope: float) -> float:
    """DOCSTRING"""
    sigma_x = sum(calculate_days(days) for days in days_data)
    sigma_y = sum(index for index in index_data)
    n = len(days_data)
    intercept = (sigma_y - slope * sigma_x) / n
    return intercept
