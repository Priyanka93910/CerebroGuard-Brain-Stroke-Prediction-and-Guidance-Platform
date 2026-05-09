import streamlit as st
import sys, re
from datetime import datetime
sys.path.append('..')

try:
    from database import create_doctor_account, init_database
    DATABASE_AVAILABLE = True
    init_database()
except Exception:
    DATABASE_AVAILABLE = False

st.set_page_config(page_title="Doctor Registration - CerebroGuard",
                   page_icon="🏥", layout="wide")

st.markdown("""
<style>
    #MainMenu, footer, header { visibility: hidden; }
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1a5276 0%, #2e86c1 100%);
    }
    .block-container { padding-top: 1rem; }

    .register-container {
        max-width: 720px;
        margin: 30px auto;
        padding: 50px;
        background: rgba(255, 255, 255, 0.98);
        border-radius: 30px;
        box-shadow: 0 25px 70px rgba(0,0,0,0.4);
    }
    .register-title {
        text-align: center;
        font-size: 48px;
        font-weight: 900;
        color: #1a5276;
        margin-bottom: 12px;
    }
    .register-subtitle {
        text-align: center;
        font-size: 18px;
        color: #555;
        margin-bottom: 30px;
        line-height: 1.6;
    }
    .section-header {
        font-size: 22px;
        font-weight: 800;
        color: #1a5276;
        border-left: 5px solid #2e86c1;
        padding-left: 14px;
        margin: 32px 0 18px 0;
    }
    .stTextInput > label,
    .stSelectbox > label,
    .stNumberInput > label {
        font-size: 18px !important;
        font-weight: 700 !important;
        color: #333 !important;
    }
    .stTextInput > div > div > input {
        border-radius: 12px !important;
        padding: 16px !important;
        font-size: 17px !important;
        border: 2px solid #d5d8dc !important;
    }
    .stButton > button {
        background: linear-gradient(135deg, #1a5276 0%, #2e86c1 100%);
        color: white;
        border: none;
        border-radius: 16px;
        padding: 18px 40px;
        font-size: 20px;
        font-weight: 800;
        width: 100%;
        transition: all 0.3s ease;
        margin-top: 20px;
    }
    .stButton > button:hover { transform: translateY(-3px); }
    .stCheckbox > label { font-size: 17px !important; font-weight: 600 !important; color: #333 !important; }

    .notice-box {
        background: linear-gradient(135deg, #d6eaf8 0%, #ebf5fb 100%);
        border-left: 5px solid #2980b9;
        padding: 18px 22px;
        border-radius: 14px;
        margin: 18px 0;
        color: #1a5276;
        font-size: 15px;
        line-height: 1.9;
    }
    .warn-box {
        background: #fef9e7;
        border-left: 5px solid #f39c12;
        padding: 14px 18px;
        border-radius: 10px;
        margin: 14px 0;
        font-size: 13px;
        color: #7d6608;
    }
    .req-met   { color: #27ae60; font-size: 15px; font-weight: 700; }
    .req-unmet { color: #e74c3c; font-size: 15px; font-weight: 600; }
    .success-result {
        background: linear-gradient(135deg, #d5f5e3, #a9dfbf);
        border: 2px solid #28b463;
        border-radius: 16px;
        padding: 24px;
        margin: 20px 0;
        color: #1d8348;
    }
    .patient-cta {
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 14px;
        padding: 20px 24px;
        text-align: center;
        color: white;
        margin-top: 28px;
    }
</style>
""", unsafe_allow_html=True)

def validate_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None

def validate_password(pwd):
    return {
        'length':  len(pwd) >= 8,
        'upper':   any(c.isupper() for c in pwd),
        'lower':   any(c.islower() for c in pwd),
        'digit':   any(c.isdigit() for c in pwd),
    }

# ──────────────────────────────────────────────────────────────────────────────
if st.session_state.get("doctor_logged_in"):
    st.info(f"✅ Already logged in as Dr. {st.session_state.doctor_name}.")
    if st.button("🏥 Go to Doctor Dashboard"):
        st.switch_page("pages/10_DoctorDashboard.py")
    st.stop()

st.markdown("<div class='register-container'>", unsafe_allow_html=True)
st.markdown("<h1 class='register-title'>🏥 Doctor Registration</h1>", unsafe_allow_html=True)
st.markdown("""<p class='register-subtitle'>
    Create your CerebroGuard medical professional account to view patient
    details, manage appointments, and write consultation notes.
</p>""", unsafe_allow_html=True)

st.markdown("""
<div class='notice-box'>
    📋 <strong>Before you register, please note:</strong><br>
    ✅ &nbsp;A valid Medical Council license number is mandatory<br>
    🚀 &nbsp;Your account is <strong>activated immediately</strong> after registration<br>
    🔐 &nbsp;You can login right away using the <strong>Doctor Login</strong> tab<br>
    📧 &nbsp;Contact admin@cerebroguard.com for any support
</div>""", unsafe_allow_html=True)

if not DATABASE_AVAILABLE:
    st.error("⚠️ Database not available. Please ensure database.py is in the project directory.")
