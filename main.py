"""
MAIN
"""
from housing_entry import IndexData
import regression
import parse
import train_test_data
import regression

# load data
data = parse.load_data('House_Price_Index.csv')

# get test_and_training_data
tt_data = train_test_data.get_train_test_data(data)

# get linear regression line from train data:
regression_dict = {}

for location in tt_data:
    regression_dict[location] = regression.least_squares_regression(tt_data[location][0])
