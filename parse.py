"""This file is used to parse the house price index data

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

from housing_entry import IndexData


def load_data(filename: str) -> dict[str, list[IndexData]]:
    """
    Returns a dictionary mapping a Canadian city to a list of housing data (including transaction
    dates and housing index prices).

    Each row in the csv must have 25 elements.

    Preconditions:
      - all(len(row) == 25 for row in reader)
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


if __name__ == '__main__':
    print(load_data('House_Price_Index.csv')['c11'][5])
