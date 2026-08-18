import pandas as pd
import numpy as np
import streamlit as st
import pickle

with open("heart_disease_model.pkl", "rb") as file:
    model = pickle.load(file)
st.title("Heart Deaseas Predictor")
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    glucose = st.number_input(
        "Glucose (mg/dL)",
        min_value=0,
        max_value=500,
        value=100
    )

    cholesterol = st.number_input(
        "Cholesterol (mg/dL)",
        min_value=0,
        max_value=500,
        value=200
    )
with col2:
    systolic_bp = st.number_input(
        "Systolic BP",
        min_value=0,
        max_value=300,
        value=120
    )

    diastolic_bp = st.number_input(
        "Diastolic BP",
        min_value=0,
        max_value=200,
        value=80
    )

    bmi = st.number_input(
        "BMI",
        min_value=0.0,
        max_value=100.0,
        value=25.0
    )

    heart_rate = st.number_input(
        "Heart Rate",
        min_value=0,
        max_value=250,
        value=70
    )

with col3:
    smoking = st.selectbox(
        "Smoking",
        ["No", "Yes"]
    )

    alcohol_consumption = st.selectbox(
        "Alcohol Consumption",
        ["No", "Yes"]
    )

    physical_activity = st.selectbox(
        "Physical Activity",
        ["Low", "Medium", "High"]
    )

    family_history = st.selectbox(
        "Family History",
        ["No", "Yes"]
    )
input_data = pd.DataFrame({
    "age": [age],
    "gender": [gender],
    "glucose_mg_dl": [glucose],
    "cholesterol_mg_dl": [cholesterol],
    "systolic_bp": [systolic_bp],
    "diastolic_bp": [diastolic_bp],
    "bmi": [bmi],
    "heart_rate": [heart_rate],
    "smoking": [smoking],
    "alcohol_consumption": [alcohol_consumption],
    "physical_activity": [physical_activity],
    "family_history": [family_history]
})
if st.button("Predict"):

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error("Heart Disease Detected")
    else:
        st.success("No Heart Disease Detected")

    st.write(f"Probability: {probability:.2%}")
