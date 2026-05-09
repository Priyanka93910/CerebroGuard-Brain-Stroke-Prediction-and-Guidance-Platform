import streamlit as st
import base64

st.set_page_config(
    page_title="Brain Stroke Prediction Portal",
    page_icon="🧠", layout="wide")

def set_bg(image_file):
    try:
        with open(image_file, "rb") as img:
            encoded = base64.b64encode(img.read()).decode()
        st.markdown(f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        [data-testid="stAppViewContainer"]::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(135deg, rgba(102,126,234,0.85) 0%, rgba(118,75,162,0.85) 100%);
            z-index: 0;
        }}
        </style>""", unsafe_allow_html=True)
    except:
        st.markdown("""
        <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        </style>""", unsafe_allow_html=True)

set_bg("img4.avif")

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stSidebar"] { display: none !important; }
    .block-container { position: relative; z-index: 1; }

    .main-content {
        text-align: center;
        padding: 40px 20px 50px 20px;
        min-height: 50vh;
    }
    .hero-title {
        font-size: 52px; font-weight: 700; color: #f0e68c;
        margin-bottom: 15px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        line-height: 1.2;
    }
    .hero-subtitle {
        font-size: 46px; font-weight: 700; color: #f0e68c;
        margin-bottom: 15px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        line-height: 1.2;
    }
    .hero-description {
        font-size: 28px; color: rgba(255,255,255,0.9);
        max-width: 650px; margin: 0 auto 40px; line-height: 1.6;
    }
    .stButton > button {
        background: rgba(255,255,255,0.15);
        color: white !important;
        border: 2px solid white;
        border-radius: 12px;
        padding: 14px 30px;
        font-size: 16px; font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        min-width: 150px;
    }
    .stButton > button:hover {
        background: white;
        color: #667eea !important;
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }
    .footer {
        text-align: center; color: white;
        padding: 30px 20px; font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-content">
    <div class="hero-title">A MACHINE LEARNING MODEL FOR BRAIN STROKE</div>
    <div class="hero-subtitle">PREDICTION AND PREVENTION</div>
    <div class="hero-description">
        Predict. Prevent. Protect — Empowering You Against Brain Stroke.
    </div>
</div>
""", unsafe_allow_html=True)

# ── Row 1: Main navigation (5 buttons — matching original) ────────────────────
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("🏠 Home",        use_container_width=True):
        st.switch_page("pages/1_Home.py")
with col2:
    if st.button("🔐 Login",       use_container_width=True):
        st.switch_page("pages/2_Login.py")
with col3:
    if st.button("💡 About",       use_container_width=True):
        st.switch_page("pages/3_About.py")
with col4:
    if st.button("📞 Contact Us",  use_container_width=True):
        st.switch_page("pages/4_Contact.py")
with col5:
    if st.button("📊 Predictor",   use_container_width=True):
        st.switch_page("pages/5_Predictor.py")

st.markdown("<br>", unsafe_allow_html=True)

# ── Row 2: Extended navigation (new pages) ────────────────────────────────────
col6, col7, col8, col9 = st.columns(4)
with col6:
    if st.button("🏥 Find Doctors",   use_container_width=True):
        st.switch_page("pages/7_DoctorFinder.py")
with col7:
    if st.button("💬 AI Assistant",   use_container_width=True):
        st.switch_page("pages/6_Chatbot.py")
with col8:
    if st.button("📈 My Dashboard",   use_container_width=True):
        st.switch_page("pages/9_Dashboard.py")
with col9:
    if st.button("👨‍⚕️ Doctor Portal", use_container_width=True):
        st.switch_page("pages/10_DoctorDashboard.py")

st.markdown("""
<div class='footer'>
    © 2025 Brain Stroke Risk Portal | Developed by <b>Priyanka Nallana & Team</b>
</div>
""", unsafe_allow_html=True)