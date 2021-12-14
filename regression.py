"""Regression: This file handles all of the regression calculations

Copyright and Usage Information
===============================

This file is provided solely for marking purposes for the CSC110 instruction
and marking team at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for this CSC110
project, please consult one of the team members.

This file is Copyright (c) 2021 Aidan Li, Youssef Soliman, Min Gi Kwon, and Tej Jaspal Capildeo.
"""
import math
import pandas as pd


def linear_least_squares_regression(df: pd.DataFrame) -> tuple[float, float]:
    """
    Return a tuple of the least squares regression slope
    and intercept for the housing price dataframe.

    Preconditions:
        - 'calculated_days' in df.columns
        - 'index' in df.columns

    >>> lst = [1, 2, 3, 4]
    >>> df = pd.DataFrame({'calculated_days': lst, 'index': lst})
    >>> linear_least_squares_regression(df)
    (1.0, 0.0)
    """
    days_data = df['calculated_days'].to_list()
    index_data = df['index'].to_list()

    return calculate_regression(days_data, index_data)


def exp_least_squares_regression(df: pd.DataFrame) -> tuple[float, float]:
    """
    Return a tuple of the least squares regression slope
    and intercept for the housing price dataframe.

    Preconditions:
        - 'calculated_days' in df.columns
        - 'index' in df.columns

    >>> lst = [1, 2, 3, 4]
    >>> exp_list = [math.exp(i) for i in range(1, 5)]
    >>> df = pd.DataFrame({'calculated_days': lst, 'index': exp_list})
    >>> exp_least_squares_regression(df)
    (1.0, 0.0)
    """
    days_data = df['calculated_days'].to_list()
    index_data = natural_logarithm(df['index'].to_list())

    return calculate_regression(days_data, index_data)


def calculate_regression(x_data: list, y_data: list) -> tuple[float, float]:
    """Returns a tuple containing the slope and intercept of the calculated regression of x and y

    Preconditions:
        - len(x_data) == len(y_data)

    >>> x_data = list(range(100))

    # Slope of 1.0
    >>> y_data = list(range(100))
    >>> calculate_regression(x_data, y_data)
    (1.0, 0.0)

    # Slope of 2.0
    >>> y_data = list(range(0, 200, 2))
    >>> calculate_regression(x_data, y_data)
    (2.0, 0.0)
    """
    n = len(x_data)

    sigma_xy = sum(x_data[i] * y_data[i] for i in range(n))
    sigma_x = sum(x_data)
    sigma_x_squared = sum((x ** 2) for x in x_data)
    sigma_y = sum(y_data)

    slope = ((n * sigma_xy) - (sigma_x * sigma_y)) / ((n * sigma_x_squared) - (sigma_x ** 2))
    intercept = (sigma_y - slope * sigma_x) / n
    return (slope, intercept)


def natural_logarithm(data: list) -> list[float]:
    """Return a list with the natural logarithm applied to all values in data.

    Preconditions:
        - all(entry > 0 for entry in data)

    >>> data = [math.e, 1]
    >>> natural_logarithm(data)
    [1.0, 0.0]
    """
    return [math.log(entry) for entry in data]


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['numpy', 'pandas', 'math'],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()
