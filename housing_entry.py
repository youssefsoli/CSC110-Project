"""Housing Entry: Holds a dataclass representing each entry in the housing price data.

Copyright and Usage Information
===============================

This file is provided solely for marking purposes for the CSC110 instruction
and marking team at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for this CSC110
project, please consult one of the team members.

This file is Copyright (c) 2021 Aidan Li, Youssef Soliman, Min Gi Kwon, and Tej Jaspal Capildeo.
"""
import datetime
from dataclasses import dataclass


@dataclass()
class IndexData:
    """
    An observation of the house price index and number of houses for a specific month and year for
    a specific city.

    Instance Attributes:
      - transaction_date: the year and month of the observation
      - index: the house price index
      - sales_pair_count: the number of houses used to calculate index
    """
    transaction_date: datetime.date
    index: float
    sales_pair_count: int
