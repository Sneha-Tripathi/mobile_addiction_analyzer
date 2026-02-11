import streamlit as st
import joblib
import os

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Mobile Addiction Analyzer",
    page_icon="📱",
    layout="centered"
)

# ------------------ Load Model ------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "mobile_addiction_model.pkl"))
encoder = joblib.load(os.path.join(BASE_DIR, "label_encoder.pkl"))

# ------------------ Minimal CSS ------------------
st.markdown("""
<style>
.main {
    background-color: #121212;
}
.title-text {
    font-size: 34px;
    font-weight: 600;
    color: #2c3e50;
    text-align: center;
    margin-bottom: 6px;
}
.subtitle-text {
    text-align: center;
    color: #6c757d;
    font-size: 16px;
    margin-bottom: 30px;
}
.card {
    background-color: #ffffff;
    padding: 22px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
}
.result-box {
    padding: 16px;
    border-radius: 10px;
    font-size: 20px;
    font-weight: 500;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ------------------ Header ------------------
st.markdown("<div class='title-text'>Mobile Addiction Analyzer</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle-text'>Machine Learning based behavioral analysis system</div>",
    unsafe_allow_html=True
)

# ------------------ Input Card ------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("Enter Usage Details")

col1, col2 = st.columns(2)

with col1:
    screen_time = st.slider("Screen Time (hours/day)", 0, 12, 4)
    phone_checks = st.slider("Phone Checks per Day", 0, 200, 50)
    addiction = st.slider("night usages (hours/day)",0,12,4)

with col2:
    social_media = st.slider("Social Media Usage (minutes/day)", 0, 400, 120)
    sleep_disturbance = st.radio("Sleep Disturbance", ["No", "Yes"])
    anxiety = st.radio("Anxiety Symptoms", ["No", "Yes"])

st.markdown("</div>", unsafe_allow_html=True)

# ------------------ Convert Inputs ------------------
sleep_disturbance = 1 if sleep_disturbance == "Yes" else 0
anxiety = 1 if anxiety == "Yes" else 0

# ------------------ Analyze Button ------------------
st.markdown("<br>", unsafe_allow_html=True)
analyze = st.button("Analyze Addiction Level")

# ------------------ Prediction ------------------
if analyze:
    input_data = [[
        screen_time,
        social_media,
        phone_checks,
        sleep_disturbance,
        anxiety,
        addiction
    ]]

    pred = model.predict(input_data)
    result = encoder.inverse_transform(pred)[0]

    if result.lower() == "healthy":
        bg = "#e9f7ef"
        text = "#1e8449"
        msg = "Healthy Usage Pattern"
    elif result.lower() == "at risk":
        bg = "#fff7e6"
        text = "#9c640c"
        msg = "User is at Risk"
    else:
        bg = "#fdecea"
        text = "#922b21"
        msg = "High Level of Addiction Detected"

    st.markdown(
        f"<div class='result-box' style='background-color:{bg}; color:{text};'>"
        f"{msg}</div>",
        unsafe_allow_html=True
    )

    st.info(
        "Prediction generated using a Random Forest machine learning model "
        "trained on mobile usage behavioral data."
    )

# ------------------ Footer ------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("AI/ML Academic Project | Mobile Addiction Analyzer")