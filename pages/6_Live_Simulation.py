# pages/6_Live_Simulation.py
import streamlit as st
import time

st.set_page_config(
    page_title="Live Call Simulation - CallShield AI",
    page_icon="🎙️",
    layout="wide"
)

# Professional Dark Theme CSS
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #0f0f23 100%);
    }
    
    /* Hide default streamlit elements */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Call Screen */
    .call-screen {
        background: linear-gradient(135deg, #1e1e2e, #2a2a3e);
        border-radius: 30px;
        padding: 40px;
        text-align: center;
        border: 1px solid rgba(78, 205, 196, 0.3);
        box-shadow: 0 10px 40px rgba(0,0,0,0.5);
    }
    
    .caller-avatar {
        width: 120px;
        height: 120px;
        background: linear-gradient(135deg, #4ecdc4, #667eea);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 20px;
        font-size: 3.5em;
        box-shadow: 0 0 30px rgba(78, 205, 196, 0.5);
        animation: avatarPulse 2s infinite;
    }
    
    @keyframes avatarPulse {
        0%, 100% { transform: scale(1); box-shadow: 0 0 30px rgba(78, 205, 196, 0.5); }
        50% { transform: scale(1.05); box-shadow: 0 0 50px rgba(78, 205, 196, 0.8); }
    }
    
    .caller-number {
        font-size: 1.2em;
        color: #888;
        margin: 10px 0;
    }
    
    .call-status {
        display: inline-block;
        padding: 5px 15px;
        background: rgba(78, 205, 196, 0.2);
        border-radius: 20px;
        color: #4ecdc4;
        font-size: 0.9em;
        animation: statusPulse 1.5s infinite;
    }
    
    @keyframes statusPulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.6; }
    }
    
    /* Message Bubbles */
    .message-container {
        margin: 20px 0;
        max-height: 400px;
        overflow-y: auto;
        padding: 10px;
    }
    
    .caller-message {
        background: linear-gradient(135deg, #2a2a3e, #1e1e2e);
        border-radius: 20px;
        padding: 12px 20px;
        margin: 10px 0;
        display: inline-block;
        max-width: 85%;
        border-left: 3px solid #4ecdc4;
        color: #e0e0e0;
        font-size: 1em;
    }
    
    .system-message {
        background: rgba(255, 107, 107, 0.15);
        border-radius: 20px;
        padding: 10px 15px;
        margin: 8px 0;
        border-left: 3px solid #ff6b6b;
        color: #ffaaaa;
        font-size: 0.9em;
    }
    
    .critical-message {
        background: rgba(255, 0, 0, 0.2);
        border-left: 3px solid #ff0000;
        color: #ff8888;
        font-weight: bold;
        animation: criticalPulse 1s infinite;
    }
    
    @keyframes criticalPulse {
        0%, 100% { background: rgba(255, 0, 0, 0.2); }
        50% { background: rgba(255, 0, 0, 0.4); }
    }
    
    /* Risk Meter */
    .risk-container {
        background: linear-gradient(135deg, #1e1e2e, #2a2a3e);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        border: 1px solid rgba(78, 205, 196, 0.2);
    }
    
    .risk-score {
        font-size: 4em;
        font-weight: bold;
        margin: 20px 0;
    }
    
    .risk-bar {
        background: #2d2d3e;
        border-radius: 15px;
        overflow: hidden;
        height: 30px;
        margin: 20px 0;
    }
    
    .risk-fill {
        height: 100%;
        transition: width 0.5s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        font-size: 0.9em;
    }
    
    /* Button Styles */
    .stButton button {
        background: linear-gradient(135deg, #4ecdc4, #667eea);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 12px 24px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(78, 205, 196, 0.4);
    }
    
    /* Pattern Progress */
    .pattern-step {
        background: rgba(255,255,255,0.05);
        border-radius: 15px;
        padding: 12px;
        margin: 10px 0;
        transition: all 0.3s;
    }
    
    .pattern-step.active {
        background: rgba(78, 205, 196, 0.2);
        border-left: 3px solid #4ecdc4;
    }
    
    .pattern-step.completed {
        background: rgba(78, 205, 196, 0.1);
        border-left: 3px solid #4ecdc4;
    }
    
    /* Title */
    .main-title {
        text-align: center;
        margin-bottom: 30px;
    }
    
    .main-title h1 {
        background: linear-gradient(135deg, #4ecdc4, #667eea);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5em;
    }
    
    .main-title p {
        color: #888;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<div class="main-title">
    <h1>🎙️ Live Call Simulation</h1>
    <p>Experience real-time scam detection during a simulated call</p>
</div>
""", unsafe_allow_html=True)

# Initialize session
if 'sim_active' not in st.session_state:
    st.session_state.sim_active = False
if 'sim_step' not in st.session_state:
    st.session_state.sim_step = 0
if 'sim_risk' not in st.session_state:
    st.session_state.sim_risk = 0
if 'sim_messages' not in st.session_state:
    st.session_state.sim_messages = []

# Call steps
steps = [
    {"text": "Hello sir, I'm calling from your bank.", "risk": 15, "type": "caller", "alert": "⚠️ Authority pattern detected", "critical": False},
    {"text": "Your account will be blocked today.", "risk": 45, "type": "caller", "alert": "⚠️ Fear/pressure tactic detected", "critical": False},
    {"text": "Please share the OTP immediately.", "risk": 90, "type": "caller", "alert": "🚨 CRITICAL: Scam pattern complete! DO NOT share OTP!", "critical": True}
]

col1, col2 = st.columns([1, 0.8], gap="large")

with col1:
    st.markdown('<div class="call-screen">', unsafe_allow_html=True)
    
    # Caller info
    st.markdown("""
    <div class="caller-avatar">📞</div>
    <h3 style="color: white;">Unknown Caller</h3>
    <div class="caller-number">+91 XXXXX XXXX</div>
    <div class="call-status">🔴 Call in progress...</div>
    """, unsafe_allow_html=True)
    
    # Message container
    st.markdown('<div class="message-container">', unsafe_allow_html=True)
    
    if not st.session_state.sim_active:
        st.info("👆 Click 'Start Simulated Call' to begin the demo")
        
        col_a, col_b, col_c = st.columns([1,2,1])
        with col_b:
            if st.button("📞 Start Simulated Scam Call", use_container_width=True):
                st.session_state.sim_active = True
                st.session_state.sim_step = 0
                st.session_state.sim_risk = 0
                st.session_state.sim_messages = []
                st.rerun()
    else:
        # Display messages
        for msg in st.session_state.sim_messages:
            if msg['type'] == 'caller':
                st.markdown(f"""
                <div style="text-align: left;">
                    <div class="caller-message">
                        📞 {msg['text']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                critical_class = " critical-message" if msg.get('critical', False) else ""
                st.markdown(f"""
                <div style="text-align: left;">
                    <div class="system-message{critical_class}">
                        🛡️ {msg['text']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Auto-advance simulation
        if st.session_state.sim_step < len(steps):
            step = steps[st.session_state.sim_step]
            
            # Check if this step already displayed
            step_displayed = False
            for msg in st.session_state.sim_messages:
                if msg.get('text') == step['text']:
                    step_displayed = True
                    break
            
            if not step_displayed:
                # Add caller message
                st.session_state.sim_messages.append({
                    'type': step['type'],
                    'text': step['text']
                })
                st.session_state.sim_risk = step['risk']
                
                # Add system alert
                st.session_state.sim_messages.append({
                    'type': 'system',
                    'text': step['alert'],
                    'critical': step['critical']
                })
                
                # Auto-advance step after delay
                time.sleep(1.5)
                st.session_state.sim_step += 1
                st.rerun()
            else:
                # Show next button for user control
                if st.button("➡️ Next", use_container_width=True):
                    st.session_state.sim_step += 1
                    st.rerun()
        else:
            st.success("✅ Call analysis complete!")
            st.markdown("""
            <div style="background: linear-gradient(135deg, #1e1e2e, #2a2a3e); border-radius: 15px; padding: 20px; margin-top: 20px;">
                <strong>📋 Final Analysis:</strong><br>
                • Scam pattern detected: <strong style="color: #4ecdc4;">Authority → Fear → Action</strong><br>
                • Risk level: <strong style="color: #ff6b6b;">CRITICAL (90%)</strong><br>
                • Recommendation: <strong>Hang up immediately and DO NOT share any information</strong>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🔄 Start New Simulation", use_container_width=True):
                st.session_state.sim_active = False
                st.session_state.sim_step = 0
                st.session_state.sim_risk = 0
                st.session_state.sim_messages = []
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="risk-container">', unsafe_allow_html=True)
    st.subheader("📊 Risk Analysis")
    
    risk = st.session_state.sim_risk
    
    if risk >= 80:
        color = "#ff0000"
        label = "CRITICAL"
        bg_color = "rgba(255,0,0,0.2)"
        message = "🚨 SCAM DETECTED! Do not share OTP!"
    elif risk >= 60:
        color = "#ff6600"
        label = "HIGH"
        bg_color = "rgba(255,102,0,0.2)"
        message = "⚠️ High scam probability"
    elif risk >= 40:
        color = "#ffcc00"
        label = "MEDIUM"
        bg_color = "rgba(255,204,0,0.2)"
        message = "⚡ Suspicious patterns detected"
    elif risk >= 20:
        color = "#99cc00"
        label = "LOW"
        bg_color = "rgba(153,204,0,0.2)"
        message = "🔔 Be cautious"
    else:
        color = "#00cc00"
        label = "SAFE"
        bg_color = "rgba(0,204,0,0.2)"
        message = "✅ No scam detected"
    
    st.markdown(f"""
    <div style="background: {bg_color}; border-radius: 15px; padding: 20px; text-align: center;">
        <div style="font-size: 2em; font-weight: bold; color: {color};">{label}</div>
        <div class="risk-score" style="color: {color};">{risk}%</div>
        <div class="risk-bar">
            <div class="risk-fill" style="width: {risk}%; background: {color};">{risk}%</div>
        </div>
        <p style="color: {color};">{message}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("🎯 Pattern Progress")
    
    patterns = [
        {"name": "Authority", "icon": "👔", "threshold": 15, "detected": risk >= 15},
        {"name": "Fear", "icon": "😨", "threshold": 45, "detected": risk >= 45},
        {"name": "Action Request", "icon": "🎯", "threshold": 80, "detected": risk >= 80}
    ]
    
    for p in patterns:
        if p["detected"]:
            status = "✅"
            active_class = "completed"
        elif risk >= p["threshold"] - 15:
            status = "⏳"
            active_class = "active"
        else:
            status = "○"
            active_class = ""
        
        st.markdown(f"""
        <div class="pattern-step {active_class}">
            {status} {p['icon']} <strong>{p['name']}</strong>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.caption("🛡️ CallShield AI analyzes manipulation patterns in real-time")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Back button
st.divider()
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("← Back to Home", use_container_width=True):
        st.switch_page("app.py")