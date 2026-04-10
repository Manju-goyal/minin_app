import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import gdown
import os

st.set_page_config(page_title="Mining Prediction", layout="wide")

st.title("⛏️ Mining Quality Prediction System")

# ---------------- DOWNLOAD MODEL ----------------
MODEL_URL = "https://drive.google.com/uc?id=1aOI_OTW-Ax6Z4Kt2dvLacUl6LNwpgum0"

if not os.path.exists("model.pkl"):
    with st.spinner("Downloading model... please wait ⏳"):
        gdown.download(MODEL_URL, "model.pkl", quiet=False)

# ---------------- DOWNLOAD DATASET ----------------
DATA_URL = "https://drive.google.com/uc?id=1V91HUonlI9l7FuSt6uoT49NNdjJ6AeYm"

if not os.path.exists("data.csv"):
    with st.spinner("Downloading dataset... please wait ⏳"):
        gdown.download(DATA_URL, "data.csv", quiet=False)

# ---------------- LOAD MODEL ----------------
model = joblib.load("model.pkl")

# ---------------- LOAD DATA ----------------
df = pd.read_csv("data.csv")

df = df.drop(columns=["date"], errors="ignore")

# Clean same as training
for col in df.columns:
    df[col] = df[col].astype(str).str.replace(',', '.')
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna()

target = "% Silica Concentrate"

# ---------------- GRAPH ----------------
st.subheader("📊 Data Insights")

fig1 = plt.figure()
df[target].hist(bins=30)
plt.title("Silica Distribution")
st.pyplot(fig1)

# ---------------- INPUT ----------------
st.subheader("🧾 Enter Sensor Values")

input_data = []

for col in df.columns:
    if col != target:
        val = st.number_input(
            f"{col}",
            value=float(df[col].mean())
        )
        input_data.append(val)

# ---------------- PREDICT ----------------
if st.button("Predict"):
    arr = np.array(input_data).reshape(1, -1)
    pred = model.predict(arr)

    st.success(f"Predicted Silica Concentrate: {pred[0]:.3f}")

    fig2 = plt.figure()
    plt.bar(["Prediction"], [pred[0]])
    plt.title("Prediction Output")
    st.pyplot(fig2)
