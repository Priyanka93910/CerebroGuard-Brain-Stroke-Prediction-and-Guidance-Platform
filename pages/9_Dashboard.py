import streamlit as st
import sys
from datetime import datetime
sys.path.append('..')

try:
    from database import (get_user, get_user_predictions, get_prediction_statistics,
                          get_user_appointments, get_patient_notes_for_user,
                          update_user_profile, init_database)
    DATABASE_AVAILABLE = True
    init_database()
except Exception:
    DATABASE_AVAILABLE = False

st.set_page_config(page_title="My Dashboard - CerebroGuard", page_icon="📊", layout="wide")

st.markdown("""
<style>
    #MainMenu, footer, header { visibility: hidden; }
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .block-container { padding-top: 1rem; }

    .dash-title { text-align:center; color:white; font-size:40px; font-weight:900; margin-bottom:4px; }
    .dash-sub   { text-align:center; color:rgba(255,255,255,0.8); font-size:16px; margin-bottom:24px; }

    .stat-card {
        background: rgba(255,255,255,0.97);
        border-radius: 16px; padding: 22px; text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.12);
    }
    .stat-val   { font-size: 40px; font-weight: 900; color: #667eea; }
    .stat-label { font-size: 14px; color: #666; font-weight: 600; margin-top: 5px; }

    .card {
        background: rgba(255,255,255,0.97);
        border-radius: 16px; padding: 26px; margin: 14px 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    .card-title {
        font-size: 20px; font-weight: 800; color: #333;
        border-left: 5px solid #667eea; padding-left: 14px;
        margin-bottom: 18px;
    }
    .risk-row {
        background: #f8f9fa; border-radius: 12px;
        padding: 14px 18px; margin: 8px 0;
        border-left: 5px solid #667eea;
        font-size: 15px; color: #333; line-height: 1.8;
    }
    .risk-high { border-left-color: #e74c3c !important; }
    .badge-high { background:#fadbd8; color:#c0392b; padding:3px 10px; border-radius:8px; font-size:12px; font-weight:700; }
    .badge-low  { background:#d5f5e3; color:#1e8449; padding:3px 10px; border-radius:8px; font-size:12px; font-weight:700; }
    .appt-row {
        background: #eaf4fb; border-radius: 12px;
        padding: 14px 18px; margin: 8px 0;
        border-left: 5px solid #2980b9;
        font-size: 14px; color: #333; line-height: 1.8;
    }
    .note-row {
        background: #fef9e7; border-radius: 12px;
        padding: 14px 18px; margin: 8px 0;
        border-left: 5px solid #f39c12;
        font-size: 14px; color: #333; line-height: 1.8;
    }
    .profile-box {
        background: linear-gradient(135deg, #eaf4fb, #d6eaf8);
        border-radius: 12px; padding: 18px 22px;
        font-size: 15px; color: #333; line-height: 2.2;
    }
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white; border: none; border-radius: 12px;
        padding: 12px 20px; font-size: 16px; font-weight: 700;
        transition: all 0.2s ease;
    }
    .stButton > button:hover { transform: translateY(-2px); }
</style>
""", unsafe_allow_html=True)

# ── Auth Gate ─────────────────────────────────────────────────────────────────
if not st.session_state.get("logged_in"):
    st.markdown("""
    <div style='background:rgba(255,255,255,0.97);border-radius:18px;padding:50px;
                text-align:center;margin:60px auto;max-width:480px;'>
        <h2 style='color:#333;'>🔐 Login Required</h2>
        <p style='color:#666;'>Please login as a patient to view your dashboard.</p>
    </div>""", unsafe_allow_html=True)
    if st.button("🔐 Go to Login"):
        st.switch_page("pages/2_Login.py")
    st.stop()

user_id  = st.session_state.user_id
username = st.session_state.username

if not DATABASE_AVAILABLE:
    st.error("⚠️ Database not available.")
    st.stop()

# ── Load data ─────────────────────────────────────────────────────────────────
user_info    = get_user(user_id) or {}
predictions  = get_user_predictions(user_id, limit=50)
stats        = get_prediction_statistics(user_id)
appointments = get_user_appointments(user_id)
doctor_notes = get_patient_notes_for_user(user_id)

total    = stats.get('total_predictions', 0)
high_cnt = stats.get('high_risk_count', 0)
low_cnt  = stats.get('low_risk_count', 0)
upcoming = [a for a in appointments if a['status'] == 'Confirmed']

# ── Header ────────────────────────────────────────────────────────────────────
name_display = user_info.get('full_name') or username
st.markdown(f"<h1 class='dash-title'>📊 {name_display}'s Health Dashboard</h1>",
            unsafe_allow_html=True)
st.markdown("<p class='dash-sub'>Your personal stroke risk overview and health history</p>",
            unsafe_allow_html=True)

