import streamlit as st
import pandas as pd
import joblib
import base64
import os
import sys

sys.path.append('..')
try:
    from database import save_prediction, init_database
    init_database()
    DB_AVAILABLE = True
except Exception:
    DB_AVAILABLE = False

# ── Load Model ────────────────────────────────────────────────────────────────
try:
    model = joblib.load("stroke_model.pkl")
    threshold = joblib.load("threshold.pkl")
except Exception:
    st.error("⚠️ Model files not found. Please run train_model.py first.")
    st.stop()

st.set_page_config(page_title="🧠 Stroke Risk Predictor", layout="wide")

# ── Background ────────────────────────────────────────────────────────────────
def set_bg(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as img:
            encoded = base64.b64encode(img.read()).decode()
        st.markdown(f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>""", unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        </style>""", unsafe_allow_html=True)

set_bg("img4.avif")

st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none !important;}
    .block-container { padding-top: 1rem; }

    .result-card {
        padding: 25px 30px;
        border-radius: 18px;
        margin: 20px 0;
        font-size: 17px;
        line-height: 1.7;
    }
    .high-risk {
        background: linear-gradient(135deg, #ff4b4b22, #ff000011);
        border: 2px solid #ff4b4b;
    }
    .low-risk {
        background: linear-gradient(135deg, #00c85122, #00800011);
        border: 2px solid #00c851;
    }
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white; border: none; border-radius: 12px;
        padding: 13px 30px; font-size: 17px; font-weight: 700;
    }
    .stButton > button:hover { transform: translateY(-2px); }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("<h1 style='text-align:center;color:#003366;'>🧠 Brain Stroke Risk Prediction</h1>",
            unsafe_allow_html=True)

# Show login reminder if not logged in
if not st.session_state.get("logged_in", False):
    st.info("💡 **Tip:** Login or register to save your predictions and track your risk over time!")

st.markdown("---")
st.subheader("📝 Enter Your Health Data")

left, right = st.columns(2)

with left:
    age = st.slider("🎂 Age", 1, 100, 45)
    gender = st.radio("⚥ Gender", ["Male", "Female"])
    hypertension = st.radio("🩺 Hypertension (High BP)?", ["Yes", "No"])
    heart_disease = st.radio("❤️ Heart Disease?", ["Yes", "No"])
    ever_married = st.radio("💑 Ever Married?", ["Yes", "No"])
    work_type = st.selectbox("💼 Work Type",
                             ["Private", "Self-employed", "Govt_job", "children", "Never_worked"])

with right:
    residence = st.radio("🏠 Residence Type", ["Urban", "Rural"])
    avg_glucose_level = st.number_input("🌿 Average Glucose Level (mg/dL)",
                                        min_value=40.0, max_value=400.0, value=100.0)
    bmi = st.number_input("⚖️ BMI", min_value=10.0, max_value=70.0, value=25.0)
    smoking_status = st.selectbox("🚬 Smoking Status",
                                  ["never smoked", "formerly smoked", "smokes", "Unknown"])

st.markdown("---")

# ── Prediction ────────────────────────────────────────────────────────────────
if st.button("🔮 Predict My Stroke Risk", use_container_width=True):
    try:
        input_data = pd.DataFrame({
            "gender": [1 if gender == "Male" else 0],
            "age": [age],
            "hypertension": [1 if hypertension == "Yes" else 0],
            "heart_disease": [1 if heart_disease == "Yes" else 0],
            "ever_married": [1 if ever_married == "Yes" else 0],
            "work_type": [work_type],
            "Residence_type": [residence],
            "avg_glucose_level": [avg_glucose_level],
            "bmi": [bmi],
            "smoking_status": [smoking_status]
        })

        input_data["work_type"] = input_data["work_type"].map({
            "Private": 0, "Self-employed": 1, "Govt_job": 2,
            "children": 3, "Never_worked": 4
        })
        input_data["Residence_type"] = input_data["Residence_type"].map({"Urban": 1, "Rural": 0})
        input_data["smoking_status"] = input_data["smoking_status"].map({
            "never smoked": 0, "formerly smoked": 1, "smokes": 2, "Unknown": 3
        })

        probability = model.predict_proba(input_data)[0][1]
        risk_level = "High" if probability >= threshold else "Low"

        # ── Save to DB if logged in ────────────────────────────────────────────
        prediction_id = None
        if DB_AVAILABLE and st.session_state.get("logged_in", False):
            prediction_id = save_prediction(
                user_id=st.session_state.user_id,
                age=age,
                gender=gender,
                bmi=bmi,
                glucose_level=avg_glucose_level,
                hypertension=1 if hypertension == "Yes" else 0,
                heart_disease=1 if heart_disease == "Yes" else 0,
                ever_married=1 if ever_married == "Yes" else 0,
                work_type=work_type,
                residence_type=residence,
                smoking_status=smoking_status,
                risk_probability=round(probability, 4),
                risk_level=risk_level
            )
            st.success("✅ Prediction saved to your health record!")

        # Store in session for chatbot and doctor finder to use
        st.session_state.last_prediction = {
            "risk_level": risk_level,
            "probability": probability,
            "prediction_id": prediction_id
        }

        # ── Display Result ─────────────────────────────────────────────────────
        if risk_level == "High":
            st.markdown(f"""
            <div class='result-card high-risk'>
                <h2 style='color:#cc0000;'>🚨 HIGH RISK of Stroke</h2>
                <p><strong>Risk Probability: {probability:.2%}</strong></p>
                <p>⚠️ Please consult a neurologist as soon as possible.
                Use the <strong>Find Doctors</strong> page to book an appointment with a nearby specialist.</p>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class='result-card low-risk'>
                <h2 style='color:#006600;'>✅ LOW RISK of Stroke</h2>
                <p><strong>Risk Probability: {probability:.2%}</strong></p>
                <p>💡 Keep maintaining a healthy lifestyle. Regular checkups are recommended.</p>
            </div>""", unsafe_allow_html=True)

        st.write(f"🔎 Medical Decision Threshold: **{threshold:.2f}**")

        # ── Risk Scale ─────────────────────────────────────────────────────────
        st.markdown("### 📊 Risk Interpretation Guide")
        if probability < 0.20:
            st.write("🟢 **Very Low Risk** — Excellent health indicators")
        elif probability < 0.40:
            st.write("🟡 **Mild Risk** — Some factors to watch")
        elif probability < 0.60:
            st.write("🟠 **Moderate Risk** — Consider lifestyle changes")
        elif probability < 0.80:
            st.write("🔴 **High Risk** — Consult a doctor soon")
        else:
            st.write("🚨 **Critical Risk** — Seek medical attention immediately")

        # ── Feature Importance ─────────────────────────────────────────────────
        try:
            base_model = model.calibrated_classifiers_[0].estimator.named_steps["model"]
            importances = base_model.feature_importances_
            importance_df = pd.DataFrame({
                "Feature": input_data.columns,
                "Importance (%)": (importances * 100).round(2)
            }).sort_values(by="Importance (%)", ascending=False)

            st.markdown("### 🔍 Key Factors Driving This Prediction")
            st.dataframe(importance_df, use_container_width=True)
        except Exception:
            pass

        # ── Action Buttons ─────────────────────────────────────────────────────
        st.markdown("---")
        st.markdown("### 🎯 Recommended Next Steps")
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("💬 Talk to AI Assistant", use_container_width=True):
                st.switch_page("pages/6_Chatbot.py")
        with c2:
            if st.button("🏥 Find Nearby Doctors", use_container_width=True):
                st.switch_page("pages/7_DoctorFinder.py")
        with c3:
            if st.session_state.get("logged_in", False):
                if st.button("📊 View My Dashboard", use_container_width=True):
                    st.switch_page("pages/9_Dashboard.py")
            else:
                if st.button("🔐 Login to Save Results", use_container_width=True):
                    st.switch_page("pages/2_Login.py")

    except Exception as e:
        st.error(f"❌ Prediction error: {str(e)}")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("main.py")
with col2:
    if st.button("💬 Chatbot", use_container_width=True):
        st.switch_page("pages/6_Chatbot.py")
with col3:
    if st.button("🏥 Find Doctors", use_container_width=True):
        st.switch_page("pages/7_DoctorFinder.py")
with col4:
    if st.button("📞 Contact", use_container_width=True):
        st.switch_page("pages/4_Contact.py")

st.markdown(
    "<div style='text-align:center;color:#003366;padding:20px;'>© 2025 CerebroGuard | AI-Based Stroke Risk Prediction</div>",
    unsafe_allow_html=True)