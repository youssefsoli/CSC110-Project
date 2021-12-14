"""Train-test Data: This file is used to generate training and testing data.

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
import python_ta


def get_train_test_data(df: pd.DataFrame) -> \
        tuple[pd.DataFrame, pd.DataFrame]:
    """Returns two dataframes for training and test data for the given dataframe

    Preconditions:
      - 'transaction_date' in df.columns
      - !df.empty()
    """

    # Generate test and train data for each location
    # Test data (>= year 2020)
    # Train data (< year 2020)
    dates = pd.to_datetime(df['transaction_date'])
    mask = (dates.dt.year == 2021) | (dates.dt.year == 2020)

    test_data = df[mask]
    train_data = df[~mask].dropna()

    return (train_data, test_data)


if __name__ == '__main__':
    python_ta.check_all(config={
        'extra-imports': ['pandas'],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
