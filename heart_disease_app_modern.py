import pandas as pd
import streamlit as st
import pickle

st.set_page_config(
    page_title="CardioCheck AI",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Custom styling
# -----------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    .stApp {
        background:
            radial-gradient(circle at 10% 10%, rgba(239,68,68,.16), transparent 30%),
            radial-gradient(circle at 90% 20%, rgba(59,130,246,.12), transparent 28%),
            #07111f;
        color: #e5e7eb;
        font-family: 'Inter', sans-serif;
    }

    #MainMenu, footer, header { visibility: hidden; }

    .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .hero {
        padding: 28px 32px;
        border: 1px solid rgba(255,255,255,.10);
        border-radius: 24px;
        background: linear-gradient(135deg, rgba(255,255,255,.09), rgba(255,255,255,.035));
        backdrop-filter: blur(18px);
        margin-bottom: 24px;
    }

    .hero-badge {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 999px;
        background: rgba(239,68,68,.14);
        color: #fca5a5;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: .4px;
        margin-bottom: 12px;
    }

    .hero h1 {
        color: white !important;
        font-size: 42px !important;
        line-height: 1.1 !important;
        margin: 0 !important;
        text-align: left !important;
        letter-spacing: -1.5px !important;
    }

    .hero p {
        color: #94a3b8;
        font-size: 16px;
        margin: 10px 0 0 0;
    }

    .section-title {
        color: #f8fafc;
        font-size: 21px;
        font-weight: 800;
        margin: 26px 0 12px 0;
    }

    .section-subtitle {
        color: #94a3b8;
        font-size: 13px;
        margin-top: -7px;
        margin-bottom: 15px;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255,255,255,.045);
        border: 1px solid rgba(255,255,255,.09);
        border-radius: 18px;
        padding: 16px;
    }

    .stNumberInput label, .stSelectbox label {
        color: #cbd5e1 !important;
        font-weight: 600 !important;
        font-size: 13px !important;
    }

    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div {
        background: rgba(15,23,42,.85) !important;
        border: 1px solid rgba(148,163,184,.20) !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="input"] input {
        color: #f8fafc !important;
    }

    div[data-baseweb="select"] * {
        color: #f8fafc !important;
    }

    .stButton > button {
        width: 100%;
        min-height: 52px;
        border: 0;
        border-radius: 13px;
        color: white;
        font-size: 16px;
        font-weight: 800;
        background: linear-gradient(135deg, #ef4444, #dc2626);
        box-shadow: 0 10px 25px rgba(220,38,38,.25);
        transition: .2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 14px 30px rgba(220,38,38,.35);
    }

    .result-card {
        margin-top: 24px;
        padding: 26px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,.10);
        background: rgba(255,255,255,.055);
        backdrop-filter: blur(15px);
    }

    .result-title {
        font-size: 26px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .result-normal { color: #4ade80; }
    .result-high { color: #f87171; }

    .probability {
        font-size: 38px;
        font-weight: 800;
        color: white;
        margin: 5px 0 12px;
    }

    .bar {
        width: 100%;
        height: 12px;
        border-radius: 999px;
        background: rgba(148,163,184,.16);
        overflow: hidden;
    }

    .bar-fill {
        height: 100%;
        border-radius: 999px;
        background: linear-gradient(90deg, #22c55e, #facc15, #ef4444);
    }

    .metric-card {
        padding: 18px;
        border-radius: 16px;
        background: rgba(255,255,255,.045);
        border: 1px solid rgba(255,255,255,.08);
        text-align: center;
    }

    .metric-label {
        color: #94a3b8;
        font-size: 12px;
        font-weight: 600;
    }

    .metric-value {
        color: #f8fafc;
        font-size: 22px;
        font-weight: 800;
        margin-top: 4px;
    }

    .footer-note {
        color: #64748b;
        text-align: center;
        font-size: 12px;
        margin-top: 30px;
    }

    .stAlert {
        border-radius: 14px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Load model
# -----------------------------
try:
    with open("heart_disease_model.pkl", "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("heart_disease_model.pkl was not found in the same folder as this app.")
    st.stop()

# -----------------------------
# Hero
# -----------------------------
st.markdown(
    """
    <div class="hero">
        <div class="hero-badge">AI-POWERED HEALTH SCREENING</div>
        <h1>🫀 CardioCheck AI</h1>
        <p>Enter patient information below to generate a heart-disease risk prediction.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Patient information
# -----------------------------
st.markdown('<div class="section-title">👤 Patient Information</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Basic demographic and metabolic information</div>',
    unsafe_allow_html=True,
)

with st.container(border=True):
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        age = st.number_input("Age", min_value=1, max_value=120, value=30)

    with c2:
        gender = st.selectbox("Gender", ["Male", "Female"])

    with c3:
        glucose = st.number_input(
            "Glucose (mg/dL)", min_value=0, max_value=500, value=100
        )

    with c4:
        cholesterol = st.number_input(
            "Cholesterol (mg/dL)", min_value=0, max_value=500, value=200
        )

# -----------------------------
# Vital signs
# -----------------------------
st.markdown('<div class="section-title">❤️ Vital Signs</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Blood pressure, BMI and heart-rate measurements</div>',
    unsafe_allow_html=True,
)

with st.container(border=True):
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        systolic_bp = st.number_input(
            "Systolic BP", min_value=0, max_value=300, value=120
        )

    with c2:
        diastolic_bp = st.number_input(
            "Diastolic BP", min_value=0, max_value=200, value=80
        )

    with c3:
        bmi = st.number_input(
            "BMI", min_value=0.0, max_value=100.0, value=25.0, step=0.1
        )

    with c4:
        heart_rate = st.number_input(
            "Heart Rate (bpm)", min_value=0, max_value=250, value=70
        )

# -----------------------------
# Lifestyle
# -----------------------------
st.markdown('<div class="section-title">🏃 Lifestyle & History</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Lifestyle habits and family history</div>',
    unsafe_allow_html=True,
)

with st.container(border=True):
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        smoking = st.selectbox("Smoking", ["No", "Yes"])

    with c2:
        alcohol_consumption = st.selectbox(
            "Alcohol Consumption", ["No", "Yes"]
        )

    with c3:
        physical_activity = st.selectbox(
            "Physical Activity", ["Low", "Medium", "High"]
        )

    with c4:
        family_history = st.selectbox("Family History", ["No", "Yes"])

# -----------------------------
# Prediction
# -----------------------------
st.markdown('<div class="section-title">🔬 Risk Assessment</div>', unsafe_allow_html=True)

input_data = pd.DataFrame(
    {
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
        "family_history": [family_history],
    }
)

if st.button("🧠 Analyze Heart-Disease Risk"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    probability_pct = probability * 100

    if prediction == 1:
        title = "Higher Predicted Risk"
        description = "The model predicts a positive heart-disease outcome."
        result_class = "result-high"
        icon = "⚠️"
    else:
        title = "Lower Predicted Risk"
        description = "The model predicts a negative heart-disease outcome."
        result_class = "result-normal"
        icon = "✅"

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-title {result_class}">{icon} {title}</div>
            <div style="color:#94a3b8; margin-bottom:12px;">{description}</div>
            <div class="probability">{probability_pct:.1f}%</div>
            <div style="color:#94a3b8; font-size:13px; margin-bottom:8px;">
                Predicted probability of a positive outcome
            </div>
            <div class="bar">
                <div class="bar-fill" style="width:{probability_pct:.1f}%;"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)

    with m1:
        st.markdown(
            f'<div class="metric-card"><div class="metric-label">AGE</div>'
            f'<div class="metric-value">{age}</div></div>',
            unsafe_allow_html=True,
        )

    with m2:
        st.markdown(
            f'<div class="metric-card"><div class="metric-label">BMI</div>'
            f'<div class="metric-value">{bmi:.1f}</div></div>',
            unsafe_allow_html=True,
        )

    with m3:
        st.markdown(
            f'<div class="metric-card"><div class="metric-label">HEART RATE</div>'
            f'<div class="metric-value">{heart_rate} bpm</div></div>',
            unsafe_allow_html=True,
        )

st.markdown(
    '<div class="footer-note">For educational/project demonstration only. '
    'This prediction is not a medical diagnosis.</div>',
    unsafe_allow_html=True,
)
