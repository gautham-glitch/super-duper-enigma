from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import fetch_openml

# as_frame=False returns NumPy arrays directly
mnist = fetch_openml(name="mnist_784", as_frame=False)
X, y = mnist.data, mnist.target.astype("int")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', LogisticRegression(max_iter=1000, solver='saga', n_jobs=-1))
])

pipeline.fit(X_train, y_train)
print(f"Accuracy: {pipeline.score(X_test, y_test):.4f}")

