import streamlit as st
import sys
from datetime import datetime, timedelta
from itertools import groupby
sys.path.append('..')

try:
    from database import (
        get_doctor_account, update_doctor_profile,
        get_doctor_appointments, get_all_high_risk_patients,
        get_patient_predictions_for_doctor,
        get_consultation_note, save_consultation_note, get_patient_notes_for_doctor,
        get_all_slots_for_doctor, add_availability_slot, remove_availability_slot,
        get_all_doctors, init_database
    )
    DATABASE_AVAILABLE = True
    init_database()
except Exception as e:
    DATABASE_AVAILABLE = False

st.set_page_config(page_title="Doctor Dashboard - CerebroGuard",
                   page_icon="🏥", layout="wide")

st.markdown("""
<style>
    #MainMenu, footer, header { visibility: hidden; }
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1a5276 0%, #154360 100%);
    }
    .block-container { padding-top: 1rem; }

    /* ── Global white text for dark background ── */
    html, body, [class*="css"], .stMarkdown, p, span, div,
    .stSelectbox, .stTextInput, .stTextArea, .stNumberInput, .stDateInput {
        color: white !important;
    }

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab-list"]  { background: transparent !important; }
    .stTabs [data-baseweb="tab"]       { color: rgba(255,255,255,0.7) !important; font-size:16px; font-weight:600; }
    .stTabs [aria-selected="true"]     { color: white !important; font-weight:800 !important; }
    .stTabs [data-baseweb="tab-highlight"] { background: #aed6f1 !important; }
    .stTabs [data-baseweb="tab-border"]    { background: rgba(255,255,255,0.2) !important; }

    /* ── Input fields — white text inside inputs, dark bg ── */
    .stTextInput input, .stTextArea textarea, .stNumberInput input {
        background: rgba(255,255,255,0.12) !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.35) !important;
        border-radius: 10px !important;
    }
    .stTextInput input::placeholder, .stTextArea textarea::placeholder {
        color: rgba(255,255,255,0.5) !important;
    }
    .stTextInput label, .stSelectbox label, .stTextArea label,
    .stDateInput label, .stNumberInput label {
        color: white !important; font-weight: 700 !important; font-size: 15px !important;
    }

    /* ── Selectbox ── */
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.12) !important;
        border: 1px solid rgba(255,255,255,0.35) !important;
        border-radius: 10px !important;
        color: white !important;
    }
    .stSelectbox svg { fill: white !important; }

    /* ── Info / warning / success boxes ── */
    .stInfo, .stWarning, .stSuccess, .stError {
        color: #333 !important;
    }
    div[data-testid="stInfoMessage"] p,
    div[data-testid="stWarningMessage"] p,
    div[data-testid="stSuccessMessage"] p,
    div[data-testid="stErrorMessage"] p { color: #333 !important; }

    /* ── Caption / small text ── */
    .stCaption, [data-testid="stCaptionContainer"] { color: rgba(255,255,255,0.65) !important; }

    /* ── Metric widgets ── */
    [data-testid="stMetricLabel"]  { color: rgba(255,255,255,0.8) !important; }
    [data-testid="stMetricValue"]  { color: white !important; }

    /* ── Expander ── */
    .streamlit-expanderHeader { color: white !important; font-weight: 700 !important; }
    .streamlit-expanderContent { background: rgba(255,255,255,0.08) !important; }

    /* ── Dataframe ── */
    [data-testid="stDataFrame"] { color: #333 !important; }

    /* ══ WHITE CARDS — keep text dark inside them ══ */
    .dash-title { text-align:center; color:#aed6f1 !important; font-size:38px; font-weight:900; margin-bottom:4px; }
    .dash-sub   { text-align:center; color:rgba(255,255,255,0.75) !important; font-size:16px; margin-bottom:24px; }

    .stat-card {
        background: rgba(255,255,255,0.97);
        border-radius: 16px; padding: 22px; text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    }
    .stat-val   { font-size: 40px; font-weight: 900; color: #1a5276 !important; }
    .stat-label { font-size: 14px; color: #555 !important; font-weight: 600; margin-top: 5px; }

    .card {
        background: rgba(255,255,255,0.97);
        border-radius: 16px; padding: 26px; margin: 14px 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    .card-title {
        font-size: 20px; font-weight: 800; color: #1a5276 !important;
        border-left: 5px solid #2e86c1; padding-left: 14px;
        margin-bottom: 18px;
    }
    .appt-row {
        background: #f4f6f7; border-radius: 12px;
        padding: 14px 18px; margin: 8px 0; color: #333 !important;
        border-left: 5px solid #2e86c1; font-size: 14px; line-height: 1.9;
    }
    .appt-row-high { border-left-color: #e74c3c !important; }
    .patient-row {
        background: #fef5f5; border-radius: 12px; color: #333 !important;
        padding: 14px 18px; margin: 8px 0;
        border-left: 5px solid #e74c3c; font-size: 14px; line-height: 1.9;
    }
    .note-box {
        background: #fef9e7; border: 1px solid #f0c040; color: #333 !important;
        border-radius: 12px; padding: 16px 20px; margin: 10px 0;
        font-size: 14px; line-height: 1.8;
    }
    .badge-conf { background:#d5f5e3; color:#1e8449 !important; padding:3px 10px; border-radius:8px; font-size:12px; font-weight:700; }
    .badge-canc { background:#fadbd8; color:#c0392b !important; padding:3px 10px; border-radius:8px; font-size:12px; font-weight:700; }
    .badge-high { background:#fadbd8; color:#c0392b !important; padding:3px 10px; border-radius:8px; font-size:12px; font-weight:700; }
    .badge-low  { background:#d5f5e3; color:#1e8449 !important; padding:3px 10px; border-radius:8px; font-size:12px; font-weight:700; }
    .profile-box {
        background: linear-gradient(135deg, #d6eaf8, #eaf4fb);
        border-radius: 12px; padding: 20px 24px;
        font-size: 15px; color: #333 !important; line-height: 2.4;
    }

    /* ── Buttons ── */
    .stButton > button {
        background: linear-gradient(135deg, #1a5276 0%, #2e86c1 100%);
        color: white !important; border: 2px solid rgba(255,255,255,0.3);
        border-radius: 12px; padding: 12px 20px;
        font-size: 15px; font-weight: 700; transition: all 0.2s ease;
    }
    .stButton > button:hover { transform: translateY(-2px); border-color: white; }

    /* ── Markdown headings outside cards ── */
    h1, h2, h3, h4 { color: white !important; }
</style>
""", unsafe_allow_html=True)

