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

import parse
from train_test_data import get_train_test_data
from plot_geo import GeoPlot
import pandas as pd
from plot import Plot
import datetime

if __name__ == '__main__':
    # Load data
    housing_data = parse.load_data('House_Price_Index.csv')

    # Holds the housing dataframe for each location
    location_dfs = {}

    # The main visualization plot
    plot = Plot({
        'title': 'Scatterplot of Housing Indexes',
        'xaxis_title': "Date",
        'yaxis_title': "Index",
        'legend_title': "Location"
    }, list(housing_data.keys()))

    for location in housing_data:
        location_df = pd.DataFrame(housing_data[location])
        location_dfs[location] = location_df
        parse.add_calculated_days(location_df)
        num_days = location_df['calculated_days'].iloc[-1]

        # Get training and testing data
        train_data, test_data = get_train_test_data(location_df)

        # Plot the location's raw housing data
        plot.add_raw_data_line(location_df, location)

        # Add the SV regression line from the train data
        plot.add_svr_line(train_data, test_data, location)

        # Add the linear regression line from the train data
        plot.add_linear_regression_line(train_data, test_data, location, num_days)

        # Add the exponential regression line from the train data
        plot.add_exponential_regression_line(train_data, test_data, location, num_days)

    # Add a vertical line from 2020 onwards (COVID comes into play)
    plot.add_vline(datetime.date(2020, 1, 1))

    # Add the RMSE tables
    plot.add_rmse_table()

    # Display the plot
    plot.show()

    # Show the heatmap overtime of each location
    geoPlot = GeoPlot(location_dfs)
    geoPlot.show()
