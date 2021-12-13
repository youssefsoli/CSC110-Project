"""MAIN

Copyright and Usage Information
===============================

This file is provided solely for marking purposes for the CSC110 instruction
and marking team at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for this CSC110
project, please consult one of the team members.

This file is Copyright (c) 2021 Aidan Li, Youssef Soliman, Min Gi Kwon, and Tej Jaspal Capildeo.
"""
from housing_entry import IndexData
import parse
import train_test_data
import regression
import evaluate_error

# load data
data = parse.load_data('House_Price_Index.csv')

# get test_and_training_data
tt_data = train_test_data.get_train_test_data(data)

# get linear regression line from train data:
regression_dict = {}
for location in tt_data:
    regression_dict[location] = regression.least_squares_regression(tt_data[location][0])

# plot interactive regression lines

# get rmse_error for test data
rmse_dict_test = {}
for location in tt_data:
    rmse_dict_test[location] = \
        evaluate_error.evaluate_rmse_manual_regression(tt_data[location][1], regression_dict[location])

# get rmse_error for training data
rmse_dict_training = {}
for location in tt_data:
    rmse_dict_training[location] = \
        evaluate_error.evaluate_rmse_manual_regression(tt_data[location][0], regression_dict[location])
