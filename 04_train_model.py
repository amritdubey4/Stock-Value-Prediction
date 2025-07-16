import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input

# Load preprocessed data
X = np.load("X.npy")
y = np.load("y.npy")

# Build model
model = Sequential([
    Input(shape=(X.shape[1], 1)),
    LSTM(50, return_sequences=True),
    LSTM(50),
    Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X, y, epochs=10, batch_size=32)
model.save("lstm_stock_model.h5")
print("✅ Model trained and saved.")