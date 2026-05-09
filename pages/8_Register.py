import streamlit as st
import sys
import re
from datetime import datetime
sys.path.append('..')

try:
    from database import create_user, init_database
    DATABASE_AVAILABLE = True
    init_database()
except Exception:
    DATABASE_AVAILABLE = False

st.set_page_config(page_title="Patient Registration - CerebroGuard",
                   page_icon="📝", layout="wide")

st.markdown("""
<style>
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .register-container {
        max-width: 700px;
        margin: 30px auto;
        padding: 50px;
        background: rgba(255, 255, 255, 0.98);
        border-radius: 30px;
        box-shadow: 0 25px 70px rgba(0,0,0,0.4);
        backdrop-filter: blur(15px);
    }
    .register-title {
        text-align: center;
        color: black;
        font-size: 52px;
        font-weight: 900;
        margin-bottom: 15px;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.1);
        letter-spacing: -1px;
    }
    .register-subtitle {
        text-align: center;
        color: black;
        font-size: 20px;
        margin-bottom: 40px;
        font-weight: 500;
        line-height: 1.6;
    }
    .section-header {
        color: white;
        font-size: 28px;
        font-weight: 800;
        margin: 35px 0 20px 0;
        padding-bottom: 12px;
        border-bottom: 3px solid white;
    }
    .section-description {
        color: yellow;
        font-size: 17px;
        margin-top: -15px;
        margin-bottom: 25px;
        font-weight: 1000;
    }
    .stTextInput > label,
    .stDateInput > label,
    .stSelectbox > label {
        font-size: 19px !important;
        font-weight: 700 !important;
        color: #333 !important;
        margin-bottom: 10px !important;
    }
    .stTextInput > div > div > input,
    .stDateInput > div > div > input,
    .stSelectbox > div > div > div {
        border-radius: 14px !important;
        border: 3px solid #e0e0e0 !important;
        padding: 18px 22px !important;
        font-size: 19px !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
    }
    .info-box {
        background: linear-gradient(135deg, #e3f2fd 0%, #e8eaf6 100%);
        border-left: 5px solid #2196f3;
        padding: 22px;
        border-radius: 15px;
        margin: 25px 0;
        box-shadow: 0 4px 15px rgba(33,150,243,0.15);
    }
    .info-text {
        color: #1565c0;
        font-size: 18px;
        margin: 0;
        font-weight: 700;
    }
    .requirement-item { color: #555; font-size: 17px; margin: 10px 0; padding-left: 25px; font-weight: 600; }
    .requirement-met   { color: #28a745; font-weight: 700; font-size: 18px; }
    .requirement-unmet { color: #dc3545; font-weight: 600; font-size: 18px; }
    .success-box {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        border-left: 5px solid #28a745;
        padding: 25px;
        border-radius: 15px;
        margin: 25px 0;
    }
    .success-text { color: #155724; font-size: 20px; margin: 0; font-weight: 700; }
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 16px;
        padding: 20px 45px;
        font-size: 22px;
        font-weight: 800;
        width: 100%;
        transition: all 0.3s ease;
        margin-top: 25px;
        box-shadow: 0 6px 25px rgba(102,126,234,0.4);
    }
    .stButton > button:hover { transform: translateY(-4px); }
    .stCheckbox > label { font-size: 18px !important; font-weight: 600 !important; color: #333 !important; }
    hr { margin: 35px 0; border: none; height: 3px; background: linear-gradient(90deg, transparent, #667eea, transparent); }
    .bottom-text { text-align: center; color: white; font-size: 20px; margin: 25px 0; font-weight: 600; }
    .doctor-cta {
        background: linear-gradient(135deg, #1a5276, #2e86c1);
        border-radius: 16px; padding: 22px 30px;
        text-align: center; color: white;
        margin-top: 30px;
    }
    .doctor-cta-text { font-size: 18px; font-weight: 600; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

def validate_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None

def validate_password(password):
    return {
        'length':    len(password) >= 8,
        'uppercase': any(c.isupper() for c in password),
        'lowercase': any(c.islower() for c in password),
        'digit':     any(c.isdigit() for c in password),
        'special':   any(c in '!@#$%^&*(),.?":{}|<>' for c in password),
    }

def validate_phone(phone):
    if not phone:
        return True
    clean = phone.replace(' ','').replace('-','').replace('(','').replace(')','')
    return clean.isdigit() and len(clean) >= 10

# ──────────────────────────────────────────────────────────────────────────────
st.markdown("<div class='register-container'>", unsafe_allow_html=True)
st.markdown("<h1 class='register-title'>📝 Patient Registration</h1>", unsafe_allow_html=True)
st.markdown("""<p class='register-subtitle'>
    Create your patient account to track your health journey
    and get personalized stroke risk insights
</p>""", unsafe_allow_html=True)

if not DATABASE_AVAILABLE:
    st.error("⚠️ Database not available. Please ensure database.py is in the project directory.")
elif st.session_state.get('logged_in', False):
    st.markdown(f"""
    <div class='success-box'>
        <p class='success-text'>✅ Already logged in as {st.session_state.get('username','User')}</p>
    </div>""", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📊 My Dashboard"): st.switch_page("pages/9_Dashboard.py")
    with c2:
        if st.button("🔮 Go to Predictor"): st.switch_page("pages/5_Predictor.py")
else:
    with st.form("patient_registration_form"):
        st.markdown("<div class='section-header'>🔐 Account Credentials</div>", unsafe_allow_html=True)

        username = st.text_input("👤 Username *", placeholder="Choose a unique username (min 3 chars)")
        email    = st.text_input("📧 Email Address *", placeholder="your.email@example.com")

        c1, c2 = st.columns(2)
        with c1:
            password = st.text_input("🔑 Password *", type="password",
                                     placeholder="Create a strong password")
        with c2:
            confirm_password = st.text_input("🔑 Confirm Password *", type="password",
                                             placeholder="Re-enter your password")

        if password:
            req = validate_password(password)
            items = [
                (req['length'],    "At least 8 characters"),
                (req['uppercase'], "One uppercase letter"),
                (req['lowercase'], "One lowercase letter"),
                (req['digit'],     "One number"),
            ]
            st.markdown("<div class='info-box'><p class='info-text'>🔒 Password Strength:</p>",
                        unsafe_allow_html=True)
            html = ""
            for ok, label in items:
                cls = "requirement-met" if ok else "requirement-unmet"
                html += f"<div class='requirement-item {cls}'>{'✓' if ok else '✗'} {label}</div>"
            st.markdown(html + "</div>", unsafe_allow_html=True)

        st.markdown("<div class='section-header'>👤 Personal Information</div>", unsafe_allow_html=True)
        st.markdown("<p class='section-description'>Optional — helps personalise your experience</p>",
                    unsafe_allow_html=True)

        full_name = st.text_input("📛 Full Name", placeholder="John Doe")
        c1, c2 = st.columns(2)
        with c1:
            phone = st.text_input("📱 Phone Number", placeholder="+91 98765 43210")
        with c2:
            gender = st.selectbox("⚥ Gender",
                                  ["Select", "Male", "Female", "Other", "Prefer not to say"])

        date_of_birth = st.date_input("🎂 Date of Birth",
                                      min_value=datetime(1900, 1, 1),
                                      max_value=datetime.now(), value=None)

        st.markdown("<br>", unsafe_allow_html=True)
        agree_terms = st.checkbox("✅ I agree to the Terms of Service and Privacy Policy *")
        submitted = st.form_submit_button("🚀 Create My Patient Account")

        if submitted:
            errors = []
            if not username or len(username) < 3:
                errors.append("Username must be at least 3 characters.")
            if not email or not validate_email(email):
                errors.append("Enter a valid email address.")
            if not password:
                errors.append("Password is required.")
            elif not all(v for k, v in validate_password(password).items() if k != 'special'):
                errors.append("Password does not meet all requirements.")
            if password != confirm_password:
                errors.append("Passwords do not match.")
            if phone and not validate_phone(phone):
                errors.append("Invalid phone number format.")
            if not agree_terms:
                errors.append("You must agree to the Terms of Service.")

            if errors:
                for e in errors:
                    st.error(f"❌ {e}")
            else:
                user_id = create_user(
                    username=username,
                    email=email,
                    password=password,
                    full_name=full_name if full_name else None,
                    phone=phone if phone else None,
                    date_of_birth=date_of_birth.strftime("%Y-%m-%d") if date_of_birth else None,
                    gender=None if gender == "Select" else gender,
                )
                if user_id:
                    st.success("🎉 Registration successful! Redirecting to login…")
                    st.balloons()
                    import time; time.sleep(2)
                    st.switch_page("pages/2_Login.py")
                else:
                    st.error("❌ Registration failed. Username or email may already exist.")

# ── Doctor CTA ────────────────────────────────────────────────────────────────
st.markdown("""
<div class='doctor-cta'>
    <div class='doctor-cta-text'>👨‍⚕️ Are you a Medical Professional?</div>
    <p style='font-size:15px;color:rgba(255,255,255,0.85);margin:0;'>
        Register as a Doctor to access patient records and appointment management.
    </p>
</div>""", unsafe_allow_html=True)
if st.button("🏥 Register as Doctor Instead", use_container_width=True):
    st.switch_page("pages/11_DoctorRegister.py")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.markdown("<p class='bottom-text'>Already have an account?</p>", unsafe_allow_html=True)
    if st.button("🔐 Login Here", use_container_width=True):
        st.switch_page("pages/2_Login.py")

st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("🏠 Home",    use_container_width=True): st.switch_page("main.py")
with c2:
    if st.button("💡 About",   use_container_width=True): st.switch_page("pages/3_About.py")
with c3:
    if st.button("📞 Contact", use_container_width=True): st.switch_page("pages/4_Contact.py")

st.markdown("""
<div style='text-align:center;color:white;padding:35px 20px;font-size:19px;font-weight:600;'>
    © 2025 CerebroGuard | Secure & Private Health Platform
</div>""", unsafe_allow_html=True)