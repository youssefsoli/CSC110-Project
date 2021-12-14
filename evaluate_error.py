"""Evaluate Error: Uses several methods to evaluate the error of regression model

Copyright and Usage Information
===============================

This file is provided solely for marking purposes for the CSC110 instruction
and marking team at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for this CSC110
project, please consult one of the team members.

This file is Copyright (c) 2021 Aidan Li, Youssef Soliman, Min Gi Kwon, and Tej Jaspal Capildeo.
"""
import pandas as pd
import regression


def evaluate_rmse_manual_regression(data: pd.DataFrame,
                                    reg_equation: tuple[float, float]) -> float:
    """
    Returns the Root Mean Square Error value of the given data with the regression line.

    >>> lst = [1, 2, 3, 4]
    >>> df = pd.DataFrame({'calculated_days': lst, 'index': lst})
    >>> equation = 1, 0
    >>> evaluate_rmse_manual_regression(df, equation)
    0.0
    """
    days_list = data['calculated_days'].to_list()
    test_index = data['index'].to_list()

    # Accumulator
    rmse_so_far = 0
    for i in range(0, len(days_list)):
        estimated = days_list[i] * reg_equation[0] + reg_equation[1]
        delta = test_index[i] - estimated
        rmse_so_far += (delta ** 2)

    rmse = (rmse_so_far / len(days_list)) ** 0.5
    return rmse
    # rmse is more forgiving to small errors and more strongly affected by outliers
    # compared to mae


def get_rmse_for_dataset(dataset: dict, regression_dict: dict, is_test: bool) -> dict:
    """
    Return the RMSE for each location of the dataset.

    The input regression_dict holds regression co-efficients of the training data by location.
    The input is_test tells us if the dataset is the test data set.

    is_test = False returns RMSE values of the training dataset, and is_test = True returns the
    RMSE values of the test dataset.

    """

    # accumulator
    rmse_dict_so_far = {}

    for location in dataset:
        rmse_dict_so_far[location] = \
            evaluate_rmse_manual_regression(dataset[location][int(is_test)],
                                            regression_dict[location])
    return rmse_dict_so_far


def evaluate_mae(data: pd.DataFrame, reg_equation: tuple[float, float]) -> float:
    """
    Return the Mean Absolute Error value of the given data with the regression line.
    """
    days_list = data['calculated_days'].to_list()
    test_index = data['index'].to_list

    # Accumulator
    mae_so_far = 0
    for i in range(0, len(days_list)):
        estimated = days_list[i] * reg_equation[0] + reg_equation[1]
        delta = abs(test_index[i] - estimated)
        mae_so_far += delta

    mae = mae_so_far / len(days_list)
    return mae


def get_mae_for_dataset(dataset: dict, regression_dict: dict, is_test: bool) -> dict:
    """
    Return the MAE for each location of the dataset.

    The input regression_dict holds regression co-efficients of the training data by location.
    The input is_test tells us if the dataset is the test data set.

    is_test = False returns MAE values of the training dataset, and is_test = True returns the
    MAE values of the test dataset.
    """

    # accumulator
    mae_dict_so_far = {}

    for location in dataset:
        mae_dict_so_far[location] = \
            evaluate_mae(dataset[location][int(is_test)], regression_dict[location])

    return mae_dict_so_far
