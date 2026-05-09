import streamlit as st

# Page Config
st.set_page_config(page_title="Brain Stroke Risk Prediction", page_icon="🧠", layout="wide")

# CSS Styling
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    [data-testid="stSidebar"] {
        display: none !important;
    }
    
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Hero Section */
    .hero-section {
        margin-top: 2px;
        text-align: center;
        padding: 5px 5px;
    }
    
    .hero-title {
        font-size: 48px;
        font-weight: 700;
        color: #f0e68c;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        line-height: 1.3;
    }
    
    .hero-subtitle {
        font-size: 28px;
        color: white;
        margin-bottom: 30px;
        font-weight: 300;
    }
    
    /* Content Cards */
    .content-section {
        max-width: 1200px;
        margin: 50px auto;
        padding: 0 20px;
    }
    
    .card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 5px 20px rgba(0,0,0,0.2);
    }
    
    .card-title {
        color: #667eea;
        font-size: 24px;
        font-weight: 600;
        margin-bottom: 15px;
    }
    
    .card-content {
        color: #555;
        font-size: 16px;
        line-height: 1.8;
    }
    
    .risk-list {
        color: #555;
        font-size: 16px;
        line-height: 2;
        margin: 20px 0;
    }
    
    .risk-item {
        padding: 8px 0;
    }
    
    /* Buttons */
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
    
    .cta-button {
        background: white !important;
        color: #667eea !important;
        font-size: 20px !important;
        padding: 15px 40px !important;
        border-radius: 50px !important;
        font-weight: 700 !important;
    }
    
    .warning-box {
        background: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    
    .warning-text {
        color: #856404;
        margin: 0;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <div class="hero-title">🧠 Brain Stroke Risk Assessment</div>
    <div class="hero-subtitle">Predict, Prevent, Protect Your Health</div>
</div>
""", unsafe_allow_html=True)

# Main Content
st.markdown("<div class='content-section'>", unsafe_allow_html=True)

# What is Brain Stroke Section
st.markdown("""
<div class="card">
    <div class="card-title">🔍 What is a Brain Stroke?</div>
    <div class="card-content">
        A stroke occurs when blood supply to part of the brain is interrupted or reduced, preventing 
        brain tissue from getting oxygen and nutrients. Brain cells begin to die within minutes. 
        Early detection and intervention are crucial for reducing brain damage and potential complications.
        <br><br>
        According to the World Health Organization, stroke is the second leading cause of death globally, 
        responsible for approximately 11% of total deaths. This makes early risk assessment more important 
        than ever.
    </div>
</div>
""", unsafe_allow_html=True)

# Risk Factors Section
st.markdown("""
<div class="card">
    <div class="card-title">⚠️ Major Risk Factors</div>
    <div class="card-content">
        Understanding your risk factors is the first step toward prevention. Our AI-powered tool 
        analyzes the following key indicators:
    </div>
    <div class="risk-list">
        <div class="risk-item">👴 <strong>Age:</strong> Risk increases significantly after age 55</div>
        <div class="risk-item">💓 <strong>Hypertension:</strong> High blood pressure is a leading risk factor</div>
        <div class="risk-item">❤️ <strong>Heart Disease:</strong> Cardiovascular conditions increase stroke risk</div>
        <div class="risk-item">🍬 <strong>Diabetes:</strong> High glucose levels damage blood vessels</div>
        <div class="risk-item">🚬 <strong>Smoking:</strong> Doubles the risk of ischemic stroke</div>
        <div class="risk-item">⚖️ <strong>Obesity & BMI:</strong> Excess weight contributes to other risk factors</div>
        <div class="risk-item">🧬 <strong>Family History:</strong> Genetic predisposition plays a role</div>
        <div class="risk-item">🥗 <strong>Lifestyle:</strong> Diet, stress, and physical activity matter</div>
    </div>
</div>
""", unsafe_allow_html=True)

# How It Works Section
st.markdown("""
<div class="card">
    <div class="card-title">🤖 How Our AI Prediction Works</div>
    <div class="card-content">
        <strong>1. Input Your Health Data:</strong> Provide information about your age, medical history, 
        lifestyle habits, and current health status.
        <br><br>
        <strong>2. Machine Learning Analysis:</strong> Our trained models (Logistic Regression and Random Forest) 
        analyze your data using patterns learned from thousands of medical records.
        <br><br>
        <strong>3. Risk Assessment:</strong> Get an instant risk prediction with probability scores to help 
        you understand your stroke risk level.
        <br><br>
        <strong>4. Take Action:</strong> Use the results to have informed discussions with your healthcare 
        provider about prevention strategies.
    </div>
</div>
""", unsafe_allow_html=True)

# Warning Section
st.markdown("""

""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Call to Action
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🧮 Check Your Stroke Risk Now", key="cta", use_container_width=True):
        st.switch_page("pages/5_Predictor.py")

st.markdown("<br>", unsafe_allow_html=True)

# Navigation Buttons
col1, col2, col3, col4 ,col5= st.columns(5)

with col1:
    if st.button("🏠 Main Menu", use_container_width=True):
        st.switch_page("main.py")

with col2:
    if st.button("🔐 Login", use_container_width=True):
        st.switch_page("pages/2_Login.py")
        col1, col2, col3, col4, col5 = st.columns(5)

with col3:  # Add this
    if st.button("📝 Register", use_container_width=True):
        st.switch_page("pages/8_Register.py")

with col4:
    if st.button("💡 About", use_container_width=True):
        st.switch_page("pages/3_About.py")

with col5:
    if st.button("📞 Contact", use_container_width=True):
        st.switch_page("pages/4_Contact.py")
        

# Footer
st.markdown("""
<div style='text-align: center; color: white; padding: 30px 20px;'>
    © 2025 Brain Stroke Risk Portal | Developed by <b>Priyanka Nallana & Team</b>
</div>
""", unsafe_allow_html=True)