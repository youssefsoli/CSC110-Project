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

from city_coords import COORDS


class GeoPlot:
    """
    A wrapper for a plotly geo plot object
    """
    _fig: go.Figure

    def __init__(self, location_dfs: dict[str, pd.DataFrame]) -> None:
        df = pd.DataFrame()
        for location in location_dfs:
            if location in COORDS:
                loc_df = location_dfs[location]
                # Add the location coordinates
                loc_df['lat'] = COORDS[location][0]
                loc_df['lon'] = COORDS[location][1]

                # Add the location's name
                loc_df['name'] = location

                # Conver the transaction date to a parsable string
                loc_df['transaction_date_str'] = pd.to_datetime(loc_df['transaction_date'])
                loc_df['transaction_date_str'] = loc_df['transaction_date_str'].dt.strftime('%m-%Y')
                df = df.append(loc_df)

        self._fig = px.scatter_geo(df, animation_frame="transaction_date_str",
                                   size="sales_pair_count",
                                   lon="lon", lat="lat", hover_name="name",
                                   scope="north america", color="index",
                                   size_max=150,
                                   projection="natural earth", range_color=(0, 300),
                                   color_continuous_scale="dense",
                                   title="Map of Housing Indexes over Time")
        self._fig.update_geos(fitbounds="locations", showcountries=True)

    def show(self) -> None:
        """Displays the geo plot to a new browser window"""
        self._fig.show()


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['city_coords', 'plotly.graph_objs',
                          'plotly.express', 'pandas'],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()
