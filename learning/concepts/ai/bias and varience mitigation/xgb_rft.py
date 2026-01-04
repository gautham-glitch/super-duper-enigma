import matplotlib.pyplot as plt
import numpy as np
import time as t

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error,r2_score

df = fetch_california_housing()
x,y = df.data, df.target

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

rft = RandomForestRegressor(n_estimators = 100, random_state = 42)
xgb = XGBRegressor(n_estimators = 100, random_state = 42)

s_time_rf_t = t.time()
rft.fit(X_train, y_train)
e_time_rf_t = t.time()
time_rf_t = e_time_rf_t - s_time_rf_t

s_time_rf_p = t.time()
y_pred_rf = rft.predict(X_test)
e_time_rf_p = t.time()
time_rf_p = e_time_rf_p - s_time_rf_p
print("training time for random forest: ", time_rf_t)
print("prediction time for random forest: ", time_rf_p)
print("accuracy using mse = ",100 * mean_squared_error(y_test, y_pred_rf), "%")
print("accuracy using r squared = ",100 * r2_score(y_test, y_pred_rf), "%\n")




s_time_xgb_t = t.time()
xgb.fit(X_train, y_train)
e_time_xgb_t = t.time()
time_xgb_t = e_time_xgb_t - s_time_xgb_t

s_time_xgb_p = t.time()
y_pred_xgb = rft.predict(X_test)
e_time_xgb_p = t.time()
time_xgb_p = e_time_rf_p - s_time_rf_p
print("training time for XGBooster: ", time_xgb_t)
print("prediction time for XGBooster: ", time_xgb_p)
print("accuracy using mse = ",100 * mean_squared_error(y_test, y_pred_xgb), "%")
print("accuracy using r squared = ",100 * r2_score(y_test, y_pred_xgb), "%\n")


std_y = np.std(y_test)

plt.figure(figsize=(14, 6))

# Random Forest plot
plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred_rf, alpha=0.5, color="blue",ec='k')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2,label="perfect model")
plt.plot([y_test.min(), y_test.max()], [y_test.min() + std_y, y_test.max() + std_y], 'r--', lw=1, label="+/-1 Std Dev")
plt.plot([y_test.min(), y_test.max()], [y_test.min() - std_y, y_test.max() - std_y], 'r--', lw=1, )
plt.ylim(0,6)
plt.title("Random Forest Predictions vs Actual")
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.legend()


# XGBoost plot
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_pred_xgb, alpha=0.5, color="orange",ec='k')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2,label="perfect model")
plt.plot([y_test.min(), y_test.max()], [y_test.min() + std_y, y_test.max() + std_y], 'r--', lw=1, label="+/-1 Std Dev")
plt.plot([y_test.min(), y_test.max()], [y_test.min() - std_y, y_test.max() - std_y], 'r--', lw=1, )
plt.ylim(0,6)
plt.title("XGBoost Predictions vs Actual")
plt.xlabel("Actual Values")
plt.legend()
plt.tight_layout()
plt.show()