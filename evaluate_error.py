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


def evaluate_rmse(actual: list[float], predicted: list[float]) -> float:
    """Returns the Root Mean Square Error value of the given actual and predicted data

    Preconditions:
        - len(actual) == len(predicted)
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
    """
    n = len(actual)
    absolute_error_sum = 0

    for i in range(n):
        absolute_error_sum += abs(predicted[i] - actual[i])

    return absolute_error_sum / n