# ── Auth Gate ─────────────────────────────────────────────────────────────────
if not st.session_state.get("doctor_logged_in"):
    st.markdown("""
    <div style='background:rgba(255,255,255,0.97);border-radius:18px;padding:50px;
                text-align:center;margin:60px auto;max-width:500px;'>
        <h2 style='color:#1a5276;'>👨‍⚕️ Doctor Login Required</h2>
        <p style='color:#555;'>Please login with your doctor credentials to access this portal.</p>
    </div>""", unsafe_allow_html=True)
    if st.button("🔐 Go to Login"):
        st.switch_page("pages/2_Login.py")
    st.stop()

if not DATABASE_AVAILABLE:
    st.error("⚠️ Database not available.")
    st.stop()

# ── Load doctor info ──────────────────────────────────────────────────────────
account_id  = st.session_state.doctor_id
doctor_info = get_doctor_account(account_id) or {}
doc_name    = doctor_info.get("full_name", "Doctor")
specialty   = doctor_info.get("specialty", "")
hospital    = doctor_info.get("hospital", "")

# Match to catalogue doctor for appointment lookup
catalogue_id = None
all_catalogue = get_all_doctors()
for d in all_catalogue:
    if (d['name'].lower() in doc_name.lower() or
            doc_name.lower() in d['name'].lower()):
        catalogue_id = d['doctor_id']
        break

# ── Header + Stats ────────────────────────────────────────────────────────────
st.markdown(f"<h1 class='dash-title'>🏥 Dr. {doc_name}'s Portal</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='dash-sub'>{specialty}  ·  {hospital}</p>", unsafe_allow_html=True)

