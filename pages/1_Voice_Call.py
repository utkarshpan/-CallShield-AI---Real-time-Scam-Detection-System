# pages/1_Voice_Call.py
import streamlit as st
import time
import os
from detection_engine import CallShieldEngine
from audio_handler import AudioProcessor

st.set_page_config(page_title="Voice Call Protection", page_icon="📞", layout="wide")

st.title("📞 Voice Call Protection")
st.caption("Real-time scam detection during phone calls")

if 'voice_engine' not in st.session_state:
    st.session_state.voice_engine = CallShieldEngine()
if 'voice_processor' not in st.session_state:
    st.session_state.voice_processor = AudioProcessor()
if 'voice_conversation' not in st.session_state:
    st.session_state.voice_conversation = []
if 'voice_risk' not in st.session_state:
    st.session_state.voice_risk = 0
if 'voice_alert' not in st.session_state:
    st.session_state.voice_alert = "No active alerts"
if 'voice_pattern' not in st.session_state:
    st.session_state.voice_pattern = "No patterns detected yet"

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 Live Conversation")
    
    conversation_container = st.container(height=350)
    with conversation_container:
        for entry in st.session_state.voice_conversation:
            if entry['type'] == 'caller':
                st.markdown(f"📞 **Caller:** {entry['text']}")
            else:
                st.markdown(f"🛡️ **System:** {entry['text']}")
    
    if st.button("🔴 Play Scam Call Demo", use_container_width=True):
        scam_files = ["sample_calls/scam_1.wav", "sample_calls/scam_2.wav", "sample_calls/scam_3.wav"]
        if all(os.path.exists(f) for f in scam_files):
            st.session_state.voice_engine.reset()
            st.session_state.voice_conversation = []
            st.session_state.voice_risk = 0
            
            progress = st.progress(0)
            status = st.empty()
            total = 9
            count = 0
            
            for file_idx, audio_file in enumerate(scam_files):
                status.text(f"🎙️ Playing part {file_idx + 1} of 3...")
                for chunk in st.session_state.voice_processor.transcribe_audio_file(audio_file):
                    count += 1
                    progress.progress(count / total)
                    if chunk['text'] and not chunk['text'].startswith('[error'):
                        st.session_state.voice_conversation.append({'type': 'caller', 'text': chunk['text']})
                        result = st.session_state.voice_engine.process_chunk(chunk['text'])
                        st.session_state.voice_risk = result['risk_score']
                        st.session_state.voice_alert = result['alert_message']
                        st.session_state.voice_pattern = result['pattern_explanation']
                        if result['risk_score'] >= 80:
                            st.session_state.voice_conversation.append({'type': 'system', 'text': f"🚨 {result['alert_message']}"})
                    time.sleep(0.5)
            
            status.text("✅ Demo complete!")
            progress.empty()
            st.rerun()
        else:
            st.error("Audio files not found")
    
    user_text = st.text_input("Enter message:", placeholder="Type a message to analyze...")
    if st.button("Analyze", use_container_width=True) and user_text:
        result = st.session_state.voice_engine.process_chunk(user_text)
        
        # Store for results page
        st.session_state.analyze_message = user_text
        st.session_state.analyze_risk = result['risk_score']
        st.session_state.analyze_pattern = result['pattern_sequence']
        st.session_state.analyze_intents = result['intents']
        st.session_state.analyze_channel = "📞 Voice Call"
        
        st.switch_page("pages/5_Results.py")

with col2:
    st.subheader("📊 Risk Analysis")
    
    risk = st.session_state.voice_risk
    if risk >= 80:
        color = "#ff0000"
        label = "CRITICAL"
    elif risk >= 60:
        color = "#ff6600"
        label = "HIGH"
    elif risk >= 40:
        color = "#ffcc00"
        label = "MEDIUM"
    elif risk >= 20:
        color = "#99cc00"
        label = "LOW"
    else:
        color = "#00cc00"
        label = "SAFE"
    
    st.markdown(f"""
    <div style="text-align: center; background: rgba(0,0,0,0.5); border-radius: 20px; padding: 20px;">
        <h2 style="color: {color};">{label}</h2>
        <div style="background-color: #2d2d2d; border-radius: 15px; overflow: hidden;">
            <div style="width: {risk}%; background-color: {color}; height: 40px; border-radius: 15px;">
                <span style="color: white; line-height: 40px; padding-left: 10px;">{risk}%</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if risk >= 80:
        st.error(f"🚨 {st.session_state.voice_alert}")
    elif risk >= 60:
        st.warning(f"⚠️ {st.session_state.voice_alert}")
    else:
        st.info(f"ℹ️ {st.session_state.voice_alert}")
    
    st.subheader("🎯 Pattern Detection")
    st.info(st.session_state.voice_pattern)

st.divider()
if st.button("← Back to Home", use_container_width=True):
    st.switch_page("app.py")