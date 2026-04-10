import streamlit as st
import joblib
import numpy as np

# --- GUI IMPROVEMENTS: Page Config and Custom CSS ---
st.set_page_config(page_title="Mining Quality Prediction", page_icon="⛏️", layout="wide")

st.markdown("""
<style>
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 50px;
        font-size: 20px;
        font-weight: bold;
        background-color: #FF4B4B;
        color: white;
        transition: all 0.3s ease-in-out;
    }
    .stButton > button:hover {
        background-color: #FF6666;
        box-shadow: 0px 4px 10px rgba(255, 75, 75, 0.4);
    }
    h1 {
        text-align: center;
        color: #2E3A59;
    }
    /* Add a clean background to the input sections */
    div[data-testid="column"] > div {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
</style>
""", unsafe_allow_html=True)

model = joblib.load("mining_model.pkl")

# --- GUI IMPROVEMENTS: Header Section ---
st.markdown("<h1>⛏️ Mining Quality Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; color: #555;'>Predict the iron concentrate based on plant process parameters</p>", unsafe_allow_html=True)

col_info1, col_info2, col_info3 = st.columns([1, 2, 1])
with col_info2:
    st.info(f"ℹ️ Model expects {model.n_features_in_} features")

st.markdown("---")

# --- GUI IMPROVEMENTS: Structured Form Layout ---
st.header("📊 Input Plant Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🟢 Feed & Pulp Properties")
    iron_feed = st.number_input("Iron Feed", format="%.4f")
    silica_feed = st.number_input("Silica Feed", format="%.4f")
    starch_flow = st.number_input("Starch Flow", format="%.4f")
    amina_flow = st.number_input("Amina Flow", format="%.4f")
    ore_pulp_flow = st.number_input("Ore Pulp Flow", format="%.4f")
    ore_pulp_ph = st.number_input("Ore Pulp pH", format="%.4f")
    ore_pulp_density = st.number_input("Ore Pulp Density", format="%.4f")
    fl8 = st.number_input("Extra Feature", format="%.4f")

with col2:
    st.subheader("💨 Flotation Col. Air Flow")
    fc1 = st.number_input("Flotation Column 01 Air Flow", format="%.4f")
    fc2 = st.number_input("Flotation Column 02 Air Flow", format="%.4f")
    fc3 = st.number_input("Flotation Column 03 Air Flow", format="%.4f")
    fc4 = st.number_input("Flotation Column 04 Air Flow", format="%.4f")
    fc5 = st.number_input("Flotation Column 05 Air Flow", format="%.4f")
    fc6 = st.number_input("Flotation Column 06 Air Flow", format="%.4f")
    fc7 = st.number_input("Flotation Column 07 Air Flow", format="%.4f")

with col3:
    st.subheader("💧 Flotation Col. Level")
    fl1 = st.number_input("Flotation Column 01 Level", format="%.4f")
    fl2 = st.number_input("Flotation Column 02 Level", format="%.4f")
    fl3 = st.number_input("Flotation Column 03 Level", format="%.4f")
    fl4 = st.number_input("Flotation Column 04 Level", format="%.4f")
    fl5 = st.number_input("Flotation Column 05 Level", format="%.4f")
    fl6 = st.number_input("Flotation Column 06 Level", format="%.4f")
    fl7 = st.number_input("Flotation Column 07 Level", format="%.4f")

st.markdown("---")

# --- GUI IMPROVEMENTS: Center-aligned prediction button ---
st.markdown("<br>", unsafe_allow_html=True)
_, col_btn, _ = st.columns([1, 2, 1])

with col_btn:
    if st.button("🚀 Predict", use_container_width=True):
        # Keep prediction logic unmodified
        data = np.array([[iron_feed,
                          silica_feed,
                          starch_flow,
                          amina_flow,
                          ore_pulp_flow,
                          ore_pulp_ph,
                          ore_pulp_density,
                          fc1,fc2,fc3,fc4,fc5,fc6,fc7,
                          fl1,fl2,fl3,fl4,fl5,fl6,fl7,fl8]])

        prediction = model.predict(data)

        st.markdown("<br>", unsafe_allow_html=True)
        st.success(f"🎯 **Predicted Iron Concentrate:** `{prediction[0]}`")
