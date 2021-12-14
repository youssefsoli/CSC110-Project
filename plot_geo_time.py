"""Geographic plot over time: This plot graphs the change in housing
price index and sampling size overtime on an interactive map of Canada

Copyright and Usage Information
===============================

This file is provided solely for marking purposes for the CSC110 instruction
and marking team at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for this CSC110
project, please consult one of the team members.

This file is Copyright (c) 2021 Aidan Li, Youssef Soliman, Min Gi Kwon, and Tej Jaspal Capildeo.
"""

import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from parse import load_data
from train_test_data import get_train_test_data
from city_coords import COORDS

if __name__ == '__main__':
    housing_data = load_data('House_Price_Index.csv')
    df = pd.DataFrame(housing_data['bc_vancouver'])
    df['lon'] = COORDS['bc_vancouver'][1]
    df['lat'] = COORDS['bc_vancouver'][0]
    df['name'] = 'bc_vancouver'
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    df['transaction_date'] = df['transaction_date'].dt.strftime('%m-%d-%Y')

    fig = px.scatter_geo(df, animation_frame="transaction_date", size="sales_pair_count",
                         lon="lon", lat="lat", hover_name="name",
                         scope="north america", color="index",
                         size_max=100,
                         projection="natural earth", range_color=(0, 300),
                         color_continuous_scale="hot", title="Canada")
    fig.update_geos(fitbounds="locations", showcountries=True)
    fig.show()
