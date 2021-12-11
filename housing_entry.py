"""
f
"""
import datetime
from dataclasses import dataclass


@dataclass()
class IndexData:
    """
    f
    """
    transaction_date: datetime.date
    index: float
    sales_pair_count: int
