"""
DOCSTRING
"""
import datetime
from housing_entry import IndexData


def least_squares_regression(data: list) -> tuple:
    """
    Return a tuple of the least squares regression equation for data.
    :param data: list
    """
    slope = calculate_regression_slope(data)
    intercept = calculate_regression_intercept(data, slope)
    return (slope, intercept)


def calculate_days(current_date: datetime.date) -> int:
    """return days passed since baseline date Jun 1990 to current_date"""
    baseline = datetime.date(1990, 7, 1)
    days_passed = current_date - baseline
    return days_passed.days


def calculate_regression_slope(data: list) -> float:
    """DOCSTRING"""
    sigma_xy = sum([calculate_days(entry.transaction_date) * entry.index for entry in data])
    sigma_x = sum([calculate_days(entry.transaction_date) for entry in data])
    sigma_x_squared = sum([(calculate_days(entry.transaction_date) ** 2) for entry in data])
    sigma_y = sum([entry.index for entry in data])
    n = len(data)

    slope = ((n * sigma_xy) - (sigma_x * sigma_y))/((n * sigma_x_squared) - (sigma_x ** 2))
    return slope


def calculate_regression_intercept(data: list, slope: float) -> float:
    """DOCSTRING"""
    sigma_x = sum([calculate_days(entry.transaction_date) for entry in data])
    sigma_y = sum([entry.index for entry in data])
    n = len(data)
    intercept = (sigma_y - slope * sigma_x) / n
    return intercept
