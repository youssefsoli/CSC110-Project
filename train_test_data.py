"""
This file is used to generate training and testing data
"""

import pandas as pd
# import datetime

from parse import load_data

housing_data = load_data('House_Price_Index.csv')

df_c11 = pd.DataFrame(housing_data['c11'])
df_bc_victoria = pd.DataFrame(housing_data['bc_victoria'])
df_bc_vancouver = pd.DataFrame(housing_data['bc_vancouver'])
df_ab_calgary = pd.DataFrame(housing_data['ab_calgary'])
df_ab_edmonton = pd.DataFrame(housing_data['ab_edmonton'])
df_mb_winnipeg = pd.DataFrame(housing_data['mb_winnipeg'])
df_on_hamilton = pd.DataFrame(housing_data['on_hamilton'])
df_on_toronto = pd.DataFrame(housing_data['on_toronto'])
df_on_ottawa = pd.DataFrame(housing_data['on_ottawa'])
df_qc_montreal = pd.DataFrame(housing_data['qc_montreal'])
df_qc_quebec_city = pd.DataFrame(housing_data['qc_quebec_city'])
df_ns_halifax = pd.DataFrame(housing_data['ns_halifax'])


# condition = (df['transaction_date'] >= datetime.date(2005, 1, 1))
#
# df = (df[condition])    # filter out all data before 2005

################################################################################
# Generating test data for the composite and each city
################################################################################

test_data_c11 = df_c11.sample(frac=0.2, random_state=21)
test_data_bc_victoria = df_bc_victoria.sample(frac=0.2, random_state=21)
test_data_bc_vancouver = df_bc_vancouver.sample(frac=0.2, random_state=21)
test_data_ab_calgary = df_ab_calgary.sample(frac=0.2, random_state=21)
test_data_ab_edmonton = df_ab_edmonton.sample(frac=0.2, random_state=21)
test_data_mb_winnipeg = df_mb_winnipeg.sample(frac=0.2, random_state=21)
test_data_on_hamilton = df_on_hamilton.sample(frac=0.2, random_state=21)
test_data_on_toronto = df_on_toronto.sample(frac=0.2, random_state=21)
test_data_on_ottawa = df_on_ottawa.sample(frac=0.2, random_state=21)
test_data_qc_montreal = df_qc_montreal.sample(frac=0.2, random_state=21)
test_data_qc_quebec_city = df_qc_quebec_city.sample(frac=0.2, random_state=21)
test_data_ns_halifax = df_ns_halifax.sample(frac=0.2, random_state=21)

################################################################################
# Generating training data for the composite and each city
################################################################################

train_data_c11 = df_c11[~df_c11.isin(test_data_c11)].dropna()
train_data_bc_victoria = df_bc_victoria[~df_bc_victoria.isin(test_data_bc_victoria)].dropna()
train_data_bc_vancouver = df_bc_vancouver[~df_bc_vancouver.isin(test_data_bc_vancouver)].dropna()
train_data_ab_calgary = df_ab_calgary[~df_ab_calgary.isin(test_data_ab_calgary)].dropna()
train_data_ab_edmonton = df_ab_edmonton[~df_ab_edmonton.isin(test_data_ab_edmonton)].dropna()
train_data_mb_winnipeg = df_mb_winnipeg[~df_mb_winnipeg.isin(test_data_mb_winnipeg)].dropna()
train_data_on_hamilton = df_on_hamilton[~df_on_hamilton.isin(test_data_on_hamilton)].dropna()
train_data_on_toronto = df_on_toronto[~df_on_toronto.isin(test_data_on_toronto)].dropna()
train_data_on_ottawa = df_on_ottawa[~df_on_ottawa.isin(test_data_on_ottawa)].dropna()
train_data_qc_montreal = df_qc_montreal[~df_qc_montreal.isin(test_data_qc_montreal)].dropna()
train_data_qc_quebec_city = df_qc_quebec_city[~df_qc_quebec_city.isin(test_data_qc_quebec_city)].dropna()
train_data_ns_halifax = df_ns_halifax[~df_ns_halifax.isin(test_data_ns_halifax)].dropna()
