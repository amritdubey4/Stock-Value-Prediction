import numpy as np
from tensorflow.keras.models import load_model

# Load model and last 60 days
model = load_model("lstm_stock_model.h5")
scaled_data = np.load("X.npy")  # use last sequence from X
last_60_days = scaled_data[-1].reshape(1, 60, 1)

# Predict
predicted_price = model.predict(last_60_days)

# Inverse scaling
scaler_min = np.load("scaler_min.npy")
scaler_max = np.load("scaler_max.npy")
actual_price = predicted_price[0][0] * (scaler_max - scaler_min) + scaler_min
print(f"📈 Predicted next day price for Tata Motors: ₹{actual_price:.2f}")