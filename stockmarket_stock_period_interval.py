import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Function to fetch stock data
def get_stock_data(ticker, period, interval):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)
    return df

# Streamlit UI
st.title("Real-Time Stock Price and Volume")

ticker = st.text_input("Enter Stock Ticker (e.g., SPY, QQQ)", "SPY")
period = st.selectbox("Select Period", ["1d", "5d", "7d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "max"], index=2)
interval = st.selectbox("Select Interval", ["1m", "5m", "15m", "30m", "60m", "90m", "1d", "5d", "1wk", "1mo", "3mo"], index=4)

df = get_stock_data(ticker, period, interval)

# Display stock price and volume
table = df[['Close', 'Volume']]
st.write(table)
