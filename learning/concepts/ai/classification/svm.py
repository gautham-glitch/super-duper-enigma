import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize,StandardScaler
from sklearn.utils.class_weight import compute_sample_weight
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score
from sklearn.svm import LinearSVC

import warnings as w
w.filterwarnings("ignore")

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/creditcard.csv"
df = pd.read_csv(url)
labels = df.Class.unique()
sizes = df.Class.value_counts().values

df.iloc[:, 1:30] = StandardScaler().fit_transform(df.iloc[:, 1:30])
data_matrix = df.values

x = data_matrix[:, 1:30]
y = data_matrix[:, 30]

x = normalize(x,"l1")

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

w_weights = compute_sample_weight("balanced",y_train)

des_clf = DecisionTreeClassifier(max_depth = 4, random_state = 35)
des_clf.fit(X_train, y_train, w_weights)

svm = LinearSVC(class_weight = "balanced", loss = "hinge", fit_intercept = False, random_state = 31)
svm.fit(X_train, y_train)

y_pred_dt = des_clf.predict_proba(X_test)[:, 1]
r_a_dt = roc_auc_score(y_test,y_pred_dt)
print(r_a_dt)

y_pred_svm = svm.decision_function(X_test)
r_a_svm = roc_auc_score(y_test, y_pred_svm)
print(r_a_svm)
