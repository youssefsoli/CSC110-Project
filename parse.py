"""
This file is used to parse the house price index data
"""

import csv
import datetime

from housing_entry import IndexData


def load_data(filename: str) -> dict[str, list[IndexData]]:
    """
    Returns a list containing housing data for each transcation date
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
    print(load_data()['c11'][5])
