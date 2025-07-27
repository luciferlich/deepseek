import streamlit as st
import os
from pages import price_prediction, volatility_modeling, portfolio_forecasting, anomaly_detection

st.set_page_config(page_title="Fintech ML Dashboard", layout="wide", initial_sidebar_state="expanded")

# Load CSS from the correct relative path
css_path = os.path.join(os.path.dirname(__file__), "assets", "style.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/6/6b/Bitcoin.svg", width=60)
st.sidebar.title("📊 ML Navigation")
page = st.sidebar.radio("Go to", ["Landing Page", "Price Prediction", "Volatility Modeling", "Portfolio Forecasting", "Anomaly Detection"])

if page == "Landing Page":
    st.title("📈 Fintech ML Dashboard")
    st.markdown("""
    Welcome to the **Fintech ML Dashboard** – an interactive platform combining **modern financial modeling** with **machine learning**.  
    Explore models for:
    - 📉 Price Prediction (LSTM, ARIMA, Linear Regression, Random Forest)
    - 📊 Volatility Modeling (LSTM, GARCH, Attention-based Models)
    - 💼 Portfolio Forecasting (VaR, DeepAR, Transformers)
    - 🚨 Anomaly Detection (Autoencoders, Isolation Forest, HDBSCAN)
    """)
elif page == "Price Prediction":
    price_prediction.show()
elif page == "Volatility Modeling":
    volatility_modeling.show()
elif page == "Portfolio Forecasting":
    portfolio_forecasting.show()
elif page == "Anomaly Detection":
    anomaly_detection.show()
