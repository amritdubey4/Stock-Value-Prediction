import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# Load data and model
X = np.load("X.npy")
y = np.load("y.npy")
model = load_model("lstm_stock_model.h5")
predicted = model.predict(X)

# Manual inverse transform
scaler_min = np.load("scaler_min.npy")
scaler_max = np.load("scaler_max.npy")
predicted_actual = predicted * (scaler_max - scaler_min) + scaler_min
y_actual = y.reshape(-1, 1) * (scaler_max - scaler_min) + scaler_min

# Plot
plt.figure(figsize=(14,6))
plt.plot(y_actual, label='Actual Price')
plt.plot(predicted_actual, label='Predicted Price')
plt.title("Tata Motors Price Prediction using LSTM")
plt.xlabel("Days")
plt.ylabel("Price (INR)")
plt.legend()
plt.grid(True)
plt.show()