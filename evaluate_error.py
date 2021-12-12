"""DOCSTRING"""
import pandas as pd
import regression


def evaluate_rmse_manual_regression(test_data: pd.DataFrame,
                                    reg_equation: tuple[float, float]) -> float:
    """return the rmse of the test data with the regression line."""

    # turn datetime.time into days that passed from baseline date 1 Jul 1990
    test_data['transaction_date'] = test_data['transaction_date'].apply(regression.calculate_days)

    days_list = test_data['transaction_date'].to_list()
    test_index = test_data['index'].to_list

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


def evaluate_mae(test_data: pd.DataFrame, reg_equation: tuple[float, float]) -> float:
    """
    Return the Mean Absolute Error of the test data with the regression line.
    """

    # turn datetime.time into days that passed from baseline date 1 Jul 1990
    test_data['transaction_date'] = test_data['transaction_date'].apply(regression.calculate_days)

    days_list = test_data['transaction_date'].to_list()
    test_index = test_data['index'].to_list

    # Accumulator
    mae_so_far = 0
    for i in range(0, len(days_list)):
        estimated = days_list[i] * reg_equation[0] + reg_equation[1]
        delta = abs(test_index[i] - estimated)
        mae_so_far += delta

    mae = mae_so_far / len(days_list)
    return mae
