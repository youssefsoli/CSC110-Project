"""
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
from housing_entry import IndexData
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
    """
    Return the number of days passed from the baseline date, Jun 1990, to current_date
    """
    baseline = datetime.date(1990, 7, 1)
    days_passed = current_date - baseline
    return days_passed.days


def calculate_regression_slope(days_data: list[datetime.date], index_data: list) -> float:
    """
    Return the regression slope as a numerical value.
    """
    sigma_xy = sum(calculate_days(days_data[i]) * index_data[i] for i in range(0, len(days_data)))
    sigma_x = sum(calculate_days(days) for days in days_data)
    sigma_x_squared = sum((calculate_days(days) ** 2) for days in days_data)
    sigma_y = sum(index for index in index_data)
    n = len(days_data)

    slope = ((n * sigma_xy) - (sigma_x * sigma_y))/((n * sigma_x_squared) - (sigma_x ** 2))
    return slope


def calculate_regression_intercept(days_data: list, index_data: list, slope: float) -> float:
    """
    Return the regression intercept as a numerical value.
    """
    sigma_x = sum(calculate_days(days) for days in days_data)
    sigma_y = sum(index for index in index_data)
    n = len(days_data)
    intercept = (sigma_y - slope * sigma_x) / n
    return intercept


def natural_logarithm(index_data: list[float]) -> list[float]:
    """
    Return a list of the natural logarithm of index values.
    """
    new_data = index_data.copy()

    for entry in new_data:
        entry.index = math.log(entry.index)

    return new_data
