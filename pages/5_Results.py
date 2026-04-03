# pages/5_Results.py
import streamlit as st
import time
from datetime import datetime

st.set_page_config(
    page_title="Analysis Results - CallShield AI",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for stunning results page
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }
    @keyframes threatPulse {
        0% { box-shadow: 0 0 0 0 rgba(255,0,0,0.7); }
        70% { box-shadow: 0 0 0 20px rgba(255,0,0,0); }
        100% { box-shadow: 0 0 0 0 rgba(255,0,0,0); }
    }
    @keyframes glitch {
        0% { transform: skew(0deg, 0deg); opacity: 1; }
        25% { transform: skew(2deg, 1deg); opacity: 0.9; }
        75% { transform: skew(-2deg, -1deg); opacity: 0.95; }
        100% { transform: skew(0deg, 0deg); opacity: 1; }
    }
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .result-card {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 25px;
        padding: 30px;
        margin: 20px 0;
        border: 1px solid rgba(255,255,255,0.2);
    }
    .risk-critical {
        background: linear-gradient(90deg, #ff0000, #ff3300, #ff0000);
        background-size: 200% 100%;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        animation: threatPulse 1.5s infinite, gradientShift 2s ease infinite;
    }
    .risk-high {
        background: linear-gradient(135deg, #ff6600, #cc5500);
        border-radius: 20px;
        padding: 20px;
        text-align: center;
    }
    .risk-medium {
        background: linear-gradient(135deg, #ffcc00, #ffaa00);
        border-radius: 20px;
        padding: 20px;
        text-align: center;
    }
    .risk-low {
        background: linear-gradient(135deg, #99cc00, #88aa00);
        border-radius: 20px;
        padding: 20px;
        text-align: center;
    }
    .risk-safe {
        background: linear-gradient(135deg, #00cc00, #00aa00);
        border-radius: 20px;
        padding: 20px;
        text-align: center;
    }
    .pattern-badge {
        display: inline-block;
        background: rgba(255,255,255,0.2);
        padding: 8px 16px;
        border-radius: 20px;
        margin: 5px;
        font-weight: bold;
    }
    .advice-card {
        background: rgba(0,0,0,0.5);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border-left: 4px solid #ff6b6b;
    }
    .tactic-card {
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
        transition: transform 0.3s;
    }
    .tactic-card:hover {
        transform: translateX(5px);
    }
</style>
""", unsafe_allow_html=True)

# Get data from session
message = st.session_state.get('analyze_message', '')
risk_score = st.session_state.get('analyze_risk', 0)
pattern = st.session_state.get('analyze_pattern', [])
intents = st.session_state.get('analyze_intents', {})
channel = st.session_state.get('analyze_channel', 'Unknown')

# Title with animation
st.markdown("<h1 style='text-align: center;'>📊 Analysis Results</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #ccc;'>Channel: {channel} | Time: {datetime.now().strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)

# Main Result Card
st.markdown('<div class="result-card">', unsafe_allow_html=True)

# Risk Level and Score
if risk_score >= 80:
    risk_class = "risk-critical"
    risk_text = "CRITICAL"
    risk_icon = "🚨"
elif risk_score >= 60:
    risk_class = "risk-high"
    risk_text = "HIGH"
    risk_icon = "⚠️"
elif risk_score >= 40:
    risk_class = "risk-medium"
    risk_text = "MEDIUM"
    risk_icon = "⚡"
elif risk_score >= 20:
    risk_class = "risk-low"
    risk_text = "LOW"
    risk_icon = "🔔"
else:
    risk_class = "risk-safe"
    risk_text = "SAFE"
    risk_icon = "✅"

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown(f"""
    <div class="{risk_class}">
        <div style="font-size: 3em;">{risk_icon}</div>
        <div style="font-size: 2em; font-weight: bold;">{risk_text} RISK</div>
        <div style="font-size: 4em; font-weight: bold;">{risk_score}%</div>
        <div style="font-size: 0.9em;">Risk Score</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Two columns for detailed analysis
col_left, col_right = st.columns(2)

with col_left:
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.subheader("📝 Message Analyzed")
    st.markdown(f"""
    <div style="background: rgba(0,0,0,0.5); padding: 15px; border-radius: 10px;">
        <p style="font-size: 1.1em;">"{message}"</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🎯 Pattern Sequence Detected")
    if pattern:
        pattern_html = ""
        for i, p in enumerate(pattern):
            icons = {'AUTHORITY': '👔', 'FEAR': '😨', 'ACTION': '🎯'}
            colors = {'AUTHORITY': '#667eea', 'FEAR': '#ff6b6b', 'ACTION': '#ffcc00'}
            icon = icons.get(p, '📝')
            color = colors.get(p, '#fff')
            pattern_html += f'<span class="pattern-badge" style="background: {color}20; border: 1px solid {color};">{icon} {p}</span> '
        st.markdown(f"<div style='text-align: center;'>{pattern_html}</div>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; margin-top: 10px;'><strong>Total Patterns:</strong> {len(pattern)}</p>", unsafe_allow_html=True)
    else:
        st.info("No manipulation patterns detected")
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.subheader("🔍 Intent Analysis")
    
    if intents:
        for intent, score in intents.items():
            intent_icons = {'AUTHORITY': '👔', 'FEAR': '😨', 'ACTION': '🎯', 'GREETING': '👋'}
            icon = intent_icons.get(intent, '📝')
            st.markdown(f"""
            <div style="margin: 10px 0;">
                <div style="display: flex; justify-content: space-between;">
                    <span>{icon} <strong>{intent}</strong></span>
                    <span>{score}%</span>
                </div>
                <div style="background: #2d2d2d; border-radius: 10px; overflow: hidden;">
                    <div style="width: {score}%; background: linear-gradient(90deg, #667eea, #764ba2); height: 8px; border-radius: 10px;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No strong intents detected")
    st.markdown('</div>', unsafe_allow_html=True)

# SCAMMER PERSONALITY PROFILE (NEW)
st.markdown('<div class="result-card">', unsafe_allow_html=True)
st.subheader("🎭 Scammer Personality Profile")

scammer_tactics = {
    'AUTHORITY': {'icon': '👔', 'name': 'Authority Impersonator', 'desc': 'Pretends to be bank/police/official', 'color': '#667eea'},
    'FEAR': {'icon': '😨', 'name': 'Fear Monger', 'desc': 'Creates urgency and panic', 'color': '#ff6b6b'},
    'ACTION': {'icon': '🎯', 'name': 'Action Pusher', 'desc': 'Forces immediate compliance', 'color': '#ffcc00'}
}

detected_tactics = []
for intent in pattern:
    if intent in scammer_tactics:
        detected_tactics.append(scammer_tactics[intent])

if detected_tactics:
    for tactic in detected_tactics:
        st.markdown(f"""
        <div class="tactic-card" style="border-left: 4px solid {tactic['color']};">
            <span style="font-size: 1.5em;">{tactic['icon']}</span>
            <strong>{tactic['name']}</strong>
            <p style="margin: 5px 0 0 0; color: #ccc; font-size: 0.85em;">{tactic['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    tactic_sequence = ' → '.join([t['icon'] for t in detected_tactics])
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #ff6b6b20, #ff6b6b10); border-radius: 10px; padding: 15px; margin-top: 10px;">
        <strong>⚠️ Scammer Strategy Detected:</strong><br>
        This scammer is using <strong>{tactic_sequence}</strong> sequence
        to manipulate you into taking immediate action without thinking.
    </div>
    """, unsafe_allow_html=True)
else:
    st.info("✅ No scammer tactics detected - this communication appears legitimate")
st.markdown('</div>', unsafe_allow_html=True)

# Safety Advice based on risk
st.markdown('<div class="result-card">', unsafe_allow_html=True)
st.subheader("🛡️ Safety Recommendations")

if risk_score >= 80:
    st.markdown("""
    <div class="advice-card">
        <h3>🚨 IMMEDIATE ACTION REQUIRED</h3>
        <ul>
            <li>❌ <strong>DO NOT</strong> share any OTP, password, or PIN</li>
            <li>❌ <strong>DO NOT</strong> click any links or download attachments</li>
            <li>❌ <strong>DO NOT</strong> transfer money or share bank details</li>
            <li>📞 <strong>Hang up immediately</strong> or stop responding</li>
            <li>📱 Call the official bank/number from their website</li>
            <li>🔒 Report this as scam to authorities</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
elif risk_score >= 60:
    st.markdown("""
    <div class="advice-card" style="border-left-color: #ff6600;">
        <h3>⚠️ HIGH RISK - BE CAREFUL</h3>
        <ul>
            <li>⚠️ This shows strong scam indicators</li>
            <li>🔍 Verify the identity through official channels</li>
            <li>📞 Call back using known official numbers</li>
            <li>❌ Do not share any sensitive information</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
elif risk_score >= 40:
    st.markdown("""
    <div class="advice-card" style="border-left-color: #ffcc00;">
        <h3>⚡ MEDIUM RISK - STAY ALERT</h3>
        <ul>
            <li>👀 Be cautious - suspicious patterns detected</li>
            <li>🔍 Verify before taking any action</li>
            <li>📝 Don't share personal information</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
elif risk_score >= 20:
    st.markdown("""
    <div class="advice-card" style="border-left-color: #99cc00;">
        <h3>🔔 LOW RISK - BE AWARE</h3>
        <ul>
            <li>✅ Low scam probability detected</li>
            <li>👀 Still remain aware of common scam tactics</li>
            <li>📚 Educate yourself about fraud prevention</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="advice-card" style="border-left-color: #00cc00;">
        <h3>✅ SAFE - NO SCAM PATTERNS</h3>
        <ul>
            <li>🎉 No manipulation patterns detected</li>
            <li>🛡️ Continue with normal caution</li>
            <li>📚 Stay informed about scam prevention</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Action Buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔄 Analyze Another", use_container_width=True):
        st.switch_page("app.py")

with col2:
    if st.button("📊 View Reports", use_container_width=True):
        st.switch_page("pages/4_Reports.py")

with col3:
    if st.button("🎙️ Live Simulation", use_container_width=True):
        st.switch_page("pages/6_Live_Simulation.py")

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 30px; padding: 20px;">
    <p style="color: #666;">🛡️ CallShield AI | Protecting you from digital scams</p>
</div>
""", unsafe_allow_html=True)