import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor

import warnings as w
w.filterwarnings("ignore")

csv_file = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/pu9kbeSaAtRZ7RxdJKX9_A/yellow-tripdata.csv"
df = pd.read_csv(csv_file)
print(df)

# extract the labels from the dataframe
y = df[['tip_amount']].values.astype('float32')

# drop the target variable from the feature matrix
proc_data = df.drop(['tip_amount'], axis=1)

# get the feature matrix used for training
X = proc_data.values

# normalize the feature matrix
X = normalize(X, axis=1, norm='l1', copy=False)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 42)

reg_tree = DecisionTreeRegressor(criterion = "squared_error", max_depth = 8, random_state = 35)
reg_tree.fit(X_train,y_train)

y_pred = reg_tree.predict(X_test)
print(mean_squared_error(y_test, y_pred))