else:
    with st.form("doctor_registration_form"):

        # ── SECTION 1: Login credentials ──────────────────────────────────────
        st.markdown("<div class='section-header'>🔐 Login Credentials</div>", unsafe_allow_html=True)

        username = st.text_input("👤 Username *", placeholder="Choose a unique username (min 4 chars)")
        email    = st.text_input("📧 Email Address *", placeholder="doctor@hospital.com")

        c1, c2 = st.columns(2)
        with c1:
            password = st.text_input("🔑 Password *", type="password",
                                     placeholder="Create a strong password")
        with c2:
            confirm  = st.text_input("🔑 Confirm Password *", type="password",
                                     placeholder="Re-enter your password")

        if password:
            req = validate_password(password)
            labels = [("length","Min 8 chars"),("upper","Uppercase"),
                      ("lower","Lowercase"),("digit","Number")]
            parts = " &nbsp; ".join(
                f"<span class='{'req-met' if req[k] else 'req-unmet'}'>{'✓' if req[k] else '✗'} {l}</span>"
                for k, l in labels)
            st.markdown(parts, unsafe_allow_html=True)

        # ── SECTION 2: Professional info ──────────────────────────────────────
        st.markdown("<div class='section-header'>👨‍⚕️ Professional Information</div>",
                    unsafe_allow_html=True)

        full_name = st.text_input("📛 Full Name (as on medical license) *",
                                  placeholder="Dr. First Last")

        c1, c2 = st.columns(2)
        with c1:
            specialty = st.selectbox("🩺 Specialty *", [
                "Select Specialty",
                "Neurologist", "Neurosurgeon", "Interventional Neurologist",
                "Cerebrovascular Surgeon", "Stroke Specialist",
                "Neuro-Physician", "Rehabilitation Specialist",
                "General Physician", "Other"
            ])
        with c2:
            experience = st.number_input("🎓 Years of Experience *",
                                         min_value=0, max_value=60, value=0)

        hospital = st.text_input("🏥 Hospital / Clinic Name *",
                                 placeholder="e.g. Apollo Hospitals, Hyderabad")
        phone    = st.text_input("📱 Contact Phone *",
                                 placeholder="+91 98765 43210")

        # ── SECTION 3: License ────────────────────────────────────────────────
        st.markdown("<div class='section-header'>📋 Medical License</div>", unsafe_allow_html=True)

        license_no = st.text_input("🪪 Medical Council License Number *",
                                   placeholder="e.g. AP-MCI-12345 or MCI-2023-XXXXX",
                                   help="Your registration number from State / National Medical Council")

        st.markdown("""
        <div class='warn-box'>
            🔒 Your license number will be cross-verified against Medical Council records.
            Providing false information will result in permanent ban from the platform.
        </div>""", unsafe_allow_html=True)

        agree = st.checkbox(
            "✅ I confirm all information provided is accurate and I am a licensed medical professional *")

        submitted = st.form_submit_button("🚀 Submit Doctor Registration", use_container_width=True)

        if submitted:
            errors = []
            if not username or len(username) < 4:
                errors.append("Username must be at least 4 characters.")
            if not email or not validate_email(email):
                errors.append("Enter a valid email address.")
            if not password:
                errors.append("Password is required.")
            elif not all(validate_password(password).values()):
                errors.append("Password does not meet all requirements.")
            if password != confirm:
                errors.append("Passwords do not match.")
            if not full_name or len(full_name.strip()) < 3:
                errors.append("Enter your full name.")
            if specialty == "Select Specialty":
                errors.append("Please select your specialty.")
            if not hospital.strip():
                errors.append("Hospital/clinic name is required.")
            if not phone.strip():
                errors.append("Phone number is required.")
            if not license_no.strip():
                errors.append("Medical license number is required.")
            if not agree:
                errors.append("You must confirm the accuracy of your information.")

            if errors:
                for e in errors:
                    st.error(f"❌ {e}")
            else:
                acc_id = create_doctor_account(
                    username=username.strip(),
                    email=email.strip(),
                    password=password,
                    full_name=full_name.strip(),
                    specialty=specialty,
                    hospital=hospital.strip(),
                    license_number=license_no.strip().upper(),
                    phone=phone.strip(),
                    experience_years=int(experience)
                )
                if acc_id:
                    st.success("🎉 Registration submitted successfully!")
                    st.balloons()
                    st.markdown(f"""
                    <div class='success-result'>
                        <h3>✅ Registration Successful!</h3>
                        <p><strong>👤 Username:</strong> {username}</p>
                        <p><strong>📛 Name:</strong> {full_name}</p>
                        <p><strong>🩺 Specialty:</strong> {specialty}</p>
                        <p><strong>🏥 Hospital:</strong> {hospital}</p>
                        <p><strong>🪪 License:</strong> {license_no.upper()}</p>
                        <hr style='border-color:#28b463;margin:12px 0;'>
                        <p style='color:#1d6a3a;'>
                            🚀 Your account is <strong>active immediately!</strong><br>
                            Go to the <strong>Doctor Login</strong> tab on the Login page
                            and login with your username and password right now.
                        </p>
                    </div>""", unsafe_allow_html=True)
                else:
                    st.error("❌ Registration failed. Username, email, or license number may already be in use.")

    # ── Patient CTA ────────────────────────────────────────────────────────────
    st.markdown("""
    <div class='patient-cta'>
        <div style='font-size:18px;font-weight:600;margin-bottom:8px;'>🧑‍💼 Are you a Patient?</div>
        <p style='font-size:14px;color:rgba(255,255,255,0.85);margin:0;'>
            Register as a patient to track your stroke risk and book doctor appointments.
        </p>
    </div>""", unsafe_allow_html=True)
    if st.button("📝 Register as Patient Instead", use_container_width=True):
        st.switch_page("pages/8_Register.py")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("🏠 Home",    use_container_width=True): st.switch_page("main.py")
with c2:
    if st.button("🔐 Login",   use_container_width=True): st.switch_page("pages/2_Login.py")
with c3:
    if st.button("📞 Contact", use_container_width=True): st.switch_page("pages/4_Contact.py")

st.markdown("""
<div style='text-align:center;color:white;padding:30px;font-size:16px;font-weight:600;'>
    © 2025 CerebroGuard | Medical Professional Portal
</div>""", unsafe_allow_html=True)