# ── Stat Cards ────────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
for col, val, label in [
    (c1, total,         "🔬 Total Assessments"),
    (c2, high_cnt,      "🚨 High-Risk Results"),
    (c3, low_cnt,       "✅ Low-Risk Results"),
    (c4, len(upcoming), "📅 Upcoming Appts"),
]:
    with col:
        st.markdown(f"""
        <div class='stat-card'>
            <div class='stat-val'>{val}</div>
            <div class='stat-label'>{label}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Risk Trend Chart ──────────────────────────────────────────────────────────
if predictions:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-title'>📈 Risk Score Trend</div>", unsafe_allow_html=True)
    try:
        import plotly.graph_objects as go
        import pandas as pd
        df = pd.DataFrame(predictions[::-1])
        df['date_short'] = df['prediction_date'].str[:16]   # show date + time
        colors = ['#e74c3c' if r == 'High' else '#27ae60' for r in df['risk_level']]
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df['date_short'], y=df['risk_probability'],
            mode='lines+markers',
            line=dict(color='#667eea', width=3),
            marker=dict(color=colors, size=12, line=dict(width=2, color='white')),
            name='Risk Score',
            hovertemplate='<b>%{x}</b><br>Risk: %{y:.1%}<extra></extra>'
        ))
        fig.add_hline(
            y=0.5, line_dash="dash", line_color="#e74c3c", line_width=2,
            annotation_text="High-Risk Threshold",
            annotation_font_color="#e74c3c",
            annotation_font_size=13
        )
        fig.update_layout(
            # ✅ Solid white background so all text is always visible
            plot_bgcolor='#ffffff',
            paper_bgcolor='#ffffff',
            # ✅ All font colors explicitly dark
            font=dict(color='#333333', size=13),
            xaxis=dict(
                title=dict(text='Date', font=dict(color='#333333', size=14)),
                tickfont=dict(color='#333333', size=12),
                gridcolor='#eeeeee',
                linecolor='#cccccc',
                showgrid=True,
            ),
            yaxis=dict(
                title=dict(text='Risk Probability', font=dict(color='#333333', size=14)),
                tickfont=dict(color='#333333', size=12),
                tickformat='.0%',
                range=[0, 1],
                gridcolor='#eeeeee',
                linecolor='#cccccc',
                showgrid=True,
            ),
            legend=dict(
                font=dict(color='#333333', size=13),
                bgcolor='rgba(255,255,255,0.9)',
                bordercolor='#cccccc',
                borderwidth=1,
            ),
            margin=dict(l=20, r=20, t=20, b=20),
            height=340,
        )
        st.plotly_chart(fig, use_container_width=True)
    except ImportError:
        import pandas as pd
        df = pd.DataFrame(predictions[::-1])
        df = df.set_index(df['prediction_date'].str[:10])
        st.line_chart(df['risk_probability'])
    st.markdown("</div>", unsafe_allow_html=True)

# ── Two columns: history + appointments ───────────────────────────────────────
col_left, col_right = st.columns([1, 1])

with col_left:
    # Assessment History
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-title'>📋 Recent Assessments</div>", unsafe_allow_html=True)
    if not predictions:
        st.info("No assessments yet. Go to the Predictor to check your risk!")
    else:
        for p in predictions[:6]:
            cls  = "risk-row risk-high" if p['risk_level'] == 'High' else "risk-row"
            bcls = "badge-high" if p['risk_level'] == 'High' else "badge-low"
            dt   = p['prediction_date'][:10] if p.get('prediction_date') else 'N/A'
            prob = p.get('risk_probability', 0)
            st.markdown(f"""
            <div class='{cls}'>
                <div style='display:flex;justify-content:space-between;'>
                    <strong>📅 {dt}</strong>
                    <span class='{bcls}'>{p['risk_level']} Risk · {prob:.1%}</span>
                </div>
                <div style='color:#555;font-size:13px;margin-top:4px;'>
                    Age {p.get('age','N/A')} · BMI {p.get('bmi','N/A')} ·
                    Glucose {p.get('glucose_level','N/A')} mg/dL
                </div>
            </div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Doctor's Notes
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-title'>📝 Doctor's Consultation Notes</div>", unsafe_allow_html=True)
    if not doctor_notes:
        st.info("No consultation notes from doctors yet.")
    else:
        for note in doctor_notes:
            dt = note.get('appointment_date', 'N/A')
            st.markdown(f"""
            <div class='note-row'>
                <strong>👨‍⚕️ {note.get('doctor_name','Doctor')}</strong>
                <span style='color:#888;font-size:12px;float:right;'>{note.get('specialty','')}</span>
                <br>📅 {dt} at {note.get('appointment_time','')}
                <br>🔬 <strong>Diagnosis:</strong> {note.get('diagnosis','N/A')}
                <br>💊 <strong>Prescription:</strong> {note.get('prescription','N/A')}
                <br>📋 <strong>Advice:</strong> {note.get('recommendations','N/A')}
                {f"<br>📆 <strong>Follow-up:</strong> {note.get('follow_up_date','')}" if note.get('follow_up_date') else ""}
            </div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_right:
    # Appointments
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-title'>📅 My Appointments</div>", unsafe_allow_html=True)
    if not appointments:
        st.info("No appointments yet.")
        if st.button("🏥 Find & Book a Doctor", use_container_width=True):
            st.switch_page("pages/7_DoctorFinder.py")
    else:
        for appt in appointments[:8]:
            status_color = "#27ae60" if appt['status'] == 'Confirmed' else "#c0392b"
            status_bg    = "#d5f5e3"  if appt['status'] == 'Confirmed' else "#fadbd8"
            st.markdown(f"""
            <div class='appt-row'>
                <div style='display:flex;justify-content:space-between;'>
                    <strong>👨‍⚕️ {appt['doctor_name']}</strong>
                    <span style='background:{status_bg};color:{status_color};
                          padding:3px 10px;border-radius:8px;font-size:12px;font-weight:700;'>
                        {appt['status']}
                    </span>
                </div>
                🏥 {appt['hospital_name']}<br>
                📅 {appt['appointment_date']} at {appt['appointment_time']}<br>
                🩺 {appt.get('doctor_specialty','Specialist')}
            </div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Profile
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-title'>👤 My Profile</div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='profile-box'>
        <strong>👤 Username:</strong> {user_info.get('username','N/A')}<br>
        <strong>📛 Name:</strong> {user_info.get('full_name','Not set')}<br>
        <strong>📧 Email:</strong> {user_info.get('email','N/A')}<br>
        <strong>📱 Phone:</strong> {user_info.get('phone','Not set')}<br>
        <strong>⚥ Gender:</strong> {user_info.get('gender','Not set')}<br>
        <strong>🎂 DOB:</strong> {user_info.get('date_of_birth','Not set')}<br>
        <strong>📅 Member since:</strong> {(user_info.get('created_at','')[:10]) or 'N/A'}
    </div>""", unsafe_allow_html=True)

    st.markdown("#### ✏️ Update Profile")
    with st.form("profile_form"):
        nf = st.text_input("Full Name",  value=user_info.get('full_name', '') or '')
        np = st.text_input("Phone",      value=user_info.get('phone', '') or '')
        ng = st.selectbox("Gender", ["Male","Female","Other","Prefer not to say"],
                          index=["Male","Female","Other","Prefer not to say"].index(
                              user_info.get('gender','Male') or 'Male')
                          if user_info.get('gender') in ["Male","Female","Other","Prefer not to say"]
                          else 0)
        if st.form_submit_button("💾 Save", use_container_width=True):
            update_user_profile(user_id, full_name=nf, phone=np, gender=ng)
            st.success("✅ Profile updated!")
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ── Health Tips ───────────────────────────────────────────────────────────────
if predictions:
    avg_risk = stats.get('avg_risk', 0) or 0
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-title'>💡 Personalised Health Tips</div>", unsafe_allow_html=True)
    if avg_risk >= 0.5:
        tips = [
            "🔴 Your average risk is HIGH. Please consult a neurologist as soon as possible.",
            "💊 If prescribed, take blood pressure and diabetes medications consistently.",
            "🥗 Follow a strict low-sodium, low-fat, high-fibre diet (DASH or Mediterranean).",
            "🚶 Walk 30 minutes daily — even gentle exercise significantly reduces stroke risk.",
            "🚭 If you smoke, quitting now cuts your stroke risk by 50% within one year.",
        ]
    else:
        tips = [
            "✅ Your risk is currently LOW — keep up the great work!",
            "🥦 Maintain a healthy, balanced diet rich in vegetables, fruits, and whole grains.",
            "🏃 Keep exercising regularly — aim for 150 minutes of moderate activity per week.",
            "🩺 Schedule an annual check-up to monitor blood pressure, glucose, and cholesterol.",
            "😴 Get 7–9 hours of sleep nightly — poor sleep is a hidden stroke risk factor.",
        ]
    for tip in tips:
        st.markdown(f"<p style='font-size:15px;margin:6px 0;'>{tip}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ── Navigation ─────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
n1, n2, n3, n4, n5 = st.columns(5)
with n1:
    if st.button("🏠 Home",       use_container_width=True): st.switch_page("main.py")
with n2:
    if st.button("🧮 Predictor",  use_container_width=True): st.switch_page("pages/5_Predictor.py")
with n3:
    if st.button("🏥 Doctors",    use_container_width=True): st.switch_page("pages/7_DoctorFinder.py")
with n4:
    if st.button("💬 Chatbot",    use_container_width=True): st.switch_page("pages/6_Chatbot.py")
with n5:
    if st.button("🚪 Logout",     use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.user_id   = None
        st.session_state.username  = None
        st.switch_page("pages/2_Login.py")

st.markdown("""
<div style='text-align:center;color:rgba(255,255,255,0.7);padding:20px;font-size:14px;'>
    © 2025 CerebroGuard | Patient Health Portal
</div>""", unsafe_allow_html=True)