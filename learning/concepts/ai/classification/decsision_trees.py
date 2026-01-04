import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics

import warnings as w
w.filterwarnings("ignore")

path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/drug200.csv"
df = pd.read_csv(path)


label_encoder = LabelEncoder()
df["Sex"] = label_encoder.fit_transform(df["Sex"])
df["Cholesterol"] = label_encoder.fit_transform(df["Cholesterol"])
df["BP"] = label_encoder.fit_transform(df["BP"])

cust_map = {
    "drugA":1,
    "drugB":2,
    "drugC":3,
    "drugX":4,
    "drugY":5
}
df['Drug_num'] = df['Drug'].map(cust_map)
print(df.drop('Drug', axis=1).corr()['Drug_num'])

category_counts = df["Drug"].value_counts()

x = df.drop(["Drug","Drug_num"], axis = 1)
y = df["Drug_num"]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 32)
Drug_tree = DecisionTreeClassifier(criterion = "entropy", max_depth = 4)

Drug_tree.fit(X_train, y_train)

print(f"accuracy = {100 * metrics.accuracy_score(y_test, Drug_tree.predict(X_test))}%")

plot_tree(Drug_tree)
plt.show()