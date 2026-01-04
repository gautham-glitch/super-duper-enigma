from scipy.io import loadmat
from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier

# Load the .mat file
mat = loadmat("C:/Users/kaart/Downloads/emnist-letters.mat")
data = mat["dataset"]

# Extract images and labels
X = data["train"][0,0]["images"][0,0]
y = data["train"][0,0]["labels"][0,0]

# Normalize pixel values
X = X / 255.0

# Split into 60,000 train and 10,000 test
X_train, X_test = X[:60000], X[60000:70000]
y_train, y_test = y[:60000], y[60000:70000]

# Reshape to flat 784-length vectors
X_train = X_train.reshape((-1, 784), order='F')
X_test = X_test.reshape((-1, 784), order='F')

mlp1 = MLPClassifier(hidden_layer_sizes=(50,), max_iter=20, solver = "sgd", alpha=1e-4, verbose=10, tol=1e-4, random_state=1,
                     learning_rate_init=.1)
mlp1.fit(X_train, y_train)
print("Training set score: %f" % mlp1.score(X_train, y_train))
print("Test set score: %f" % mlp1.score(X_test, y_test))