appts         = get_doctor_appointments(catalogue_id) if catalogue_id else []
confirmed     = [a for a in appts if a['status'] == 'Confirmed']
high_risk_pts = get_all_high_risk_patients()
all_slots     = get_all_slots_for_doctor(catalogue_id) if catalogue_id else []
free_slots    = [s for s in all_slots if not s['is_booked']]

c1, c2, c3, c4 = st.columns(4)
for col, val, label in [
    (c1, len(confirmed),    "📅 Upcoming Appointments"),
    (c2, len(appts),        "📋 Total Appointments"),
    (c3, len(high_risk_pts),"🚨 High-Risk Patients"),
    (c4, len(free_slots),   "🟢 Free Slots Available"),
]:
    with col:
        st.markdown(f"""
        <div class='stat-card'>
            <div class='stat-val'>{val}</div>
            <div class='stat-label'>{label}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📅 My Appointments",
    "🚨 High-Risk Patients",
    "📝 Consultation Notes",
    "🗓️ Manage Schedule",
    "👤 My Profile",
])


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 1 ─ MY APPOINTMENTS
# ═══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-title'>📅 Patient Appointments</div>", unsafe_allow_html=True)

    if not catalogue_id:
        st.warning("⚠️ Your account is not yet linked to the doctor catalogue. Please contact admin.")
    elif not appts:
        st.info("📭 No appointments yet. They will appear here once patients book with you.")
    else:
        status_filter = st.selectbox("Filter by Status", ["All","Confirmed","Cancelled"],
                                     key="t1_filter")
        shown = appts if status_filter == "All" else [a for a in appts if a['status'] == status_filter]
        st.markdown(f"**Showing {len(shown)} appointment(s)**")

        for appt in shown:
            bcls = "badge-conf" if appt['status'] == 'Confirmed' else "badge-canc"
            rcls = "appt-row appt-row-high" if appt.get('risk_level') == 'High' else "appt-row"
            risk_badge = ""
            if appt.get('risk_level'):
                rb = "badge-high" if appt['risk_level'] == 'High' else "badge-low"
                risk_badge = f"&nbsp;<span class='{rb}'>{appt['risk_level']} Risk ({appt.get('risk_probability',0):.0%})</span>"

            st.markdown(f"""
            <div class='{rcls}'>
                <div style='display:flex;justify-content:space-between;align-items:center;'>
                    <strong style='font-size:16px;color:#1a5276;'>
                        {appt.get('patient_name','Unknown')}
                    </strong>
                    <span><span class='{bcls}'>{appt['status']}</span>{risk_badge}</span>
                </div>
                📆 <strong>{appt['appointment_date']}</strong> at <strong>{appt['appointment_time']}</strong>
                &nbsp;|&nbsp; 🆔 APT-{appt['appointment_id']:04d}<br>
                📞 {appt.get('patient_phone','N/A')}
                &nbsp;|&nbsp; 📧 {appt.get('patient_email','N/A')}
                {f"<br>📝 <em>{appt['patient_notes']}</em>" if appt.get('patient_notes') else ""}
            </div>""", unsafe_allow_html=True)

            # Health data expander
            if any([appt.get('bmi'), appt.get('glucose_level'), appt.get('patient_age')]):
                with st.expander(f"🔬 Health Data — {appt.get('patient_name','Patient')}"):
                    m1, m2, m3, m4 = st.columns(4)
                    m1.metric("Age",        appt.get('patient_age','N/A'))
                    m2.metric("BMI",        appt.get('bmi','N/A'))
                    m3.metric("Glucose",    f"{appt.get('glucose_level','N/A')} mg/dL")
                    m4.metric("Risk Score", f"{appt.get('risk_probability',0):.1%}")
                    flags = []
                    if appt.get('hypertension'):  flags.append("🔴 Hypertension")
                    if appt.get('heart_disease'): flags.append("🔴 Heart Disease")
                    if appt.get('smoking_status') in ['smokes','formerly smoked']:
                        flags.append("🟡 Smoker/Ex-smoker")
                    if flags:
                        st.markdown("**Clinical flags:** " + " &nbsp; ".join(flags),
                                    unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 2 ─ HIGH-RISK PATIENTS
# ═══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-title'>🚨 Platform-wide High-Risk Patients</div>",
                unsafe_allow_html=True)
    st.caption("All patients on CerebroGuard who have at least one High-Risk assessment.")

    if not high_risk_pts:
        st.info("✅ No high-risk patients found on the platform.")
    else:
        search = st.text_input("🔍 Search by name / email", key="hr_search",
                               placeholder="Type to filter...")
        filtered = [p for p in high_risk_pts
                    if not search or search.lower() in
                    (p.get('full_name','') + p.get('email','')).lower()]
        st.markdown(f"**{len(filtered)} high-risk patient(s)**")

        for pt in filtered:
            st.markdown(f"""
            <div class='patient-row'>
                <div style='display:flex;justify-content:space-between;'>
                    <strong style='color:#1a5276;font-size:15px;'>{pt.get('full_name','Unknown')}</strong>
                    <span class='badge-high'>Max Risk: {pt.get('max_risk',0):.1%}</span>
                </div>
                📧 {pt.get('email','N/A')} &nbsp;|&nbsp; 📞 {pt.get('phone','N/A')}<br>
                🔢 {pt.get('total_checks',0)} assessment(s)
                &nbsp;|&nbsp; 📅 Last: {(pt.get('last_check','')[:10]) or 'N/A'}
            </div>""", unsafe_allow_html=True)

            with st.expander(f"📋 Full Risk History — {pt.get('full_name','Patient')}"):
                history = get_patient_predictions_for_doctor(pt['user_id'])
                if history:
                    import pandas as pd
                    df = pd.DataFrame(history)[
                        ['prediction_date','risk_level','risk_probability',
                         'age','bmi','glucose_level','hypertension',
                         'heart_disease','smoking_status']
                    ]
                    df.columns = ['Date','Risk','Score','Age','BMI',
                                  'Glucose (mg/dL)','BP','Heart Dis.','Smoking']
                    df['Date']  = df['Date'].str[:16]
                    df['Score'] = df['Score'].apply(lambda x: f"{x:.1%}")
                    st.dataframe(df, use_container_width=True)
                else:
                    st.info("No history available.")
    st.markdown("</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 3 ─ CONSULTATION NOTES
# ═══════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-title'>📝 Write / View Consultation Notes</div>",
                unsafe_allow_html=True)

    confirmed_appts = [a for a in appts if a['status'] == 'Confirmed']

    if not confirmed_appts:
        st.info("📭 No confirmed appointments found. Notes can be written for confirmed appointments.")
    else:
        labels = [
            f"APT-{a['appointment_id']:04d}  |  {a.get('patient_name','?')}  |  "
            f"{a['appointment_date']}  {a['appointment_time']}"
            for a in confirmed_appts
        ]
        chosen_label = st.selectbox("Select Appointment", labels, key="note_sel")
        chosen_appt  = confirmed_appts[labels.index(chosen_label)]
        appt_id      = chosen_appt['appointment_id']
        patient_id   = chosen_appt['user_id']

        existing = get_consultation_note(appt_id)

        # Context banner
        risk_txt = f"{chosen_appt.get('risk_level','Not assessed')} ({chosen_appt.get('risk_probability',0):.1%})" \
                   if chosen_appt.get('risk_level') else "Not assessed"
        st.markdown(f"""
        <div style='background:#eaf4fb;border-radius:10px;padding:12px 16px;
                    margin-bottom:14px;font-size:14px;color:#1a5276;'>
            👤 <strong>{chosen_appt.get('patient_name','N/A')}</strong> &nbsp;|&nbsp;
            📅 {chosen_appt['appointment_date']} at {chosen_appt['appointment_time']}<br>
            🚨 <strong>Risk:</strong> {risk_txt}
            {f" &nbsp;|&nbsp; 🎂 {chosen_appt.get('date_of_birth','')}" if chosen_appt.get('date_of_birth') else ""}
        </div>""", unsafe_allow_html=True)

        with st.form(f"note_form_{appt_id}"):
            diagnosis = st.text_area(
                "🔬 Diagnosis / Clinical Assessment *",
                value=existing.get('diagnosis','') if existing else "",
                height=100, placeholder="Describe your clinical findings and diagnosis...")
            prescription = st.text_area(
                "💊 Prescription / Medications",
                value=existing.get('prescription','') if existing else "",
                height=100, placeholder="List medications, dosage, and duration...")
            recommendations = st.text_area(
                "📋 Lifestyle Recommendations",
                value=existing.get('recommendations','') if existing else "",
                height=100, placeholder="Diet, exercise, follow-up tests, lifestyle changes...")
            follow_up = st.text_input(
                "📆 Follow-Up Date (optional)",
                value=existing.get('follow_up_date','') if existing else "",
                placeholder="YYYY-MM-DD")

            btn_label = "🔄 Update Consultation Note" if existing else "💾 Save Consultation Note"
            if st.form_submit_button(btn_label, use_container_width=True):
                if not diagnosis.strip():
                    st.error("❌ Diagnosis/Assessment field is required.")
                else:
                    note_id = save_consultation_note(
                        appointment_id=appt_id,
                        doctor_account_id=account_id,
                        patient_user_id=patient_id,
                        diagnosis=diagnosis.strip(),
                        prescription=prescription.strip(),
                        recommendations=recommendations.strip(),
                        follow_up_date=follow_up.strip() or None,
                    )
                    if note_id:
                        st.success("✅ Consultation note saved! The patient can view it on their dashboard.")
                        st.rerun()

        # Previous notes for this patient
        prev = get_patient_notes_for_doctor(account_id, patient_id)
        if len(prev) > 1:
            st.markdown("#### 📁 Previous Notes for This Patient")
            for n in prev[1:]:
                st.markdown(f"""
                <div class='note-box'>
                    <strong>📅 {n.get('appointment_date','')} at {n.get('appointment_time','')}</strong><br>
                    🔬 <strong>Diagnosis:</strong> {n.get('diagnosis','')}<br>
                    💊 <strong>Prescription:</strong> {n.get('prescription','N/A')}<br>
                    📋 <strong>Recommendations:</strong> {n.get('recommendations','N/A')}<br>
                    {f"📆 <strong>Follow-up:</strong> {n.get('follow_up_date','')}" if n.get('follow_up_date') else ""}
                </div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 4 ─ MANAGE SCHEDULE
# ═══════════════════════════════════════════════════════════════════════════════
with tab4:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-title'>🗓️ Manage Your Availability</div>", unsafe_allow_html=True)

    if not catalogue_id:
        st.warning("⚠️ Your account is not linked to the doctor catalogue. Contact admin to link it.")
    else:
        # Add slot
        st.markdown("#### ➕ Add New Availability Slot")
        a1, a2, a3 = st.columns([2, 2, 1])
        with a1:
            new_date = st.date_input("📅 Date",
                                     min_value=datetime.now().date() + timedelta(days=1),
                                     key="add_date")
        with a2:
            time_opts = [
                "08:00 AM","08:30 AM","09:00 AM","09:30 AM","10:00 AM","10:30 AM",
                "11:00 AM","11:30 AM","12:00 PM","02:00 PM","02:30 PM",
                "03:00 PM","03:30 PM","04:00 PM","04:30 PM","05:00 PM","05:30 PM"
            ]
            new_time = st.selectbox("🕐 Time Slot", time_opts, key="add_time")
        with a3:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("➕ Add Slot", use_container_width=True):
                r = add_availability_slot(catalogue_id, str(new_date), new_time)
                if r:
                    st.success(f"✅ Added: {new_date} at {new_time}")
                    st.rerun()
                else:
                    st.warning("⚠️ Slot already exists.")

        st.markdown("---")
        st.markdown("#### 📋 Your Upcoming Schedule")

        schedule = get_all_slots_for_doctor(catalogue_id)
        if not schedule:
            st.info("📭 No upcoming slots. Add some above.")
        else:
            schedule.sort(key=lambda x: x['date'])
            for date_key, grp in groupby(schedule, key=lambda x: x['date']):
                date_slots = list(grp)
                try:
                    date_display = datetime.strptime(date_key,"%Y-%m-%d").strftime("%A, %d %b %Y")
                except Exception:
                    date_display = date_key
                st.markdown(f"**📅 {date_display}**")
                cols = st.columns(4)
                for idx, slot in enumerate(date_slots):
                    with cols[idx % 4]:
                        if slot['is_booked']:
                            st.markdown(f"""
                            <div style='background:#fadbd8;border-radius:8px;padding:8px 10px;
                                        margin:4px 0;font-size:12px;color:#c0392b;font-weight:700;'>
                                🔴 {slot['time_slot']}<br>
                                <span style='color:#555;font-size:11px;font-weight:400;'>
                                    {slot.get('patient_name','Booked')}
                                </span>
                            </div>""", unsafe_allow_html=True)
                        else:
                            st.markdown(f"""
                            <div style='background:#d5f5e3;border-radius:8px;padding:8px 10px;
                                        margin:4px 0;font-size:12px;color:#1e8449;font-weight:700;'>
                                🟢 {slot['time_slot']}
                            </div>""", unsafe_allow_html=True)
                            if st.button(f"❌ {slot['time_slot']}",
                                         key=f"rm_{slot['slot_id']}",
                                         use_container_width=True):
                                if remove_availability_slot(slot['slot_id'], catalogue_id):
                                    st.success("Slot removed.")
                                    st.rerun()
                st.markdown("---")
    st.markdown("</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 5 ─ MY PROFILE
# ═══════════════════════════════════════════════════════════════════════════════
with tab5:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-title'>👤 My Profile</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        <div class='profile-box'>
            <strong>📛 Name:</strong> {doctor_info.get('full_name','N/A')}<br>
            <strong>📧 Email:</strong> {doctor_info.get('email','N/A')}<br>
            <strong>📱 Phone:</strong> {doctor_info.get('phone','Not set')}<br>
            <strong>🪪 License:</strong> {doctor_info.get('license_number','N/A')}<br>
            <strong>✅ Verified:</strong> {'Yes ✅' if doctor_info.get('is_verified') else 'Pending ⏳'}
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class='profile-box'>
            <strong>🩺 Specialty:</strong> {doctor_info.get('specialty','N/A')}<br>
            <strong>🏥 Hospital:</strong> {doctor_info.get('hospital','N/A')}<br>
            <strong>🎓 Experience:</strong> {doctor_info.get('experience_years',0)} years<br>
            <strong>📅 Member since:</strong> {(doctor_info.get('created_at','')[:10]) or 'N/A'}<br>
            <strong>🕐 Last login:</strong> {(doctor_info.get('last_login','')[:16]) or 'N/A'}
        </div>""", unsafe_allow_html=True)

    st.markdown("#### ✏️ Update Profile")
    with st.form("doc_profile_form"):
        nf = st.text_input("Full Name",    value=doctor_info.get('full_name','') or '')
        nh = st.text_input("Hospital",     value=doctor_info.get('hospital','') or '')
        np = st.text_input("Phone",        value=doctor_info.get('phone','') or '')
        nx = st.number_input("Years of Experience", min_value=0, max_value=60,
                             value=int(doctor_info.get('experience_years',0) or 0))
        if st.form_submit_button("💾 Save Changes", use_container_width=True):
            update_doctor_profile(account_id, full_name=nf, hospital=nh, phone=np, experience_years=nx)
            st.success("✅ Profile updated successfully!")
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# ── Navigation ─────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
n1, n2, n3, n4 = st.columns(4)
with n1:
    if st.button("🏠 Home",    use_container_width=True): st.switch_page("main.py")
with n2:
    if st.button("💬 Chatbot", use_container_width=True): st.switch_page("pages/6_Chatbot.py")
with n3:
    if st.button("📞 Contact", use_container_width=True): st.switch_page("pages/4_Contact.py")
with n4:
    if st.button("🚪 Logout",  use_container_width=True):
        st.session_state.doctor_logged_in = False
        st.session_state.doctor_id        = None
        st.session_state.doctor_name      = None
        st.session_state.is_verified      = False
        st.switch_page("pages/2_Login.py")

st.markdown("""
<div style='text-align:center;color:rgba(255,255,255,0.6);padding:20px;font-size:13px;'>
    © 2025 CerebroGuard | Doctor Portal
</div>""", unsafe_allow_html=True)