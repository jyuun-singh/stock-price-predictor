import streamlit as st
import yfinance as yf
import pandas as pd
import joblib

model = joblib.load('models/stock_model.pkl')
scaler = joblib.load('models/scaler.pkl')

st.title("📈 Stock Return Predictor")

ticker = st.text_input(
    "Enter Stock Ticker",
    "AAPL"
)

data = yf.download(
    ticker,
    period='6mo'
)

data.columns = data.columns.get_level_values(0)

data.reset_index(inplace=True)

data['Return'] = data['Close'].pct_change()

data['Lag1'] = data['Return'].shift(1)

data['Lag2'] = data['Return'].shift(2)

data['MA5'] = (
    data['Close']
    .rolling(5)
    .mean()
)

data['Volatility'] = (
    data['Return']
    .rolling(5)
    .std()
)

data['Volume_MA5'] = (
    data['Volume']
    .rolling(5)
    .mean()
)

data = data.dropna()

st.subheader("Closing Price")

st.line_chart(
    data.set_index('Date')['Close']
)

features = [
    'Return',
    'Lag1',
    'Lag2',
    'MA5',
    'Volatility',
    'Volume_MA5'
]

latest_data = data[features].iloc[-1:]

latest_scaled = scaler.transform(
    latest_data
)

prediction = model.predict(
    latest_scaled
)[0]

st.subheader("Prediction")

st.metric(
    "Predicted Next-Day Return",
    f"{prediction * 100:.2f}%"
)

if prediction > 0:

    st.success(
        "📈 Model predicts UP movement"
    )

else:

    st.error(
        "📉 Model predicts DOWN movement"
    )

st.subheader("Latest Features")

st.dataframe(latest_data)
