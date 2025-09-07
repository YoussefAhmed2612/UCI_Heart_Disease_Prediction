import joblib
import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="❤️ Heart Disease Prediction", layout="centered")
st.title("❤️ Heart Disease Prediction App")

pipeline = joblib.load("final_model.pkl")

FEATURES = [    
    "age", "sex", "cp", "fbs", "restecg", "thalach",
    "exang", "oldpeak", "slope", "ca", "thal"
]

user_inputs = {}

# ---------------- PERSONAL INFO ----------------
st.header("👤 Personal Information")
user_inputs["age"] = st.number_input("Age (years)", min_value=18, max_value=100, value=40, step=1)

user_inputs["sex"] = st.radio(
    "Sex",
    options=[0, 1],
    format_func=lambda x: f"{x} - {'Female' if x == 0 else 'Male'}"
)

# ---------------- SYMPTOMS ----------------
st.header("🩺 Symptoms & History")
user_inputs["cp"] = st.selectbox(
    "Chest Pain Type",
    options=[1, 2, 3, 4],
    format_func=lambda x: f"{x} - {['Typical Angina','Atypical Angina','Non-anginal Pain','Asymptomatic'][x-1]}"
)

user_inputs["fbs"] = st.radio(
    "Fasting Blood Sugar > 120 mg/dl",
    options=[0, 1],
    format_func=lambda x: f"{x} - {'No' if x == 0 else 'Yes'}"
)

user_inputs["restecg"] = st.selectbox(
    "Resting ECG Results",
    options=[0, 1, 2],
    format_func=lambda x: f"{x} - {['Normal','ST-T Wave Abnormality','Left Ventricular Hypertrophy'][x]}"
)

# ---------------- EXERCISE TEST RESULTS ----------------
st.header("🏃 Exercise Test Results")
user_inputs["thalach"] = st.slider(
    "Maximum Heart Rate Achieved (thalach)",
    min_value=60, max_value=220, value=150, step=1
)

user_inputs["exang"] = st.radio(
    "Exercise Induced Angina",
    options=[0, 1],
    format_func=lambda x: f"{x} - {'No' if x == 0 else 'Yes'}"
)

user_inputs["oldpeak"] = st.slider(
    "ST Depression (oldpeak)",
    min_value=0.0, max_value=6.0, value=1.0, step=0.1
)

user_inputs["slope"] = st.selectbox(
    "Slope of Peak Exercise ST Segment",
    options=[1, 2, 3],
    format_func=lambda x: f"{x} - {['Upsloping','Flat','Downsloping'][x-1]}"
)

# ---------------- IMAGING ----------------
st.header("🧪 Imaging Results")
user_inputs["ca"] = st.selectbox(
    "Number of Major Vessels Colored by Fluoroscopy",
    options=[0, 1, 2, 3],
    format_func=lambda x: f"{x} - {x} Vessels"
)

user_inputs["thal"] = st.selectbox(
    "Thalassemia",
    options=[3, 6, 7],
    format_func=lambda x: f"{x} - {['Normal','Fixed Defect','Reversible Defect'][[3,6,7].index(x)]}"
)

# ---------------- PREDICTION ----------------
input_df = pd.DataFrame([user_inputs], columns=FEATURES)

if st.button("🔍 Predict"):
    prediction = pipeline.predict(input_df)[0]
    proba = pipeline.predict_proba(input_df)[0][1]

    st.header("📊 Prediction Result")
    if prediction == 1:
        st.error("⚠️ The model predicts **Heart Disease**")
    else:
        st.success("✅ The model predicts **No Heart Disease**")

    st.info(f"Probability of Heart Disease: **{proba:.2f}**")
