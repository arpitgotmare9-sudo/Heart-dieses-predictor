import pandas as pd
import numpy as np
import streamlit as st
import pickle
st.set_page_config(
    page_title="Heart Disease Predictor", page_icon="🫀", layout="wide"
)

# Custom CSS for modern UI design
st.markdown(
    """
    <style>
    /* Background with dark overlay for readability */
    .stApp {
        background: linear-gradient(rgba(15, 23, 42, 0.75), rgba(15, 23, 42, 0.75)),
                    url("https://images.stockcake.com/public/d/9/e/d9e0f1cb-6bb7-406a-aa30-c72cf629d5ac_large/hospital-emergency-room-stockcake.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* Header Styling */
    h1 {
        color: #ffffff !important;
        text-align: center;
        font-weight: 700 !important;
        letter-spacing: 1px;
        margin-bottom: 2rem !important;
        text-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
    }

    /* Input Field Labels */
    .stNumberInput label, .stSelectbox label {
        color: #e2e8f0 !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }

    /* Input Container Cards (Glassmorphism Effect) */
    div[data-testid="column"] {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 16px;
        padding: 24px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }

    /* Style Input Controls */
    div[data-baseweb="input"] input, div[data-baseweb="select"] {
        border-radius: 8px !important;
        background-color: rgba(255, 255, 255, 0.9) !important;
        color: #0f172a !important;
    }

    /* Primary Button Styling */
    div.stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        color: white;
        font-size: 1.1rem;
        font-weight: 700;
        padding: 12px 24px;
        border-radius: 10px;
        border: none;
        box-shadow: 0 4px 14px 0 rgba(220, 38, 38, 0.4);
        transition: all 0.3s ease;
        margin-top: 1.5rem;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px 0 rgba(220, 38, 38, 0.6);
        background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%);
        color: white;
    }

    /* Hide default Streamlit footer & top header bar */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)
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
