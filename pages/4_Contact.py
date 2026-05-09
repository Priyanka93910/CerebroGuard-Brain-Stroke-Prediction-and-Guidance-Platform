
import streamlit as st

st.set_page_config(page_title="Contact - Brain Stroke Portal", page_icon="📞", layout="wide")

# ----------------- Custom CSS Styling -----------------
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* 🌤️ Light pastel gradient background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f9f9ff 0%, #e6f0ff 100%);
        background-attachment: fixed;
    }

    [data-testid="stSidebar"] {
        display: none !important;
    }

    .contact-container {
        max-width: 700px;
        margin: 50px auto;
        padding: 40px;
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.15);
    }

    .contact-title {
        text-align: center;
        color: #3366cc;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 20px;
    }

    .contact-subtitle {
        text-align: center;
        color: #555;
        font-size: 18px;
        margin-bottom: 40px;
    }

    .info-card {
        background: linear-gradient(135deg, #eef5ff 0%, #f7f9ff 100%);
        padding: 20px;
        border-radius: 12px;
        margin: 20px 0;
        border-left: 4px solid #3366cc;
    }

    .info-title {
        color: #003399;
        font-weight: 600;
        font-size: 18px;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .info-text {
        color: #444;
        font-size: 16px;
        margin: 5px 0;
    }

    .stButton > button {
        background: linear-gradient(135deg, #3366cc 0%, #66a3ff 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 30px;
        font-size: 18px;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(51, 102, 204, 0.4);
    }

    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        border-radius: 10px;
        border: 2px solid #d0d0d0;
        padding: 12px;
        font-size: 16px;
        background-color: #fff;
    }

    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #3366cc;
        box-shadow: 0 0 0 0.2rem rgba(51, 102, 204, 0.25);
    }
</style>
""", unsafe_allow_html=True)

# ----------------- Back to Home Button -----------------
if st.button("← Back to Home"):
    st.switch_page("pages/1_Home.py")

# ----------------- Contact Container -----------------
st.markdown("<div class='contact-container'>", unsafe_allow_html=True)

st.markdown("<h1 class='contact-title'>📞 Contact Us</h1>", unsafe_allow_html=True)
st.markdown("<p class='contact-subtitle'>We'd love to hear from you! Reach out for support, feedback, or collaborations.</p>", unsafe_allow_html=True)

# ----------------- Contact Information -----------------
st.markdown("""
<div class='info-card'>
    <div class='info-title'>👨‍💻 Developers</div>
    <p class='info-text'><strong>Priyanka Nallana</strong></p>
   <p class='info-text'><strong>Vasantha Nacharam</strong></p>
            <p class='info-text'><strong>Nanda Kishore Chalam</strong></p>
            <p class='info-text'><strong> Vamshi Krishna Jaligama</strong></p>
</div>

<div class='info-card'>
    <div class='info-title'>📧 Email</div>
    <p class='info-text'>priyankanallana11@gmail.com</p>
    <p class='info-text' style='font-size: 14px; color: #888;'>For general inquiries and support</p>
</div>

<div class='info-card'>
    <div class='info-title'>🌐 Connect With Us</div>
    <p class='info-text'>LinkedIn:https://www.linkedin.com/in/priyanka-nallana-8b4909278</p>
    <p class='info-text'>GitHub: https://github.com/Priyanka93910</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ----------------- Contact Form -----------------
st.markdown("<h3 style='color: #003399; text-align: center; margin: 30px 0 20px 0;'>📝 Send Us a Message</h3>", unsafe_allow_html=True)

with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("👤 Your Name", placeholder="Enter your full name")
    email = st.text_input("📧 Your Email", placeholder="your.email@example.com")
    subject = st.selectbox("📌 Subject", [
        "General Inquiry",
        "Technical Support",
        "Feature Request",
        "Bug Report",
        "Collaboration Opportunity",
        "Other"
    ])
    message = st.text_area("💬 Message", placeholder="Type your message here...", height=150)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    submitted = st.form_submit_button("📤 Send Message")
    
    if submitted:
        if name and email and message:
            st.success("✅ Thank you for reaching out! Your message has been sent successfully. We'll get back to you soon.")
            st.balloons()
        else:
            st.error("❌ Please fill in all required fields (Name, Email, and Message)")

st.markdown("<br>", unsafe_allow_html=True)

# ----------------- Business Hours -----------------
st.markdown("""
<div class='info-card'>
    <div class='info-title'>🕒 Response Time</div>
    <p class='info-text'>We typically respond within 24-48 hours </p>
    <p class='info-text' style='font-size: 14px; color: #888;'>Monday - Friday: 9:00 AM - 6:00 PM IST</p>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ----------------- Navigation Buttons -----------------
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("main.py")

with col2:
    if st.button("🔐 Login", use_container_width=True):
        st.switch_page("pages/2_Login.py")

with col3:
    if st.button("💡 About", use_container_width=True):
        st.switch_page("pages/3_About.py")

with col4:
    if st.button("🧮 Predictor", use_container_width=True):
        st.switch_page("pages/5_Predictor.py")

# ----------------- Footer -----------------
st.markdown("""
<div style='text-align: center; color: #444; padding: 30px 20px;'>
    © 2025 Brain Stroke Risk Portal | Developed by <b>Priyanka Nallana & Team</b>
</div>
""", unsafe_allow_html=True)