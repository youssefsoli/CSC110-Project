"""Evaluate Error: Uses several methods to evaluate the error

Copyright and Usage Information
===============================

This file is provided solely for marking purposes for the CSC110 instruction
and marking team at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for this CSC110
project, please consult one of the team members.

This file is Copyright (c) 2021 Aidan Li, Youssef Soliman, Min Gi Kwon, and Tej Jaspal Capildeo.
"""
import python_ta


def evaluate_rmse(actual: list[float], predicted: list[float]) -> float:
    """Returns the Root Mean Square Error value of the given actual and predicted data

    Preconditions:
        - len(actual) == len(predicted)
        - len(actual) != 0
        - len(predicted) != 0

    >>> evaluate_rmse([11, 22, 33], [10, 20, 30])
    2.160246899469287

    """
    n = len(actual)
    squared_error_sum = 0

    for i in range(n):
        squared_error_sum += (actual[i] - predicted[i]) ** 2

    return (squared_error_sum / n) ** 0.5


def evaluate_mae(actual: list[float], predicted: list[float]) -> float:
    """Return the Mean Absolute Error value of the given actual and predicted data

    Preconditions:
        - len(actual) == len(predicted)
        - len(actual) != 0
        - len(predicted) != 0

        >>> evaluate_mae([11, 22, 33], [10, 20, 30])
        2.0
    """
    n = len(actual)
    absolute_error_sum = 0

    for i in range(n):
        absolute_error_sum += abs(predicted[i] - actual[i])

    return absolute_error_sum / n


if __name__ == '__main__':
    python_ta.check_all(config={
        'extra-imports': [],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
