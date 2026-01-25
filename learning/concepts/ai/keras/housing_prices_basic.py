import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score, mean_absolute_percentage_error
import keras
from keras import layers
import warnings
warnings.filterwarnings("ignore")

# 1. Direct loading
X, y = fetch_california_housing(return_X_y=True)

# 2. Split data 
X_train_raw, X_test_raw, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Proper Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train_raw)
X_test = scaler.transform(X_test_raw)

# 4. Keras Model
def build_nn(input_dim):
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=(input_dim,)),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

# --- Execution ---

# Neural Network
nn_model = build_nn(X_train.shape[1])
callback = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

nn_model.fit(X_train, y_train, epochs=10, 
             validation_split=0.2, callbacks=[callback])

# Polynomial Regression
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_reg = LinearRegression().fit(X_train_poly, y_train)

# --- Results with Accuracy ---
def evaluate(name, model, x, y_true, is_nn=False):
    preds = model.predict(x, verbose=0).flatten() if is_nn else model.predict(x)
    
    mae = mean_absolute_error(y_true, preds)
    r2 = r2_score(y_true, preds)
    
    # In regression, "Accuracy" is interpreted via MAPE (1 - error rate)
    mape = mean_absolute_percentage_error(y_true, preds)
    accuracy = (1 - mape) * 100

    print(f"{name} Results:")
    print(f"  MAE:      {mae:.4f}")
    print(f"  R2 Score: {r2:.4f}")
    print(f"  Accuracy: {accuracy:.2f}%")
    print("-" * 25)

evaluate("Neural Network", nn_model, X_test, y_test, is_nn=True)
evaluate("Polynomial Reg", poly_reg, X_test_poly, y_test)