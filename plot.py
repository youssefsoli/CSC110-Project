"""
Plotting
"""

import plotly.express as px
import pandas as pd
from parse import load_data


if __name__ == '__main__':
    housing_data = load_data('House_Price_Index.csv')
    df = pd.DataFrame(housing_data['c11'])
    fig = px.line(df, x="transaction_date", y="index", title="Unsorted Input")
    fig.show()
