"""
This file is used to generate training and testing data
"""

import pandas as pd
from housing_entry import IndexData


def get_train_test_data(housing_data: dict[str, list[IndexData]]) -> dict[str, tuple[pd.DataFrame, pd.DataFrame]]:
    """
    Returns a dictionary mapping locations to training and test data
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
