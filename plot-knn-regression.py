"""
Plotting
"""

import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from parse import load_data
from train_test_data import get_train_test_data
from sklearn.neighbors import KNeighborsRegressor
from regression import calculate_days

if __name__ == '__main__':
    knn_model = KNeighborsRegressor(n_neighbors=3)

    housing_data = load_data('House_Price_Index.csv')
    train_data, test_data = get_train_test_data(housing_data)['c11']

    train_data['transaction_date'] = train_data['transaction_date'].apply(calculate_days)
    x_train = train_data[['sales_pair_count', 'transaction_date']].to_numpy()
    y_train = train_data['index']

    test_data['transaction_date'] = test_data['transaction_date'].apply(calculate_days)
    x_test = test_data[['sales_pair_count', 'transaction_date']].to_numpy()
    y_test = test_data['index']

    knn_model.fit(x_train, y_train)
    test_preds = knn_model.predict(x_test)

    test_data['pred_index'] = test_preds

    test_data = test_data.sort_values(by=['transaction_date'])

    fig = px.line(test_data, x="transaction_date", y=["index", 'pred_index'], title="test")
    fig.show()
