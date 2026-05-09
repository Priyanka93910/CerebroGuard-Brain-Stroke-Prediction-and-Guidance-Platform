import streamlit as st
import base64
import os
import re

st.set_page_config(page_title="Health Assistant - CerebroGuard", page_icon="💬", layout="wide")

# ── Session State Init ────────────────────────────────────────────────────────
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'last_prediction' not in st.session_state:
    st.session_state.last_prediction = None
if 'pending_question' not in st.session_state:
    st.session_state.pending_question = None

# ── Background ────────────────────────────────────────────────────────────────
def set_bg(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as img:
            encoded = base64.b64encode(img.read()).decode()
        st.markdown(f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover; background-position: center;
            background-repeat: no-repeat; background-attachment: fixed;
        }}
        </style>""", unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #f0f4f8 0%, #d9e8f5 100%);
        }
        </style>""", unsafe_allow_html=True)

set_bg("img4.avif")

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none !important;}
    .block-container { padding-top: 1rem; }

    .chat-title {
        text-align: center; color: #003366;
        font-size: 36px; font-weight: 700; margin-bottom: 5px;
    }
    .chat-subtitle {
        text-align: center; color: #555;
        font-size: 16px; margin-bottom: 20px;
    }
    .message-user {
        background: linear-gradient(135deg, #3366cc, #66a3ff);
        color: white; padding: 12px 18px;
        border-radius: 18px 18px 5px 18px;
        margin: 8px 0 8px auto; max-width: 72%;
        width: fit-content; float: right; clear: both;
        font-size: 15px;
    }
    .message-bot {
        background: rgba(255,255,255,0.95);
        color: #222; padding: 14px 18px;
        border-radius: 18px 18px 18px 5px;
        border-left: 4px solid #3366cc;
        margin: 8px auto 8px 0; max-width: 75%;
        width: fit-content; float: left; clear: both;
        line-height: 1.7; font-size: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }
    .ai-badge {
        display: inline-block; background: #3366cc; color: white;
        font-size: 11px; padding: 2px 8px; border-radius: 10px;
        margin-bottom: 6px; font-weight: 600;
    }
    .stButton > button {
        background: linear-gradient(135deg, #3366cc 0%, #66a3ff 100%);
        color: white; border: none; border-radius: 10px;
        padding: 10px 20px; font-size: 15px; font-weight: 600;
        transition: all 0.2s ease;
    }
    .stButton > button:hover { transform: translateY(-2px); }
    .warning-badge {
        background: #fff3cd; border-left: 4px solid #ffc107;
        padding: 15px; border-radius: 10px;
        margin: 15px 0; color: #856404;
    }
</style>
""", unsafe_allow_html=True)


# ── AI Response Function ───────────────────────────────────────────────────────
def get_ai_response(question: str, risk_info: dict = None) -> str:
    try:
        import anthropic

        risk_context = ""
        if risk_info:
            risk_context = (
                f"\n\nUSER CONTEXT: This patient completed a stroke risk assessment. "
                f"Risk Level = {risk_info.get('risk_level', 'Unknown')}, "
                f"Probability = {risk_info.get('probability', 0):.1%}. "
                f"Personalise your response to their risk level."
            )

        system_prompt = (
            "You are CerebroGuard, a specialized AI health assistant for brain stroke "
            "prevention, awareness, and guidance. You work inside a medical web application "
            "used by patients in India.\n\n"
            "Guidelines:\n"
            "- Answer questions about stroke symptoms, prevention, risk factors, diet, "
            "exercise, medications, and recovery\n"
            "- Be empathetic, accurate, and medically informed\n"
            "- Always recommend consulting a certified doctor for serious concerns\n"
            "- Keep responses clear and concise (4-6 sentences max)\n"
            "- Use simple language, avoid heavy jargon\n"
            "- Never diagnose. Focus on education, prevention, and next steps\n"
            "- If unrelated to health, politely redirect to stroke topics\n"
            + risk_context
        )

        client = anthropic.Anthropic()   # reads ANTHROPIC_API_KEY from environment
        message = client.messages.create(
            model="claude-sonnet-4-5",   # correct model string
            max_tokens=400,
            system=system_prompt,
            messages=[{"role": "user", "content": question}]
        )
        return message.content[0].text

    except ImportError:
        return _local_response(question)
    except Exception:
        return _local_response(question)


# ── Local Fallback Knowledge Base ─────────────────────────────────────────────
def _local_response(question: str) -> str:
    try:
        from chatbot_knowledge_base import get_enhanced_response
        return get_enhanced_response(question)
    except ImportError:
        pass

    q = question.lower()
    kb = {
        "what is stroke":  "A stroke occurs when blood supply to the brain is cut off. Two main types: ischemic (blood clot, 87%) and hemorrhagic (bleeding, 13%). Brain cells die within minutes — immediate care is critical.",
        "symptom":         "Remember F.A.S.T — Face drooping, Arm weakness, Speech difficulty, Time to call 108. Other signs: sudden confusion, vision loss, severe headache, loss of balance.",
        "prevention":      "Control blood pressure, maintain healthy BMI, exercise 150 min/week, eat a balanced diet (low sodium), quit smoking, limit alcohol, manage diabetes, get regular checkups.",
        "risk factor":     "Major risk factors: high blood pressure (#1), diabetes, heart disease, smoking, obesity, high cholesterol, age 55+, family history, physical inactivity.",
        "diet":            "Eat more fruits, vegetables, whole grains, fish, nuts, and olive oil (Mediterranean or DASH diet). Reduce sodium to under 1,500 mg/day and cut processed foods.",
        "exercise":        "Aim for 150 min/week of moderate aerobic exercise — brisk walking, swimming, or cycling. Add strength training 2x/week. Even 30 min daily walks significantly reduce stroke risk.",
        "blood pressure":  "Normal BP is below 120/80 mmHg. High BP (140/90+) is the #1 controllable stroke risk factor. Manage with low-sodium diet, exercise, stress reduction, and prescribed medication.",
        "emergency":       "STROKE IS AN EMERGENCY — call 108 immediately! Note the exact time symptoms started. Clot-busting drugs (tPA) must be given within 3-4.5 hours for ischemic stroke.",
        "treatment":       "Ischemic stroke: tPA clot-busting drugs (within 3-4.5 hrs) or mechanical thrombectomy. Hemorrhagic stroke may need surgery. Time is brain — every minute counts.",
        "recovery":        "Recovery varies by severity. Includes physical, occupational, and speech therapy. Most improvement is in the first 3-6 months, but progress continues for years with consistent rehab.",
        "diabetes":        "Diabetes increases stroke risk 1.5-4x by damaging blood vessels. Keep HbA1c under 7%, monitor blood sugar, exercise regularly, and take medications as prescribed.",
        "smoking":         "Smoking doubles stroke risk by thickening blood, raising BP, and damaging vessel walls. Quitting reduces risk by 50% within 1 year and normalizes within 5-15 years.",
        "stress":          "Chronic stress raises blood pressure and causes inflammation. Manage with meditation, deep breathing, yoga, regular exercise, and adequate sleep of 7-9 hours nightly.",
        "cholesterol":     "High LDL cholesterol builds plaque in arteries. Keep LDL under 100 mg/dL through diet, exercise, and statins if prescribed by your doctor.",
        "bmi":             "BMI over 25 increases stroke risk by contributing to high BP, diabetes, and high cholesterol. Even 5-10% weight loss significantly lowers your overall risk.",
    }
    for key, resp in kb.items():
        if key in q:
            return resp
    return ("I'm here to help with stroke-related questions! Ask me about symptoms, "
            "prevention, diet, exercise, blood pressure, recovery, and more. "
            "For a medical emergency, call 108 immediately.")


# ── Process pending quick question (runs at top of each rerun) ────────────────
if st.session_state.pending_question:
    q_to_ask = st.session_state.pending_question
    st.session_state.pending_question = None
    st.session_state.chat_history.append({"role": "user", "content": q_to_ask})
    with st.spinner("🤖 Thinking..."):
        bot_reply = get_ai_response(q_to_ask, st.session_state.last_prediction)
    st.session_state.chat_history.append({"role": "bot", "content": bot_reply})


# ── Page Header ───────────────────────────────────────────────────────────────
st.markdown("<h1 class='chat-title'>🤖 CerebroGuard AI Health Assistant</h1>",
            unsafe_allow_html=True)
st.markdown(
    "<p class='chat-subtitle'>Ask anything about "
    "stroke prevention & healthy living</p>",
    unsafe_allow_html=True)

# ── Risk Banner ────────────────────────────────────────────────────────────────
pred = st.session_state.last_prediction
if pred:
    rl   = pred.get('risk_level', 'Unknown')
    prob = pred.get('probability', 0)
    if rl == "High":
        st.markdown(f"""
        <div class='warning-badge'>
            <strong>⚠️ Your Latest Assessment: High Risk ({prob:.1%})</strong><br>
            I know your risk score and will tailor my advice to you.
            Consider booking a doctor soon.
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style='background:#d4edda;border-left:4px solid #28a745;padding:15px;
                    border-radius:10px;margin:15px 0;color:#155724;'>
            <strong>✅ Your Latest Assessment: Low Risk ({prob:.1%})</strong><br>
            Great result! Ask me how to maintain and improve your health.
        </div>""", unsafe_allow_html=True)

# ── Quick Question Buttons ────────────────────────────────────────────────────
# NOTE: buttons set pending_question then rerun — this avoids calling a
# function inside a column block which caused the original error.
st.markdown("### 💡 Quick Questions")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🎯 What is a stroke?", use_container_width=True):
        st.session_state.pending_question = "What is a brain stroke and what causes it?"
        st.rerun()
    if st.button("🍎 Healthy diet tips?", use_container_width=True):
        st.session_state.pending_question = "What diet should I follow to prevent stroke?"
        st.rerun()

with col2:
    if st.button("⚠️ Stroke symptoms?", use_container_width=True):
        st.session_state.pending_question = "What are the warning signs and symptoms of a stroke?"
        st.rerun()
    if st.button("🏃 Exercise guidance?", use_container_width=True):
        st.session_state.pending_question = "What exercises help reduce stroke risk?"
        st.rerun()

with col3:
    if st.button("🛡️ Prevention tips?", use_container_width=True):
        st.session_state.pending_question = "How can I prevent a brain stroke?"
        st.rerun()
    if st.button("📊 Risk factors?", use_container_width=True):
        st.session_state.pending_question = "What are the major risk factors for brain stroke?"
        st.rerun()

# ── Chat Display ───────────────────────────────────────────────────────────────
st.markdown("---")

if not st.session_state.chat_history:
    st.markdown("""
    <div style='text-align:center;color:#555;padding:40px 20px;
                background:rgba(255,255,255,0.75);border-radius:15px;margin:15px 0;'>
        <h3 style='color:#003366;'>👋 Hello! I'm your CerebroGuard AI Assistant.</h3>
        <p>I can answer questions about stroke prevention, symptoms, diet, exercise,
        risk factors, and more.<br>
        Click a quick question above or type your own below!</p>
    </div>""", unsafe_allow_html=True)
else:
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(
                f"<div class='message-user'>👤 {msg['content']}</div>"
                "<div style='clear:both;'></div>",
                unsafe_allow_html=True)
        else:
            # Convert **bold** and newlines so they render inside HTML divs
            content = msg['content']
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            content = content.replace('\n', '<br>')
            st.markdown(
                f"<div class='message-bot'>"
                f"<span class='ai-badge'>🤖 CerebroGuard AI</span><br>{content}"
                f"</div><div style='clear:both;'></div>",
                unsafe_allow_html=True)

# ── Text Input + Buttons ──────────────────────────────────────────────────────
st.markdown("---")
user_input = st.text_input(
    "💬 Type your question here...",
    key="user_input",
    placeholder="e.g. What foods should I avoid? Is my blood pressure dangerous?"
)

col_a, col_b, col_c = st.columns([4, 1, 1])
with col_b:
    send_clicked = st.button("Send 📤", use_container_width=True)
with col_c:
    clear_clicked = st.button("Clear 🗑️", use_container_width=True)

# Handle send
if send_clicked:
    if user_input and user_input.strip():
        st.session_state.chat_history.append({"role": "user", "content": user_input.strip()})
        with st.spinner("🤖 Thinking..."):
            response = get_ai_response(user_input.strip(), st.session_state.last_prediction)
        st.session_state.chat_history.append({"role": "bot", "content": response})
        st.rerun()
    else:
        st.warning("⚠️ Please type a question before sending.")

# Handle clear
if clear_clicked:
    st.session_state.chat_history = []
    st.rerun()

# ── Disclaimer ────────────────────────────────────────────────────────────────
st.markdown("""
<div style='background:#fff3cd;border-left:4px solid #ffc107;padding:12px 18px;
            border-radius:10px;margin:20px 0;font-size:13px;color:#856404;'>
    ⚕️ <strong>Medical Disclaimer:</strong> This AI assistant provides general health
    information only. It is NOT a substitute for professional medical advice.
    Always consult a certified doctor for diagnosis or treatment.
    For a stroke emergency, call <strong>108</strong> immediately.
</div>""", unsafe_allow_html=True)

# ── Navigation ─────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
n1, n2, n3, n4, n5 = st.columns(5)

with n1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("main.py")
with n2:
    if st.button("🔒 Login", use_container_width=True):
        st.switch_page("pages/2_Login.py")
with n3:
    if st.button("🧮 Predictor", use_container_width=True):
        st.switch_page("pages/5_Predictor.py")
with n4:
    if st.button("🏥 Find Doctors", use_container_width=True):
        st.switch_page("pages/7_DoctorFinder.py")
with n5:
    if st.button("📞 Contact", use_container_width=True):
        st.switch_page("pages/4_Contact.py")

st.markdown("""
<div style='text-align:center;color:#003366;padding:20px;font-size:14px;'>
    © 2025 CerebroGuard | AI-Powered Health Assistant
</div>""", unsafe_allow_html=True)