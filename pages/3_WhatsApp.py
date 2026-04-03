# pages/3_WhatsApp.py
import streamlit as st
from detection_engine import CallShieldEngine

st.set_page_config(
    page_title="WhatsApp Protection - CallShield AI",
    page_icon="💚",
    layout="wide"
)

st.title("💚 WhatsApp Protection")
st.caption("Analyze WhatsApp messages for scam patterns")

if 'wa_engine' not in st.session_state:
    st.session_state.wa_engine = CallShieldEngine()
if 'wa_history' not in st.session_state:
    st.session_state.wa_history = []

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔴 Scam WhatsApp Examples")
    scam_examples = [
        "Hello, I'm calling from SBI bank. Your account will be blocked today. Share OTP now",
        "Urgent! Your KYC needs update. Click here: http://fake-link.com",
        "Hi, I'm from RBI. Your PAN card is being misused. Verify immediately"
    ]
    for i, example in enumerate(scam_examples):
        if st.button(f"💚 {example[:50]}...", key=f"scam_{i}"):
            st.session_state.wa_text = example
            st.rerun()

with col2:
    st.markdown("### 🟢 Normal WhatsApp Examples")
    normal_examples = [
        "Hey, want to grab coffee later?",
        "Your pizza order is out for delivery!",
        "Mom: Please get milk on your way home"
    ]
    for i, example in enumerate(normal_examples):
        if st.button(f"💬 {example[:50]}...", key=f"normal_{i}"):
            st.session_state.wa_text = example
            st.rerun()

wa_text = st.text_area(
    "💚 Paste WhatsApp message here:",
    value=st.session_state.get('wa_text', ''),
    height=120,
    placeholder="Enter WhatsApp message to analyze..."
)

if st.button("🔍 Analyze WhatsApp", type="primary", use_container_width=True):
    if wa_text:
        result = st.session_state.wa_engine.process_chunk(wa_text)
        
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Risk Score", f"{result['risk_score']}%")
        with col_b:
            risk_level = "CRITICAL" if result['risk_score'] >= 80 else "HIGH" if result['risk_score'] >= 60 else "MEDIUM" if result['risk_score'] >= 40 else "LOW"
            st.metric("Risk Level", risk_level)
        with col_c:
            st.metric("Patterns Found", len(result['pattern_sequence']))
        
        if result['risk_score'] >= 80:
            st.error(f"🚨 {result['alert_message']}")
        elif result['risk_score'] >= 60:
            st.warning(f"⚠️ {result['alert_message']}")
        else:
            st.success(f"✅ {result['alert_message']}")
        
        st.info(f"**🎯 Pattern Detected:** {result['pattern_explanation']}")
        
        st.session_state.wa_history.append({
            'text': wa_text,
            'risk': result['risk_score']
        })

if st.session_state.wa_history:
    st.divider()
    st.subheader("📜 Analysis History")
    for item in reversed(st.session_state.wa_history[-5:]):
        risk_color = "🔴" if item['risk'] >= 80 else "🟠" if item['risk'] >= 60 else "🟡"
        st.markdown(f"{risk_color} **Risk: {item['risk']}%** | {item['text'][:80]}...")

st.divider()
if st.button("← Back to Home", use_container_width=True):
    st.switch_page("app.py")