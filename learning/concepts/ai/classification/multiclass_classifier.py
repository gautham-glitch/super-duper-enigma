import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsOneClassifier

import warnings
warnings.filterwarnings("ignore")

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/GkDzb7bWrtvGXdPOfk6CIg/Obesity-level-prediction-dataset.csv"
data = pd.read_csv(url)

continuous_columns = data.select_dtypes("float64").columns.tolist()

scalar = StandardScaler()
scaled_features = scalar.fit_transform(data[continuous_columns])

scaled_df = pd.DataFrame(scaled_features, columns = scalar.get_feature_names_out(continuous_columns))
scaled_data = pd.concat([data.drop(columns=continuous_columns), scaled_df], axis = 1)

categorial_columns = scaled_data.select_dtypes("object").columns.tolist()
categorial_columns.remove("NObeyesdad")

encoder = OneHotEncoder(sparse_output = False, drop = "first")
encoded_features = encoder.fit_transform(scaled_data[categorial_columns])
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorial_columns))
prepped_data = pd.concat([scaled_data.drop(columns=categorial_columns), encoded_df], axis=1)

prepped_data["NObeyesdad"] = prepped_data['NObeyesdad'].astype('category').cat.codes

X = prepped_data.drop("NObeyesdad",axis = 1)
y = prepped_data["NObeyesdad"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, random_state = 42)


#one over all
LR_ova = LogisticRegression(multi_class="ovr", max_iter = 1000)
LR_ova.fit(X_train, y_train)
y_test_proba_ova = LR_ova.predict(X_test)

print(f"accuracy of one over all strategy = {np.round(100 * accuracy_score(y_test,y_test_proba_ova), 2)}%")

#one over one
LR_ovo = OneVsOneClassifier(LogisticRegression(max_iter = 1000))
LR_ovo.fit(X_train,y_train)
y_test_proba_ovo = LR_ovo.predict(X_test)

print(f"accuracy of one over one strategy = {np.round(100 * accuracy_score(y_test,y_test_proba_ovo), 2)}%")


feature_importance = np.mean(np.abs(LR_ova.coef_), axis=0)
plt.barh(X.columns, feature_importance)
plt.title("Feature Importance")
plt.xlabel("Importance")
plt.show()

# For One vs One model
# Collect all coefficients from each underlying binary classifier
coefs = np.array([est.coef_[0] for est in LR_ovo.estimators_])

# Now take the mean across all those classifiers
feature_importance = np.mean(np.abs(coefs), axis=0)

# Plot feature importance
plt.barh(X.columns, feature_importance)
plt.title("Feature Importance (One-vs-One)")
plt.xlabel("Importance")
plt.show()