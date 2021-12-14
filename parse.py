"""Parse: This file is used to parse the house price index data.

Copyright and Usage Information
===============================

This file is provided solely for marking purposes for the CSC110 instruction
and marking team at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for this CSC110
project, please consult one of the team members.

This file is Copyright (c) 2021 Aidan Li, Youssef Soliman, Min Gi Kwon, and Tej Jaspal Capildeo.
"""

import csv
import datetime
import pandas as pd

from housing_entry import IndexData


def load_data(filename: str) -> dict[str, list[IndexData]]:
    """
    Returns a dictionary mapping a Canadian city to a list of housing data (including transaction
    dates and housing index prices).

    Each row in the csv must have 25 elements.

    Preconditions:
      - all(len(row) == 25 for row in csv.reader(open(filename), delimiter=',')
    """
    data = {}
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # Skip the header
        next(reader)  # Skip the header

        locations = ['c11', 'bc_victoria', 'bc_vancouver', 'ab_calgary',
                     'ab_edmonton', 'mb_winnipeg', 'on_hamilton', 'on_toronto',
                     'on_ottawa', 'qc_montreal', 'qc_quebec_city', 'ns_halifax']

        for location in locations:
            data[location] = []

        for row in reader:
            assert len(row) == 25, 'Expected every row to contain 25 elements.'
            date = datetime.datetime.strptime(row[0], '%b-%Y').date()
            for i in range(len(locations)):
                location = locations[i]
                if row[2 * i + 1] == '' or row[2 * i + 2] == '':
                    continue
                data[location].append(IndexData(date, float(row[2 * i + 1]), int(row[2 * i + 2])))

    return data


def calculate_days(current_date: datetime.date) -> int:
    """Return the number of days passed from the baseline date, Jul 1990, to current_date

    Preconditions:
        - current_date >= datetime.date(1990, 7, 1)

    >>> calculate_days(datetime.date(1990, 7, 1))
    0
    >>> calculate_days(datetime.date(1991, 7, 1))
    365
    """
    baseline = datetime.date(1990, 7, 1)
    days_passed = current_date - baseline
    return days_passed.days


def calculate_days_str(current_date: str) -> int:
    """Return the number of days passed from the baseline date, Jul 1990, to current_date

    Preconditions:
        - datetime.datetime.strptime(current_date, '%m-%d-%Y').date() >= datetime.date(1990, 7, 1)

    >>> calculate_days_str('7-1-1990')
    0
    >>> calculate_days_str('7-1-1991')
    365
    """
    current_date_obj = datetime.datetime.strptime(current_date, '%m-%d-%Y').date()
    return calculate_days(current_date_obj)


def days_to_date(days: int) -> datetime.date:
    """Return the datetime.date from the days from Jul 1990

    Preconditions:
        - days >= 0

    >>> days_to_date(calculate_days(datetime.date(1990, 7, 1))) == datetime.date(1990, 7, 1)
    True
    >>> days_to_date(calculate_days(datetime.date(1991, 7, 1))) == datetime.date(1991, 7, 1)
    True
    """
    baseline = datetime.date(1990, 7, 1)
    delta = datetime.timedelta(days=days)
    return baseline + delta


def add_calculated_days(df: pd.DataFrame) -> None:
    """Mutates the inputted housing dataframe with a calculated_days column

    Preconditions:
        - 'transaction_date' in df.columns

    >>> df = pd.DataFrame({'transaction_date': [datetime.date(1990, 7, 1), \
     datetime.date(1991, 7, 1)]})
    >>> add_calculated_days(df)
    >>> df['calculated_days'].to_list() == [0, 365]
    True
    """
    df['calculated_days'] = df['transaction_date'].apply(calculate_days)


if __name__ == '__main__':
    print(load_data('House_Price_Index.csv')['c11'][5])
