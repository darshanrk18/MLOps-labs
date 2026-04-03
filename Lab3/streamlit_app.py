import os

import requests
import streamlit as st


API_URL = os.getenv("API_URL", "http://127.0.0.1:8080")

st.set_page_config(
    page_title="Iris Predictor",
    page_icon="🌿",
    layout="centered",
)

st.title("Iris Prediction Dashboard")
st.write(
    "This customized frontend sends flower measurements to the Flask API and "
    "displays both the predicted class and model confidence."
)

with st.sidebar:
    st.header("API Configuration")
    st.code(API_URL)
    st.caption("Set the `API_URL` environment variable to point to Cloud Run or a local server.")

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1, 0.1)
    sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5, 0.1)

with col2:
    petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4, 0.1)
    petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2, 0.1)

if st.button("Predict Iris Class"):
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
    }

    try:
        response = requests.post(f"{API_URL}/predict", json=payload, timeout=10)
        response.raise_for_status()
        result = response.json()

        st.success(f"Prediction: {result['prediction']}")
        st.metric("Confidence", f"{result['confidence']:.2%}")
        st.json(result["probabilities"])
    except requests.RequestException as exc:
        st.error(f"Request failed: {exc}")
