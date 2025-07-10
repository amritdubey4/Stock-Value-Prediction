# Stock-Value-Prediction
Interactive UI with date range and ticker selection for real-time forecasts of Indian and global stocks using deep learning.
# 📊 AI Stock Price Predictor with LSTM (Colab UI)

This project is an interactive, AI-based stock price prediction tool built in Google Colab using an LSTM (Long Short-Term Memory) neural network. It allows users to select a stock ticker (e.g., TATAMOTORS.NS), pick a custom date range, and get real-time predicted prices along with a visual comparison of actual vs predicted stock movements.

---

## 🚀 Features

- 📅 **Dynamic Date Range Picker**  
  Select any time period from the last decade for analysis.

- 📈 **Interactive UI**  
  Built with `ipywidgets` to provide a user-friendly experience directly inside Colab.

- 🧠 **Deep Learning with LSTM**  
  Uses a two-layer LSTM neural network to predict next-day stock prices based on historical data.

- 🌐 **Supports Indian & Global Stocks**  
  Uses Yahoo Finance (`yfinance`) so you can enter any valid ticker (e.g., `TATAMOTORS.NS`, `AAPL`, `RELIANCE.NS`, `GOOG`, etc.).

---

## 🛠️ How It Works

1. **Enter a stock ticker** (e.g., `TATAMOTORS.NS`)
2. **Pick a start and end date**
3. **Choose the number of training epochs**
4. **Click "Predict ➡️"**
5. 📉 See a plot comparing actual vs predicted closing prices
6. 📌 Get the predicted closing price for the next trading day

---

## 🧪 Technologies Used

- Python
- [Google Colab](https://colab.research.google.com/drive/176zTO7z3kGa8-cWlhVDYNxy70-8HIhMx?usp=sharing)
- TensorFlow / Keras
- scikit-learn
- yfinance
- matplotlib
- ipywidgets

---

## 🖥️ Screenshots

![UI Preview](https://user-images.githubusercontent.com/your-screenshot-placeholder.png)

---

## 📂 File Structure

