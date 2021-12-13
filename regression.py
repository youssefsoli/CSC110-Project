"""DOCSTRING

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


def least_squares_regression(df: pd.DataFrame) -> tuple[float, float]:
    """
    Return a tuple of the least squares regression slope
    and intercept for df.

    >>> baseline = datetime.date(1990, 7, 1)
    >>> days = [(baseline + datetime.timedelta(days=i)) for i in range(100)]

    # Slope of 1.0
    >>> indexes = list(range(100))
    >>> calculate_regression(days, indexes)
    (1.0, 0.0)

    # Slope of 2.0
    >>> indexes = list(range(0, 200, 2))
    >>> calculate_regression(days, indexes)
    (2.0, 0.0)
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


def calculate_days(current_date: datetime.date) -> int:
    """Return the number of days passed from the baseline date, Jun 1990, to current_date

    Preconditions:
        - current_date >= datetime.date(1990, 7, 1)

    >>> calculate_days(datetime.date(1990, 7, 1))
    0
    >>> calculate_days(datetime.date(1991, 7, 1))
    365
    """
    baseline = datetime.date(1990, 7, 1)
    days_passed = current_date - baseline
    return days_passed.days


def natural_logarithm(data: list[IndexData]) -> list[IndexData]:
    """
    Return a list of IndexData with the natural logarithm applied to all index values.
    """
    new_data = data.copy()

    for entry in new_data:
        entry.index = math.log(entry.index)

    return new_data
