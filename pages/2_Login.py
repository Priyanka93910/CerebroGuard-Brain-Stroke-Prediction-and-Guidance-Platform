import streamlit as st
import sys
sys.path.append('..')

try:
    from database import authenticate_user, authenticate_doctor, init_database
    DATABASE_AVAILABLE = True
    init_database()
except Exception as e:
    DATABASE_AVAILABLE = False

st.set_page_config(page_title="Login - CerebroGuard", page_icon="🔒",
                   layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    [data-testid="stHeader"],
    [data-testid="stToolbar"] { display: none !important; }
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding-top: 0rem !important; }
    [data-testid="stAppViewContainer"] > .main { padding-top: 0px !important; }
    [data-testid="stSidebar"] { display: none !important; }

    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

    .login-container {
        max-width: 580px;
        margin: 50px auto;
        padding: 50px;
        background: rgba(255, 255, 255, 0.95);
        border-radius: 30px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.4);
        backdrop-filter: blur(10px);
    }

    .welcome-text {
        text-align: center;
        color: black;
        font-size: 48px;
        font-weight: 900;
        margin-bottom: 10px;
    }
    .welcome-subtitle {
        text-align: center;
        color: #555;
        font-size: 18px;
        margin-bottom: 30px;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab"] {
        font-size: 20px;
        font-weight: 700;
        padding: 14px 28px;
        color: orange !important;
    }
    .stTabs [aria-selected="true"] {
        color: black !important;
        font-weight: 900 !important;
    }

    /* Input labels */
    .stTextInput label {
        font-weight: 800 !important;
        font-size: 20px !important;
        color: black !important;
    }
    .stTextInput input {
        border-radius: 12px !important;
        padding: 16px !important;
        font-size: 17px !important;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        padding: 16px;
        font-size: 20px;
        font-weight: 700;
        border: none;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton > button:hover { transform: translateY(-2px); }

    .helper-text {
        text-align: center;
        color: #888;
        font-size: 15px;
        margin-top: 12px;
    }

    .doctor-info-box {
        background: linear-gradient(135deg, #e8f4fd 0%, #d6eaf8 100%);
        border-left: 5px solid #2980b9;
        padding: 18px 20px;
        border-radius: 12px;
        margin: 16px 0 20px 0;
        color: #1a5276;
        font-size: 15px;
        line-height: 1.8;
    }
    .pending-box {
        background: #fff3cd;
        border-left: 5px solid #ffc107;
        padding: 18px 20px;
        border-radius: 12px;
        margin: 12px 0;
        color: #856404;
        font-size: 15px;
        line-height: 1.7;
    }
    .logged-in-box {
        background: linear-gradient(135deg, #d4edda, #c3e6cb);
        border-left: 5px solid #28a745;
        padding: 22px;
        border-radius: 15px;
        margin: 20px 0;
        color: #155724;
        font-size: 18px;
        font-weight: 700;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ── Session state defaults ─────────────────────────────────────────────────────
for key, val in [
    ("logged_in", False), ("user_id", None), ("username", None),
    ("doctor_logged_in", False), ("doctor_id", None), ("doctor_name", None),
    ("doctor_hospital", None), ("doctor_specialty", None), ("is_verified", False)
]:
    if key not in st.session_state:
        st.session_state[key] = val

# ── Already logged in as patient ──────────────────────────────────────────────
if st.session_state.logged_in:
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    st.markdown(f"<div class='welcome-text'>👋 Hi, {st.session_state.username}!</div>",
                unsafe_allow_html=True)
    st.markdown("<div class='logged-in-box'>✅ You are logged in as a Patient</div>",
                unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📊 My Dashboard", use_container_width=True):
            st.switch_page("pages/9_Dashboard.py")
    with c2:
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.user_id   = None
            st.session_state.username  = None
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# ── Already logged in as doctor ────────────────────────────────────────────────
if st.session_state.doctor_logged_in:
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    st.markdown(f"<div class='welcome-text'>👨‍⚕️ Dr. {st.session_state.doctor_name}</div>",
                unsafe_allow_html=True)
    st.markdown("<div class='logged-in-box'>✅ You are logged in as a Doctor</div>",
                unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🏥 Doctor Dashboard", use_container_width=True):
            st.switch_page("pages/10_DoctorDashboard.py")
    with c2:
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.doctor_logged_in = False
            st.session_state.doctor_id        = None
            st.session_state.doctor_name      = None
            st.session_state.is_verified      = False
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# ── Login UI ──────────────────────────────────────────────────────────────────
st.markdown("<div class='login-container'>", unsafe_allow_html=True)
st.markdown("<div class='welcome-text'>🔐 Welcome Back!</div>", unsafe_allow_html=True)
st.markdown("<div class='welcome-subtitle'>Login to access your CerebroGuard account</div>",
            unsafe_allow_html=True)

if not DATABASE_AVAILABLE:
    st.error("⚠️ Database not available. Please ensure database.py is in the project folder.")
    st.stop()

tab_patient, tab_doctor = st.tabs(["🧑‍💼 Patient Login", "👨‍⚕️ Doctor Login"])

# ── PATIENT TAB ───────────────────────────────────────────────────────────────
with tab_patient:
    p_user = st.text_input("👤 Username", key="p_user",
                           placeholder="Enter your username")
    p_pass = st.text_input("🔑 Password", type="password", key="p_pass",
                           placeholder="Enter your password")

    if st.button("🚀 Login as Patient", use_container_width=True, key="btn_plogin"):
        if not p_user or not p_pass:
            st.error("❌ Please enter both username and password.")
        else:
            user = authenticate_user(p_user, p_pass)
            if user:
                st.session_state.logged_in = True
                st.session_state.user_id   = user["user_id"]
                st.session_state.username  = user["username"]
                st.success(f"✅ Welcome back, {user['username']}!")
                st.rerun()
            else:
                st.error("❌ Invalid username or password.")

    st.markdown("<p class='helper-text'>🔒 Forgot password? Contact support.</p>",
                unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<p class='helper-text'>Don't have an account?</p>",
                unsafe_allow_html=True)
    if st.button("📝 Register as Patient", use_container_width=True, key="btn_preg"):
        st.switch_page("pages/8_Register.py")

# ── DOCTOR TAB ────────────────────────────────────────────────────────────────
with tab_doctor:
    st.markdown("""
    <div class='doctor-info-box'>
        👨‍⚕️ <strong>Doctor Portal</strong><br>
        Login with your registered medical credentials to access:<br>
        &nbsp;&nbsp;📅 Patient appointments &nbsp;|&nbsp; 🚨 High-risk patient alerts<br>
        &nbsp;&nbsp;📝 Consultation notes &nbsp;|&nbsp; 🗓️ Schedule management<br>
        <em style='font-size:13px;'>Your account must be verified by admin before access is granted.</em>
    </div>""", unsafe_allow_html=True)

    d_user = st.text_input("👤 Doctor Username", key="d_user",
                           placeholder="Enter your doctor username")
    d_pass = st.text_input("🔑 Password", type="password", key="d_pass",
                           placeholder="Enter your password")

    if st.button("🚀 Login as Doctor", use_container_width=True, key="btn_dlogin"):
        if not d_user or not d_pass:
            st.error("❌ Please enter both username and password.")
        else:
            doc = authenticate_doctor(d_user, d_pass)
            if doc:
                st.session_state.doctor_logged_in = True
                st.session_state.doctor_id        = doc["account_id"]
                st.session_state.doctor_name      = doc["full_name"]
                st.session_state.doctor_hospital  = doc.get("hospital", "")
                st.session_state.doctor_specialty = doc.get("specialty", "")
                st.session_state.is_verified      = True
                st.success(f"✅ Welcome, Dr. {doc['full_name']}!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials. Please check your username and password.")

    st.markdown("---")
    st.markdown("<p class='helper-text'>New medical professional?</p>",
                unsafe_allow_html=True)
    if st.button("🏥 Register as Doctor", use_container_width=True, key="btn_dreg"):
        st.switch_page("pages/11_DoctorRegister.py")

st.markdown("</div>", unsafe_allow_html=True)

# ── Footer nav ─────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("🏠 Home",    use_container_width=True): st.switch_page("main.py")
with c2:
    if st.button("💡 About",   use_container_width=True): st.switch_page("pages/3_About.py")
with c3:
    if st.button("📞 Contact", use_container_width=True): st.switch_page("pages/4_Contact.py")

st.markdown("""
<div style='text-align:center;color:white;padding:25px;font-size:15px;font-weight:600;'>
    © 2025 CerebroGuard | Secure Health Platform
</div>""", unsafe_allow_html=True)