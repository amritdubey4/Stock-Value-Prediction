import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load and clean data
df = pd.read_csv("TATAMOTORS.csv")
df = df[['Close']].dropna()
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df)

# Create sequences
X = []
y = []
for i in range(60, len(scaled_data)):
    X.append(scaled_data[i-60:i, 0])
    y.append(scaled_data[i, 0])

X = np.array(X)
y = np.array(y)
X = X.reshape((X.shape[0], X.shape[1], 1))

np.save("X.npy", X)
np.save("y.npy", y)
np.save("scaler_min.npy", scaler.data_min_)
np.save("scaler_max.npy", scaler.data_max_)

print("✅ Preprocessing done. Saved X, y, and scaler values.")