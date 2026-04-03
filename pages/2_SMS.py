# pages/2_SMS.py
import streamlit as st
from detection_engine import CallShieldEngine

st.set_page_config(
    page_title="SMS Protection - CallShield AI",
    page_icon="💬",
    layout="wide"
)

st.title("💬 SMS Protection")
st.caption("Analyze SMS messages for scam patterns")

if 'sms_engine' not in st.session_state:
    st.session_state.sms_engine = CallShieldEngine()

# Example buttons
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔴 Scam SMS Examples")
    scam_examples = [
        "Your SBI account will be blocked. Click here: http://fake-link.com",
        "URGENT: Your OTP is 123456. Share to confirm transaction",
        "Congratulations! You won ₹10,00,000. Send ₹5000 to claim"
    ]
    for i, example in enumerate(scam_examples):
        if st.button(f"📱 {example[:50]}...", key=f"scam_{i}"):
            st.session_state.sms_text = example
            st.rerun()

with col2:
    st.markdown("### 🟢 Normal SMS Examples")
    normal_examples = [
        "Your order has been shipped. Tracking ID: ABC123",
        "Reminder: Doctor appointment tomorrow at 10 AM",
        "Your bill payment of ₹1500 was successful"
    ]
    for i, example in enumerate(normal_examples):
        if st.button(f"💬 {example[:50]}...", key=f"normal_{i}"):
            st.session_state.sms_text = example
            st.rerun()

sms_text = st.text_area(
    "📱 Paste SMS message here:",
    value=st.session_state.get('sms_text', ''),
    height=120,
    placeholder="Enter SMS content to analyze..."
)

if st.button("🔍 Analyze SMS", type="primary", use_container_width=True):
    if sms_text:
        # Process the message
        result = st.session_state.sms_engine.process_chunk(sms_text)
        
        # Store results in session
        st.session_state.analyze_message = sms_text
        st.session_state.analyze_risk = result['risk_score']
        st.session_state.analyze_pattern = result['pattern_sequence']
        st.session_state.analyze_intents = result['intents']
        st.session_state.analyze_channel = "💬 SMS"
        
        # Store history
        if 'sms_history' not in st.session_state:
            st.session_state.sms_history = []
        st.session_state.sms_history.append({
            'text': sms_text,
            'risk': result['risk_score'],
            'pattern': result['pattern_sequence']
        })
        
        # Go to results page
        st.switch_page("pages/5_Results.py")

# Back button
st.divider()
if st.button("← Back to Home", use_container_width=True):
    st.switch_page("app.py")