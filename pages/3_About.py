import streamlit as st
import base64
import os

st.set_page_config(page_title="About - Brain Stroke Portal", page_icon="💡", layout="wide")

# -----------------------------------------------------
# Function to set background image (Local image support)
# -----------------------------------------------------
def set_bg(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as img:
            encoded = base64.b64encode(img.read()).decode()
        bg_style = f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/avif;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """
        st.markdown(bg_style, unsafe_allow_html=True)
    else:
        st.warning(f"⚠️ Background image not found: {image_file}")

# Apply background
set_bg("img4.avif")

# -----------------------------------------------------
# Custom CSS for content styling
# -----------------------------------------------------
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    [data-testid="stSidebar"] {
        display: none !important;
    }
    
    .about-container {
        max-width: 900px;
        margin: 50px auto;
        padding: 40px;
        background: rgba(255, 255, 255, 0.92);
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        backdrop-filter: blur(6px);
    }
    
    .about-title {
        text-align: center;
        color: #333;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 30px;
    }
    
    .section-title {
        color: #222;
        font-size: 24px;
        font-weight: 700;
        margin-top: 30px;
        margin-bottom: 15px;
        border-left: 4px solid #667eea;
        padding-left: 15px;
    }
    
    .feature-list {
        color: #444;
        font-size: 16px;
        line-height: 2;
        margin: 20px 0;
    }
    
    .feature-item {
        padding: 8px 0;
    }
    
    .ml-model-item {
        background: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
        border-left: 4px solid #667eea;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    
    /* 🔥 Model Title in Bold Black */
    .model-title {
        color: black;
        font-weight: 800;
        font-size: 18px;
        margin-bottom: 8px;
    }
    
    .tech-badge {
        display: inline-block;
        background: #667eea;
        color: white;
        padding: 6px 15px;
        border-radius: 20px;
        margin: 5px;
        font-size: 14px;
        font-weight: 500;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 30px;
        font-size: 16px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# Back Button
# -----------------------------------------------------
if st.button("← Back to Home"):
    st.switch_page("main.py")

# -----------------------------------------------------
# About Section
# -----------------------------------------------------
st.markdown("<div class='about-container'>", unsafe_allow_html=True)

st.markdown("<h1 class='about-title'>💡 About This Project</h1>", unsafe_allow_html=True)

st.markdown("""
<p style='font-size: 18px; text-align: center; color: #555; margin-bottom: 30px;'>
    An AI-powered web application designed to predict brain stroke risk using advanced 
    machine learning algorithms trained on comprehensive medical datasets.
</p>
""", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>🎯 Project Overview</h2>", unsafe_allow_html=True)
st.markdown("""
<p style='color: #333; line-height: 1.8;'>
    Brain stroke is one of the leading causes of death and disability worldwide. Early detection 
    and risk assessment can save lives. This project combines machine learning with healthcare 
    to provide an accessible tool for stroke risk prediction based on various health parameters 
    including age, BMI, glucose levels, blood pressure, and lifestyle factors.
</p>
""", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>🔬 Machine Learning Models</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='ml-model-item'>
    <div class='model-title'>📊 <b>Logistic Regression</b></div>
    <p style='color: #555;'>A statistical model that analyzes the relationship between health 
    parameters and stroke risk, providing probabilistic predictions.</p>
</div>

<div class='ml-model-item'>
    <div class='model-title'>🌲 <b>Random Forest Classifier</b></div>
    <p style='color: #555;'>An ensemble learning method that creates multiple decision trees 
    to improve prediction accuracy and handle complex patterns in medical data.</p>
</div>

<div class='ml-model-item'>
    <div class='model-title'>⚖️ <b>SMOTE (Synthetic Minority Over-sampling)</b></div>
    <p style='color: #555;'>A technique used to balance the dataset by generating synthetic 
    samples, ensuring the model doesn't bias towards the majority class.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>✨ Key Features</h2>", unsafe_allow_html=True)
st.markdown("""
<div class="feature-list">
    <div class="feature-item">🎯 <strong>Accurate Predictions:</strong> High precision and recall rates achieved through ensemble methods</div>
    <div class="feature-item">🖥️ <strong>User-Friendly Interface:</strong> Clean, intuitive design built with Streamlit framework</div>
    <div class="feature-item">📊 <strong>Multiple Risk Factors:</strong> Analyzes age, BMI, glucose, hypertension, and more</div>
    <div class="feature-item">🔒 <strong>Secure & Private:</strong> Your health data is processed securely and not stored</div>
    <div class="feature-item">📱 <strong>Responsive Design:</strong> Works seamlessly across all devices</div>
    <div class="feature-item">🚀 <strong>Real-time Analysis:</strong> Get instant risk assessment results</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>🛠️ Technology Stack</h2>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; margin: 25px 0;'>
    <span class='tech-badge'>Python</span>
    <span class='tech-badge'>Streamlit</span>
    <span class='tech-badge'>Scikit-learn</span>
    <span class='tech-badge'>Pandas</span>
    <span class='tech-badge'>NumPy</span>
    <span class='tech-badge'>Joblib</span>
    <span class='tech-badge'>SMOTE</span>
    <span class='tech-badge'>Random Forest</span>
</div>
""", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>⚠️ Important Disclaimer</h2>", unsafe_allow_html=True)
st.markdown("""
<div style='background: #fff3cd; padding: 20px; border-radius: 10px; border-left: 4px solid #ffc107;'>
    <p style='color: #856404; margin: 0; font-weight: 500;'>
        <strong>Medical Notice:</strong> This tool is designed for educational and informational 
        purposes only. It should NOT be used as a substitute for professional medical advice, 
        diagnosis, or treatment. Always consult with qualified healthcare providers for medical 
        concerns and decisions.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<p style='text-align: center; color: #667eea; font-size: 20px; font-weight: 600;'>
    💻 Developed by Priyanka Nallana
</p>
<p style='text-align: center; color: #888;'>
    A machine learning project focused on healthcare innovation
</p>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------
# Navigation Buttons
# -----------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("main.py")

with col2:
    if st.button("🔐 Login", use_container_width=True):
        st.switch_page("pages/2_Login.py")

with col3:
    if st.button("📞 Contact", use_container_width=True):
        st.switch_page("pages/4_Contact.py")

with col4:
    if st.button("🧮 Predictor", use_container_width=True):
        st.switch_page("pages/5_Predictor.py")

# -----------------------------------------------------
# Footer
# -----------------------------------------------------
st.markdown("""
<div style='text-align: center; color: white; padding: 30px 20px;'>
    © 2025 Brain Stroke Risk Portal | Developed by <b>Priyanka Nallana</b>
</div>
""", unsafe_allow_html=True)
