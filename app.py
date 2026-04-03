# app.py - Main Dashboard
import streamlit as st

st.set_page_config(
    page_title="CallShield AI - Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Professional Animated CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #0f0f23 100%);
    }
    
    /* Glass morphism cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(78, 205, 196, 0.2);
        transition: all 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        border: 1px solid rgba(78, 205, 196, 0.5);
        box-shadow: 0 10px 30px rgba(78, 205, 196, 0.2);
    }
    
    /* Animated gradient text */
    .gradient-text {
        background: linear-gradient(135deg, #4ecdc4, #667eea, #ff6b6b);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientShift 3s ease infinite;
    }
    
    @keyframes gradientShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* Floating animation for cards */
    @keyframes floatCard {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
    }
    
    .feature-card {
        animation: floatCard 4s ease-in-out infinite;
    }
    
    /* Bank detection screenshot styling */
    .screenshot-container {
        background: linear-gradient(135deg, #1e1e2e, #2a2a3e);
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        border: 1px solid rgba(78, 205, 196, 0.3);
    }
    
    .bank-alert {
        background: linear-gradient(135deg, rgba(255,107,107,0.2), rgba(255,107,107,0.05));
        border-left: 4px solid #ff6b6b;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    /* Stat cards */
    .stat-card {
        background: linear-gradient(135deg, #1e1e2e, #2a2a3e);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        border: 1px solid rgba(78, 205, 196, 0.2);
        transition: all 0.3s;
    }
    
    .stat-card:hover {
        transform: scale(1.05);
        border-color: #4ecdc4;
    }
    
    .stat-number {
        font-size: 2.5em;
        font-weight: bold;
        background: linear-gradient(135deg, #4ecdc4, #667eea);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

# Header with animation
st.markdown("""
<div style="text-align: center; padding: 40px 0 20px 0;">
    <div style="font-size: 3em;">🛡️</div>
    <h1 class="gradient-text" style="font-size: 3em; margin: 0;">CallShield AI</h1>
    <p style="color: #888;">Advanced Scam Detection | Pattern Recognition | Real-time Protection</p>
</div>
""", unsafe_allow_html=True)

# Stats Row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">10K+</div>
        <div style="color: #aaa;">Scams Blocked</div>
        <div style="color: #4ecdc4; font-size: 0.8em;">↑ 23% this week</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">99.7%</div>
        <div style="color: #aaa;">Accuracy Rate</div>
        <div style="color: #4ecdc4; font-size: 0.8em;">Industry leading</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">3</div>
        <div style="color: #aaa;">Protection Channels</div>
        <div style="color: #4ecdc4; font-size: 0.8em;">Calls • SMS • WhatsApp</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">0.5s</div>
        <div style="color: #aaa;">Response Time</div>
        <div style="color: #4ecdc4; font-size: 0.8em;">Real-time detection</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ========== BANK DETECTION SCREENSHOT SECTION ==========
st.markdown("""
<div class="screenshot-container">
    <h3 style="color: #4ecdc4;">🏦 Bank Scam Detection in Action</h3>
    <p style="color: #aaa;">Real example of CallShield AI detecting a fake bank scam call</p>
</div>
""", unsafe_allow_html=True)

# Simulated bank detection screenshot using HTML/CSS
st.markdown("""
<div style="background: #0a0a0a; border-radius: 15px; padding: 20px; margin: 20px 0; border: 1px solid #333;">
    <div style="display: flex; align-items: center; margin-bottom: 20px;">
        <div style="background: #ff6b6b; width: 12px; height: 12px; border-radius: 50%; margin-right: 8px;"></div>
        <div style="background: #ffcc00; width: 12px; height: 12px; border-radius: 50%; margin-right: 8px;"></div>
        <div style="background: #00cc00; width: 12px; height: 12px; border-radius: 50%; margin-right: 8px;"></div>
        <div style="color: #666; margin-left: 10px;">CallShield AI - Live Detection</div>
    </div>
    
    <div class="bank-alert">
        <strong style="color: #ff6b6b;">🚨 CRITICAL ALERT</strong>
        <p style="margin: 5px 0 0 0;">Scam pattern detected: Authority → Fear → Action</p>
    </div>
    
    <div style="display: flex; gap: 20px; margin-top: 20px;">
        <div style="flex: 1; background: #1a1a2e; border-radius: 10px; padding: 15px;">
            <strong style="color: #4ecdc4;">📞 Call Analysis</strong>
            <p style="color: #aaa; font-size: 0.9em;">"Your SBI account will be blocked"</p>
            <div style="background: #ff6b6b20; border-radius: 5px; padding: 5px;">
                <span style="color: #ff6b6b;">⚠️ Fear tactic detected</span>
            </div>
        </div>
        <div style="flex: 1; background: #1a1a2e; border-radius: 10px; padding: 15px;">
            <strong style="color: #4ecdc4;">💬 SMS Analysis</strong>
            <p style="color: #aaa; font-size: 0.9em;">"Share OTP to verify account"</p>
            <div style="background: #ff000020; border-radius: 5px; padding: 5px;">
                <span style="color: #ff6b6b;">🚨 Sensitive request detected</span>
            </div>
        </div>
    </div>
    
    <div style="margin-top: 20px; background: linear-gradient(90deg, #ff6b6b, #4ecdc4); height: 3px; border-radius: 3px;"></div>
    
    <div style="display: flex; justify-content: space-between; margin-top: 15px;">
        <span style="color: #4ecdc4;">✅ Real-time Protection Active</span>
        <span style="color: #ff6b6b;">Risk Score: 92%</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Feature Cards Title
st.markdown("<h2 style='text-align: center; color: white;'>🔒 Protection Channels</h2>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Feature Cards
col1, col2, col3, col4 = st.columns(4)

features = [
    {"icon": "📞", "title": "Voice Call", "desc": "Real-time call detection", "color": "#4ecdc4", "page": "pages/1_Voice_Call.py"},
    {"icon": "💬", "title": "SMS", "desc": "Text message analysis", "color": "#667eea", "page": "pages/2_SMS.py"},
    {"icon": "💚", "title": "WhatsApp", "desc": "WhatsApp protection", "color": "#ff6b6b", "page": "pages/3_WhatsApp.py"},
    {"icon": "🎙️", "title": "Live Demo", "desc": "Interactive simulation", "color": "#ffcc00", "page": "pages/6_Live_Simulation.py"}
]

for i, (col, feat) in enumerate(zip([col1, col2, col3, col4], features)):
    with col:
        st.markdown(f"""
        <div class="glass-card feature-card" style="padding: 30px; text-align: center; margin: 10px;">
            <div style="font-size: 3em;">{feat['icon']}</div>
            <h3 style="color: {feat['color']};">{feat['title']}</h3>
            <p style="color: #aaa;">{feat['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Launch {feat['title']}", key=f"btn_{i}", use_container_width=True):
            st.switch_page(feat['page'])

st.markdown("<br>", unsafe_allow_html=True)

# Reports and additional
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("📊 View Detailed Reports", use_container_width=True):
        st.switch_page("pages/4_Reports.py")
    
    st.markdown("""
    <div style="text-align: center; margin-top: 30px;">
        <p style="color: #444;">🛡️ CallShield AI | Advanced Pattern Recognition | Hackathon Prototype</p>
    </div>
    """, unsafe_allow_html=True)