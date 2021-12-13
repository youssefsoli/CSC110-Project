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
import pandas as pd
import regression


def evaluate_rmse_manual_regression(data: pd.DataFrame,
                                    reg_equation: tuple[float, float]) -> float:
    """
    Returns the Root Mean Square Error value of the given data with the regression line.
    """

    # turn datetime.time into days that passed from baseline date 1 Jul 1990
    data['transaction_date'] = data['transaction_date'].apply(regression.calculate_days)

    days_list = data['transaction_date'].to_list()
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
    """Return the rmse for each location of the dataset dictionary, after passing in the dictionary
    regression dict which holds regression co-efficients of the training data by location, and the
    whether the dataset is the test data set.

    is_test = False returns  rmse values of the training dataset, and is_test = True returns the
    rmse values of the test dataset.
    ."""

    # accumulator
    rmse_dict_so_far = {}

    for location in dataset:
        rmse_dict_so_far[location] = \
            evaluate_rmse_manual_regression(dataset[location][int(is_test)],
                                            regression_dict[location])
    return rmse_dict_so_far


def evaluate_mae(test_data: pd.DataFrame, reg_equation: tuple[float, float]) -> float:
def evaluate_mae(data: pd.DataFrame, reg_equation: tuple[float, float]) -> float:
    """
    Return the Mean Absolute Error value of the given data with the regression line.
    """

    # turn datetime.time into days that passed from baseline date 1 Jul 1990
    data['transaction_date'] = data['transaction_date'].apply(regression.calculate_days)

    days_list = data['transaction_date'].to_list()
    test_index = data['index'].to_list

    # Accumulator
    mae_so_far = 0
    for i in range(0, len(days_list)):
        estimated = days_list[i] * reg_equation[0] + reg_equation[1]
        delta = abs(test_index[i] - estimated)
        mae_so_far += delta

    mae = mae_so_far / len(days_list)
    return mae
