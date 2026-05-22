# 📈 Multi-Stock Return Prediction using Machine Learning

## Project Overview

This project predicts the **next day's stock return percentage** using a Machine Learning regression model trained on historical stock market data.

The model was trained using multiple major technology stocks:

- Apple (AAPL)
- Microsoft (MSFT)
- Tesla (TSLA)
- NVIDIA (NVDA)
- Amazon (AMZN)

The project demonstrates:
- Data collection using Yahoo Finance API
- Feature engineering
- Multi-stock training
- Regression modeling
- Model evaluation
- Data visualization
- Deployment with Streamlit

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- yfinance
- Streamlit
- Joblib

---

# Dataset

Historical stock market data was downloaded using the `yfinance` library.

Data included:
- Open price
- High price
- Low price
- Close price
- Volume

Time range:
- 5 years of daily stock data

---

# Machine Learning Model

Model used:
- Linear Regression

Prediction target:
- Next-day stock return percentage

---

# Features Used

The following engineered features were used for training:

| Feature | Description |
|---|---|
| Return | Daily percentage return |
| Lag1 | Previous day's return |
| Lag2 | Return from 2 days ago |
| MA5 | 5-day moving average |
| Volatility | 5-day rolling standard deviation |
| Volume_MA5 | 5-day average trading volume |

---

# Project Workflow

1. Download stock market data
2. Combine multiple stock datasets
3. Perform feature engineering
4. Create target variable
5. Scale features
6. Train Linear Regression model
7. Evaluate performance
8. Save model and scaler
9. Build Streamlit web app

---

# Evaluation Metrics

The model was evaluated using:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score
- MAPE (Mean Absolute Percentage Error)

---

# Visualizations

The project includes:

- Stock closing price visualization
- Daily returns graph
- Actual vs predicted returns
- Feature importance chart

---

# Streamlit App

The project includes a Streamlit web application where users can:

- Enter any stock ticker
- View stock price chart
- Predict next-day return
- View latest feature values

---

# Folder Structure

```text
stock-price-predictor/
│
├── app/
│   └── app.py
│
├── models/
│   ├── stock_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   └── stock_prediction.ipynb
│
├── README.md
└── requirements.txt
```

---

# Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run the Streamlit App

```bash
cd app
streamlit run app.py
```

If Streamlit command does not work:

```bash
python -m streamlit run app.py
```

---

# Example Output

The model predicts:

```text
Predicted Next-Day Return: 1.24%
```

Positive values:
- expected upward movement

Negative values:
- expected downward movement

---

# Future Improvements

Possible future enhancements:

- Random Forest Regressor
- XGBoost
- LSTM Neural Networks
- Real-time prediction dashboard
- Sentiment analysis using news data
- Market index integration
- Sector-specific models

---

# Key Learnings

This project helped in understanding:

- Time-series machine learning
- Feature engineering
- Multi-stock generalization
- Model evaluation
- Data preprocessing
- ML deployment using Streamlit

---

# Author

Jyuun Singh

# Links

1.Github repo - https://github.com/jyuun-singh/stock-price-predictor.git

2.Streamlit(Deployed model) - https://stock-price-predictor-xjy9hewrd39qz8plnuqjin.streamlit.app/
