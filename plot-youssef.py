"""
Plotting
"""

import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from parse import load_data
from train_test_data import get_train_test_data
from city_coords import COORDS

if __name__ == '__main__':
    colors = ["royalblue", "crimson", "lightseagreen", "orange", "lightgrey"]
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
