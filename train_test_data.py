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
from housing_entry import IndexData


def get_train_test_data(housing_data: dict[str, list[IndexData]]) -> \
        dict[str, tuple[pd.DataFrame, pd.DataFrame]]:
    """
    Returns a dictionary mapping locations in Canada to their corresponding training and test data.

    Preconditions:
      - housing_data != {}
    """
    train_test_data = {}
    for location in housing_data:
        df = pd.DataFrame(housing_data[location])

        # Generate test data for each location
        test_data = df.sample(frac=0.2, random_state=21)

        # Generate training data for each location
        train_data = df[~df.isin(test_data)].dropna()

        train_test_data[location] = (train_data, test_data)

    return train_test_data
