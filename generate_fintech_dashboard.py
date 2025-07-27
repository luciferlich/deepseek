import os

base_dir = "fintech_dashboard"
folders = [
    f"{base_dir}/pages",
    f"{base_dir}/assets",
    f"{base_dir}/models",
    f"{base_dir}/utils"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Init files
init_paths = [
    f"{base_dir}/__init__.py",
    f"{base_dir}/models/__init__.py",
    f"{base_dir}/utils/__init__.py"
]
for path in init_paths:
    with open(path, 'w') as f:
        f.write("")

# Main app
main_app = '''\
import streamlit as st
from pages import price_prediction, volatility_modeling, portfolio_forecasting, anomaly_detection

st.set_page_config(page_title="Fintech ML Dashboard", layout="wide", initial_sidebar_state="expanded")

# Apply dark theme styling
with open("assets/style.css") as f:
    st.markdown(f"<style>{{f.read()}}</style>", unsafe_allow_html=True)

st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/6/6b/Bitcoin.svg", width=60)
st.sidebar.title("📊 ML Navigation")
page = st.sidebar.radio("Go to", ["Landing Page", "Price Prediction", "Volatility Modeling", "Portfolio Forecasting", "Anomaly Detection"])

if page == "Landing Page":
    st.title("📈 Fintech ML Dashboard")
    st.markdown(\"""
    Welcome to the **Fintech ML Dashboard** – an interactive platform combining **modern financial modeling** with **machine learning**.  
    Explore models for:
    - 📉 Price Prediction (LSTM, ARIMA, Linear Regression, Random Forest)
    - 📊 Volatility Modeling (LSTM, GARCH, Attention-based Models)
    - 💼 Portfolio Forecasting (VaR, DeepAR, Transformers)
    - 🚨 Anomaly Detection (Autoencoders, Isolation Forest, HDBSCAN)
    \""")
elif page == "Price Prediction":
    price_prediction.show()
elif page == "Volatility Modeling":
    volatility_modeling.show()
elif page == "Portfolio Forecasting":
    portfolio_forecasting.show()
elif page == "Anomaly Detection":
    anomaly_detection.show()
'''
with open(f"{base_dir}/app.py", "w") as f:
    f.write(main_app)

# CSS (dark theme)
css = '''
body {
    background-color: #111111;
    color: #e0e0e0;
}
h1, h2, h3, h4 {
    color: #66ffcc;
}
.sidebar .sidebar-content {
    background-color: #1e1e1e;
}
.css-1d391kg, .stButton>button {
    background-color: #222831;
    color: #eeeeee;
    border-radius: 5px;
}
'''
with open(f"{base_dir}/assets/style.css", "w") as f:
    f.write(css)

# Page templates
page_template = '''\
import streamlit as st

def show():
    st.title("{title}")
    st.markdown("This section will include interactive visualizations and models for **{desc}**.")
    st.info("🚧 Demo models will appear here. You can later integrate your ML pipelines.")
'''

pages = {
    "price_prediction": ("Price Prediction", "price prediction using LSTM, ARIMA, Linear Regression, and Random Forest"),
    "volatility_modeling": ("Volatility Modeling", "volatility modeling using LSTM, GARCH, and Attention-based models"),
    "portfolio_forecasting": ("Portfolio Forecasting", "portfolio forecasting using VaR, DeepAR, and Transformer-based models"),
    "anomaly_detection": ("Anomaly Detection", "anomaly detection using Autoencoders, Isolation Forest, and HDBSCAN")
}

for filename, (title, desc) in pages.items():
    with open(f"{base_dir}/pages/{filename}.py", "w") as f:
        f.write(page_template.format(title=title, desc=desc))
