from sklearn.datasets import fetch_openml
from sklearn.pipeline import Pipeline
import sklearn as sk
mnist = fetch_openml(name = "mnist_784")
train = mnist.data
test = mnist.target.astype("int")

X_train, X_test, y_train, y_test = sk.model_selection.train_test_split(train, test, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', LogisticRegression(max_iter=1000))
])

pipeline.fit(X_train, y_train)
print("Accuracy:", pipeline.score(X_test, y_test))

