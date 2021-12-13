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
import plotly.express as px
import parse
import train_test_data
import regression
import evaluate_error
import plot


# load data
data = parse.load_data('House_Price_Index.csv')

# get test_and_training_data
tt_data = train_test_data.get_train_test_data(data)

# get linear regression line from train data:
regression_dict = {}
for location in tt_data:
    regression_dict[location] = regression.least_squares_regression(tt_data[location][0])

# get exponential regression line from train data:
exp_regression_dict = {}
for location in tt_data:
    date_list = tt_data[location][0]['transaction_date'].to_list()
    index_list = tt_data[location][0]['index'].to_list()
    log_index_list = regression.natural_logarithm(index_list)
    exp_regression_dict[location] = regression.calculate_regression(date_list, log_index_list)


# plot figure of actual prices
fig = px.line(tt_data['c11'][0], x="transaction_date", y="index", title="Unsorted Input")

# plot interactive linear regression lines
for location in regression_dict:
    # creates a dataframe for plotting
    df = plot.df_linear_regression(regression_dict[location][0], regression_dict[location][1])

    # plot both figs on same axis
    fig.add_scatter(x=df['x'], y=df['y'], name="Linear: " + location)

# plot interactive exponential regression lines
for location in exp_regression_dict:
    df = plot.df_exponential_regression(exp_regression_dict[location][0],
                                        exp_regression_dict[location][1])

    # plot both figs on same axis
    fig.add_scatter(x=df['x'], y=df['y'], name="Exponential: " + location)

fig.show()


# get rmse_error for test data
test_rmse = evaluate_error.get_rmse_for_dataset(tt_data, regression_dict, True)

# get rmse_error for training data
training_rmse = evaluate_error.get_rmse_for_dataset(tt_data, regression_dict, False)

# compare rmse_error between test and training data
