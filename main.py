import streamlit as st
import pandas as pd

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.sidebar.text_input("current stock price", key="current_stock_price")
st.sidebar.text_input("strike price", key="strike_price")
st.sidebar.text_input("time to maturity", key="time_to_maturity")
st.sidebar.text_input("risk free interest rate", key="risk_free_interest_rate")
st.sidebar.text_input("volatility", key="volatility")

st.sidebar.text_input("dividend yield (optional)", key="dividend_yield")

st.write(st.session_state.current_stock_price)